# All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛

> 本文于**2017年8月28日**发布于 https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain


[上周的博客文章](https://www.sifive.com/blog/all-aboard-part-2-relocations)讨论了重定位及其在 RISC-V 工具链中的应用。本周，我们将更深入地探讨 RISC-V 链接器，讨论链接器松弛（linker relaxation），这是一个非常重要的概念，它极大地影响了 RISC-V ISA 的设计。链接器松弛是一种在链接时优化程序的机制，与传统的在编译时进行的程序优化不同。本博客将通过一个例子来追踪链接器松弛在工具链中的过程，演示链接器松弛如何有意义地提高一个真实程序的性能，并介绍一种新的 RISC-V 重定位。我们将暂不讨论链接器松弛对 RISC-V ISA 的影响，直到另一篇博客文章再作探讨。

> 译者注：链接器松弛 (Linker Relaxation) 是 RISC-V 工具链的一项关键优化。其核心思想是，编译器在生成代码时，会使用最保守、最通用的指令序列（通常更长）来完成某项任务（如函数调用或全局变量访问），因为此时它并不知道符号的最终地址。链接器在链接阶段，当所有符号的地址都确定后，可以判断是否能用更短、更高效的指令序列来替换原有的序列。如果可以，链接器就会“松弛”掉原来的长指令序列，替换为短指令序列，从而优化代码大小和性能。这是 RISC-V 实现简洁指令集（特别是寻址模式）同时保持高性能和高代码密度的关键技术。

和上次一样，我们将从一个不链接任何其他东西的简单 C 测试程序开始。这个程序不会执行任何有意义的计算，其目的仅仅是足够简单以传达要点。这次我将跳过汇编部分：因为这篇文章是关于链接器的，所以我们直到获得目标文件才能真正讨论任何事情。既然你现在已经是工具链专家了，我就直接在这里执行一些命令：

```sh
$ cat test.c
int func(int a) __attribute__((noinline));
int func(int a) {
  return a + 1;
}

int _start(int a) {
  return func(a);
}
$ riscv64-unknown-linux-gnu-gcc test.c -o test -O3
$ riscv64-unknown-linux-gnu-objdump -d -r test.o
test.o:     file format elf64-littleriscv
Disassembly of section .text:

0000000000000000 <func>:
   0:   2505                    addiw   a0,a0,1
   2:   8082                    ret

0000000000000004 <_start>:
   4:   00000317                auipc   ra,0x0
                        4: R_RISCV_CALL func
                        4: R_RISCV_RELAX        *ABS*
   8:   00030067                jr      ra
```

现在你可以看到一个新的 RISC-V 重定位：`R_RISCV_CALL`。这个重定位位于一条 `auipc` 和一条 `jalr` 指令之间（这里因为是尾调用，被反汇编为 `jr` 伪指令），并指向应该是跳转目标的符号，在本例中是 `func` 符号。`R_RISCV_CALL` 重定位与一个 `R_RISCV_RELAX` 重定位配对，这允许链接器松弛这个重定位对——这正是本博客的重点！

为了理解松弛，我们首先必须稍微研究一下 RISC-V ISA。在 RISC-V ISA 中，有两个无条件控制转移指令：`jalr`，它跳转到一个由寄存器加上立即数偏移指定的绝对地址；和 `jal`，它跳转到一个由立即数指定的 PC 相对偏移。这个目标文件中的 `auipc`+`jalr` 对与单个 `jal` 之间的唯一区别是，前者可以寻址当前 PC 的 32 位有符号偏移，而 `jal` 只能寻址当前 PC 的 21 位有符号偏移，并且 `jal` 指令的大小是前者的一半（这可以很好地代表速度是其两倍）。

> 译者注：`auipc` (Add Upper Immediate to PC) 将一个 20 位的立即数左移 12 位后与 PC 相加，结果存入目标寄存器。`jalr` (Jump and Link Register) 则以寄存器的值为基地址，加上一个 12 位的有符号偏移量进行跳转。两者结合 `auipc rd, imm_hi; jalr x1, rd, imm_lo` 可以实现一个 PC 相关的 32 位远距离跳转。而 `jal` (Jump and Link) 指令本身只有一个 20 位的有符号立即数（乘以2后范围是 +/- 1MiB），所以跳转范围较小。

由于编译器无法知道 `_start` 和 `func` 之间的偏移是否能容纳在一个 21 位的偏移量内，它被迫生成更长的调用序列。我们不希望在不必要的情况下强加这种成本，所以我们转而在链接器中优化这种情况。让我们看看可执行文件，以了解链接器松弛的结果：

```sh
$ riscv64-unknown-linux-gnu-objdump -d -r test
test:     file format elf64-littleriscv

Disassembly of section .text:

0000000000010078 <func>:
   10078:       2505                    addiw   a0,a0,1
   1007a:       8082                    ret

000000000001007c <_start>:
   1007c:       ffdff06f                j       10078 <func>
```

如你所见，链接器知道从 `_start` 到 `func` 的调用可以容纳在 `jal` 指令的 21 位偏移范围内，并将其转换为单个指令。
> 译者注：这里的 `j` 是 `jal x0, offset` 的伪指令，表示一个不保存返回地址的跳转。

## RISC-V 中链接器松弛的实现

虽然链接器松弛的概念相当直接，但有很多棘手的细节需要正确处理，以确保链接器在各处都能产生正确的符号地址。据我所知，RISC-V 的 BFD 移植是最大胆使用链接器松弛的：基本上在链接时之前，没有任何 `.text` 段的符号地址是已知的。这带来了一些有趣的副作用：

*   对于任何可松弛的段，`.align` 指令必须由链接器处理。
*   调试信息必须被发出两次：一次由编译器为目标文件发出，另一次由链接器为可执行文件再次发出。

所有这些点可能都值得各自写一篇博客文章——有些已经计划好了，其他的则需要我先修复一些 bug，然后才好意思谈论它们 :)。

链接器松弛的实际实现，如你所料，是相当深奥的。代码位于 `binutils-gdb/bfd/elfnn-riscv.c` 文件中的 `_bfd_riscv_relax_section` 函数里，大致如下所示：

```c
_bfd_riscv_relax_section:
  if section shouldn't be relaxed:
    return DONE
  for each relocation:
    if relocation is relaxable:
      store per-relocation function pointer
    read the symbol table
    obtain the symbol's address
    call the per-relocation function
```

基本上，它所做的就是一些共享的簿记工作，然后调用一个特定于重定位的函数来实际松弛该重定位。这些松弛函数看起来都有些相似，所以我将展示一个松弛上面讨论的 `R_RISCV_CALL` 重定位的函数示例：

```c
_bfd_riscv_relax_call:
  compute a pessimistic address range
  if relocation doesn't fit into a UJ-type immediate:
    return DONE
  compute offsets for various short jumps
  if RVC is enabled and the relocation fits in a C.JAL:
    convert the jump to c.jal
  if relocation fits in an JAL:
    convert the jump to a jal
  if call target is near absolute address 0:
    convert the jump to a x0-offset JALR
  delete the JALR, as it's not necessary anymore
```

虽然这个特定的函数只松弛 `R_RISCV_CALL` 重定位，但它遵循了大多数松弛函数实现的模式：

```c
generic_relax_function:
  add some slack to the address, as all addresses can move
  for each possible instruction to shorten the relocation:
    if possible instruction can fit the target address:
      replace the relocation
      cleanup
      return DONE
  return DONE
```

对于 RISC-V 工具链知道如何松弛的每一类重定位，都有一个这样的函数：

*   `_bfd_riscv_relax_call`：通过 `R_RISCV_CALL` 和 `R_RISCV_CALL_PLT` 重定位，松弛双指令 `auipc`+`jalr` 序列。
*   `_bfd_riscv_relax_lui`：通过 `R_RISCV_HI20`+`R_RISCV_LO12_I` 类的重定位对，松弛双指令 `lui`+`addi` 类的序列。第二个指令/重定位可以是任何匹配 `R_RISCV_LO12_I` 或 `R_RISCV_LO12_S` 重定位的各种指令（`addi`, `lw`, `sd` 等）。
*   `_bfd_riscv_relax_pc`：通过 `R_RISCV_PCREL_HI20`+`R_RISCV_PCREL_LO12_I` 类的重定位对，松弛双指令 `auipc`+`addi` 类的序列。与 `lui` 的情况很像，第二个指令有多种可能的重定位类型，所有这些都是 PC 相关的。
*   `_bfd_riscv_relax_tls_le`：在使用本地可执行模型时，松弛线程局部存储（TLS）的引用。我们将在后续的博客中讨论 TLS，因为这里有很多内容。
*   `_bfd_riscv_relax_align`：松弛文本段中的 `.align` 指令。这是我们稍后会讨论的另一个，但这里有一个特别有趣的约束是，`R_RISCV_ALIGN` 重定位必须为了正确性而被松弛，这意味着即使在禁用松弛时它们也会被松弛。

## 针对全局指针进行松弛

链接器松弛似乎为了一个小小的收益而引入了巨大的复杂性：我们以链接时之前不知道任何 `.text` 段符号地址为代价，将少数序列缩短了一个指令。但事实证明，链接器松弛对于在真实代码上获得良好性能非常重要。在我们第一次审视真实代码时，我们将看一下 Dhrystone 基准测试——除了超级简单之外，Dhrystone 还花费大量时间从全局变量加载数据，因此它能非常清晰地从链接器松弛中受益。

让我们先看看 Dhrystone 的源代码。虽然它比本博客中出现的例子要复杂一些，但如果你仔细看，代码实际上是相当直接的。这里是一个 Dhrystone 函数的源码，以及它引用的各种全局变量的定义：

```c
/* Global Variables: */
Boolean         Bool_Glob;
char            Ch_1_Glob,
                Ch_2_Glob;

Proc_4 () /* without parameters */
/*******/
    /* executed once */
{
  Boolean Bool_Loc;

  Bool_Loc = Ch_1_Glob == 'A';
  Bool_Glob = Bool_Loc | Bool_Glob;
  Ch_2_Glob = 'B';
} /* Proc_4 */
```

如你所见，为了进行一个简单的比较和逻辑运算，代码执行了三次对全局变量的访问。虽然这可能看起来有点傻，但 Dhrystone 基准测试的很多部分都是这样的。由于 Dhrystone 基本上是唯一一个能*在任何地方*运行的基准测试（例如，SPECInt 无法在我的手表上运行），它仍然被用作许多微架构比较的基线，所以我们需要让它跑得快。

为了理解在这种情况下执行的具体松弛，最好从工具链在此优化前生成的代码开始，我已将其复制如下：

```asm
0000000040400826 <Proc_4>:
    40400826:   3fc00797                auipc   a5,0x3fc00
    4040082a:   f777c783                lbu     a5,-137(a5) # 8000079d <Ch_1_Glob>
    4040082e:   3fc00717                auipc   a4,0x3fc00
    40400832:   f7272703                lw      a4,-142(a4) # 800007a0 <Bool_Glob>
    40400836:   fbf78793                addi    a5,a5,-65
    4040083a:   0017b793                seqz    a5,a5
    4040083e:   8fd9                    or      a5,a5,a4
    40400840:   3fc00717                auipc   a4,0x3fc00
    40400844:   f6f72023                sw      a5,-160(a4) # 800007a0 <Bool_Glob>
    40400848:   3fc00797                auipc   a5,0x3fc00
    4040084c:   04200713                li      a4,66
    40400850:   f4e78a23                sb      a4,-172(a5) # 8000079c <Ch_2_Glob>
    40400854:   8082                    ret
```

如你所见，这个函数由 13 条指令组成，其中 4 条是 `auipc` 指令。所有这些 `auipc` 指令都用于为后续的内存访问计算全局变量的地址，并且所有这些生成的地址都在彼此的 12 位偏移范围内。如果你在想“我们实际上只需要其中一条 `auipc` 指令”，那么你既对又错：虽然我们可以生成一条 `auipc`（但这需要一些我们尚未完成的 GCC 工作，因此是未来博客文章的主题），但我们实际上可以做得更好，只用*零条* `auipc` 指令！

如果你刚刚费力地查阅了 RISC-V ISA 手册，想找到一条能单指令加载 `Ch_1_Glob`（位于 `0x8000079D`）的指令，那么你现在可以放弃了，因为根本没有这样的指令。当然，这里有一个技巧——在寄存器丰富、寻址模式贫乏的 ISA 上，通常会有一个专用的 ABI 寄存器，称为全局指针（global pointer），它包含 `.data` 段中的一个地址。链接器随后能够松弛对位于该值 12 位有符号偏移范围内的全局变量的访问——本质上，我们只是将 `lui` 的结果缓存到了全局指针寄存器中，从而优化了这个常见的代码路径。

> 译者注：全局指针 (Global Pointer, `gp` or `x3`) 是 RISC-V ABI 中一个重要的寄存器。它由启动代码设置为指向静态数据区（`.sdata` 和 `.sbss`）中间的某个位置。这样，编译器就可以通过 `gp` 加上一个短的（12位）偏移量来访问大部分全局变量和静态变量，从而将原本需要 `lui`+`ld/sd` 两条指令的访问序列，优化成一条 `ld/sd` 指令，极大地提高了代码密度和性能。这就是针对 `gp` 的链接器松弛。

为了更深入地了解这是如何工作的，让我们看一下 GCC 为 RISC-V 默认链接器脚本的一段片段：

```ld
/* 我们希望小数据段放在一起，这样单指令偏移
   就可以访问它们全部，并且初始化的数据都在未初始化的数据之前，
   这样我们可以缩短磁盘上的段大小。 */
.sdata          :
{
  __global_pointer$ = . + 0x800;
  *(.srodata.cst16) *(.srodata.cst8) *(.srodata.cst4) *(.srodata.cst2) *(.srodata .srodata.*)
  *(.sdata .sdata.* .gnu.linkonce.s.*)
}
_edata = .; PROVIDE (edata = .);
. = .;
__bss_start = .;
.sbss           :
{
  *(.dynsbss)
  *(.sbss .sbss.* .gnu.linkonce.sb.*)
  *(.scommon)
```

如你所见，神奇的 `__global_pointer$` 符号被定义为指向 `.sdata` 段开始处之后 `0x800` 字节的位置。`0x800` 这个魔术数字允许从 `__global_pointer$` 开始的有符号 12 位偏移能够寻址到 `.sdata` 段开始处的符号。链接器假设如果这个符号被定义了，那么 `gp` 寄存器就包含那个值，然后它就可以用这个值来松弛对该 12 位范围内的全局符号的访问。编译器将 `gp` 寄存器视为一个常量，所以它不需要被保存或恢复，这意味着它通常只由 ELF 的入口点 `_start` 来写入。这里是来自 RISC-V newlib 移植的 `crt0.S` 文件的一个例子：

```asm
.option push
.option norelax
1:auipc gp, %pcrel_hi(__global_pointer$)
  addi  gp, gp, %pcrel_lo(1b)
.option pop
```

注意，在设置 `gp` 时，我们需要禁用松弛，否则链接器会把这个双指令序列松弛成 `mv gp, gp`。

松弛的实际实现，位于 `_bfd_riscv_relax_lui` 和 `_bfd_riscv_relax_pc` 中，相当乏味。像所有其他的松弛一样，它执行一些边界检查，删除未使用的指令，然后将短偏移指令转换为另一种类型。我们可能会在未来的博客文章中更深入地探讨各种链接器松弛的实现，但现在我只把松弛后的输出放在这里，以证明它确实有效：

```asm
00000000400003f0 <Proc_4>:
    400003f0:   8651c783                lbu     a5,-1947(gp) # 80001fbd <Ch_1_Glob>
    400003f4:   8681a703                lw      a4,-1944(gp) # 80001fc0 <Bool_Glob>
    400003f8:   fbf78793                addi    a5,a5,-65
    400003fc:   0017b793                seqz    a5,a5
    40000400:   00e7e7b3                or      a5,a5,a4
    40000404:   86f1a423                sw      a5,-1944(gp) # 80001fc0 <Bool_Glob>
    40000408:   04200713                li      a4,66
    4000040c:   86e18223                sb      a4,-1948(gp) # 80001fbc <Ch_2_Glob>
    40000410:   00008067                ret
```

## 12 位偏移对任何人来说都不够用

需要明确的是：链接器松弛是针对常见情况的优化。对于无法优化的符号，链接器会透明地发出双指令寻址序列。为了演示当链接器无法松弛一个符号时会发生什么，让我们再看一个例子：

```sh
$ cat relax.c
long near;
long far[2];

long data(void) {
  return near | far;
}

int main() {
  return data();
}
$ riscv64-unknown-linux-gnu-gcc relax.c -O3 -o relax --save-temps
$ riscv64-unknown-linux-gnu-objdump -d relax.o
relax.o:     file format elf64-littleriscv

Disassembly of section .text:

0000000000000000 data:
   0:   000007b7                lui     a5,0x0
                        0: R_RISCV_HI20 near
                        0: R_RISCV_RELAX        *ABS*
   4:   0007b503                ld      a0,0(a5) # 0 data
                        4: R_RISCV_LO12_I       near
                        4: R_RISCV_RELAX        *ABS*
   8:   000007b7                lui     a5,0x0
                        8: R_RISCV_HI20 far
                        8: R_RISCV_RELAX        *ABS*
   c:   0007b783                ld      a5,0(a5) # 0 data
                        c: R_RISCV_LO12_I       far
                        c: R_RISCV_RELAX        *ABS*
  10:   8d5d                    or      a0,a0,a5
  12:   8082                    ret

Disassembly of section .text.startup:

0000000000000000 main:
   0:   1141                    addi    sp,sp,-16
   2:   e406                    sd      ra,8(sp)
   4:   00000097                auipc   ra,0x0
                        4: R_RISCV_CALL data
                        4: R_RISCV_RELAX        *ABS*
   8:   000080e7                jalr    ra
   c:   60a2                    ld      ra,8(sp)
   e:   2501                    sext.w  a0,a0
  10:   0141                    addi    sp,sp,16
  12:   8082                    ret
```

这里我们可以看到三组重定位：两对 `HI20`/`LO12` 重定位和一个 `CALL` 重定位。在这种情况下，`CALL` 重定位可以被松弛，引用 `near` 的 `HI20`/`LO12` 对也可以被松弛，但是引用 `far` 的 `HI20`/`LO12` 对则不能。在这种情况下，链接器仍然能正常工作，为它可以松弛的 `near` 符号生成单指令寻址序列，而对于它无法用单指令引用的 `far` 符号，则只是对其寻址序列进行重定位。

```sh
$ riscv64-unknown-linux-gnu-objdump -d -r relax
Disassembly of section .text:

0000000000010330 main:
   10330:       1141                    addi    sp,sp,-16
   10332:       e406                    sd      ra,8(sp)
   10334:       0b8000ef                jal     ra,103ec data
   10338:       60a2                    ld      ra,8(sp)
   1033a:       2501                    sext.w  a0,a0
   1033c:       0141                    addi    sp,sp,16
   1033e:       8082                    ret

00000000000103ec data:
   103ec:       8181b503                ld      a0,-2024(gp) # 12038 near
   103f0:       67e9                    lui     a5,0x1a
   103f2:       0407b783                ld      a5,64(a5) # 1a040 far
   103f6:       8d5d                    or      a0,a0,a5
   103f8:       8082                    ret
```

尽管到这里可能有点多余了，但我已经写好了下面的例子，所以我想还是把它们留在这里，以便更明确地说明：

```diff
--- relax.o
+++ relax
-      4:   00000097                auipc   ra,0x0
-                           4: R_RISCV_CALL         data
-                           4: R_RISCV_RELAX        *ABS*
-      8:   000080e7                jalr    ra
+  10334:   0b8000ef                jal     ra,103ec data
```

在上面的例子中，我们可以看到请求了 `R_RISCV_CALL` 重定位。这个重定位被定义为作用于一个相邻的 `auipc`/`jalr` 对，引用一个有符号 32 位 PC 相对的调用目标。在这种情况下，我们能够将这个指令对松弛为单个 `jal` 指令，因为实际的调用目标在当前 PC 的 21 位有符号偏移范围内。你会发现几乎所有的 `R_RISCV_CALL` 重定位都是可以松弛的，因为大多数代码都表现出一定程度的调用局部性。

```diff
--- relax.o
+++ relax
-      0:   000007b7                lui     a5,0x0
-                          0: R_RISCV_HI20         near
-                          0: R_RISCV_RELAX        *ABS*
-      4:   0007b503                ld      a0,0(a5) # 0 data
-                          4: R_RISCV_LO12_I       near
-                          4: R_RISCV_RELAX        *ABS*
+  103ec:   8181b503                ld      a0,-2024(gp) # 12038 near
```

在上面的例子中，我们可以看到请求了一对 `R_RISCV_HI20`/`R_RISCV_LO12_I` 重定位。这些重定位各自被定义为作用于单个指令：`R_RISCV_HI20` 重定位 `lui` 的 20 位偏移，而 `R_RISCV_LO12_I` 重定位各种 I-type 指令（本例中是 `ld`）的 12 位偏移。在这种情况下，我们能够将这个指令对松弛为单个 `ld` 指令，因为最终的符号地址在全局指针 `gp` 的 12 位偏移范围内。

```diff
--- relax.o
+++ relax
-      8:   000007b7                lui     a5,0x0
-                           8: R_RISCV_HI20         far
-                           8: R_RISCV_RELAX        *ABS*
-      c:   0007b783                ld      a5,0(a5) # 0 data
-                           c: R_RISCV_LO12_I       far
-                           c: R_RISCV_RELAX        *ABS*
+  103f0:   67e9                    lui     a5,0x1a
+  103f2:   0407b783                ld      a5,64(a5) # 1a040 far
```

在上面的例子中，我们看到另一对 `R_RISCV_HI20`/`R_RISCV_LO12_I`，但这次我们无法松弛它，因为它不在 `gp` 的 12 位偏移范围内。注意，我们仍然通过填充重定位来为这种情况生成正确的代码。每当无法正确重定位一个请求的重定位时，你都会得到一个链接时错误，否则链接后的可执行文件将无法产生正确的结果。

敬请关注，因为在未来的博客文章中，还会有更多关于链接器松弛的内容。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛 (当前页面)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)
