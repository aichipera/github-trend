

### 译者注

随着大模型军备竞赛进入白热化，算力已成为新的“石油”，而连接成千上万个GPU的“管道”——网络，则成为了决定AI集群效率的命脉。长久以来，英伟达凭借其闭环的InfiniBand生态，在高性能AI网络领域独占鳌头。然而，博通（Broadcom）此次推出的Tomahawk Ultra交换芯片，正是以太网阵营发起的有力反击。它试图通过引入低延迟、无损传输和在网计算等特性，证明开放标准的以太网同样能胜任大规模AI训练的严苛要求。这不仅是一场技术路线之争，更关乎未来AI基础设施的开放性与成本。

---

# [Hot Chips 2025: 博通Tomahawk Ultra芯片深度解析](20250902-broadcom-tomahawk-ultra-at-hot-chips-2025.mp3)

> 作者：[Patrick Kennedy](https://www.servethehome.com/author/patrick/)
>
> 原文链接：https://www.servethehome.com/broadcom-tomahawk-ultra-at-hot-chips-2025/
>
> 发布日期：2025年8月25日

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_04](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_04-696x348.jpg)

<center>博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_04</center>

几周前，我们报道了[博通发布用于纵向扩展（Scale-up）以太网的Tomahawk Ultra芯片](https://www.servethehome.com/broadcom-tomahawk-ultra-launch-for-scale-up-ethernet/)。而在今年的Hot Chips 2025大会上，我们获得了更多关于这款芯片的细节。

再次提醒，本文内容是在主题演讲现场实时记录的，如有疏漏或笔误，敬请谅解。

## 博通Tomahawk Ultra亮相Hot Chips 2025

首先，我们快速看一下当前高性能计算（HPC）和纵向扩展AI网络集群（AI fabric）的需求背景：

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_02](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_02-800x400.jpg)
<center>网络集群的需求</center>

博通表示，长久以来，以太网一直被认为不适合承载这类工作负载，但他们希望通过推出Tomahawk Ultra来改变这一局面。这款芯片支持 512 x 100G-PAM4，这意味着它甚至可以处理512个100GbE端口。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_04](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_04-800x400.jpg)
<center>Tomahawk Ultra芯片</center>

这是一款全新的51.2T交换芯片，专为高性能场景设计，具备在网计算（in-network computing）、稳定低延迟和高吞吐性能。在处理64字节（64B）大小的数据包时，其51.2T的交换容量能达到约每秒770亿个数据包的处理速度。

![博ahawk Ultra在Hot Chips 2025大会上的展示幻灯片_05](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_05-800x400.jpg)
<center>Tomahawk Ultra 核心亮点</center>

下图是Tomahawk Ultra芯片内部数据包转发流水线的简要示意图。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_06](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_06-800x400.jpg)
<center>数据包转发流水线</center>

我们再来看一下它的关键特性。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_07](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_07-800x400.jpg)
<center>关键特性</center>

我们在之前的文章中已经介绍过，这款芯片具备链路层重试（Link Layer Retry, LLR）功能，该功能在交换机的底层硬件层面实现。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_08](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_08-800x400.jpg)
<center>链路层重试（LLR）功能介绍 1</center>

下图更详细地解释了其工作原理。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_09](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_09-800x400.jpg)
<center>链路层重试（LLR）功能介绍 2</center>

此外，芯片还引入了基于信用的流控（Credit Based Flow Control, CBFC）功能，以确保缓冲区不会溢出。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_10](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_10-800x400.jpg)
<center>基于信用的流控（CBFC）</center>

数据包头也经过了优化，采用了专为AI网络集群设计的AI Fabric Header (AFH)，其中只包含最核心的字段，以提升头荷比（header to payload ratio）。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_11](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_11-800x400.jpg)
<center>AI Fabric Header (AFH)</center>

下图展示了该技术在纵向扩展以太网（Scale-up Ethernet, SUE）中的应用方式。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_12](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_12-800x400.jpg)
<center>AFH在纵向扩展以太网中的应用</center>

与英伟达的方案类似，Tomahawk Ultra在很多方面也支持用于集合操作（collective operations）的在网计算功能。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_13](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_13-800x400.jpg)
<center>在网计算（INC）</center>

拓扑感知的自适应路由（Topology aware adaptive routing）对于保持网络高效运行至关重要。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-Topology-Aware-Adaptive-Routing-800x400.jpeg)
<center>拓扑感知的自适应路由</center>

下面这张信息密集的幻灯片介绍了交换机上的可编程可见性（programmable visibility）和可观测性（observability）。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_15](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_15-800x400.jpg)
<center>网络可见性</center>

拥塞控制（Congestion control）确保了特定链路不会过载。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_16](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_16-800x400.jpg)
<center>拥塞控制</center>

这款交换芯片的一大亮点是，它能在所有端口上实现对64字节小包的线速处理，而不仅仅是一台处理大包的吞吐量机器。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_17](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_17-800x400.jpg)
<center>性能表现 1</center>

其延迟表现也非常优秀，低至250纳秒（ns）。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_18](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_18-800x400.jpg)
<center>性能表现 2</center>

（译者注：原文作者在此处提及他们实验室引入了新的测试设备，与文章主题关联不大，故此处略去。）

下面是博通交换芯片产品线的最新阵容，其中Tomahawk 6是总吞吐量高达102.4T的旗舰ASIC。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_20](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_20-800x400.jpg)
<center>交换芯片家族与市场定位图</center>

## 结语

我不确定这次大会上公布了多少我们之前未曾报道过的新信息，但这无疑是一款非常酷的芯片。博通正在全力推进其“纵向扩展以太网”项目，我们将拭目以待它将如何落地部署。或许更确切地说，我们期待着在未来参观HPC或AI数据中心时，能亲眼见到它的身影。

![博通Tomahawk Ultra在Hot Chips 2025大会上的展示幻灯片_21](https://www.servethehome.com/wp-content/uploads/2025/08/Broadcom-Tomahawk-Ultra-Hot-Chips-2025-_Page_21-800x402.jpg)
<center>总结</center>

---

## 技术前沿，等你开聊

这篇文章带我们领略了AI时代网络技术的前沿进展。博通的Tomahawk Ultra芯片显然是冲着打破英伟达InfiniBand在AI训练领域的垄断地位而来。对此，我们想听听你的看法：

1.  **以太网 vs. InfiniBand：** 你认为开放的以太网生态最终能否在性能上追平甚至超越专有的InfiniBand，成为未来AI数据中心的主流选择？为什么？
2.  **“在网计算”的价值：** 像集合操作这类计算任务从CPU/GPU卸载到网络设备上，你觉得在实际应用中能带来多大的性能提升？它会成为未来高性能交换机的标配吗？
3.  **对国内厂商的启示：** 面对这样的技术趋势，你认为国内的网络设备和芯片厂商应该如何布局，才能在未来的AI基础设施浪潮中抓住机遇？

欢迎在评论区留下你的真知灼见，一起探讨技术的未来！