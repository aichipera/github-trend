# All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献

> 原文于**2018年2月20日**发布于 https://www.sifive.com/blog/all-aboard-part-10-how-to-contribute-to-the-risc-v-software-ecosystem

我们最近发布了 [HiFive Unleashed](https://www.crowdsupply.com/sifive/hifive-unleashed)，这是 Freedom U540-C000 的开发板，也是世界上第一款支持 Linux 的 RISC-V ASIC。该板的发布大致与包含 RISC-V 支持的 Linux 和 glibc 的首个上游版本发布时间吻合。因此，我们的新闻吸引了大量来自开源软件社区的兴趣——这正是我们发布该板的初衷，所以从这个意义上说，它进行得非常顺利。

这股新的兴趣浪潮表明，我们关于 RISC-V 软件开发方式的信息还远远不够。我们基本上又回到了促使我开始这个博客的同样处境，但这次是面对一套新的工具：我最初开始这个博客时，binutils 和 GCC 已经进入上游，我描述了这些移植是如何工作的，以供那些在这些移植发布后产生兴趣的开发者参考。现在我们有一批全新的感兴趣的开发者，他们发现了我们的 Linux 和 glibc 移植，并想知道如何参与进来。

虽然有一些关于 RISC-V binutils、GCC 和 Linux 移植结构的技术描述，但没有关于我们开发流程的描述。自我们公司成立以来，我们长期维护着树外（out-of-tree）的 RISC-V 移植，这对于刚开始接触 RISC-V 的新开发者来说有点困惑，因为我们过去在维护树外移植时使用了很多奇怪的做法，而我们正在逐步淘汰这些做法。在收到一些人询问他们应该如何贡献的邮件后（包括一些来自 SiFive 员工的邮件 :)），我想最好还是描述一下我们的开发流程。

现在我们已经进入上游，开发流程实际上非常简单：你可以像为该项目的任何其他移植做贡献一样，为该项目的 RISC-V 移植做贡献。因此，如果你已经熟悉一个项目的开发流程，那么就继续做你正在做的事情——我们会阅读所有相关的邮件列表和 bug 跟踪器。通常最好用一个类似`[PATCH] RISC-V: Fix a bug in...`这样的主题来表明你的补丁与 RISC-V 相关，以确保你的邮件不会在邮件洪流中丢失。

如果你不熟悉一个项目的上游开发，正在寻找一个更具体的需要完成的事情列表，或者有兴趣分发 RISC-V 软件，那么请继续阅读 :)。

## 向后移植、代码仓库、分支名称和带标签的发布版本

我们一直试图在我维护的所有项目中遵循相同的分支和发布方案，目前包括 binutils、GCC、glibc 和 Linux。我们有以下分支（以 binutils 为例，因为它是列表中的第一个）：

*   `master` (或者对于像 GCC 这样基于 SVN 的项目，是 `trunk`)：主开发分支。
*   `riscv-all`：RISC-V 集成分支，它基于 master 分支，并包含任何质量级别的额外补丁。这个分支可能不稳定或质量不高，但如果你发现了一个 bug，你应该查看这个分支，看看是否有一个正在进行的补丁来修复它，以避免重复工作。我不建议直接在这个分支上工作，因为它是自动生成的并且变动很大。
*   `binutils-2_30-branch`：上游发布分支。我们会在适当的时候将 RISC-V 补丁向后移植（backport）到这个分支。请注意，向后移植的标准在这里往往相当严格：补丁必须经过上游的代码审查，并且必须是 bug 修复。这意味着功能增加和性能改进通常不适合向后移植到上游发布分支。
*   `riscv-binutils-2.30`：RISC-V 发布分支。这基于上游的实际发布版本（而不是移动的发布分支），并包含尽可能多的 RISC-V 特定向后移植。这包括不适合上游的向后移植，比如新功能和性能改进，只要它们能直接向后移植到旧版本的软件包即可。我们维护这个分支一个发布周期。如果你打算分发 RISC-V 软件，那么这是最好的地方：SiFive 的二进制工具链发布版本就来自这里，并且最终会被标记为稳定版。

有这么多分支，确保补丁得到妥善跟踪很重要。因此，我们有一个流程来跟踪一个补丁从在制品到二进制发布的生命周期。一个补丁的生命周期是：

*   在你的个人仓库中创建一个新的 `wip-feature_name` 分支来开发你的功能。如果你是一个常规贡献者，你可以提交一个拉取请求（pull request），将你的仓库添加到生成 `riscv-all` 的来源列表中，该列表位于 [riscv-linux-infra](https://github.com/riscv/riscv-linux-infra)。
*   当你认为你的补丁已经足够好可以合并到上游时，就提交它。你可以在 github 上针对 `master` 提交一个拉取请求，或者通过电子邮件发送一个补丁。
*   补丁将被收集并合并到上游。
*   如果你的补丁应该被向后移植到上游发布分支，提交另一个拉取请求（针对 `binutils-2_30-branch`）或发送另一封电子邮件（指明这是一个向后移植），请求将补丁向后移植。
*   如果你的补丁不应该被向后移植到上游发布分支，但应该被向后移植到 RISC-V 特定发布分支（在这种情况下是 `riscv-binutils-2.30`），那么针对该分支提交另一个包含你的补丁的拉取请求。
*   最终，我们会用你的补丁标记一个 RISC-V 特定版本，届时它将被发行版采纳（包括 SiFive 二进制工具链发布）。

虽然我正试图将这个流程强加给我深度参与的所有项目，但为了适应相关的上游开发流程，项目之间存在一些差异。

## GNU 工具链 (binutils, GCC, 和 glibc)

我们工具链的绝大部分代码，无论是用于嵌入式系统（基于 newlib）还是 Linux（基于 glibc），都已提交到上游，并位于相关的 FSF 仓库中。具体来说，这意味着：

*   我们的 binutils 移植位于 [sourceware.org git 仓库](https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git)。除了 binutils，这个仓库还包含 GDB 和 SIM 的移植，但我们还没有完全将它们合并到上游，所以这些仍然作为向后移植存在于 [RISC-V GitHub 仓库](https://github.com/riscv/riscv-binutils-gdb)中。除了 GDB 和 SIM 的移植，我们的 GitHub 仓库还包含 RISC-V 特定的向后移植分支。
*   我们的 GCC 移植位于 [gcc.gnu.org SVN 仓库](https://gcc.gnu.org/viewcvs/gcc/)。除了日常工作，我们的整个移植都可以在这个上游仓库中找到。我们还在 [RISC-V GitHub](https://github.com/riscv/riscv-gcc) 中维护了一个 git 镜像，其中也包含了我们的向后移植分支。请注意，GCC 的主上游开发分支叫做 `trunk` 而不是 `master`，因为上游使用 subversion。
*   我们的 glibc 移植位于 [sourceware.org git 仓库](https://sourceware.org/git/?p=glibc.git)。

这些项目的开发流程非常直接：我们的移植已经进入上游并且大体上是完整的，我们绝大多数的开发工作直接在上游的 master 分支上进行。因此，你应该真的可以期望将所有这些仓库的主开发分支（`master` 或 `trunk`）一起使用，并得到一个可以工作的系统——或者至少是在混合一堆开发分支时你能期望的那么工作。

尽管各种工具链仓库的 RISC-V 移植绝大部分已经合并到上游，但仍有大量工作尚待完成。这些工作分为三类：

*   支持新的 RISC-V ISA。这包括在所有地方支持 E 基础 ISA，在 glibc 中支持 RV32I 基础 ISA，以及未来的 ISA 如 V 和 J ISA。这是非常广泛的工具链工作，所以可能不是一个好的入门点。
*   支持新功能和性能优化。这里的例子包括 GCC 调优、更好的链接器松弛和优化的 glibc 字符串例程。这里的一些项目是很好的入门点，但我们通常需要有好的基准测试来证明一个优化确实有帮助。
*   修复我们工具链中的 bug。我们的测试套件结果相当好，所以我们在这里发现的大多数 bug 可能都来自启动各种发行版的 RISC-V 移植。如果你有兴趣为 RISC-V 工具链工作做出贡献，这是最好的入门点。

下面有更多关于如何参与发行版移植工作的信息。

## GDB

RISC-V GDB 移植停滞了一段时间，但 Embecosm 的 Andrew Burgess 最近接管了该移植，进展迅速。Andrew 上周提交了一个为 GDB 添加 RISC-V 支持的补丁，所以希望我们很快就能合并到上游，届时我们就可以将我们的 GDB 移植视为 RISC-V 软件生态系统的一等成员！

如果你有兴趣为 RISC-V GDB 移植做出贡献，那么最好是参与代码审查过程，直接在上游提供帮助。

## QEMU

Michael Clark 自从加入 SiFive 以来，已经接管成为 RISC-V QEMU 移植的主要维护者。在过去的几个月里，他成功地将 QEMU 升级到最新的 ISA 规范，修复了一大堆 bug，添加了新的设备模型，并多次将代码提交到上游进行审查。我们距离拥有一个适合合并到上游的东西已经很近了，所以希望我们能赶上下一个版本。

与 GDB 很像，如果你有兴趣帮助 QEMU，那么最好是帮助代码审查过程，并直接在上游工作。

## Linux

于二月初发布的 Linux 4.15 是第一个支持 RISC-V 的上游版本。虽然这对 RISC-V 来说是一个重要的里程碑，但在让一个完整的基于 Linux 的系统启动和运行方面还有很长的路要走——基本上归结为缺少设备驱动程序，但我们缺少所有设备的驱动程序，所以你真的什么也做不了。在我们开始讨论如何帮助启动我们的设备之前，了解一些关于 Linux 开发过程的基本知识很重要——在 Linux 领域比在 GNU 领域要复杂一些，因为 Linux 发布更频繁，因此开发过程更加分散。

Linux 的开发比 GNU 工具链的开发要分散得多，并且可能比你习惯的任何项目都要分散得多。在大多数项目中，有一个规范的代码仓库（可能是 git 或 subversion）包含源代码，以及一组对该仓库有写（或提交）权限的开发人员。Linux 的工作方式有点不同：有一个公共的 git 仓库包含规范的 Linux 源代码，但只有 Linus 对该仓库有写权限。贡献者不被允许直接写入该仓库，而是被期望在他们自己的公共 git 仓库中工作，并向 Linus 提交拉取请求。虽然这种分布式模型确实是 git 设计的初衷，但它是一种不常见的开发流程，所以如果你不熟悉它，你可能需要阅读一些关于 Linux 开发流程的资料。对于 RISC-V 开发流程，有四个相关的仓库：

*   [kernel.org/torvalds/linux.git](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/)：规范的 Linux 代码树。这个仓库的 master 分支是发布版本的来源，所以它真正定义了 Linux。
*   [kernel.org/palmer/riscv-linux.git](https://git.kernel.org/pub/scm/linux/kernel/git/palmer/riscv-linux.git/)：RISC-V 开发树。这个树拥有 `arch/riscv` 下的所有东西，RISC-V 特定的拉取请求都来自这里。这个树中有四个分支，按稳定性顺序列出：
    *   `master`：Linus 的 master 分支的副本，直到最新的 RC 版。
    *   `for-linus`：被拉入 Linus 的 `master` 分支的 RISC-V 分支。这里的代码旨在具有最高质量，因为它通常在进入 `for-linus` 几天后就进入 `master`。
    *   `for-next`：被拉入 `linux-next` 的 RISC-V 分支。这遵循标准的 `linux-next` 规则，所以它只包含已经经过审查并且基本上准备就绪的代码。所有进入 `for-linus` 的提交都必须先经过 `for-next`。
    *   `riscv-all`：RISC-V 集成分支，包含所有正在进行中的补丁。由于这个树包含正在进行中的补丁，它甚至可能无法编译，但随着我们越来越多的代码进入上游，我希望让这个分支成为一个相当稳定的分支。
*   [kernel.org/palmer/linux.git](https://git.kernel.org/pub/scm/linux/kernel/git/palmer/linux.git/)：我个人的 Linux 开发树。这包含了我在不同开发阶段收集的（并将最终清理并提交到上游的）正在进行中的补丁。来自这个仓库的分支被自动合并形成规范的 RISC-V 仓库中的 `for-next` 和 `riscv-all`，并最终提交给 Linus。
*   [github.com/riscv/riscv-linux.git](https://github.com/riscv/riscv-linux.git)：旧的 RISC-V 开发树。这基本上已经废弃，但我仍然监控这里的拉取请求，并通过 Linux 内核开发流程移动它们。如果你最习惯使用 GitHub 进行开发，那么请随意使用这个，但如果可以的话，请使用标准的 Linux 开发流程。

除了这些仓库，我们还有 [linux-riscv@lists.infradead.org](http://lists.infradead.org/mailman/listinfo/linux-riscv) 邮件列表和 freenode 上的 [#linux-riscv](http://webchat.freenode.net?randomnick=1&channels=%23linux-riscv&prompt=1&uio=d4) 频道。

## 其他项目

除了我直接参与的项目，还有一些其他项目已经有上游的 RISC-V 支持。虽然我不是它们开发流程的专家，但我觉得至少提供一个其他 RISC-V 项目开发地点的简要概述是好的：

*   FreeBSD 有一个 RISC-V 移植，其 [wiki 页面](https://wiki.freebsd.org/riscv) 看起来质量很高，所以它可能是最好的起点。
*   LLVM 有一个 RISC-V 移植，由 lowRISC 的 Alex Bradbury 领导。他们有一个[状态页面](http://www.lowrisc.org/llvm/status/)，但我不确定它是否最新，因为最后一次更新似乎是 2017 年 9 月。需要特别注意的是，RISC-V GitHub 组织有一个 LLVM 仓库，但这与真正的 RISC-V LLVM 移植无关。
*   Go 有一个 RISC-V 移植，目前在 [RISC-V GitHub 仓库](https://github.com/riscv/riscv-go) 上进行树外维护。我不确定状态如何。
*   OpenJDK 移植的开端已经存在，但目前仅限于邮件列表帖子。Berkeley 的一个[树外实现](https://content.riscv.org/wp-content/uploads/2017/12/Tue1412-riscv-java-2017-export.pdf)也存在，至少是以幻灯片的形式 :)。
*   Newlib 有一个 RISC-V 移植，已经进入上游一段时间，并已作为 tarball 发布。Kito Cheng 维护这个移植，SiFive 的 Jim Wilson 也提供了一些帮助。newlib 的开发在上游进行，并且有一个 [RISC-V GitHub 仓库](https://github.com/riscv/riscv-newlib) 包含各种向后移植分支和正在进行中的功能。
*   Coreboot 有一个 RISC-V 移植，但他们的[博客](https://blogs.coreboot.org/blog/tag/risc-v/)上似乎没有太多关于 RISC-V 移植的新内容。Jonathan Neuschäfer 负责该移植。
*   OpenEmbedded 有一个正在进行的 RISC-V 移植，由 Khem Raj 领导。据我所知，最新的 RISC-V 支持位于 [Khem 的 GitHub 仓库](https://github.com/kraj/meta-riscv)上。上游的 OpenEmbedded 中也合并了一些支持，请参见相关的[拉取请求](http://lists.openembedded.org/pipermail/openembedded-core/2017-October/143072.html)。
*   OpenWRT 有一个正在进行的 RISC-V 移植，由 Zoltan Herapi 领导。我不确定在哪里可以找到关于这个移植的更多信息。
*   Debian 有一个正在进行的 RISC-V 移植，有一个 [wiki 页面](https://wiki.debian.org/RISC-V) 描述了该移植并包含了进度日志。
*   Fedora 有一个正在进行的 RISC-V 移植，目前处于引导阶段。虽然我个人没有用过，但 Jim 用过并且对他来说是可用的。他们在他们的 [wiki 页面](https://fedoraproject.org/wiki/Architectures/RISC-V) 上有详尽的信息。

如果你喜欢的项目没有在这里列出，那么我要么是忘记了它，要么是目前没有正在进行的移植。找到所有 RISC-V 软件开发者的最好方法是在[软件开发邮件列表](https://groups.google.com/a/groups.riscv.org/forum/#!forum/sw-dev)上发帖，或者跳进 freenode 上的 [#riscv](http://webchat.freenode.net?randomnick=1&channels=%23riscv&prompt=1&uio=d4) 频道。

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
*   [All Aboard 系列，第 9 部分：RISC-V Linux 内核中的分页与 MMU](https://www.sifive.com/blog/all-aboard-part-9-paging-and-mmu-in-risc-v-linux-kernel)
*   All Aboard 系列，第 10 部分：如何为 RISC-V 软件生态系统做出贡献 (当前页面)
*   [All Aboard 系列，第 11 部分：由 SiFive 主办的 RISC-V 黑客松](https://www.sifive.com/blog/all-aboard-part-11-risc-v-hackathon-presented-by-sifive)
