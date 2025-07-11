# All Aboard 系列，第 0 部分：引言

> 译者注：All Aboard 是一个常见的英文短语，意为“请上车”，常用于火车、轮船等交通工具即将出发时召集乘客。作者在此处使用该短语作为其博客系列的标题，寓意带领读者踏上学习 RISC-V 软件生态的旅程。 本文翻译仅供学习分享使用。

> 本文于2017年8月7日发布于 https://www.sifive.com/blog/all-aboard-part-0-introduction

我是 [Palmer Dabbelt](http://www.dabbelt.com/~palmer/)，SiFive 的一名软件工程师，同时也是各种 RISC-V 移植项目的维护者。我从事 RISC-V ISA 相关工作已有数年，现在它终于开始为黄金时代做好准备了。虽然我们的代码尚未被合并到 Linux 或 glibc 的上游，但希望到今年年底，我们能将核心的系统软件集提交到相关的上游代码仓库中——届时，各种发行版就可以开始向 RISC-V 移植，用户也可以开始使用我们的软件了。我从用户 ISA（至少是 v2 版本，也就是真正的那个版本 :)）尚未最终确定时就开始参与 RISC-V 的工作，在过去几年里，事情的发展变得如此真实，甚至有点让人感到不可思议。

虽然我认为 RISC-V 软件生态系统的核心部分已经相当不错了，但我注意到，由于缺乏非代码形式的内容，用户们很难快速上手 RISC-V 软件。尽管 SiFive 已经极大地改进了文档和用户体验，但在搜索引擎上似乎很难找到关于 RISC-V 软件生态系统的、优质且具体的长篇技术内容。因此，对于刚接触 RISC-V 的人来说，要为他们的问题找到解决方案非常困难。在过去的一年左右，邮件列表一直在弥补这一不足，但随着社区的不断扩大，仅仅依赖用户提问的负担正变得越来越重。

在可预见的未来，我将在每周一发布一篇博客。这些文章将面向我帮助维护的各种 RISC-V 移植项目的用户和潜在开发者。我将精心撰写这些文章，使其读起来有趣，能为社区新成员提供良好的参考，并且易于在 Google 上搜索到。

下周一，我们将抵达我们的第一站：RISC-V 编译器的 `-march`、`-mabi` 和 `-mtune` 参数！我们到时见！

## 阅读更多 All Aboard 系列博客：

*   All Aboard 系列，第 0 部分：引言 (当前页面)
*   [All Aboard 系列，第 1 部分：RISC-V 编译器的 -march, -mabi 和 -mtune 参数](https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
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
