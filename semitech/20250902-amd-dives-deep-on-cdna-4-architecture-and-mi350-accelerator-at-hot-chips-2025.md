

### 译者注

在人工智能算力竞赛白热化的今天，AMD正以前所未有的速度追赶行业领导者NVIDIA。本文深入剖析的MI350加速器及其背后的CDNA 4架构，正是AMD投下的一枚重磅炸弹。通过延续并优化Chiplet（芯粒）和3D堆叠技术，同时引入FP4/FP6等前沿数据格式，AMD旨在大幅提升AI训练与推理的能效比。这不仅是对NVIDIA Blackwell架构的直接回应，也彰显了AMD执行其年度产品迭代路线图的决心。苏姿丰博士带领下的AMD，正试图通过硬件性能和日渐成熟的ROCm软件生态，撬动被CUDA长期统治的AI计算市场。

---

# [AMD 在 Hot Chips 2025 大会深入解读 CDNA 4 架构与 MI350 加速器](20250902-amd-dives-deep-on-cdna-4-architecture-and-mi350-accelerator-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月26日
> 原文链接：[https://www.servethehome.com/amd-dives-deep-on-cdna-4-architecture-and-mi350-accelerator-at-hot-chips-2025/](https://www.servethehome.com/amd-dives-deep-on-cdna-4-architecture-and-mi350-accelerator-at-hot-chips-2025/)

![AMD MI350 加速器](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-6-696x392.jpg "AMD MI350 加速器")
*AMD MI350 加速器*

今天下午第二场重磅的机器学习加速器演讲属于AMD。该公司的芯片架构师们在今年的大会上，向观众详细介绍了为全新MI350系列加速器提供动力的CDNA 4架构。

与其前身MI300一样，AMD继续采用3D die堆叠技术来构建一颗强大的芯片，将多达8个加速器计算Die（XCDs）堆叠在一对I/O Die之上，最终打造出一个拥有1850亿晶体管的庞然大物。

![大语言模型：爆炸式增长](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-2-800x450.jpg)
*大语言模型：爆炸式增长*

大语言模型（LLM）的应用正在蓬勃发展。AMD正乘着这股硬件需求浪潮而来。

模型正变得越来越复杂。LLM的参数量不断增长，同时推理模型也需要更长的上下文长度。

![生成式AI的需求](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-3-800x450.jpg)
*生成式AI的需求*

要让这些模型保持高性能，需要更大的内存带宽和容量，更不用说还要保持高能效。当然，还需要能够将多个GPU集群化，以容纳那些最庞大的模型。

![Instinct MI350 系列](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-4-800x450.jpg)
*Instinct MI350 系列*

MI350已于今年交付，AMD强调他们正严格按照其路线图的时间表推进。

![MI350 架构增强](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-5-800x450.jpg)
*MI350 架构增强*

MI350被用于两个平台：MI350X面向风冷系统，而MI355X则面向液冷系统。

![MI350 GPU](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-6-1-800x450.jpg)*MI350 GPU*

MI350集成了1850亿个晶体管，AMD继续沿用芯粒（chiplet）和die堆叠技术。与MI300类似，计算die位于基础die（base die）之上，每个基础die承载4个计算die。

一套液冷系统的总板载功耗为1.4千瓦。

I/O die仍然采用6nm工艺。AMD表示，试图在更先进的工艺上制造基础die所能带来的收益甚微。

与此同时，计算die则采用了台积电最新一代的3nm N3P节点，旨在优化每瓦性能。

![MI350 GPU 芯粒](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-7-800x450.jpg)
*MI350 GPU 芯粒*

深入了解I/O die，其上的Infinity Fabric互联技术已经为适应MI350较少的基础die数量而做出改变。2个die的设计减少了芯片到芯片之间的die跨接数量，并允许更宽、时钟频率更低的D2D（Die-to-Die）连接，从而确保了能效。

每个插槽（socket）有7个Infinity Fabric（IF）链路。

![MI350 GPU 关键指标](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-8-800x450.jpg)
*MI350 GPU 关键指标*

总体而言，第四代Infinity Fabric（IF 4）比MI300中使用的IF 3多提供了2TB/s的带宽。而巨大的内存容量使得部署时所需的GPU总数更少，从而减少了同步开销。

![MI350 GPU 缓存与内存层级](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-9-800x450.jpg)
*MI350 GPU 缓存与内存层级*

从缓存和内存层级来看，本地数据共享存储（LDS）的容量相比MI300翻了一番。

![加速器计算Die (XCD)](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-10-800x450.jpg)
*加速器计算Die (XCD)*

每个全新的、更大的I/O die上可以放置4个计算die。因此，每个MI350共包含8个计算die。引擎的峰值时钟频率可达2.4GHz。每个XCD都拥有一个4MB的L2缓存，并与其他XCD的缓存保持一致性。

![支持的数据格式](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-11-800x450.jpg)
*支持的数据格式*

CDNA 4架构为多种数据类型带来了近乎翻倍的吞吐量，并首次引入了对FP6和FP4数据类型的硬件支持。

![支持数据格式的性能对比](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-12-800x450.jpg)
*支持数据格式的性能对比*

通过将AI数据类型的数学吞吐量几乎翻倍，AMD估计其速度比竞争对手的加速器快上2倍之多。

![SoC 逻辑框图](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-13-800x450.jpg)
*SoC 逻辑框图*

这是一张SoC逻辑框图，展示了Infinity Fabric、Infinity Cache、内存和XCDs是如何协同工作的。

![灵活的GPU分区](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-14-800x450.jpg)
*灵活的GPU分区*

转换视角，AMD开始关注平台层面的硬件视图，以及如何使用这些GPU来构建完整的系统。

一个MI350可以被配置为单个NUMA域，或者两个NUMA域。

访问连接到另一个基础die上的HBM内存会产生一定的延迟。这就是引入两个NUMA域配置的原因，它可以将一个XCD的访问限制在其本地内存中。

![灵活的GPU分区（续）](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-15-800x450.jpg)
*灵活的GPU分区（续）*

除了内存分区选项外，XCDs还可以被拆分成多个计算分区。配置范围可以从单个域，到将每个XCD都作为一个独立的GPU。

![Infinity 平台](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-16-800x450.jpg)
*Infinity 平台*

再将视野放大，一个多路（multi-socket）系统允许在单个基板上集成多达8个GPU。Infinity Fabric用于以全互联（all-to-all）拓扑结构连接这些GPU，而PCIe则用于连接主机CPU和网卡（NICs）。

![风冷 OAM 模块](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-17-800x450.jpg)
*风冷 OAM 模块*

AMD使用标准的OAM（OCP Accelerator Module）模块来承载MI350 GPU。

![风冷 UBB](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-18-800x450.jpg)
*风冷 UBB*

在一块通用基板（Universal Baseboard, UBB）上，最多可安装8个这样的模块。

![利用现有数据中心基础设施](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-19-800x450.jpg)
*利用现有数据中心基础设施*

对于现有的风冷MI300和MI325系统，MI350X是一个可以直接替换的升级选项。

![液冷方案](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-20-800x450.jpg)
*液冷方案*

与此同时，液冷的MI355X平台提供了更高的性能，代价是每个GPU的TDP（热设计功耗）高达1.4千瓦。这仍然使用OAM模块，但用更小的直接液冷冷板取代了庞大的风冷散热器。

![MI350X 和 MI355X 平台](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-21-800x450.jpg)
*MI350X 和 MI355X 平台*

两种MI350平台拥有相同的内存容量和带宽，但它们的计算性能有所不同，这反映了两者时钟频率的差异。

![机柜级解决方案](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-22-800x450.jpg)
*机柜级解决方案*

对于超大规模数据中心客户，液冷机柜可配置多达96或128个GPU。而风冷方案则支持每个机柜64个GPU。

![机柜基础设施](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-23-800x450.jpg)
*机柜基础设施*

当你需要一整套机柜时，AMD提供了一个参考机柜解决方案，其中所有主要芯片——GPU、CPU和横向扩展网卡——都来自AMD。

![ROCm 7](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-24-800x450.jpg)
*ROCm 7*

AMD的ROCm软件生态正逐渐成熟。基于软件的性能增益与硬件性能的提升，对于提高整体性能同等重要。

![推理性能](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-25-800x450.jpg)
*推理性能*

![大规模推理性能](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-26-800x450.jpg)
*大规模推理性能*

![GPU 训练性能](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-27-800x450.jpg)
*GPU 训练性能*

这里有几张幻灯片展示了在推理和训练方面的性能表现。

![年度路线图](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-28-800x450.jpg)
*年度路线图*

AMD再次重申了其路线图，以及其可靠的交付能力。这一承诺将延续到明年的MI400。

![加速AI计算性能](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-29-800x450.jpg)
*加速AI计算性能*

![Instinct MI400](https://www.servethehome.com/wp-content/uploads/2025/08/HC-AMD-Instinct-MI350-Series-GPUs-and-Platforms-FINAL-30-800x450.jpg)
*Instinct MI400*

明年，MI400将为前沿AI模型带来高达10倍的性能提升。

以上就是在Hot Chips 2025大会上关于MI350/CDNA 4的要点回顾。MI350已经开始向AMD的合作伙伴发货，因此公司非常期待在未来几个季度产能爬坡后，看到它能带来怎样的表现。

***

### “芯”潮澎湃，一“鉴”高下

看完了AMD最新的AI核弹，你有什么想法？欢迎在下方留下你的真知灼见，一起探讨技术的未来！

1.  **挑战者姿态：** AMD的MI350系列在硬件规格上直指NVIDIA的最新架构，你认为在实际应用中，AMD能否凭借其性能和日渐开放的ROCm生态，真正撼动NVIDIA在AI领域的霸主地位？差距主要还存在于哪些方面？
2.  **技术前沿：** CDNA 4架构引入了对FP4/FP6数据格式的硬件支持，这对于大模型推理和训练的能效比将带来多大提升？这会成为未来AI芯片设计的标配吗？
3.  **迭代速度：** AMD强调了其“一年一代”产品路线图的可靠性（MI300 -> MI350 -> MI400），这种快速迭代的策略对客户和开发者社区来说，是巨大的机遇还是艰巨的挑战？