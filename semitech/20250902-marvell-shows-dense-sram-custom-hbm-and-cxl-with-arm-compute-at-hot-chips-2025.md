
### 译者注

在人工智能（AI）算力需求爆炸式增长的今天，“内存墙”问题已成为限制芯片性能提升的核心瓶颈。Marvell 这次在 Hot Chips 大会上展示的成果，正是应对这一挑战的系统性解决方案。它不再孤立地看待某个环节，而是从最底层的片上 SRAM，到近存（near-memory）的定制化 HBM，再到远存（far-memory）的 CXL 内存扩展，构建了一个完整的多层级内存优化体系。这不仅展示了 Marvell 深厚的技术 IP 积累，也预示着未来高性能计算芯片设计的核心趋势：以数据为中心，通过异构和定制化打破传统架构的束缚。

***

# [Marvell 在 Hot Chips 2025 大会展示：高密度 SRAM、定制化 HBM 与集成 Arm 计算核心的 CXL 技术](20250902-marvell-shows-dense-sram-custom-hbm-and-cxl-with-arm-compute-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月26日
> 原文链接：https://www.servethehome.com/marvell-shows-dense-sram-custom-hbm-and-cxl-with-arm-compute-at-hot-chips-2025/

[![为什么内存如此重要](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-5-696x392.jpg "为什么内存如此重要")](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-5.jpg)

<center>为什么内存如此重要</center>

如果说机器学习在芯片制造领域举足轻重，那都算是轻描淡写了。作为我们这个时代的“淘金热”，与机器学习及其驱动硬件相关的演讲在今年的 Hot Chips 大会上占据了重要地位。事实上，就内容而言，机器学习是本届 Hot Chips 大会上最大的单一主题，有整整两个专场（3小时）专门用于来自机器学习和人工智能领域顶级公司的六场演讲。

为今天下午第一场会议拉开序幕的是 Marvell。这家芯片制造商和 IP 公司以各种方式参与了大量高性能机器学习芯片的研发，通常是通过其内存控制器设计。恰如其分地，该公司在今年的大会上探讨了为什么内存**几乎**是数据中心唯一重要的事情——以及 Marvell 的技术如何能让客户在内存带宽和内存容量方面保持领先。

[![为什么内存如此重要](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-5-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-5.jpg)

<center>为什么内存如此重要</center>

为什么内存如此重要？它是解决一切问题的关键。

如今的处理器（无论是 CPU 还是加速器）都在使用 SRAM 来提供巨大的带宽。因此，优化内存的使用变得至关重要。

目前存在多种内存技术：SRAM、HBM、DDR，它们在数据中心各司其职，都有一席之地。

### 嵌入式 SRAM

[![嵌入式 SRAM](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-6-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-6.jpg)

<center>嵌入式 SRAM</center>

我们从嵌入式 SRAM 讲起。如今，SRAM 单元的密度增长速度已经显著放缓。

[![带宽与容量](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-7-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-7.jpg)

<center>带宽与容量</center>

因此，Marvell 正在寻求突破这一瓶颈，并尽其所能推动技术向前发展。

[![Marvell 的 2nm 高密度 SRAM](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-8-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-8.jpg)

<center>Marvell 的 2nm 高密度 SRAM</center>

Marvell 将其定制的高密度 SRAM IP 应用于所有领先的芯片产品中。他们将在台积电（TSMC）的 2nm 节点上构建 SRAM。

[![改善 Vmin 的创新](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-9-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-9.jpg)

<center>改善 Vmin 的创新</center>

这是 2nm 节点的性能数据。他们在 2nm 工艺上实现了突破性的最低工作电压（Vmin）。这一切都有助于节省功耗，并从更宏观的角度降低总拥有成本（TCO）。

[![Marvell 定制化 SRAM](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-10-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-10.jpg)

<center>Marvell 定制化 SRAM</center>

Marvell 声称，在相同的工艺尺寸下，其定制的高密度 SRAM 的带宽密度是市面上通用 IP 的 **17倍**。Marvell 将向 Hot Chips 的与会者详细介绍他们是如何实现这一点的。

[![运行更快](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-12-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-12.jpg)

<center>运行更快</center>

他们是如何做到的？通过三种方式。首先，就是直接比业界其他高密度（HD）单元运行得更快。而且，Marvell 的独特之处在于，即使在大型 1Mbit SRAM 阵列中，他们也能保持其高目标频率。

[![构建更宽](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-13-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-13.jpg)

<center>构建更宽</center>

Marvell 还将其 SRAM 单元构建得更宽，通过更大的宏（macro）实现更高的倍数增益。

[![更多端口](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-14-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-14.jpg)

<center>更多端口</center>

最后，他们在相同面积内增加了更多端口，以提供更多带宽。这三者的结合最终使他们实现了 17 倍的提升。

[![Hot Chips 的精髓在于硬件实证](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-15-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-15.jpg)

<center>Hot Chips 的精髓在于硬件实证</center>

事实胜于雄辩，硬件就是最好的证明。上图是 Marvell 在 N3P 工艺上的高密度 SRAM 比较图。据该公司称，Mavell 的宏单元性能表现优异。

### 定制化 HBM 基础裸片（Base Die）

[![定制化 HBM 基础裸片](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-16-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-16.jpg)

<center>定制化 HBM 基础裸片</center>

接下来是定制化 HBM。Marvell 在这个领域已经深耕多年，并与所有三家主要的 HBM 供应商都建立了合作关系。

[![标准 vs 定制化基础裸片](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-17-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-17.jpg)

<center>标准 vs 定制化基础裸片</center>

定制化 HBM 是什么样的？它由一堆 DRAM 裸片堆叠在一个定制化的基础裸片（base die）之上。Marvell 采用标准的 DRAM 裸片，并搭配其专为与之配对的加速器而优化的定制化基础裸片。

[![通过定制化 HBM 架构增强各种处理器（XPU）](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-18-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-18.jpg)

<center>通过定制化 HBM 架构增强各种处理器（XPU）</center>

为什么要费这么大功夫呢？因为 HBM 接口会占用大量的片上（on-chip）面积，这会挤占计算单元的面积。为了解决这个问题，Marvell 尽可能地使用 die-to-die (D2D) IP，从而减少了片上面积的占用。据该公司称，他们还能在此过程中大幅降低功耗。

Marvell 还可以利用定制化 HBM 堆栈上的一些空闲区域来实现其他附加功能。

[![Marvell 定制化 HBM 的定义](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-19-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-19.jpg)

<center>Marvell 定制化 HBM 的定义</center>

在这里，Marvell 进一步阐述了标准 HBM PHY 和其定制化设计的区别。他们将大部分硬件从计算芯片上移到了 HBM 的基础裸片上。

[![关键对比](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-20-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-20.jpg)

<center>关键对比</center>

由于这些改变，Marvell 的方案显著减小了接口面积，同时接口功耗也大幅降低。

[![Marvell D2D IP 赋能定制化 HBM](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-21-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-21.jpg)

<center>Marvell D2D IP 赋能定制化 HBM</center>

Marvell 使用的是自家的 die-to-die IP。几年前，他们就率先推出了 32Gbps 的 D2D IP。

右侧的眼图显示：Marvell 在实验室里无法让它出现故障。他们推断其误码率（BER）小于 1E-30。

### 高容量内存

[![高容量内存](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-23-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-23.jpg)

<center>高容量内存</center>

接下来我们谈谈高容量内存，即 DDR 内存。（HBM 速度虽快，但容量不大）。这使得高容量内存对于 AI 系统和大型模型来说至关重要。

[![扩展至高容量内存](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-24-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-24.jpg)

<center>扩展至高容量内存</center>

Marvell 正在构建自己的高容量内存扩展设备。他们甚至在内存扩展设备中集成了处理器。

[![Structera A 近存加速器模块图](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-25-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-25.jpg)

<center>Structera A 近存加速器模块图</center>

这是一张 Structera A 近存加速器的模块图。它应有尽有，从加密和压缩功能到 Arm Neoverse v2 CPU 核心一应俱全。其中还包含一个嵌入式硬件安全宏，以确保数据中心内存的安全性。

[![高容量内存（基础案例）](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-26-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-26.jpg)

<center>高容量内存（基础案例）</center>

Marvell 表示，他们的技术可以显著改善系统内的延迟和带宽。

[![高容量内存（扩展案例）](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-27-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-27.jpg)

<center>高容量内存（扩展案例）</center>

使用内存扩展器设备可以避免数据绕道 CPU 和任何 PCIe 交换机，从而显著降低延迟。

### 总结：全方位的内存优化

[![总结：全方位的内存优化](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-28-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/40_Marvell_Kuemerle_final-28.jpg)

<center>总结：全方位的内存优化</center>

总结一下：高密度 SRAM、定制化 HBM 和优化的 DDR 内存协同工作，在内存层次结构的每一层都提供了更高的内存带宽和更低的延迟。

***

### 技术前沿，思想碰撞

看完了 Marvell 这套从片上到远端的“内存组合拳”，相信大家都有不少想法。欢迎在评论区分享你的观点：

1.  **“内存墙”依旧是瓶颈吗？** 你认为在 AI 大模型时代，限制算力发展的最大瓶颈是内存带宽、容量还是延迟？Marvell 的多层次方案能从根本上解决问题吗？
2.  **定制化是未来吗？** Marvell 将 HBM 的控制逻辑移出计算芯片的做法，本质上是一种“卸载”。你如何看待这种设计思路的优缺点？它会成为未来异构计算的主流吗？
3.  **CXL 的想象空间有多大？** 随着 CXL 技术的成熟，你认为由内存池组成的“可组合式基础架构”会成为数据中心的主流吗？实现这一愿景的最大挑战是什么？
4.  **计算向数据移动。** Marvell 在内存扩展器中集成了 Arm 核心，实现了“近内存计算”。你觉得这种架构最适合哪些应用场景？它会如何改变我们编写软件的方式？