

# All Aboard 系列，第 2 部分：ELF 工具链中的重定位

> 本文于**2017年8月21日**发布于 https://www.sifive.com/blog/all-aboard-part-2-relocations

我们探索 RISC-V 工具链的第一站，将是对 ELF 重定位（relocations）及其在 RISC-V 工具链中用法的概述。为了避免篇幅过长，我们将把链接器松弛（linker relaxations）及其对性能的影响留到后续的博客文章中讨论。本文的示例经过精心构造，是不可松弛的，以避免混淆。此外，我们只讨论静态链接可执行文件所使用的重定位，避免讨论位置无关可执行文件（position independent executables），并暂不考虑线程局部存储（thread local storage）——就像链接器松弛一样，这些都值得用一整篇文章来单独讨论。在后续的博客文章中，还会有更多关于重定位的内容。

## C 程序中重定位的一个例子

重定位这个概念的存在，是由于大多数工具链中编译器和链接器是分离的。虽然本文的具体内容仅适用于基于 ELF 的 RISC-V 工具链（即 GCC+binutils 或 LLVM），但重定位的一般概念存在于更广泛的编译器中，比如 Hotspot。由于重定位的存在是为了在编译器和链接器之间传递信息，让我们首先看看一个简单的程序是如何被编译的。以下面这段 C 代码为例：

```c
long global_symbol[2];

int main() {
  return global_symbol[0] != 0;
}
```

尽管对于这个简单案例，一次 GCC 调用就能生成一个二进制文件，但在这背后，GCC 驱动脚本实际上是依次运行了预处理器、编译器、汇编器，最后是链接器。GCC 的 `--save-temps` 参数允许用户查看所有这些中间文件，这是深入探究工具链内部的一个有用参数。

```sh
$ riscv64-unknown-linux-gnu-gcc relocation.c -o relocation -O3 --save-temps
```

GCC 包装脚本运行的每一步都会生成一个文件：

*   `relocation.i`：预处理后的源文件，它会展开任何预处理器指令（如 `#include` 或 `#ifdef`）。
*   `relocation.s`：实际编译器的输出，这是一个汇编文件（RISC-V 汇编格式的文本文件）。
*   `relocation.o`：汇编器的输出，这是一个未链接的目标文件（一个 ELF 文件，但不是可执行的 ELF）。
*   `relocation`：链接器的输出，这是一个已链接的可执行文件（一个可执行的 ELF 文件）。

第一步是运行预处理器。由于这是一个没有预处理器宏的简单源文件，预处理的运行过程相当乏味：它只是发出一些指令，用于后续如果生成调试信息时使用：

```sh
$ cat relocation.i
# 1 "relocation.c"
# 1 "built-in"
# 1 "command-line"
# 31 "command-line"
# 1 "/scratch/palmer/work/upstream/riscv-gnu-toolchain/build/install/sysroot/usr/include/stdc-predef.h" 1 3 4
# 32 "command-line" 2
# 1 "relocation.c"
long global_symbol;

int main() {
  return global_symbol != 0;
}
```

预处理后的输出随后被送入编译器，生成一个汇编文件。正是在这一点上，我们开始看到为什么重定位是必要的。这个文件是包含 RISC-V 汇编代码的纯文本，因此易于阅读，让我们现在就来看看：

```sh
$ cat relocation.s
main:
  lui   a5,%hi(global_symbol)
  ld    a0,%lo(global_symbol)(a5)
  snez  a0,a0
  ret
```

如果你不习惯阅读 RISC-V GCC 移植的汇编输出，这可能看起来有点奇怪：这里有一对额外的寻址模式，它们没有在 RISC-V 指令手册的任何地方列出，而且看起来也不像是硬件能够合理实现的：`%hi(global_symbol)` 和 `%lo(global_symbol)(a5)`。

这些寻址模式的存在是为了让编译器能够寻址全局符号。寻址全局符号的根本问题是，编译器必须发出汇编指令来访问这些符号，但这些全局符号的实际地址直到链接时才能知道，这是一个不可能完成的任务。举一个具体的例子，试着想一下编译器会为寻址 `global_symbol` 的 `lui` 指令发出什么样的比特位。

重定位解决了这个矛盾：当编译器无法知道某个特定指令应该发出的比特位时，它会为该指令发出任意的比特位，并同时发出一个重定位条目。这个重定位条目指向将要被填充的比特位，并包含足够的信息让链接器来填充这些比特位。

具体细节最好通过例子来解释，所以让我们来看看上面的简单程序，看看这一切是如何工作的。工具链中的下一个环节是汇编器，它接收上面的汇编文件并生成一个尚未链接的 ELF 目标文件。你可以用 `objdump` 来检查这些目标文件，我已在下面展示了：

```sh
$ riscv64-unknown-linux-gnu-objdump -d -t -r relocation.o

relocation.o:     file format elf64-littleriscv

SYMBOL TABLE:
0000000000000000 l    df *ABS*  0000000000000000 relocation.c
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

现在是你第一次明确看到重定位的地方（只有当 `-r` 参数传递给 `objdump` 时才会显示）。在这里，我们可以看到四个 RISC-V 特定的重定位，成对出现：一个 `R_RISCV_HI20`+`R_RISCV_RELAX` 对用于 `lui`，一个 `R-RISCV_LO12_I`+`R_RISCV_RELAX` 对用于 `ld`。`R_RISCV_RELAX` 重定位的存在仅仅是为了表明对前一个重定位执行链接器松弛是合法的。由于我们在这篇博客中不讨论链接器松弛，我们现在可以忽略这些条目。

另外两个重定位与 RISC-V ISA 中存在的寻址模式明确配对：`R_RISCV_HI20` 与 U-format 立即数配对，而 `R_RISCV_LO12_I` 与 I-format 立即数配对。总的来说，你会发现每个带有立即数的寻址模式至少会有一个重定位来填充那个立即数——有时如果该指令格式也用于链接更复杂的符号形式（例如，PIC 或 TLS 重定位），还会有更多一些。

在我们深入研究重定位之前，让我们快速看看当可以正确填充重定位时，工具链是如何工作的。工具链的下一个环节是链接器，它会消费汇编器生成的重定位，以填充输出的 ELF 可执行文件中的相关比特位。现在程序已经包含了所有的 glibc 启动代码，所以它变得相当大。因此，我下面只贴出相关的片段：

```sh
$ riscv64-unknown-linux-gnu-objdump -d -t -r relocation
relocation:     file format elf64-littleriscv

SYMBOL TABLE:
0000000000012038 g     O .bss 0000000000000010              global_symbol
...

Disassembly of section .text:

0000000000010330 main:
 10330:       67c9                    lui     a5,0x12
 10332:       0387b503                ld      a0,56(a5) # 12038 global_symbol
 10336:       00a03533                snez    a0,a0
 1033a:       8082                    ret
```

正如你所见，符号表现在有了 `global_symbol` 的实际地址，被重定位引用的指令中有了一些非零的比特位被填充以引用 `global_symbol`，并且重定位已经从 ELF 文件中被移除，因为它们不再是必需的——这严格来说只在静态链接符号的情况下成立，对于动态符号的重定位则会推迟到加载器执行。

## `relocation truncated to fit` 错误信息

现在你对重定位有了一些了解，我们可以讨论大多数人唯一接触到重定位的情形：链接时出现的 `relocation truncated to fit` 错误信息。对于不理解重定位的人来说，很难解释这个信息，但如果你理解什么是重定位，那么它其实并不是一个那么难懂的错误信息。

为了解释这个错误信息，我们将从一个极其简单的程序开始。在这种情况下，我们不希望 C 库的任何东西出现在我们的错误信息中，所以我们定义了 `_start` 而不是 `main`，然后通过向 GCC 传递 `-nostdlib -nostartfiles` 来避免任何标准库对象——这个程序实际上无法工作，但它足以解释正在发生的事情。使用 `-Wl,-Ttext-segment,0x80000000` 移动 text 段实际上会触发这个 bug，下面你将看到原因：

```sh
$ cat reloc_fail.c
long global_symbol;
int _start() {
  return global_symbol;
}
$ riscv64-unknown-linux-gnu-gcc reloc_fail.c -o reloc_fail -O3 -nostartfiles -nostdlib --save-temps  -Wl,-Ttext-segment,0x80000000
reloc_fail.o: In function `_start':
reloc_fail.c:(.text+0x0): relocation truncated to fit: R_RISCV_HI20 against symbol `global_symbol' defined in COMMON section in reloc_fail.o
/scratch/palmer/work/20170725-binutils-2.29/install/bin/../lib/gcc/riscv64-unknown-linux-gnu/7.1.1/../../../../riscv64-unknown-linux-gnu/bin/ld: final link failed: Symbol needs debug section which does not exist
collect2: error: ld returned 1 exit status
```

表面上看，这像是一个非常吓人的错误信息：有各种对临时对象的引用；提到了符号、段和重定位；还有一个关于调试段的奇怪信息。这通常是人们放弃并求助于工具链黑客的时候，但凭借你新学的重定位知识，你应该能弄清楚这里发生了什么。

首先，让我们只关注错误信息的重要部分，忽略所有实际上不相关的冗余信息。你真正需要看的错误是：

```
reloc_fail.c:(.text+0x0): relocation truncated to fit: R_RISCV_HI20 against symbol `global_symbol'
```

这简单地说明了编译器针对地址 `global_symbol` 生成了一个 `R_RISCV_HI20` 重定位，但链接器无法将该符号的完整地址放入该重定位指定的比特位中。短语 "truncated to fit"（为适配而截断）有点奇怪：链接器实际上是说，重定位中的地址必须被截断才能放入重定位分配的比特位中，但因为这是一个错误，链接器实际上并没有截断任何东西。

为了开始真正探究这个错误信息的“为什么”，我们首先需要查看链接器的输入，在这种情况下是汇编器生成的目标文件。像上面的例子一样，我们需要重定位，因为编译器需要引用一个它无法知道地址的全局符号。

```sh
$ riscv64-unknown-linux-gnu-objdump -d -r reloc_fail.o
reloc_fail.o:     file format elf64-littleriscv

Disassembly of section .text:

0000000000000000 <_start>:
   0:   000007b7                lui     a5,0x0
                        0: R_RISCV_HI20 global_symbol
                        0: R_RISCV_RELAX        *ABS*
   4:   0007a503                lw      a0,0(a5) # 0 <_start>
                        4: R_RISCV_LO12_I       global_symbol
                        4: R_RISCV_RELAX        *ABS*
   8:   8082                    ret
```

我们实际上看不到链接器的输出，因为链接这个文件是不可能的。由于我讨厌手动计算，我干脆修改了链接器，在执行重定位时忽略范围检查，补丁如下所示：

```sh
$ git diff
diff --git a/bfd/elfnn-riscv.c b/bfd/elfnn-riscv.c
index 3c04507623c3..f8a97411de35 100644
--- a/bfd/elfnn-riscv.c
+++ b/bfd/elfnn-riscv.c
@@ -1492,8 +1492,6 @@ perform_relocation (const reloc_howto_type *howto,
     case R_RISCV_GOT_HI20:
     case R_RISCV_TLS_GOT_HI20:
     case R_RISCV_TLS_GD_HI20:
-      if (ARCH_SIZE > 32 && !VALID_UTYPE_IMM (RISCV_CONST_HIGH_PART (value)))
-       return bfd_reloc_overflow;
       value = ENCODE_UTYPE_IMM (RISCV_CONST_HIGH_PART (value));
       break;
```

有了上面的补丁，链接器可以生成一个不正确的目标文件供我们检查，如下所示：

```sh
$ riscv64-unknown-linux-gnu-objdump -d -t reloc_fail
reloc_fail:     file format elf64-littleriscv

SYMBOL TABLE:
00000000800000b0 l    d  .text  0000000000000000 .text
00000000800010c0 l    d  .bss   0000000000000000 .bss
0000000000000000 l    d  .comment       0000000000000000 .comment
0000000000000000 l    df *ABS*  0000000000000000 reloc_fail.c
00000000800018ba g       .text  0000000000000000 __global_pointer$
00000000800010c0 g     O .bss   0000000000000008 global_symbol
00000000800000b0 g     F .text  000000000000000a _start
00000000800010ba g       .bss   0000000000000000 __bss_start
00000000800010ba g       .bss   0000000000000000 _edata
00000000800010c8 g       .bss   0000000000000000 _end

Disassembly of section .text:

00000000800000b0 <_start>:
    800000b0:   800017b7                lui     a5,0x80001
    800000b4:   0c07a503                lw      a0,192(a5) # ffffffff800010c0 <__global_pointer$+0xfffffffefffff806>
    800000b8:   8082                    ret
```

我们可以清楚地看到，加载 `global_symbol` 值的指令实际上与符号表中列出的 `global_symbol` 的地址不匹配，这正是 `relocation truncated to fit` 错误信息想要表达的。在 `R_RISCV_HI20`+`R_RISCV_LO12_I` 重定位对的特定情况下，可以生成的最大绝对地址是 `0x7FFFFFFF`——请记住，在 RISC-V 上，U-type 立即数是有符号的，因此任何更大的绝对地址在 RV64 上都会溢出。

> 译者注：`lui` 指令将 20 位立即数加载到寄存器的高 20 位，低 12 位补 0。`addi` 等 I-type 指令使用 12 位有符号立即数。两者组合 `lui rd, imm_hi; addi rd, rd, imm_lo` 可以构造一个 32 位的地址。由于 `imm_lo` 是有符号的，当 `imm_hi` 的最高位为 1 (即地址大于 `0x7FFFFFFF` 时)，`imm_hi` 部分会被符号扩展，导致 `addi` 时的加法产生错误的结果。例如，地址 `0x800010C0`，`lui` 加载 `0x80001` (HI20 部分)，`ld` 的偏移是 `0x0C0` (LO12 部分)。但 `0x800010C0` 的高位是 1，在 RV64 中，`lui` 产生的地址 `0x80001000` 会被符号扩展为 `0xFFFFFFFF80001000`，再与 `0x0C0` 相加就错了。这就是溢出的原因。

虽然每个架构在链接时都会执行一些重定位，但 RISC-V 比任何其他架构都更积极地利用链接器的重定位基础设施，因此这类问题可能会比在其他移植中更频繁地出现。我们将在博客中大量讨论重定位，因为它们经常驱动其他工具链的设计问题。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   All Aboard 系列，第 2 部分：ELF 工具链中的重定位 (当前页面)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)
