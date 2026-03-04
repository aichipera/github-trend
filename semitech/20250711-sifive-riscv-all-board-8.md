# All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！

> 本文于**2017年12月5日**发布于 https://www.sifive.com/blog/all-aboard-part-8-the-risc-v-linux-port-is-upstream

正如你们中一些人可能已经听说的，RISC-V Linux 移植已经被接纳进入 Linus 的代码树，并计划作为 4.15 版本的一部分发布。虽然这是一个重要的里程碑，但我们在 Linux 内核领域还有很长的路要走，而且在用户空间还有大量的工作要做。

尽管如此，这是一个足够大的进展，值得用一篇博客文章来专门记录——至少可以作为我有一段时间没有写博客的借口 :)。

## 哪些已经进入上游了？

我们移植的核心部分已经进入上游。这包括：

*   RISC-V CPU 的设备树绑定。
*   早期启动和初始化代码。
*   Linux 的原子操作和内存模型内部函数（intrinsics），针对一个非正式的内存模型（也就是我做的一堆猜测）。
*   一些中断和定时器基础设施，但这需要清理。
*   分页和 MMU 相关代码。
*   为 RISC-V Linux 系统实现的用户侧 ABI，这将形成一个规范。

所有这些代码，加上一些修复，将包含在 4.15 的 tarball 发布中。我们的目标是下一个 glibc 版本，它应该在二月初发布。届时，ABI 将被固定下来，各种发行版就可以在保持二进制永久兼容性的前提下开始工作。

## 哪些还没有进入上游？

我们仍然缺少相当多的功能，最值得注意的是：

*   我们需要清理 RISC-V 系统上的第一级中断处理，我可能会借鉴 ARMv8 和 OpenRISC 的做法。
*   SBI 控制台驱动程序尚未进入上游，但它看起来状态相当不错。
*   每个 hart 的中断控制器需要修改以适应新的中断处理方案。
*   PLIC 驱动程序应该转换为 FastEOI 流程，但我尚未完成那次重构。
*   ISA 强制要求的定时器驱动程序需要进行转换，以避免在 `arch/riscv/` 中有初始化代码，处理更多的设备树规范，并使用新的中断处理基础设施。
*   我们的 32 位 DMA 补丁需要清理并提交审查。
*   我们有一些针对 Xilinx PCIe 控制器中 bug 的变通方法，需要被合理地修复。
*   在 PCI 和 OF（Open Firmware）领域有一些清理工作需要最终进入。其中一些也正在由上游以更好的方式进行工作，所以希望这能自行解决。
*   我们有一些设备树文档的修复应该要提交。

## 如何提供帮助

如果你有兴趣帮助 RISC-V Linux 的工作（或任何其他 RISC-V 软件项目），最好的起点是我们的 [GitHub](http://github.com/riscv/) 页面。每个项目在 GitHub 上都有自己的开发仓库，其中包含各种待处理的补丁，这些项目的 RISC-V 维护者在那些 GitHub 页面上活跃地讨论开发。

如果你已经熟悉某个特定项目的开发流程，那么我们当然会遵循该项目上游所有已合并移植的标准开发实践。通常，某种形式的 `MAINTAINERS` 文件会包含联系 RISC-V 开发人员的机制。还有一个 `patches@groups.riscv.org` 邮件列表，所有上游 RISC-V 软件的补丁都应该抄送（CC'd）到这里——这主要是为了让发行版维护者能方便地找到所有软件补丁，但也作为一个讨论的地方。

此外，对于不适合上述任何一类的问题，欢迎你将它们发送到 RISC-V 软件邮件列表 `sw-dev@groups.riscv.org`，或者在 freenode 的 `#riscv` 频道上提问。

## 阅读更多 All Aboard 系列博客：

*   [All Aboard 系列，第 0 部分：引言](https://www.sifive.com/blog/all-aboard-part-0-introduction)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
*   [All Aboard 系列，第 2 部分：ELF 工具链中的重定位](https://www.sifive.com/blog/all-aboard-part-2-relocations)
*   [All Aboard 系列，第 3 部分：RISC-V 工具链中的链接器松弛](https://www.sifive.com/blog/all-aboard-part-3-linker-relaxation-in-riscv-toolchain)
*   [All Aboard 系列，第 4 部分：RISC-V 代码模型](https://www.sifive.com/blog/all-aboard-part-4-risc-v-code-models)
*   [All Aboard 系列，第 5 部分：RISC-V 系统上基于 -march 和 -mabi 的库路径](https://www.sifive.com/blog/all-aboard-part-5-risc-v-multilib)
*   [All Aboard 系列，第 6 部分：启动一个 RISC-V Linux 内核](https://www.sifive.com/blog/all-aboard-part-6-booting-a-risc-v-linux-kernel)
*   [All Aboard 系列，第 7 部分：在 RISC-V 上进入和退出 Linux 内核](https://www.sifive.com/blog/all-aboard-part-7-entering-and-exiting-the-linux-kernel-on-risc-v)
*   All Aboard 系列，第 8 部分：RISC-V Linux 移植已进入上游！ (当前页面)
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   [All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献](https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)
