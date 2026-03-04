# All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径

> 本文于**2017年9月18日**发布于 https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib

[之前的一篇博客](https://www.sifive.com/blog/all-aboard-part-1-compiler-args) 描述了如何使用 GCC 的 `-march` 和 `-mabi` 命令行参数来控制用户编译源代码时的代码生成，但大多数程序需要链接系统库才能正常运行。由于用户通常不希望将每个库都与他们的程序一起编译，要么是因为库太复杂，要么是因为它们旨在被共享，因此需要一种机制来链接正确的系统库集，以匹配用户目标系统的 ISA 和用户生成代码的 ABI。

处理多套系统库的机制被称为“multilib”。与 RISC-V 工具链的大多数部分一样，multilib 机制是所有架构移植共享的，但它如何应用于 RISC-V 的具体细节则特定于我们的 ISA。由于 RISC-V 是一个模块化的 ISA，从一开始就拥有广泛的 multilib 支持是很自然的。这使得我们的 multilib 实现比许多其他架构的要清晰得多，这很好，因为我们拥有的大量 ISA 和 ABI 组合需要良好的 multilib 支持。

## GCC 编译器包装器

如前一篇博客文章所讨论，用户直接交互的 `gcc` 命令实际上只是一个包装器，它按顺序调用工具链中的每一步：预处理、编译、汇编和链接你的程序。`gcc` 实际上不是一个脚本，而是一个协调编译过程的小型 C 程序。该程序的架构特定钩子由一种特定于 GCC 命令行参数处理的领域特定语言（DSL）组成，它描述了 `gcc` 包装器的参数在传递给被调用的各种其他工具时应如何转换。

为了确保事情足够复杂，有三种不同的语言用于描述路径在用户调用 `gcc` 和实际执行工作的 `cc1` 或 `collect2` 调用之间是如何被修改的。所有这些都特定于 GCC 命令行参数解析。`gcc` 命令行包装器使用这些工具的各种组合来指定以下与 multilib 相关的参数：

*   汇编器需要知道要生成的 ELF 类，根据目标处理器的架构，是 ELF32 还是 ELF64。
*   链接器需要知道应该搜索库的链接时路径。
*   汇编器需要知道 ABI，以便它可以填充相关的 ELF 标志。这让链接器可以禁止链接不同 ABI 的对象，因为它们会不兼容。
*   链接器需要知道动态链接器的路径，以便它可以填充 ELF 的解释器字段。动态链接器内置了路径，知道去哪里搜索库。
*   链接器需要知道应该链接到可执行文件中的 C 运行时文件，以及任何默认应链接的其他库，如 `libatomic` 或 `libgloss`。

所有这些工具都有些耦合在一起，所以我们将在下面逐一介绍，并描述每个工具帮助指定了上述哪些参数。

### `*_SPEC` 领域特定语言

在描述 GCC 命令行参数处理的三种语言中，最低级、因此也最通用的是用于各种目标可以定义的 `*_SPEC` 宏的语言。这些宏描述了用于转换 GCC 调用的每个工具的命令行参数的转换过程，所以虽然它们不特定于 multilib 路径处理，但它们被用来生成传递给链接器的完整参数集，因此我觉得至少值得一提。为每个目标程序定义一个宏：例如 `ASM_SPEC` 定义了如何为汇编器转换命令行参数，`LINK_SPEC` 为链接器，等等。

`*_SPEC` 宏控制一个字符串到字符串的转换，将 `gcc` 命令的命令行参数转换为传递给另一个命令的参数。虽然我记得在某个时候见过关于这些宏可以包含什么内容的文档，但我现在能找到的最好的资料在 GCC 文档的 [Controlling the Compilation Driver](https://gcc.gnu.org/onlinedocs/gccint/Driver.html) 部分。由于那并没有真正指定任何工作原理，我将尝试描述我们实际使用的部分——我们的大部分移植工作都是通过阅读其他移植中的代码和反复试验来完成的。

作为 `*_SPEC` 行如何行为的一个例子，让我们看看 RISC-V 的 `STARTFILE_PREFIX_SPEC` 宏，它决定了链接器应该在哪里寻找 C 运行时启动文件，如 `crt0.o`：

```c
#define XLEN_SPEC \
  "%{march=rv32*:32}" \
  "%{march=rv64*:64}" \

#define ABI_SPEC \
  "%{mabi=ilp32:ilp32}" \
  "%{mabi=ilp32f:ilp32f}" \
  "%{mabi=ilp32d:ilp32d}" \
  "%{mabi=lp64:lp64}" \
  "%{mabi=lp64f:lp64f}" \
  "%{mabi=lp64d:lp64d}" \

#define STARTFILE_PREFIX_SPEC                   \
   "/lib" XLEN_SPEC "/" ABI_SPEC "/ "           \
   "/usr/lib" XLEN_SPEC "/" ABI_SPEC "/ "       \
   "/lib/ "                                     \
   "/usr/lib/ "
```

这是一个非常标准的 RISC-V 的 `*_SPEC` 定义：它们将整个 `gcc` 命令行参数集作为一个以空格分隔的列表来消费，通过一些模式匹配进行过滤，执行替换，然后将结果作为以空格分隔的参数列表传递给某个其他命令。我们只使用少数几种模式：

*   `"STRING"`：将 `"STRING"` 直接传递到输出中。任何未被 `%{` 和 `}` 包裹的内容都会直接传递到输出。
*   `%{argument}`：如果 `-argument` 作为一个完整的词出现在输入中，则将 `-argument` 传递到输出。
*   `%{argument:substitution}`：如果 `-argument` 作为一个完整的词出现在输入中，则将替换项传递到输出中。这些是递归的，所以像 `%{arg1:%{arg2:-arg3}}` 这样的东西，如果 `-arg1` 和 `-arg2` 都存在，则传递 `-arg3`。
*   `%{glob:substitution}`：如果一个参数匹配 `-glob`，则将 `substitution` 传递到输出。像上面一样，`substitution` 可以是递归的。我能找到的关于 glob 语法的最好参考是，它看起来像非常简单的 shell globbing。例如，`%{march=rv32*:32}` 如果传递了任何 `-march=rv32i`、`-march=rv32imafdc` 或 `-march=rv32INVALID_ISA_STRING`，都会传递 `32`（当然 GCC 会在命令行参数解析时捕获最后一个）。
*   `%{!glob:substitution}`：与上面类似，但如果 `-glob` 不存在则传递替换项。

这差不多就是 RISC-V 移植使用的 `*_SPEC` 宏的全部内容了：没什么特别有趣的，只是一些文本模式匹配。
> 译者注：原文中此处没有示例输出，根据 `STARTFILE_PREFIX_SPEC` 的定义，为方便理解，补充一些示例：
> * `-march=rv32imafdc -mabi=ilp32d`: 生成的搜索路径前缀为 `/lib32/ilp32d/ /usr/lib32/ilp32d/ /lib/ /usr/lib/`
> * `-march=rv32imafdc -mabi=ilp32`: 生成的搜索路径前缀为 `/lib32/ilp32/ /usr/lib32/ilp32/ /lib/ /usr/lib/`
> * `-march=rv32i -mabi=ilp32`: 生成的搜索路径前缀为 `/lib32/ilp32/ /usr/lib32/ilp32/ /lib/ /usr/lib/`
> * `-march=rv64i -mabi=lp64`: 生成的搜索路径前缀为 `/lib64/lp64/ /usr/lib64/lp64/ /lib/ /usr/lib/`
>   (原文作者在后面GCC wrapper输出示例中弄错了 `-mabi=ilp32` 和 `lp64` 的对应关系)

### 目标片段 (Target Fragments)

由于许多目标的 multilib 路径描述过于复杂，无法使用 spec DSL 来描述，GCC 包含第二种 DSL，专门用于指定 multilib 系统中的库路径。GCC 的 [target fragment](https://gcc.gnu.org/onlinedocs/gccint/Target-Fragment.html) 部分有更多关于这应该做什么的文档。总而言之，RISC-V 移植在这个文件中设置了四个变量：

*   `MULTILIB_OPTIONS`：包含在扩展 multilib 路径时应考虑的命令行参数集。互斥的选项用斜杠分隔，不相关的组用空格分隔。
*   `MULTILIB_PATHS`：一个以空格分隔的列表，包含与上述每个参数相对应的路径组件。Multilib 路径将通过将与传递的参数相对应的路径用斜杠连接起来构建。
*   `MULTILIB_MATCHES`：当两个与 multilib 相关的参数足够相似，以至于我们应该在两种模式下链接时都使用相同的库路径时，映射关系就放在这里。
*   `MULTILIB_REQUIRED`：没有这个参数，GCC 将构建覆盖 `MULTILIB_OPTIONS` 中所有组合的笛卡尔积的库。在库太多的系统上，这个变量控制实际构建的子集。

在 RISC-V 上，我们有太多的 ISA/ABI 组合，无法为每一种组合构建库并作为库发布，所以我们通过 `MULTILIB_REQUIRED` 变量严重限制了实际构建的集合——没有这个，我们最终会构建数百个库，其中绝大多数永远不会被使用，因为它们代表了没有多大意义的系统——例如，谁会构建一个有双精度浮点但没有整数乘法器的系统呢？

然后，这些变量作为参数提供给 `gcc/genmultilib` 脚本，该脚本既生成 `gcc` 包装器使用的用于解码这些参数的表，也生成各种构建脚本的输入，这些脚本指示 GCC 为其安装的每个库构建多个副本（例如，`libgcc.so`）。

### RISC-V 的 `multilib-generator` 脚本

RISC-V 被设计成一个模块化的 ISA。因此，我们已经有超过一百种被工具链支持的 ISA 和 ABI 组合，而且这个数字只会不断增加。虽然我们的目标是在工具链中支持所有这些组合，但期望用户构建所有这些库（或者甚至作为发行版的一部分下载所有这些库）是不合理的。

为了将这一切都纳入 GCC 的目标片段框架，我们将 `MULTILIB_OPTIONS` 设置为包含许多目标，然后将 `MULTILIB_REQUIRED` 设置为我们实际想要构建的集合。然后，我们通过向 `MULTILIB_MATCHES` 添加一些相关条目来稍微增加支持的 ISA/ABI 对的集合。由于手动输入所有这些很痛苦，我们转而使用一个脚本来生成我们的目标片段（它又是 `genmultilibs` 脚本的输入，然后该脚本生成 `gcc` 编译器包装器的输入，接着生成传递给 `collect2` 的命令行参数以实际进行链接）。

这个脚本叫做 `multilib-generator`，用 Python 编写。它在命令行上接受一个由破折号分隔的参数列表，并生成一个实现这些参数所描述的 multilib 配置的目标片段。这个脚本并不是为最终用户设计的，所以文档不完善，但如果你想生成一个与 GCC 默认设置不同的 multilib 集合的工具链，你就得和它打交道了。

每个参数由四个破折号分隔的部分组成。前两个部分控制将实际构建的 multilibs。例如：

```
# This file was generated by multilib-generator with the command:
#  ./multilib-generator ARCH0-ABI0-- ARCH1-ABI1--
MULTILIB_OPTIONS = march=ARCH0/march=ARCH1 mabi=ABI0/mabi=ABI1
MULTILIB_DIRNAMES = ARCH0 \
ARCH1 ABI0 \
ABI1
MULTILIB_REQUIRED = march=ARCH0/mabi=ABI0 \
march=ARCH1/mabi=ABI1
MULTILIB_REUSE =

```

将生成两个 multilibs：`-march=ARCH0 -mabi=ABI0` 和 `-march=ARCH1 -mabi=ABI1`。任何其他的 march/mabi 对将导致 GCC 使用默认的 multilib（就是安装在 “lib” 里的那个），这可能会在链接时导致错误。这种“回退到默认”的行为是 GCC 内置的，虽然它可能有点问题，但我们现在没有时间去修复它。如果你想构建一个额外的 multilib，你应该向 `multilib-generator` 添加一个额外的参数，指定该 multilib 的 ISA/ABI 对。

> 译者注：原文中此处的示例代码块疑似有误，根据上下文描述，正确的输出应该是 `MULTILIB_REUSE` 而非 `MULTILIB_MATCHES`。同时，`MULTILIB_REUSE` 的语法也与后文描述不同。以下为根据上下文修正的示例。

接下来两个部分控制 `MULTILIB_REUSE`，它指定了 GCC 如何搜索那些不完全匹配 `MULTILIB_REQUIRED` 构建的 multilibs。两者都指定了一组额外的逗号分隔的 ‘-march’ 参数，这些参数映射到由前两个参数指定的 multilib。

第三个位置的参数更简单：它是一个逗号分隔的附加 ISA 值列表，这些值应该映射到由前两个部分指定的 multilib。例如：

```
# This file was generated by multilib-generator with the command:
#  ./multilib-generator ARCH0-ABI0-ARCHa,ARCHb-
MULTILIB_OPTIONS = march=ARCH0/march=ARCHa/march=ARCHb mabi=ABI0
MULTILIB_DIRNAMES = ARCH0 \
ARCHa \
ARCHb ABI0
MULTILIB_REQUIRED = march=ARCH0/mabi=ABI0
MULTILIB_REUSE = march.ARCH0/mabi.ABI0=march.ARCHa/mabi.ABI0 \
march.ARCH0/mabi.ABI0=march.ARCHb/mabi.ABI0
```

为生成的 multilib 添加了两个额外的 ISA 映射：当传递 “-march=ARCH0 -mabi=ABI0”、“-march=ARCHa -mabi=ABI0” 或 “-march=ARCHb -mabi=ABI0” 中任何一个时，都会使用 “-march=ARCH0 -mabi=ABI0” 的库。当有多个生成的 multilib 时，你可以指定这些，额外的 ISA 会应用到同一个参数中的那个 multilib。

第四个参数与第一个非常相似，但它不是指定应映射到指定 multilib 的整个 ISA，而只是指定应映射的附加后缀。例如：

```
# This file was generated by multilib-generator with the command:
#  ./multilib-generator ARCH0-ABI0--c,d
MULTILIB_OPTIONS = march=ARCH0/march=ARCH0c/march=ARCH0d mabi=ABI0
MULTILIB_DIRNAMES = ARCH0 \
ARCH0c \
ARCH0d ABI0
MULTILIB_REQUIRED = march=ARCH0/mabi=ABI0
MULTILIB_REUSE = march.ARCH0/mabi.ABI0=march.ARCH0c/mabi.ABI0 \
march.ARCH0/mabi.ABI0=march.ARCH0d/mabi.ABI0
```

为生成的 multilib 添加了两个额外的 ISA 映射：当传递 “-march=ARCH0 -mabi=ABI0”、“-march=ARCH0c -mabi=ABI0” 或 “-march=ARCH0d -mabi=ABI0” 中任何一个时，都会使用 “-march=ARCH0 -mabi=ABI0” 的库——如你所见，与上面大致相同。

## 其他支持 Multilib 的组件

虽然 GCC 处理了绝大多数的 multilib 支持，但系统中还有少数其他组件以其他方式为我们的 multilib 支持做出贡献：

*   `ld`，链接器，拒绝链接具有不兼容 ABI 的目标文件。虽然这不直接支持 multilib，但它确实防止了它被悄悄地搞砸。
*   `ld.so`，动态加载器，内置了一些 multilib 路径，以便它能正确搜索库。我们为每个 multilib 编译一个动态加载器，然后使用 GCC 填充相应的 ELF 解释器字段，所以 glibc 在这里做的事情不多。

## 捷径

你可能在想“那太复杂了，我真正想做的只是知道我的编译器使用了哪些库路径”。虽然你可以通过查看 GCC 源代码来推断出这一点，但更简单的方法是使用类似下面的脚本通过实验来确定 multilib 集合：

```bash
#!/bin/bash
for abi in ilp32 ilp32f ilp32d lp64 lp64f lp64d; do
  for isa in rv32e rv32i rv64i; do
    for m in "" m; do
      for a in "" a; do
        for f in "" f fd; do
          for c in "" c; do
            readlink -f $(riscv64-unknown-elf-gcc -march=$isa$m$a$f$c -mabi=$abi -print-search-dirs | grep ^libraries | sed 's/:/ /g') | grep 'riscv64-unknown-elf/lib' | grep -ve 'lib$' | sed 's@^.*/lib/@@' | while read path; do
              echo "riscv64-unknown-elf-gcc -march=$isa$m$a$f$c -mabi=$abi => $path"
            done
          done
        done
      done
    done
  done
done
```

> 译者注：这个脚本会尝试各种 `-march` 和 `-mabi` 组合，然后使用 `-print-search-dirs` 选项让 GCC 打印出它会搜索的库目录，最后解析出 multilib 路径。

它会生成我们支持的全部 multilib 集合及其对应的参数：

对于嵌入式（elf）工具链：
```
riscv64-unknown-elf-gcc -march=rv32i -mabi=ilp32 => rv32i/ilp32
riscv64-unknown-elf-gcc -march=rv32ic -mabi=ilp32 => rv32i/ilp32
riscv64-unknown-elf-gcc -march=rv32iac -mabi=ilp32 => rv32iac/ilp32
riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 => rv32im/ilp32
riscv64-unknown-elf-gcc -march=rv32imc -mabi=ilp32 => rv32im/ilp32
riscv64-unknown-elf-gcc -march=rv32imac -mabi=ilp32 => rv32imac/ilp32
riscv64-unknown-elf-gcc -march=rv32imafc -mabi=ilp32f => rv32imafc/ilp32f
riscv64-unknown-elf-gcc -march=rv32imafdc -mabi=ilp32f => rv32imafc/ilp32f
riscv64-unknown-elf-gcc -march=rv64imac -mabi=lp64 => rv64imac/lp64
riscv64-unknown-elf-gcc -march=rv64imafdc -mabi=lp64d => rv64imafdc/lp64d
```

或对于 Linux 工具链：

```
riscv64-unknown-linux-gnu-gcc -march=rv32ima -mabi=ilp32 => lib32/ilp32
riscv64-unknown-linux-gnu-gcc -march=rv32imac -mabi=ilp32 => lib32/ilp32
riscv64-unknown-linux-gnu-gcc -march=rv32imaf -mabi=ilp32 => lib32/ilp32
riscv64-unknown-linux-gnu-gcc -march=rv32imafc -mabi=ilp32 => lib32/ilp32
riscv64-unknown-linux-gnu-gcc -march=rv32imafd -mabi=ilp32 => lib32/ilp32
riscv64-unknown-linux-gnu-gcc -march=rv32imafdc -mabi=ilp32 => lib32/ilp32
riscv64-unknown-linux-gnu-gcc -march=rv32imafd -mabi=ilp32d => lib32/ilp32d
riscv64-unknown-linux-gnu-gcc -march=rv32imafdc -mabi=ilp32d => lib32/ilp32d
riscv64-unknown-linux-gnu-gcc -march=rv64ima -mabi=lp64 => lib64/lp64
riscv64-unknown-linux-gnu-gcc -march=rv64imac -mabi=lp64 => lib64/lp64
riscv64-unknown-linux-gnu-gcc -march=rv64imaf -mabi=lp64 => lib64/lp64
riscv64-unknown-linux-gnu-gcc -march=rv64imafc -mabi=lp64 => lib64/lp64
riscv64-unknown-linux-gnu-gcc -march=rv64imafd -mabi=lp64 => lib64/lp64
riscv64-unknown-linux-gnu-gcc -march=rv64imafdc -mabi=lp64 => lib64/lp64
riscv64-unknown-linux-gnu-gcc -march=rv64imafd -mabi=lp64d => lib64/lp64d
riscv64-unknown-linux-gnu-gcc -march=rv64imafdc -mabi=lp64d => lib64/lp64d
```

### 我们 Multilib 集合背后的基本原理

虽然我们默认设置的 multilib 集合可能看起来有些随意，但实际上我们对每一个都经过了深思熟虑。这里的大部分工作都投入到了嵌入式集合中，所以让我们逐一过一下列表，描述每一个存在的原因：

*   `rv32i/ilp32`：最简单的 RISC-V ISA。虽然我们不期望它会有太多的商业用途，但我们预计它会在教育和业余爱好者中得到大量使用。而且，不支持基础 ISA 似乎有点奇怪——否则它的意义何在呢 :)。
*   `rv32iac/ilp32`：尽管有很多技巧可以制造出任意慢的小型乘法器，但有些人似乎对硬件乘法过敏。这个目标就是为了满足那些人。
*   `rv32im/ilp32`：这个的存在主要是为了支持从其他 ISA 改装过来的核心，在这些核心中，简单的内存系统排除了 A 和 C 扩展的实现。
*   `rv32imac/ilp32`：我们预计这个会得到大量使用，如果你要构建一个独立的微控制器芯片，这可能就是你想要的。
*   `rv32imafc/ilp32f`：一个 32 位的浮点目标。这里的另一个选择本可以是 `rv32imafdc/ilp32d`，但我们选择了这个，假设如果你能处理拥有一个 64 位 FPU，你可能就直接想构建一个 64 位的核心了。
*   `rv64imac/lp64`：在可预见的未来，这可能会是核心产量最大的 RISC-V ISA 配置，因为对于需要与地址空间大于 32 位的 SOC 通信的深度嵌入式核心（想想电源管理单元、IP 控制核心等），没有好的选择。
*   `rv64imafdc/lp64d`： “全功能”嵌入式核心。这些可能不会直接作为嵌入式核心生产，但我们认为人们会把 Linux 级别的核心 repurposed（重新利用）为嵌入式核心，因为在 RISC-V 上运行 Linux 并不那么昂贵。

我们不希望列表变得太大，所以我们决定将其限制在这个集合内。我们对 Linux 配置的考虑较少，因为在更大的系统中，事情往往更常规一些。在这里我们只决定支持四种库配置：32/64 位和软/硬浮点的笛卡尔积。

### 更改 Multilib 集合

虽然我们试图确保默认的工具链构建中包含了一套合理的库，但你可能想要一些稍微不同的东西。你有几个选择：

*   构建一个非 multilib 工具链，这样所有东西都将是你的 ISA/ABI 组合。这是最简单的选择，但如果你要发布产品，你应该至少针对你选择的组合运行 GCC 测试套件，因为默认 multilib 集合之外的目标得到的测试较少。
*   请求 GCC 开发者添加一个 `MULTILIB_MATCHES`，为你感兴趣的 ISA 提供一个用稍微不同的标志集编译的库。如果你的目标 ISA 在 C 库中不怎么使用，这是理想的选择：例如，一个好的添加候选可能是让 `-march=rv64imafdc -mabi=lp64` 与 `rv64imac/lp64` 库匹配，因为 newlib 不做太多浮点运算。这是低开销的，所以我们很可能会接受你的建议。
*   请求 GCC 开发者添加一个 `MULTILIB_REQUIRED`，提供你想要的 ISA/ABI 组合。这比添加到 `MULTILIB_MATCHES` 的开销要大，因为它会导致更高的支持负担。如果一个 ISA 有常用的可用芯片，我们会强烈考虑将其添加到默认集合中，因为 multilib 的全部意义就在于避免需要多个工具链。
*   Fork 工具链并更改默认的 multilib 集合。这不是一个理想的选择，我们请求如果你这样做，请选择一个不同的三元组（tuple）来表明你有一个非标准的构建。例如，你可能会选择 `riscv64-my_company-elf` 而不是 `riscv64-unknown-elf` 来表示“我的公司”正在提供一个非标准的工具链。由于 `unknown` 字段并没有真正定义，没有程序应该会查看它，所以你应该没事。我们真的希望尽可能避免工具链的 fork，所以请至少先联系我们谈谈！

我想关于 RISC-V multilib 实现的内容就这么多了，希望这个博客系列不会再有更多关于它的报道了。下周我们将尝试回到讨论一些稍微有趣的话题 :)。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径 (当前页面)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)