# All Aboard 系列，第 4 部分：RISC-V 代码模型

> 本文于**2017年9月11日**发布于 https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models

RISC-V ISA 被设计得既简单又模块化。为了实现这些设计目标，RISC-V 最小化了实现复杂 ISA 的最大成本之一：寻址模式。寻址模式无论在小型设计（由于解码成本）还是大型设计（由于隐式依赖）中都是昂贵的。RISC-V 只有三种寻址模式：

*   PC 相对寻址，通过 `auipc`、`jal` 和 `br*` 系列指令实现。
*   寄存器偏移寻址，通过 `jalr`、`addi` 和所有内存指令实现。
*   绝对寻址，通过 `lui` 指令实现（尽管可以说这只是 `x0` 寄存器偏移寻址）。

这些寻址模式经过精心挑选，以便在最小化硬件复杂性的同时实现高效的代码生成。我们通过依赖现代工具链在软件中优化寻址来实现这种简单性——这与传统的 ISA 形成鲜明对比，后者在硬件中实现了大量的寻址模式。研究表明，RISC-V 的方法是合理的：我们能够在基准测试中实现相似的代码大小，同时拥有极其简单的解码规则和大量的可用编码空间。

所有这些硬件复杂性的降低都是以增加软件复杂性为代价的。这篇博客文章介绍了 RISC-V 中另一个软件复杂性的体现：代码模型（code model）的概念。就像重定位和松弛一样，代码模型并非 RISC-V 特有——事实上，RISC-V 工具链的代码模型比大多数流行的 ISA 要少，这主要是因为我们依赖软件优化而不是奇特的寻址模式，这使得我们的寻址模式具有显著的灵活性。

## 什么是代码模型

大多数程序不会用符号填满它们可用的整个地址空间（大多数根本填不满，而那些确实填满的往往是用堆来填充）。ISA 倾向于利用这种局部性，在硬件中实现较短的寻址模式，并依赖软件来提供较大的寻址模式。代码模型决定了使用哪种软件寻址模式，并因此决定了对链接程序施加的约束。软件寻址模式决定了程序员如何看待地址，而硬件寻址模式则决定了指令中的地址位如何被处理。

由于编译器和链接器之间的分离，代码模型是必要的：在生成未链接的目标文件时，编译器不知道任何符号的绝对地址，但它仍然必须知道使用哪种寻址模式，因为某些寻址模式可能需要临时寄存器来操作。由于编译器无法生成实际的寻址代码，它会生成寻址模板（称为[重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)），链接器可以在知道每个符号的实际地址后修复这些模板。代码模型决定了这些寻址模板的样子，并因此决定了发出哪些重定位。

这最好通过一个例子来解释。想象一下下面的 C 代码：

```c
long global_symbol[2];

int main() {
  return global_symbol[0] != 0;
}
```

尽管对于这个简单情况，一次 GCC 调用就能生成一个二进制文件，但在这背后，GCC 驱动脚本实际上是依次运行了预处理器、编译器、汇编器，最后是链接器。GCC 的 `--save-temps` 参数允许用户查看所有这些中间文件，这是深入探究工具链内部的一个有用参数。

```sh
$ riscv64-unknown-linux-gnu-gcc cmodel.c -o cmodel -O3 --save-temps
```

GCC 包装脚本运行的每一步都会生成一个文件：

*   `cmodel.i`：预处理后的源文件，它会展开任何预处理器指令（如 `#include` 或 `#ifdef`）。
*   `cmodel.s`：实际编译器的输出，这是一个汇编文件（RISC-V 汇编格式的文本文件）。
*   `cmodel.o`：汇编器的输出，这是一个未链接的目标文件（一个 ELF 文件，但不是可执行的 ELF）。
*   `cmodel`：链接器的输出，这是一个已链接的可执行文件（一个可执行的 ELF 文件）。

为了理解代码模型为何存在，我们必须首先更详细地审视这个工具链流程。由于这是一个没有预处理器宏的简单源文件，预处理运行过程相当乏味：它只是发出一些指令，用于后续如果生成调试信息时使用：

```sh
$ cat cmodel.i
# 1 "cmodel.c"
# 1 "built-in"
# 1 "command-line"
# 31 "command-line"
# 1 "/scratch/palmer/work/upstream/riscv-gnu-toolchain/build/install/sysroot/usr/include/stdc-predef.h" 1 3 4
# 32 "command-line" 2
# 1 "cmodel.c"
long global_symbol;

int main() {
  return global_symbol != 0;
}
```

预处理后的输出随后被送入编译器，生成一个汇编文件。这个文件是包含 RISC-V 汇编代码的纯文本，因此易于阅读：

```sh
$ cat cmodel.s
main:
  lui   a5,%hi(global_symbol)
  ld    a0,%lo(global_symbol)(a5)
  snez  a0,a0
  ret
```

生成的汇编包含一对指令来寻址 `global_symbol`：`lui` 然后是 `ld`。这对 `global_symbol` 可以占用的地址施加了一个约束：它必须能被一个 32 位有符号绝对常量寻址（不是相对于某个寄存器或 PC 的 32 位偏移，而是实际的 32 位地址）。请注意，对符号地址的限制与该架构上指针的大小无关：具体来说，这里的指针仍然可以是 64 位的，但所有全局符号都必须能被 32 位绝对地址寻址。

在编译器生成汇编之后，GCC 包装脚本调用汇编器来生成一个目标文件。这个文件是一个 ELF 二进制文件，可以用 Binutils 提供的各种工具来读取。在这种情况下，我们将使用 `objdump` 来显示符号表，反汇编文本段，并显示汇编器生成的重定位：

```sh
$ riscv64-unknown-linux-gnu-objdump -d -t -r cmodel.o

cmodel.o:     file format elf64-littleriscv

SYMBOL TABLE:
0000000000000000 l    df *ABS*  0000000000000000 cmodel.c
0000000000000000 l    d  .text  0000000000000000 .text
0000000000000000 l    d  .data  0000000000000000 .data
0000000000000000 l    d  .bss   0000000000000000 .bss
0000000000000000 l    d  .text.startup  0000000000000000 .text.startup
0000000000000000 l    d  .comment       0000000000000000 .comment
0000000000000000 g     F .text.startup  000000000000000e main
0000000000000010       O *COM*  0000000000000008 global_symbol

Disassembly of section .text.startup:

0000000000000000 main:
   0:   000007b7                lui     a5,0x0
                        0: R_RISCV_HI20 global_symbol
                        0: R_RISCV_RELAX        *ABS*
   4:   0007b503                ld      a0,0(a5) # 0 main
                        4: R_RISCV_LO12_I       global_symbol
                        4: R_RISCV_RELAX        *ABS*
   8:   00a03533                snez    a0,a0
   c:   8082                    ret
```

此时我们有了一个目标文件，但我们仍然不知道任何全局符号的实际地址。在这里，工具链各组件的角色有一些重叠：汇编器的工作是将文本指令转换为比特位，但在那些比特位依赖于全局符号地址的情况下（例如上面代码中的 `lui`），汇编器无法知道这些比特位实际上应该是什么。为了让链接器能够在最终的可执行目标文件中填充这些比特位，汇编器为每个期望链接器填充的比特范围生成一个重定位表条目。重定位定义了一个链接器在链接代码时要填充的比特范围。文本段中存在的任何重定位类型的具体定义是 ISA 特定的，RISC-V 的定义可以在我们的 [ELF psABI 文档](https://github.com/riscv/riscv-elf-psabi-doc/blob/master/riscv-elf.md)中找到。

在汇编程序之后，GCC 包装脚本运行链接器来生成一个可执行文件。这是另一个 ELF 文件，但这次它是一个完整的可执行文件。由于它包含大量 C 库代码，我将只在这里显示其相关片段：

```sh
$ riscv64-unknown-linux-gnu-objdump -d -t -r cmodel
cmodel:     file format elf64-littleriscv

SYMBOL TABLE:
0000000000012038 g     O .bss    0000000000000010              global_symbol
...

Disassembly of section .text:

0000000000010330 main:
 10330:       67c9                    lui     a5,0x12
 10332:       0387b503                ld      a0,56(a5) # 12038 global_symbol
 10336:       00a03533                snez    a0,a0
 1033a:       8082                    ret
```

这里有几点值得注意：

*   符号表包含具有实际、绝对值的符号。这正是链接器的全部意义所在。
*   文本段包含实际引用全局符号的正确比特位，而不是一堆 0。
*   针对全局符号的重定位已被移除，因为它们不再需要。某些重定位可能仍然存在于可执行文件中，以支持动态链接等，但在这个简单的情况下没有。

到目前为止，这个例子一直在使用 RISC-V 的默认代码模型 [medlow](#what-does--mcmodelmedlow-mean)。为了更具体地演示什么是代码模型，最好将其与我们的另一个代码模型 [medany](#what-does--mcmodelmedany-mean) 进行对比。区别可以用一个例子输出来概括：

```asm
0000000000000000 main:
   0:   00000797                auipc   a5,0x0
                        0: R_RISCV_PCREL_HI20   global_symbol
                        0: R_RISCV_RELAX        *ABS*
   4:   0007b503                ld      a0,0(a5) # 0 main
                        4: R_RISCV_PCREL_LO12_I .LA0
                        4: R_RISCV_RELAX        *ABS*
   8:   00a03533                snez    a0,a0
   c:   8082                    ret
```

具体来说，[medany](#what-does--mcmodelmedany-mean) 代码模型生成 `auipc`/`ld` 对来引用全局符号，这允许代码在任何地址进行链接；而 [medlow](#what-does--mcmodelmedlow-mean) 生成 `lui`/`ld` 对来引用全局符号，这将代码限制在地址零附近进行链接。它们都为引用符号生成 32 位有符号偏移，因此它们都将生成的代码限制在 2GiB 的窗口内链接。

## `-mcmodel=medlow` 是什么意思？

这选择了中低（medium-low）[代码模型](#what-is-a-code-model)，这意味着程序及其静态定义的符号必须位于单个 2 GiB 的地址范围内，并且必须位于绝对地址 -2 GiB 和 +2 GiB 之间。对全局符号的寻址使用 `lui`/`addi` 指令对，这会发出 `R_RISCV_HI20`/`R_RISCV_LO12_I` 序列。以下是使用 medlow 代码模型生成的一些代码示例：

```sh
$ cat cmodel.c
long global_symbol[2];

int main() {
  return global_symbol[0] != 0;
}

$ riscv64-unknown-linux-gnu-gcc cmodel.c -o cmodel -O3 --save-temps -mcmodel=medlow

$ cat cmodel.s
main:
        lui     a5,%hi(global_symbol)
        ld      a0,%lo(global_symbol)(a5)
        snez    a0,a0
        ret

$ riscv64-unknown-linux-gnu-objdump -d -r cmodel.o
cmodel.o:     file format elf64-littleriscv

Disassembly of section .text.startup:

0000000000000000 main:
   0:   000007b7                lui     a5,0x0
                        0: R_RISCV_HI20 global_symbol
                        0: R_RISCV_RELAX        *ABS*
   4:   0007b503                ld      a0,0(a5) # 0 main
                        4: R_RISCV_LO12_I       global_symbol
                        4: R_RISCV_RELAX        *ABS*
   8:   00a03533                snez    a0,a0
   c:   8082                    ret

$ riscv64-unknown-linux-gnu-objdump -d -r cmodel
Disassembly of section .text:

0000000000010330 main:
   10330:       67c9                    lui     a5,0x12
   10332:       0387b503                ld      a0,56(a5) # 12038 global_symbol
   10336:       00a03533                snez    a0,a0
   1033a:       8082                    ret
```

## `-mcmodel=medany` 是什么意思？

这选择了中等-任意（medium-any）[代码模型](#what-is-a-code-model)，这意味着程序及其静态定义的符号必须位于任何单个 2 GiB 的地址范围内。对全局符号的寻址使用 `auipc`/`addi` 指令对，这会发出 `R_RISCV_PCREL_HI20`/`R_RISCV_PCREL_LO12_I` 序列。以下是使用 medany 代码模型生成的一些代码示例（使用了 `-mexplicit-relocs`，以便使其与 [-mcmodel=medlow](#what-does--mcmodelmedlow-mean) 示例更清晰地匹配）：

> 译者注：`medlow` 使用绝对地址寻址 (`lui`)，代码和数据必须被链接在低 2GiB 地址空间内（靠近0）。`medany` 使用 PC 相对地址寻址 (`auipc`)，代码和数据可以被链接在 64 位地址空间的任何位置，只要它们之间的相对距离在 +/- 2GiB 范围内即可。这使得 `medany` 更适合生成位置无关代码 (PIC)。

```sh
$ cat cmodel.c
long global_symbol[2];

int main() {
  return global_symbol[0] != 0;
}

$ riscv64-unknown-linux-gnu-gcc cmodel.c -o cmodel -O3 --save-temps -mcmodel=medany -mexplicit-relocs

$ cat cmodel.s
main:
        .LA0: auipc     a5,%pcrel_hi(global_symbol)
        ld      a0,%pcrel_lo(.LA0)(a5)
        snez    a0,a0
        ret

$ riscv64-unknown-linux-gnu-objdump -d -r cmodel.o
cmodel.o:     file format elf64-littleriscv

SYMBOL TABLE:
0000000000000000 l    df *ABS*  0000000000000000 cmodel.c
0000000000000000 l    d  .text  0000000000000000 .text
0000000000000000 l    d  .data  0000000000000000 .data
0000000000000000 l    d  .bss   0000000000000000 .bss
0000000000000000 l    d  .text.startup  0000000000000000 .text.startup
0000000000000000 l       .text.startup  0000000000000000 .LA0
0000000000000000 l    d  .comment       0000000000000000 .comment
0000000000000000 g     F .text.startup  000000000000000e main
0000000000000010       O *COM*  0000000000000008 global_symbol

Disassembly of section .text.startup:

0000000000000000 main:
   0:   00000797                auipc   a5,0x0
                        0: R_RISCV_PCREL_HI20   global_symbol
                        0: R_RISCV_RELAX        *ABS*
   4:   0007b503                ld      a0,0(a5) # 0 main
                        4: R_RISCV_PCREL_LO12_I .LA0
                        4: R_RISCV_RELAX        *ABS*
   8:   00a03533                snez    a0,a0
   c:   8082                    ret

$ riscv64-unknown-linux-gnu-objdump -d -r cmodel.o
Disassembly of section .text:

0000000000010330 main:
   10330:       00002797                auipc   a5,0x2
   10334:       d087b503                ld      a0,-760(a5) # 12038 global_symbol
   10338:       00a03533                snez    a0,a0
   1033c:       8082                    ret
        ...
```

注意，`-mcmodel=medany` 目前默认为 `-mno-explicit-relocs`，这可能会对性能产生可观的影响。该性能影响有一些细微之处，所以我们将在后续的博客中讨论它。

## 代码模型和 ABI 之间的区别

一个常被误解的区别是代码模型和 ABI 之间的差异。ABI 决定了函数之间的接口，而代码模型决定了函数内部代码的生成方式。具体来说：两种 RISC-V 代码模型都将寻址符号的代码限制在 32 位偏移内，但在基于 RV64I 的系统上，它们仍然将指针编码为 64 位。

具体来说，这意味着用 `-mcmodel=medany` 编译的函数可以被用 `-mcmodel=medlow` 编译的函数调用，反之亦然。为了允许链接可执行文件，这两个函数对符号寻址施加的限制都需要得到满足，但这只是一个普遍为真的约束。由于代码模型不影响内存中结构体的布局或参数在函数间传递的方式，它对程序来说基本上是透明的。

与之形成对比的是链接为两种不同 ABI 生成的代码，这是无效的。想象一个包含 `double` 参数的函数。一个为 `lp64d` 编译的函数会期望这个参数在浮点寄存器中。当被一个为 `lp64` 编译的函数调用时，后者会将参数放在一个 X 寄存器（整数寄存器）中，程序将无法正常工作。

## 代码模型和链接器松弛

到目前为止，我们还没有讨论代码模型如何与[链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)相互作用，主要是因为答案现在相当简单：一切都能正常工作，前提是你使用各种工具链组件的 RISC-V 分支，因为还有一些补丁尚未进入上游。

链接器松弛实际上是一个足够重要的优化，以至于它显著地影响了 RISC-V ISA：链接器松弛允许 RISC-V 放弃一种寻址模式，否则这种寻址模式对于在许多代码库上获得合理性能是必需的。在 RISC-V 目标上，以下寻址模式是可用的：

*   距离 0（或 `__global_pointer$`）7 位偏移内的符号：2 字节。
*   距离 0（或 `__global_pointer$`）12 位偏移内的符号：4 字节。
*   距离 0 17 位偏移内的符号：6 字节。
*   距离 0 32 位偏移内的符号：8 字节。在 RV32I 上，这是整个地址空间。

> 译者注：这里的字节数指的是生成地址和加载/存储该地址所需的指令序列的总大小。例如，2字节对应一条压缩指令，4字节对应一条标准指令，6字节对应一条标准指令+一条压缩指令，8字节对应两条标准指令。

这一切都可以通过单个代码模型实现，并且在使用单个硬件寻址模式（寄存器+偏移）的同时，通过八种指令格式（U, I, S, CI, CR, CIW, CL, 和 CS）而没有任何模式位。你可以将此视为一种可选硬件支持的可变长度地址编码——更多信息请参见“Compressed Macro-Op Fusion”论文。由于这种压缩全部由链接器透明地实现，我们只需要一个代码模型。将这种行为与 ARMv8 GCC 移植进行对比，后者要求为其可以发出的每种地址生成序列选择不同的代码模型。

实现可变长度寻址序列通常是 CISC 处理器才有的功能，它们通过在硬件中实现大量的寻址模式，并在汇编时尽可能地收缩寻址序列来实现这一点。RISC-V 使用可融合的多指令寻址序列和链接器松弛的方法，既允许简单的实现，又导致了相似的代码大小，兼具二者之长。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   All Aboard 系列，第 4 部分：RISC-V 代码模型 (当前页面)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客马拉松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)
