
### 译者注

在AI算力需求呈指数级增长的今天，算力的瓶颈已从单纯的芯片计算能力，逐渐转移到了芯片之间的通信效率上。NVIDIA凭借其NVLink和InfiniBand技术构建了强大的护城河。而华为此次在Hot Chips上展示的UB-Mesh，则是一次从根基上挑战现有架构的雄心勃勃的尝试。“统一总线”理念直指当前数据中心内部PCIe、Ethernet、CXL等多种协议并存的“乱象”，旨在降低延迟和复杂性。更关键的是，其提出的“亚线性”成本增长模型，精准地切中了当前构建大规模AI集群最大的痛点之一——高昂的网络成本。这不仅是一项技术发布，更是华为对未来AI数据中心形态的一次深刻思考和布局。

***

# [华为在 Hot Chips 2025 大会发布面向大型 AI 超级节点的 UB-Mesh 互联技术](20250902-huawei-presents-ub-mesh-interconnect-for-large-ai-supernodes-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月26日
> 原文链接：[https://www.servethehome.com/huawei-presents-ub-mesh-interconnect-for-large-ai-supernodes-at-hot-chips-2025/](https://www.servethehome.com/huawei-presents-ub-mesh-interconnect-for-large-ai-supernodes-at-hot-chips-2025/)

![华为 UB-mesh](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-1-696x392.jpg)

<center>华为 UB-mesh</center>

午休前的第三场、也是最后一场机器学习相关的演讲来自华为。与其他许多前来推销产品的机器学习厂商不同，华为的演讲更侧重于基础技术。具体来说，就是如何高效地利用网格（mesh）架构来互联大型AI系统中的芯片。

着眼于所谓的“超级节点”（SuperNodes）——即拥有超过一百万个芯片的单一超级计算集群——华为正在展示其统一总线网格（United Bus mesh, UB-mesh）技术。当前面临的核心挑战是：如何在将网络规模扩展到能够为超级节点中所有芯片提供低延迟连接的同时，避免网络设备的成本超过加速器芯片本身，并在此过程中保持互联的极高可靠性。

本次演讲一反 Hot Chips 的常态，是一场线上虚拟演讲。廖博士（Dr. Liao）从中国远程发表了这次演讲。

![超级节点正成为吉瓦级 AI 数据中心的常态](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-2-800x450.jpg)

<center>超级节点正成为吉瓦级 AI 数据中心的常态</center>

这场演讲更偏向于架构和计算机科学，而非纯粹的工程技术。华为期望构建一个可以扩展到百万级处理器规模的网格网络。在这样的规模下，一个超级节点的大小可能相当于一整个数据中心。

系统的庞大规模意味着，它不仅仅是连接GPU，内存池、SSD、网卡和交换机等所有组件都成为了这个统一节点的一部分。

![统一总线：统一通用总线与网络协议](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-3-800x450.jpg)

<center>统一总线：<br>统一通用总线与网络协议</center>

华为倡导使用一种统一总线，通过单一协议取代当前各种特定技术协议“大杂烩”的局面。通用协议意味着任何端口都可以连接到任何端口，且无需进行协议转换。这通过消除那些可能增加延迟的环节，从而有效降低了延迟。

统一协议还将允许一个更简化的体系结构。

即使有这些宏伟目标，UB（统一总线）仍然可以在以太网上运行。

![将本地总线扩展至数据中心规模所面临的挑战](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-4-800x450.jpg)

<center>将本地总线扩展至数据中心规模所面临的挑战</center>

但要实现这些目标，必须克服几个挑战。其中一个特别值得关注的问题是物理链路变得更长——网络需要跨越整个数据中心——这意味着必须使用光纤连接。而光网络的错误率比电连接高出2到3个数量级。这就要求在其上层构建更优秀的错误恢复技术。

同时，巨大的规模意味着整个节点必须能够抵御节点故障。在如此大的规模下，单个服务器的故障不再是 *“是否会发生”* 的问题，而是 *“何时会发生”* 的问题。

![百倍节点带宽，成本却远低于百倍](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-5-800x450.jpg)

<center>百倍节点带宽，成本却远低于百倍</center>

如何构建一个物理网络，使其带宽增加100倍，而成本却远低于100倍？

华为认为，这需要一种全新的拓扑结构。可以说是一种混合拓扑，它在不同层级上融合了多种网络类型的优势。

华为正在探索的一种可能性是融合三种技术：在最高层使用CLOS架构，其下使用n维网格（n-dimensional mesh）——适用于从单个机架到数十个节点的规模——然后在更低成本的选项中使用n维稀疏网格（n-dimensional spare mesh）。

![关键洞察：大语言模型训练呈现成对的层级式流量模式](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-6-800x450.jpg)

<center>关键洞察：大语言模型训练呈现成对的层级式流量模式</center>

大语言模型（LLM）的训练达到了五维并行。

![UB-Mesh：层级化、局部化的nD-FullMesh网络拓扑](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-7-800x450.jpg)

<center>UB-Mesh：层级化、局部化的nD-FullMesh网络拓扑</center>

这是一张UB-mesh拓扑的概念图。它被实现为多个维度。每个维度内的任意节点之间都具有全连接（full connectivity）。然后，更高维度负责连接较低的维度。

![Clos 与 UB-Mesh 系统成本对比](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-8-800x450.jpg)

<center>Clos 与 UB-Mesh 系统成本对比</center>

所有这些设计都需要与成本进行权衡。你绝不希望网络设备的成本超过那些真正执行计算工作的计算设备。

随着网络规模的扩大，传统网络的成本会呈超线性（super-linear）增长。但UB-mesh的成本增长是亚线性（sub-linear）的，即使计算节点数量大幅增加，也只会带来适度的成本上升。

![8000节点真实案例 – CLOS + 2D-Mesh](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-9-800x450.jpg)

<center>8000节点真实案例 – CLOS + 2D-Mesh</center>

这是一个真实世界的例子。一个拥有64个节点的系统，采用了CLOS + 2D-Mesh的配置。

![高弹性光链路](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-10-800x450.jpg)

<center>高弹性光链路</center>

但是，如何才能让光链路的可靠性足以满足超级节点的需求呢？

需要提升光链路本身的弹性。首先，支持在同一光模块上的备用光链路上进行链路级重试，以确保数据包不会再次通过有问题的路径。

针对更严重故障的第二种方案是，以交叉（crossover）方式将MAC（媒体访问控制层）连接到多个光模块，这样一来，即使一个光模块发生故障，仍然有一个可用的好模块。

![层级化系统弹性：百倍平均无故障时间](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-11-800x450.jpg)

<center>层级化系统弹性：百倍平均无故障时间（MTBF）</center>

华为的目标是将平均无故障时间（MTBF）提升100倍。实现这一目标的方法之一是提供热备用（hot spare）机架，以便在某个节点发生故障时接管其工作。发生故障的机架随后被修复，并作为新的热备用机架重新加入节点。此外，如果机架本身内置了额外的备用芯片，那么该机架自身也具备一定的弹性；在这种情况下，它可以作为一个“弱热备件”（weak hot spare）返回系统。

![总结](https://www.servethehome.com/wp-content/uploads/2025/08/67_Huawei_Liao_final-12-800x450.jpg)

<center>总结</center>

总而言之，通过转向统一协议，并对网络拓扑和硬件冗余进行多重改进，UB-mesh将使得构建和部署可靠的数据中心规模的超级节点成为可能。那么，有人想要一个1GW（吉瓦）级别的AI数据中心吗？

***

## 碰撞思想的火花

看完了华为对未来AI超级节点网络架构的构想，相信你一定有很多想法。欢迎在下方分享你的观点，让我们一起探讨技术的未来！

1.  **UB-Mesh vs. NVLink/InfiniBand**：华为的UB-Mesh方案，在您看来与NVIDIA的NVLink/NVSwitch或业界主流的InfiniBand/RoCE方案相比，其核心优势和潜在挑战分别是什么？
2.  **“统一总线”的未来**：“统一总线”的理念非常吸引人，它是否会成为未来数据中心架构的主流？在实现这一目标的路上，最大的障碍会是什么？（例如，行业标准、生态系统支持等）
3.  **成本与可靠性的权衡**：在您构建或管理大规模计算集群的过程中，网络成本和可靠性是否是主要的痛点？对于华为提出的“亚线性成本”和“百倍可靠性”的目标，您认为在现实世界中实现的可能性有多大？