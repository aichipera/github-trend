# All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数

> 本文于2017年8月14日发布于 https://www.sifive.com/blog/all-aboard-part-1-compiler-args

在我们登上 RISC-V 这趟列车之前，我们得在一个象征性的售票处稍作停留：也就是那些针对特定机器的 GCC 命令行参数。这些参数都以 `-m` 开头，并且都是 RISC-V 架构移植所特有的。总的来说，我们试图让这些参数遵循现有的惯例，但就像其他所有事情一样，这里面也存在足够多的特殊之处，值得用一篇博客文章来专门说明。本篇博客将讨论对于 RISC-V ISA 最为基础的几个参数：`-march`、`-mabi` 和 `-mtune`。

在 SiFive 的接口稳定下来之前，我们已经拥有一个功能完备的 GCC 移植很长时间了，这样做的一个优势是，我们可以为 RISC-V 的 C 和 C++ 编译器设计一个深思熟虑的命令行接口。这使得我们能够让 GNU 工具（GCC 和 binutils）和 LLVM 工具都提供相同的命令行接口，同时也避免了用户需要通过编译器的 `-Wa` 和 `-Wl` 参数来直接向汇编器或链接器传递标志。

为了确保 RISC-V 编译器的命令行接口在未来易于扩展，我们决定采用一种方案，让用户通过三个参数来描述他们试图为其编译的 RISC-V 目标：

*   `-march=ISA` 选择目标架构。这控制了编译器可以使用的指令和寄存器。
*   `-mabi=ABI` 选择目标 ABI。这控制了调用约定（哪些参数通过哪些寄存器传递）以及数据在内存中的布局。
*   `-mtune=CODENAME` 选择目标微架构。这会告知 GCC 每条指令的性能情况，使其能够执行针对特定目标的优化。

## `-march` 参数

`-march` 参数基本上是由 RISC-V 用户级 ISA 手册定义的。`-march` 控制了编译器允许生成指令的指令集。这个参数决定了一个程序可以在哪些实现上运行：任何包含了编译程序时所用 `-march` 值的 RISC-V 兼容系统都应该能够运行该程序。

> 译者注：这里的“包含” (subsume) 指的是硬件实现的指令集是编译器 `-march` 指定的指令集的超集。例如，一个为 `rv64im` 编译的程序可以在一个实现了 `rv64imafdc` 的硬件上运行。

具体来说：RISC-V 用户级 ISA 2.2 版本定义了三个目前被工具链支持的基础 ISA：

*   `RV32I`：一个加载-存储（load-store）ISA，拥有 32 个 32 位通用整数寄存器。
*   `RV32E`：RV32I 的一个嵌入式版本，只有 16 个整数寄存器。
*   `RV64I`：RV32I 的一个 64 位版本，其通用整数寄存器是 64 位宽的。

除了这些基础 ISA，还规定了一些扩展。已被规定且被工具链支持的扩展有：

*   M：整数乘法和除法 (Integer Multiplication and Division)
*   A：原子指令 (Atomic Instructions)
*   F：单精度浮点 (Single-Precision Floating-Point)
*   D：双精度浮点 (Double-Precision Floating-Point)
*   C：压缩指令 (Compressed Instructions)

RISC-V ISA 字符串是通过将支持的扩展按上述顺序列在基础 ISA 之后来定义的。例如，拥有 32 个 32 位整数寄存器和乘法指令的 RISC-V ISA 将表示为 `RV32IM`。用户可以通过将小写的 ISA 字符串传递给 GCC 的 `-march` 参数来控制 GCC 在生成汇编代码时使用的指令集：例如 `-march=rv32im`。

在不支持特定操作的 RISC-V 系统上，可以使用仿真程序（emulation routines）来提供缺失的功能。例如，下面的 C 代码：

```c
    double dmul(double a, double b) {
      return a * b;
    }
```

当使用 D 扩展编译时，将直接编译成一条浮点乘法指令：

```sh
    $ riscv64-unknown-elf-gcc test.c -march=rv64imafdc -mabi=lp64d -o- -S -O3
    dmul:
      fmul.d  fa0,fa0,fa1
      ret
```

但如果没有 D 扩展，则会编译成一个对仿真程序的调用：

```sh
    $ riscv64-unknown-elf-gcc test.c -march=rv64i -mabi=lp64 -o- -S -O3
    dmul:
      add     sp,sp,-16
      sd      ra,8(sp)
      call    __muldf3
      ld      ra,8(sp)
      add     sp,sp,16
      jr      ra
```

对于 M 和 F 扩展能够轻易实现的 C 内部函数（intrinsics），也存在类似的仿真程序。截至本文撰写之时，还没有 A 扩展的仿真程序，因为它们在 Linux 上游化过程中被拒绝了——这在未来可能会改变，但就目前而言，我们计划强制要求能够运行 Linux 的机器必须包含 A 扩展，作为 RISC-V 平台规范的一部分。

## `-mabi` 参数

GCC 的 `-mabi` 参数指定了生成代码所遵循的整数和浮点 ABI。就像 `-march` 参数指定了生成代码可以在何种硬件上运行一样，`-mabi` 参数指定了生成代码可以与何种软件进行链接。我们对整数 ABI 使用标准的命名方案（`ilp32` 或 `lp64`），并在其后附加一个字母来选择 ABI 使用的浮点寄存器（`ilp32` vs `ilp32f` vs `ilp32d`）。为了让目标文件能够链接在一起，它们必须遵循相同的 ABI。

> 译者注：ABI，即应用程序二进制接口 (Application Binary Interface)。它定义了程序模块间的接口，包括函数调用约定、数据类型大小和对齐、目标文件格式等。

RISC-V 定义了两种整数 ABI 和三种浮点 ABI，它们共同组成一个单一的 ABI 字符串。整数 ABI 遵循标准的 ABI 命名方案：

*   `ilp32`：`int`、`long` 和指针都是 32 位长。`long long` 是 64 位类型，`char` 是 8 位，`short` 是 16 位。
    > 译者注：原文中 `long` is a 64-bit type 疑似笔误。在 `ilp32` 模型中，`long` 是 32 位的。`long long` 才是 64 位的。
*   `lp64`：`long` 和指针是 64 位长，而 `int` 是 32 位类型。其他类型与 `ilp32` 保持一致。

而浮点 ABI 是 RISC-V 特有的补充：

*   "" (空字符串)：没有浮点参数通过寄存器传递。这被称为软浮点(soft-float) ABI。
*   `f`：32 位及更小的浮点参数通过寄存器传递。这个 ABI 需要 F 扩展，因为没有 F 扩展就没有浮点寄存器。
*   `d`：64 位及更小的浮点参数通过寄存器传递。这个 ABI 需要 D 扩展。

就像 ISA 字符串一样，ABI 字符串被连接在一起并通过 `-mabi` 参数传递给 GCC。为了解释为什么 ISA 和 ABI 应该被视为两个独立的参数，让我们来看几个 `-march`/`-mabi` 的组合：

*   `-march=rv32imafdc -mabi=ilp32d`：可以生成硬件浮点指令，并且浮点参数通过寄存器传递。这类似于 ARM GCC 的 `-mfloat-abi=hard` 参数。
*   `-march=rv32imac -mabi=ilp32`：不能生成浮点指令，也没有浮点参数通过寄存器传递。这类似于 ARM GCC 的 `-mfloat-abi=soft` 参数。
*   `-march=rv32imafdc -mabi=ilp32`：可以生成硬件浮点指令，但没有浮点参数会通过寄存器传递。这类似于 ARM GCC 的 `-mfloat-abi=softfp` 参数，通常用于在一个支持硬浮点的系统上与软浮点二进制文件进行接口交互。
*   `-march=rv32imac -mabi=ilp32d`：非法组合，因为 ABI 要求浮点参数通过寄存器传递，但 ISA 却没有定义任何浮点寄存器来传递它们。

作为一个更具体的例子，让我们来看一个简单的 C 函数，它接受两个双精度参数并返回它们的乘积。为了在所有情况下都明确参数的位置，我们将在函数调用和乘法之间颠倒参数的顺序：

```c
    double dmul(double a, double b) {
      return b * a;
    }
```

第一种情况是最简单的：如果 ABI 和 ISA 都不包含浮点硬件的概念，那么 C 编译器就不能发出任何与浮点相关的指令。在这种情况下，会使用仿真程序来执行计算，并且参数通过整数寄存器传递。如你所见，双精度参数通过 32 位整数寄存器对传递，参数顺序被交换，`ra` 被保存（因为它是被调用者保存的），仿真程序被调用，栈被展开，然后返回结果（结果已经从 `__muldf3` 放在 `a0,a1` 中）。

```sh
    $ riscv64-unknown-elf-gcc test.c -march=rv32imac -mabi=ilp32 -o- -S -O3
    dmul:
      mv      a4,a2
      mv      a5,a3
      add     sp,sp,-16
      mv      a2,a0
      mv      a3,a1
      mv      a0,a4
      mv      a1,a5
      sw      ra,12(sp)
      call    __muldf3
      lw      ra,12(sp)
      add     sp,sp,16
      jr      ra
```

第二种情况与此完全相反：所有东西都在硬件中支持。在这种情况下，我们可以发一条 `fmul.d` 指令来执行计算，当寄存器分配正确时，它能处理输入参数的颠倒并产生返回值。

```sh
    $ riscv64-unknown-elf-gcc test.c -march=rv32imafdc -mabi=ilp32d -o- -S -O3
    dmul:
      fmul.d  fa0,fa1,fa0
      ret
```

最后一种情况揭示了为什么 RISC-V 编译器的 `-march` 和 `-mabi` 参数是分开的：用户可能希望生成的代码能够与那些为不支持特定扩展的系统设计的代码进行链接，同时又能利用特定扩展中存在的额外指令。这是一个在处理需要集成到新系统中的遗留库时常见的问题，因此我们设计了我们的编译器参数和多库路径（multilib paths）来清晰地集成这种工作流程。

生成的代码基本上是上述两种输出的混合体：参数通过 `ilp32` ABI 指定的寄存器传递（而不是 `ilp32d` ABI，后者可以将这些参数通过寄存器传递），但在函数内部，编译器可以自由地使用 `rv32imafdc` ISA 的全部能力来实际计算结果。因此，编译器在内存中生成双精度参数（这是在 `rv32` 上构造一个 double 的唯一方法），将它们加载到 `F` 寄存器中，执行计算，将 `F` 寄存器中的结果存回栈中，并将结果加载到符合 ABI 的返回寄存器（`a0` 和 `a1`）中。虽然这比编译器在允许充分利用 D 扩展寄存器时生成的代码效率低，但它比没有 D 扩展指令来计算浮点乘法要高效得多。

```sh
    $ riscv64-unknown-elf-gcc test.c -march=rv32imafdc -mabi=ilp32 -o- -S -O3
    dmul:
      add     sp,sp,-16
      sw      a0,8(sp)
      sw      a1,12(sp)
      fld     fa5,8(sp)
      sw      a2,8(sp)
      sw      a3,12(sp)
      fld     fa4,8(sp)
      fmul.d  fa5,fa5,fa4
      fsd     fa5,8(sp)
      lw      a0,8(sp)
      lw      a1,12(sp)
      add     sp,sp,16
      jr      ra
```

最后一种可能的 ABI/ISA 组合很简单：它是非法的。编译器不可能为一个要求在 `F` 寄存器中传递参数的 ISA 生成代码，如果它无法访问操作这些寄存器所需的指令。由于这必定是用户错误，我们立即退出。

```sh
    $ riscv64-unknown-elf-gcc test.c -march=rv32imac -mabi=ilp32d -o- -S -O3
    cc1: error: requested ABI requires -march to subsume the 'D' extension
```

## `-mtune` 参数

在指定目标时涉及的最后一个编译器参数是这组参数中最简单的一个。`-march` 参数可能导致系统无法执行代码，`-mabi` 参数可能导致目标文件彼此不兼容，而 `-mtune` 参数应该只会改变生成代码的性能。就目前而言，我们实际上没有任何用于 RISC-V 系统的调优模型。除非你刚刚在我们的 GCC 移植中添加了一个新的调优参数，否则你可能不需要对这个参数做任何事情。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://mp.weixin.qq.com/s/qqAVcsux02Tw5_gugQiasQ)
*   All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数 (当前页面)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)