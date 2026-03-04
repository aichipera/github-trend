# All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU

> 本文于**2017年12月11日**发布于 https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel

这篇文章将涵盖 Linux 内存管理子系统的 RISC-V 移植。由于 Linux 中绝大多数的内存管理代码都是架构无关的，我们绝大多数的内存管理代码都用于与我们的 MMU 接口、定义我们的页表格式，以及与有内存分配约束的驱动程序接口。

我将避免在本博客中讨论 RISC-V 内存模型，一是因为它尚未完成，二是因为它足够复杂，值得用一系列博客文章来专门讨论。

另外，顺便提一下：对于那些没有关注互联网消息的人，我们已经将我们的核心架构移植合并到了 Linus 的代码树中，并计划作为 4.15 版本的一部分发布。这不会是一个完全可启动的 RISC-V 系统，但至少是一个好的第一步！

## RISC-V 系统中的特权级别

RISC-V ISA 定义了一个执行环境的堆栈。虽然每个环境都被设计为可以被经典地虚拟化，但在标准系统中，堆栈中的每一层都旨在为下一层提供执行环境。从堆栈中特权最低的级别开始，执行环境是：

*   用户模式软件在 AEE（Application Execution Environment，应用程序执行环境）中执行。在 Linux 系统上，AEE 也被称为用户 ABI：内核支持的系统调用集。AEE 还包括整个用户 ISA，因为用户模式程序被期望能够执行除了 `scall` 之外的指令。
*   监督者模式软件在 SEE（Supervisor Execution Environment，监督者执行环境）中执行。该环境由特权 ISA 文档定义的监督者模式指令和 CSR，以及 SBI 组成。监督者模式软件被期望提供多个 AEE，Linux 为每个进程提供一个 AEE。
*   虚拟机管理模式软件在 HEE（Hypervisor Execution Environment，虚拟机管理程序执行环境）中执行，并被期望提供多个 SEE。特权 ISA 文档的虚拟机管理模式部分仍在编写中，所以我们暂时忽略这个。
*   机器模式软件在 MEE（Machine Execution Environment，机器执行环境）中执行，并被期望提供一个更高级别的执行上下文。由于特权模式 ISA 将实现 U、S 和 H 扩展设为可选（因此允许 M、M+U、M+S+U 和 M+H+S+U 系统），预计不同的机器模式软件实现将提供一个 HEE、SEE 或 AEE。

虽然提供与此层次结构不匹配的执行环境堆栈是相当标准的做法，但在每个环境中执行的软件无法分辨出差异。这并不是说用户模式软件是完全可移植的：例如，Linux AEE 与 FreeBSD AEE 不同，因为它们提供不同的系统调用。其意图仅仅是，为在 Linux AEE 中执行而编写的程序无法分辨它们是在硬件上的 Linux 中执行，在 Spike 中运行的 Linux 中执行，还是在 QEMU 的用户模式仿真中执行。这些都不是新概念，只是在 RISC-V ISA 规范中比在许多其他架构中更明确地说明了。

由于 RISC-V 在特权堆栈的每一层都是可经典虚拟化的，因此提供任何执行环境都不需要显式的硬件支持：例如，QEMU 的用户模式仿真在没有任何 RISC-V ISA 硬件支持的系统上提供了一个 AEE。虽然这些系统可以做到相当高的性能，但 RISC-V 的主要目的是支持 ISA 的硬件实现——例如，即使运行 QEMU 的至强（Xeon）处理器在可预见的未来可能是 RISC-V Linux AEE 的最快实现，但在我的手表上运行一个 RISC-V 的硬件实现会更合适。

RISC-V ISA 文档旨在允许在特权堆栈的各个级别的软件实现利用它们所编写的执行环境，以提供它们之上的执行环境。其中一些是如此明显，你可能没有注意到我们已经讨论了一段时间了：例如，假设硬件在用户空间处理执行一条 `addi` 指令而无需内核干预，因为不这样做会很傻。

到目前为止，我们能够推迟对特权级别的讨论，因为绝大多数设计都是显而易见的：所有用户指令都由硬件处理，无需监督者干预，除了 `scall`，它只是将控制权转移到内核的单一陷阱入口点——详情请见我之前的博客文章 [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)。由于应用程序执行环境提供了用户空间程序拥有一个大的、平坦的地址空间的幻觉，我们在讨论用户应用程序时或多或少可以忽略内存。正如计算系统中常见的那样，内存是困难的部分——因此，我们只有在谈论分页时才真正需要讨论 RISC-V 的特权模式。

对于这篇博客文章，我们将专注于在合理系统上运行的监督者代码——因此我们不会做像从用户空间仿真不支持的指令这样的事情。博客的重点将是如何在给定一个监督者执行环境的情况下提供一个 RISC-V 应用程序执行环境。

### RISC-V 应用级监督者执行环境

像 Linux 这样的监督者程序，在一个监督者执行环境中执行。就像用户级 ISA 将 AEE 的许多具体细节留给不同平台以不同方式实现一样（例如 Linux vs BSD 上的系统调用），特权 ISA 并没有规定应用级监督者（如 Linux 或 BSD）可以期望的 SEE 的所有细节——这些将在平台规范中规定。

在这篇博客中，我将快速介绍一下应用级监督者的 RISC-V 监督者执行环境的几个关键方面。这个环境旨在支持在监督者模式下运行的类 UNIX 操作系统，仿真符合 POSIX 的应用程序执行环境。提议的（需要说明的是，我不在平台规范工作组，所以这都只是我的猜测）应用级 SEE 的要求亮点是：

*   RV32I 或 RV64I 基础 ISA 之一，以及 M、A 和 C 扩展。F 和 D 扩展是可选的但成对出现，使得应用级 SEE 可能的标准 ISA 为 RV32IMAC、RV32IMAFDC (RV32GC)、RV64IMAC 和 RV64IMAFDC (RV64GC)。
*   在基于 RV32I 的系统上，支持 Sv32 基于页的虚拟内存。
*   在基于 RV64I 的系统上，支持至少 Sv48 基于页的虚拟内存。
*   进入 SEE 时，PMA（物理内存属性）被设置成使得内存访问在 harts 和设备之间是点对点强有序的。
*   一个实现了各种 fence、定时器和控制台的 SBI。

应用级 SEE，正如即将到来的 RISC-V 平台规范所规定的，是标准 Linux 发行版和硬件供应商之间的合同——当然，这些限制不适用于嵌入式领域，在那里许多限制会很繁重。在实践中：如果你期望用户能够在你的平台上更换启动介质，那么你应该满足应用级 SEE 的要求。

### RISC-V Linux 应用程序执行环境

RISC-V 上的监督者模式软件使用一个监督者执行环境来提供一个或多个应用程序执行环境。从根本上说，一个 AEE（像任何执行环境一样）仅仅是机器在每条指令执行后下一个状态的定义。在 RISC-V 系统上，AEE 依赖于：

*   ISA 字符串，它决定了绝大多数指令的作用以及哪些寄存器构成了机器的当前状态。
*   监督者的用户可见 ABI，它决定了 `scall` 指令的作用。这不同于 C 编译器的 ABI，后者定义了应用程序不同组件之间的接口。
*   整个内存地址空间的内容。

在一个理想化的世界里，每个进程都由其自己独立的 AEE 组成，Linux 将这些 AEE 复用在一个单一的 SEE 之上。当然，在实践中，这个模型存在各种各样的问题，但这些都不是 RISC-V 系统特有的。一个自包含且定义明确的 AEE 的概念从标准角度来看仍然是有用的，我们希望随着我们移植工作的进展，在正确指定 RISC-V Linux AEE 系列（以及其他类 POSIX 系统的 AEE）方面取得进展。

## RISC-V 系统上的分页

在对 RISC-V 特权模式进行了冗长的偏离讨论之后，我们终于可以回到这篇博客文章的重点：RISC-V 系统上的分页。分页是用来向用户模式提供拥有一个 AEE 幻觉的主要机制——就像计算机架构中的大多数事情一样，事实证明内存是棘手的部分。

在 RISC-V 设计的时代设计一个 ISA 的好处之一是，对于困难问题已经尝试了如此多的不同解决方案，以至于我们现在基本上知道该怎么做了。因此，在设计 RISC-V 的监督者虚拟内存接口时，我们得到了一个相当标准的基于页的虚拟内存系统。确切的页表格式等在相关的 RISC-V ISA 手册中有列出，所以我不会在这里详细介绍，但有几个亮点：

*   页在叶节点是 4KiB，并且可以用页表的每一级来映射大的连续区域。
*   基于 RV32I 的系统可以用三级页表拥有最多 34 位的物理地址。
*   基于 RV64I 的系统可以有多种虚拟地址宽度，从 39 位开始，以 9 位的增量扩展到 64 位。
*   映射必须通过 `sfence.vma` 指令进行同步。
*   有用于全局映射、仅监督者、读/写/执行、以及已访问/已脏的位。
*   有一个单一的有效位，允许在原本未使用的页表中存储 `XLEN-1` 位的标志。此外，在已映射的页中有两位软件标志。
*   地址空间标识符（ASID）在 RV32I 上是 9 位，在 RV64I 上是 16 位，它们是一个提示，所以一个有效的实现是忽略它们。
*   已访问位和已脏位相对于来自同一 hart 的访问是强有序的，但是是可选的（在不支持时有基于陷阱的机制）。

Linux 的分页实现是功能性的但不是完整的：例如，我们缺少对 ASID 的支持。像我们移植中的许多事情一样，这些额外的功能会随着时间的推移而到来。

## 处理设备 DMA

RISC-V 目前没有定义 IOMMU，所以设备访问是在 SEE 提供的单个线性地址空间（即物理内存）中执行的。再加上缺乏修改 PMA 的机制，这使得 RISC-V 上的设备 IO 非常简单：我们基本上没有做任何特定于我们 ISA 的事情。

### 处理 32 位 DMA 区域

一些设备即使连接到具有更长物理地址的系统上，也只支持 32 位寻址。由于 RISC-V 缺乏 IOMMU，我们通过使用内核的 bounce buffers 来处理这些设备。这是正确的但速度慢：虽然对于在设计时设备集已经众所周知的 SoC 式系统可能没问题，但随着更复杂的 RISC-V 系统变得可用，我们最终将需要标准化一种虚拟化设备寻址的机制。

我们的 bounce buffer 机制只是使用了 Linux 提供的标准机制，所以没有什么 RISC-V 特定的东西。我们提供一个 32 位的 `ZONE_DMA`，允许从中分配，并使用 bounce buffers 来处理对合法区域外已分配页面的 `ioremap()`。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU (当前页面)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)