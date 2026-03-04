
### 译者注

> PEZY Computing 是一家颇具传奇色彩的日本高性能计算公司，其创始人齐藤元章曾是超级计算机领域的风云人物，致力于通过“液浸冷却”和自研的众核处理器挑战世界超算TOP500榜单。尽管公司曾经历波折，但他们仍在坚持研发独特的MIMD（多指令多数据流）架构。与主流GPU采用的SIMD（单指令多数据流）不同，MIMD在处理高度分支、不规则的并行任务时理论上更具优势，这篇文章介绍的正是其第四代产品。

***

# [Hot Chips 2025速览：Pezy Computing的MIMD众核架构芯片PEZY-SC4s](20250902-pezy-computings-pezy-sc4s-a-mimd-many-core-architecture-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) 日期：2025年8月25日
> 原文链接：[https://www.servethehome.com/pezy-computings-pezy-sc4s-a-mimd-many-core-architecture-at-hot-chips-2025/](https://www.servethehome.com/pezy-computings-pezy-sc4s-a-mimd-many-core-architecture-at-hot-chips-2025/)

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_07-696x538.jpg)
*PEZY的MIMD架构*

今天在 Hot Chips 2025 CPU 议程上第二位登场的是 Pezy Computing 公司。这是一家来自日本、风格独特的CPU开发公司，专注于研发“多指令多数据流”（MIMD）CPU设计。

MIMD 是 CPU 设计中的一个旧概念，但在现实世界中我们并不常见到这种设计。目前，大多数设计都是“单指令多数据流”（SIMD）的变体。然而，MIMD 有潜力在性能上超越 SIMD，因为它能更优雅地处理那些线程高度独立或分化严重的场景——在这些场景下，只有少数（甚至没有）线程在同一时间执行相同的指令。

![PEZY 公司发展史](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_03-800x618.jpg)
*PEZY 公司发展史*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_10-800x618.jpg)
*PEZY MIMD 架构*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_11-800x618.jpg)
*PEZY MIMD 架构*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_12-800x618.jpg)
*PEZY MIMD 架构*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_13-800x618.jpg)
*PEZY MIMD 架构*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_14-800x618.jpg)*PEZY MIMD 架构*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_15-800x618.jpg)
*PEZY MIMD 架构*

![PEZY MIMD 架构](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_16-800x618.jpg)
*PEZY MIMD 架构*

这是一个时长25分钟、包含了大约40张幻灯片的演讲。因此，说它节奏飞快都算是轻描淡写了。

![PEZY-SC4s 的具体实现](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_19-800x618.jpg)
*PEZY-SC4s 的具体实现*

PEZY-SC4s 将采用台积电（TSMC）的5纳米工艺制造。单颗芯片的尺寸相当大，裸片面积（die size）约为556平方毫米。

![PEZY-SC4s 的具体实现](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_20-800x618.jpg)
*PEZY-SC4s 的具体实现*

![PEZY-SC4s 的具体实现](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_21-800x618.jpg)
*PEZY-SC4s 的具体实现*

![PEZY-SC4s 的处理单元（PEs）](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_25-800x618.jpg)
*PEZY-SC4s 的处理单元（PEs）*

![PEZY SC4s 的内存与IO](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_27-800x618.jpg)
*PEZY SC4s 的内存与IO*

![PEZY SC4s 的内存与IO](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_28-800x618.jpg)
*PEZY SC4s 的内存与IO*

![PEZY SC4s 的内存与IO](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_29-800x618.jpg)
*PEZY SC4s 的内存与IO*

![PEZY SC4s 系统主板](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_30-800x618.jpg)
*PEZY SC4s 系统主板*

![PEZY SC4s 功耗](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_37-800x618.jpg)
*PEZY SC4s 功耗*

除了设计工作，PEZY 还对他们的设计进行了仿真，以便了解其功耗和性能表现。与他们的上一代 SC3 设计相比，预计在执行 DGEMM（双精度通用矩阵乘法）工作负载时，能效将提升超过2倍。

![PEZY SC4s 性能](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_38-800x618.jpg)
*PEZY SC4s 性能*

在性能仿真中，他们观察到在使用 Smith-Waterman 算法（一种用于基因组序列比对的算法）时，性能提升了近4倍。

![PEZY 的未来计划](https://www.servethehome.com/wp-content/uploads/2025/08/22_pezy_hatta_v3_42-800x618.jpg)
*PEZY 的未来计划*

此外，第五代 PEZY 设计的研发工作已经启动。该公司计划采用3纳米（或更小）的工艺来设计 PEZY 5，并定于2027年发布。

***

### 芯海潮声：技术交流

看完这篇关于 Pezy Computing 的最新动态，你有什么想法？欢迎在下方留言，分享你的观点。

*   **MIMD vs. SIMD：** 在 GPU（典型的SIMD架构）主导AI和高性能计算的今天，你认为MIMD架构能否在特定领域（如文中提到的基因测序、或复杂的物理模拟）开辟出一条新路？它的优势和挑战分别是什么？
*   **日本的“芯”势力：** 日本在半导体材料和设备领域是绝对的王者，但在芯片设计，特别是超算芯片上，似乎总是走着一条与众不同的路。你如何看待 PEZY 这种“小而美”的公司的发展前景？它能在NVIDIA、AMD、Intel等巨头的夹缝中生存并壮大吗？
*   **性能预测：** 文章提到 SC4s 在特定算法上性能提升了4倍，能效提升了2倍。你认为这个数据在最终的实际产品中能兑现多少？对于这类专用性强的加速器，你更看重其峰值性能还是通用性和编程的便利性？