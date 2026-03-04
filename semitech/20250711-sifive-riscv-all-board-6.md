# All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核

> 本文于**2017年10月9日**发布于 https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel

这篇文章将开始一段关于 Linux 的简短旅程，在此期间我们将讨论 RISC-V Linux 内核移植。SiFive 最近发布了[支持 Linux 的 U54-MC RISC-V 核心 IP](https://www.sifive.com/cores/essential)，我们的 Linux 移植最近也已提交到 Linux 的暂存分支 linux-next，所以如果一切顺利，我们应该会在下一个合并窗口结束时被合并。与 Linux 一同，我们很快就将拥有全套核心系统组件的上游版本，既有针对嵌入式系统的（通过 binutils、GCC 和 newlib），也有针对更大型系统的（通过 binutils、GCC、glibc 和 Linux）。

这个博客系列将讨论当前状态下的 Linux 移植，自然会涉及 RISC-V 监督者规范（supervisor spec）的各个方面。希望这个系列对有兴趣深入研究 RISC-V Linux 内核移植的人，以及正在移植其他操作系统的人都有用，这样他们可以看到我们做出的一些设计决策。

## `bbl`, 伯克利引导加载程序

标准的 RISC-V 特权模型包含四种模式：

*   用户模式（User mode）是用户空间程序运行的地方。这由 RISC-V ISA 手册的第一部分（用户规范）指定，而所有更低级的模式都由第二部分（监督者规范）指定。
*   监督者模式（Supervisor mode）是 Linux 运行的地方。
*   虚拟机管理模式（Hypervisor mode）目前尚未规定。
*   机器模式（Machine mode）是最低的保护模式，旨在运行机器特定的固件，这些固件在其他机器上可能以微码的形式存在。

> 译者注：Hart，即 Hardware Thread，是 RISC-V 规范中用来指代一个硬件执行线程的术语，可以理解为一个独立的、拥有自己程序计数器和寄存器状态的执行单元。它类似于其他架构中的“硬件线程”或“逻辑处理器”。一个物理核心（core）可以包含一个或多个 hart。

RISC-V 监督者规范的一个总体目标是允许单个内核镜像在任何 RISC-V 平台上运行。为了避免将关于硬件的假设固化到 Linux 镜像中，我们依赖两种抽象机制：

*   底层硬件的细节由设备树（device tree）描述，这是大多数现代系统用来描述机器的标准格式。它指定了内存映射、系统中所有 hart 的配置，以及所有静态分配的设备是如何连接的。
*   通常会作为微码陷阱（microcode traps）实现的复杂功能的实现，被隐藏在监督者二进制接口（supervisor binary interface，简称 SBI）之后。这使得像 Linux 这样的监督者可以针对由更低特权级别提供的接口进行编写，而无需增加一堆仿真指令所带来的硬件复杂性。

在我们的 RISC-V 监督者模式实现中（据我所知，这是迄今为止使用最广泛的实现），设备树和 SBI 都是由一个称为伯克利引导加载程序（Berkeley Boot Loader，或 `bbl`）的机器模式垫片（shim）提供的。这被认为是用户可能合理地想要替换的第一阶段引导加载程序，并对应于 PC 式系统上的 BIOS 或 EFI —— 存在 UEFI 和 LinuxBIOS 到 RISC-V 的移植，但我对它们知之甚少，所以我将只局限于 `bbl`。

`bbl` 预期会从另一个引导加载程序链式加载而来，其入口点在机器模式下运行。它从前一个引导加载阶段接收一个设备树，并执行以下步骤：

*   选择一个 hart 作为主 hart。其他 harts 进入休眠状态，直到 `bbl` 准备好将控制权移交给 Linux，届时它们都将被唤醒并大约在同一时间进入 Linux。
*   读取并过滤从前一阶段传入的设备树。这允许 `bbl` 剥离 Linux 不应关心的信息。例如，在 SiFive 系统上，我们通常有一个额外的工具 hart 来处理各种低级任务，如电源管理。在我们当前的系统上，这个 hart 实现为一个非常小的核心，缺少浮点、缓存和虚拟内存。为了避免向 Linux 添加一堆 SiFive 特定的逻辑，我们转而直接剥离掉那些 Linux 无法启动的 harts。
*   唤醒所有其他 harts，以便它们可以设置自己的 PMP、陷阱处理程序并进入监督者模式。
    > 译者注：PMP (Physical Memory Protection) 是 RISC-V 的物理内存保护单元，用于在物理地址级别上设置内存区域的访问权限。
*   读取 `mhartid` CSR，以便可以向 Linux 传递一个每个 hart 唯一的标识符。
*   设置一个 PMP，以允许监督者模式访问所有内存。
*   设置机器模式陷阱处理程序，包括一个机器模式堆栈。`bbl` 的机器模式代码需要处理未实现指令和机器模式中断。
*   处理器执行一条 `mret` 指令，从机器模式跳转到监督者模式。
*   `bbl` 跳转到其有效载荷（payload）的起始处，在这种情况下就是 Linux。

## Linux 中的早期启动

当 Linux 启动时，它期望系统处于以下状态：

*   `a0` 寄存器包含一个每个 hart 唯一的 ID。我们目前将这些 ID 映射到 Linux 的 CPU ID，因此它们应是连续且接近 0 的。
*   `a1` 寄存器包含一个指向设备树的指针，表示为一个二进制的扁平化设备树（DTB）。
*   内存是恒等映射（identity mapped）的，`bbl` 通过不启用分页来实现这一点。
*   内核的 ELF 镜像已正确加载，各个段位于其正确的地址。这对 Linux 来说并非特别繁重，因为它有一个简单的 ELF 镜像需要加载。

Linux 启动时需要做的第一件事是处理 RISC-V 规范和 Linux 期望之间的不匹配：RISC-V 系统以任意顺序和任意时间启动 harts，而 Linux 期望单个 hart 首先启动，然后唤醒所有其他 harts。我们用“hart 抽签”（hart lottery）来处理这个问题，这是一个非常短的、基于 AMO 的序列，用来选出第一个启动的 hart。其余的 harts 则自旋等待，直到 Linux 启动到足够远，它们可以继续。
> 译者注：AMO (Atomic Memory Operations) 是 RISC-V 的原子内存操作指令，可以实现无锁的同步。

此时，我们继续进行一个相当标准的 Linux 早期启动过程：

*   建立一个所有物理内存的线性映射，以 `PAGE_OFFSET` 作为偏移量。
*   启用分页。
*   设置 C 运行时环境，包括堆栈和全局指针。
*   设置一个只自旋的陷阱向量（trap vector），用于捕获启动过程早期的任何错误。
*   调用 `start_kernel` 进入标准的 Linux 启动过程。

这就结束了我们移植中整个汇编部分的早期启动——我数了一下，只有 71 条指令！我们对我们移植中汇编代码如此之少感到非常自豪，这是监督者 ISA 规范简洁性的一个证明。

## `setup_arch`

正常的 Linux 早期启动过程会一直进行到我们到达 `setup_arch`，这是在内核启动过程中相当早期的、特定于架构的设置代码。在 RISC-V 系统上，`setup_arch` 会执行以下操作：

*   如果 SBI 控制台驱动程序已启用，则启用 `EARLY_PRINTK` 控制台。在 RISC-V 上，我们无条件启用早期 printk，因为 SBI 控制台行为良好，所以没有理由不启用它。由于这发生在启动过程的极早期，你几乎在整个过程中都能得到调试输出。
*   解析内核命令行，并处理早期的架构特定选项。在这里，我们只允许用户控制 Linux 实际使用的物理内存量。
*   解析设备树的内存映射，以找到内核镜像的内存块，并将其标记为保留。设备树的其余内存被释放给内核用于分配。
*   初始化内存管理子系统，包括零页和各种区域（zones）。我们只支持 `ZONE_NORMAL`，所以这非常简单。
*   唤醒系统中的任何其他 hart。
*   从设备树中读取处理器的 ISA，用于填充 ELF 辅助向量（auxvec）中的 `HWCAP` 字段。这允许用户空间程序确定它们正在执行的硬件是什么样的。目前我们假设 ISA 是同构的，因为任何其他情况都不能很好地映射到 UNIX 的进程模型中。

这是启动过程中唯一特定于 RISC-V 的部分；此后，控制权返回到上游内核代码。

## 在 SMP 系统中启动其他 Harts

RISC-V 启动过程中最有趣的部分是我们如何唤醒系统中的其他 harts。回想一下，在 RISC-V 系统上，harts 通过在任意时间跳转到内核的起始地址来启动。我们这样做是为了简化 ISA 的规范：如果没有一个被禁用的 hart 的概念，那么就不需要规定如何开启或关闭 harts。由于电源管理常常是一件棘手的事情，我们将其推迟到机器特定的代码中，并为监督者提供一个干净的接口。

为了处理这个难题，输掉抽签的 harts 会自旋等待，直到主 hart 在启动过程中走得足够远，以至于它们已经被分配了运行所需的内存——在这种情况下，是一个位于内核 `tp` 变量中的 `task_struct`（这有点滥用线程指针，但我们只是想要一个编译器不会篡改的东西）和一个堆栈。

> 译者注：`tp` (thread pointer) 在 RISC-V ABI 中是 `x4` 寄存器，通常用于指向线程局部存储。内核在这里借用它来为每个 hart 存储其 `task_struct` 的地址。

做这件事的代码相当直接，即使它占了我们启动函数中汇编代码的相当大一部分：

```asm
.Lsecondary_start:
        li a1, CONFIG_NR_CPUS
        bgeu a0, a1, .Lsecondary_park

        /* Set trap vector to spin forever to help debug */
        la a3, .Lsecondary_park
        csrw stvec, a3

        slli a3, a0, LGREG
        la a1, __cpu_up_stack_pointer
        la a2, __cpu_up_task_pointer
        add a1, a3, a1
        add a2, a3, a2

        /*
         * This hart didn't win the lottery, so we wait for the winning hart to
         * get far enough along the boot process that it should continue.
         */
.Lwait_for_cpu_up:
        REG_L sp, (a1)
        REG_L tp, (a2)
        beqz sp, .Lwait_for_cpu_up
        beqz tp, .Lwait_for_cpu_up
        fence

        /* Enable virtual memory and relocate to virtual address */
        call relocate

        tail smp_callin
```

这使得 `__cpu_up` 函数（通过 ID 启动一个目标 hart）也相当简单：

```c
int __cpu_up(unsigned int cpu, struct task_struct *tidle)
{
        tidle->thread_info.cpu = cpu;

        /*
         * On RISC-V systems, all harts boot on their own accord.  Our _start
         * selects the first hart to boot the kernel and causes the remainder
         * of the harts to spin in a loop waiting for their stack pointer to be
         * setup by that main hart. Writing __cpu_up_stack_pointer signals to
         * the spinning harts that they can continue the boot process.
         */
        smp_mb();
        __cpu_up_stack_pointer[cpu] = task_stack_page(tidle) + THREAD_SIZE;
        __cpu_up_task_pointer[cpu] = tidle;

        while (!cpu_online(cpu))
                cpu_relax();

        return 0;
}
```

## 关机

将关机过程与启动过程一起讨论似乎最自然，但这个过程在 RISC-V 上实际上非常简单：通用内核代码清理整个内核，然后调用 `sbi_shutdown` 来通知机器模式代码它应该终止。

这差不多就是启动（和停止）一个 RISC-V Linux 内核所涉及的全部内容了。由于我们使用设备树并将大部分平台特定的工作推到固件中，这个过程实际上是相当直接的。

下周我们将讨论任务切换，这是内核在启动过程完成后做的第一件事。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核 (当前页面)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   [All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！](https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)