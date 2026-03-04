### 译者注

RISC-V 架构正从低功耗的物联网领域，大步迈向高性能计算的星辰大海。本文介绍的 Condor Computing 及其 Cuzco 核心，正是这股浪潮中的一个缩影。它并非简单地堆砌执行单元，而是另辟蹊径，采用了创新的“基于时间的微架构”（TBM），试图在性能与功耗之间找到比传统乱序执行（OoO）更优的平衡点。这不仅是 RISC-V 生态对性能极限的一次冲击，更是对沿用数十年的经典处理器设计思想的一次大胆探索。

---

# [Condor Computing 在 Hot Chips 2025 大会上发布高性能 RISC-V 设计 —— Cuzco](20250902-condor-computings-cuzco-a-high-perf-risc-v-design-at-hot-chip-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月25日
> 原文链接：[https://www.servethehome.com/condor-computings-cuzco-a-high-perf-risc-v-design-at-hot-chip-2025/](https://www.servethehome.com/condor-computings-cuzco-a-high-perf-risc-v-design-at-hot-chip-2025/)

[![Cuzco 核心](https://www.servethehome.com/wp-content/uploads/2025/08/Cuzco-Hero-696x392.jpg "Cuzco")](https://www.servethehome.com/wp-content/uploads/2025/08/Cuzco-Hero.jpg)

Cuzco 核心

半导体行业的顶级盛会，专注于高性能微处理器及相关集成电路的 Hot Chips 大会，于本周拉开帷幕。正如其名，这场大会深度揭示了业内最新、最热门的芯片技术，参与者既有专攻 RISC-V 的小型厂商，也不乏英特尔、IBM 和英伟达等手握重磅芯片的行业巨头。大会议题广泛，涵盖了从 CPU、GPU 到安全和硅光子等多个领域。

完整的会议日程可以在[这里](https://www.servethehome.com/hot-chips-2025-preliminary-schedule-released/)查看。今天上午的会议聚焦于 CPU 架构，而打头阵的便是 Condor Computing 公司及其 Cuzco RISC-V 架构。话不多说，让我们一探究竟。

作为 Andes Technology（晶心科技）的子公司，Condor Computing 专注于开发高性能的 RISC-V 核心。Cuzco 是他们的首款设计，出自一个仅有50名工程师的精悍团队。

[![Cuzco 介绍幻灯片](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_03-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_03.jpg)

Cuzco 介绍幻灯片

目前有多家公司正在开发高性能 RISC-V 核心。Condor 的目标是成为其中的佼佼者，在相似的功耗范围内提供最顶级的性能。RISC-V 生态系统仍在走向成熟，这意味着在其发展的当前阶段，市场仍有空间容纳众多玩家，直到最终大浪淘沙，胜者为王。

[![Cuzco 概览](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_04-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_04.jpg)

Cuzco 概览

从宏观层面看，Cuzco 的设计与其它高性能处理器有很多相似之处。例如，它拥有一个宽前端、一个相当深的 256 项重排序缓冲区（reorder buffer）以及 8 条执行流水线等。Condor 并不打算重新发明轮子，他们的目标是制造一个比 RISC-V 生态中其他参与者优化得更好的轮子。

[![Cuzco CPU 核心特性](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_05-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_05.jpg)

Cuzco CPU 核心特性

Cuzco 是一个完整的 IP 设计。也就是说，它不仅仅是一个 CPU 核心，还包含了缓存与一致性管理模块；基本上可以即插即用地连接到内存和 I/O 总线上。但毫无疑问，CPU 核心本身才是重头戏——这也是 Condor 最关注的部分。

Cuzco 遵循 RISC-V 的 RVA23 规范，这是首个面向高性能 RISC-V 计算的主流规范。尤其值得注意的是，该规范包含了对向量指令的支持，这对于高性能计算至关重要，同时也是以高能效方式处理海量数据的关键。

[![Cuzco CPU 框图](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_06-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_06.jpg)

Cuzco CPU 框图

[![Cuzco CPU 流水线](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_07-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_07.jpg)

Cuzco CPU 流水线

Condor 为 Cuzco 采用了一种“基于时间的微架构”（Time-Based Microarchitecture, TBM）。这个概念的技术深度远超一篇现场博客所能详尽解释的范畴，但其核心思想是利用硬件编译（hardware compilation）来进行指令定序。简而言之，他们试图通过设计一种晶体管数量更少、能效更高的方法来改进乱序执行（Out-of-Order execution）。从某些方面来看，这听起来像是传统静态调度（即通过编译器在软件层面提前安排好指令顺序）的一种变体，但又将部分工作移到了硬件中，同时并未完全摒弃其核心理念。

[![Cuzco 基于时间的微架构](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_08-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_08.jpg)

Cuzco 基于时间的微架构

[![Cuzco TBM 流程与时间资源矩阵](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_09-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_09.jpg)

Cuzco TBM 流程与时间资源矩阵

[![Cuzco 为何采用 TBM?](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_10-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_10.jpg)

Cuzco 为何采用 TBM?

[![Cuzco TBM 的优势](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_12-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_12.jpg)

Cuzco TBM 的优势

最终，Condor 相信他们的硬件调度系统能够以远低于传统乱序执行（OoO）的功耗和复杂度，实现更优异的结果。鉴于功耗已成为整体性能的关键瓶颈，这方面的优化无疑将转化为更高的性能回报。

[![Cuzco CPU 切片](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_14-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_14.jpg)

Cuzco CPU 切片

Cuzco 采用了基于切片（slice-based）的 CPU 设计，最多可集成 8 个 CPU 核心。

[![与 Andes 其他 CPU 核心的比较](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_18-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_18.jpg)

与 Andes 其他 CPU 核心的比较

与母公司 Andes 的其他乱序执行设计相比，Cuzco 团队相信，他们的设计在 SPECint2006 测试中的每时钟周期性能（IPC）几乎可以达到 Andes 现有 AX65 核心的两倍。

[![Cuzco 总结](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_20-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/46_condor_garibay_v3_20.jpg)

Cuzco 总结

该 IP 将以最多 8 核心的配置交付，每个核心拥有私有 L2 缓存和共享的 L3 缓存，并通过宽带 CHI 总线进行互联。

---

### 芯海回声，邀你共鸣

这篇文章为我们揭开了高性能 RISC-V 核心的神秘面纱，特别是其独特的微架构设计引人深思。那么，不如让我们畅所欲言，聊聊你对这些前沿技术的看法：

1.  **关于架构创新**：Cuzco 核心的“基于时间的微架构”（TBM）号称比传统乱序执行（OoO）更高效。大家怎么看这种技术路线？它会是未来高性能CPU的一个发展方向，还是一个过于激进的尝试？
2.  **关于生态之争**：RISC-V 阵营正涌现出越来越多像 Condor Computing 这样的高性能核心设计者。你认为 RISC-V 在服务器和数据中心领域，未来能否真正撼动 x86 和 Arm 的霸主地位？最大的挑战是什么？
3.  **关于团队与市场**：从一家仅有50名工程师的初创公司，到推出对标业界顶尖水平的 CPU 内核。你对 Condor Computing 的发展前景有何看法？在激烈的芯片市场竞争中，小团队如何才能脱颖而出？

期待在评论区看到你的真知灼见！