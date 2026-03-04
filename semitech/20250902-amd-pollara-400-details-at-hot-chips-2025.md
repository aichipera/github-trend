
### 译者注

AMD 的 Pollara 400 不仅仅是一张高速网卡，更是其在 AI 基础设施领域挑战 NVIDIA 霸主地位的关键一步。通过鼎力支持开放的“超级以太网联盟”（UEC）标准，AMD 联合众多行业巨头，意图打造一个能与 NVIDIA 专有的 InfiniBand 相抗衡的生态系统。这张 AI 网卡与其 Instinct GPU 和 EPYC CPU 相结合，构成了完整的 AMD AI 平台解决方案，为市场带来了更开放、更具选择性的“全家桶”。AI 数据中心的网络之战，已然烽烟四起。

---

# [AMD 在 Hot Chips 2025 大会揭晓 Pollara 400 网卡细节](20250902-amd-pollara-400-details-at-hot-chips-2025.mp3)

> 作者：[Patrick Kennedy](https://www.servethehome.com/author/patrick/) - 2025年8月25日
> 原文链接: https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第4页](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_04-696x392.jpg "AMD Pollara 400 Hot Chips 2025 _Page_04")](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_04-scaled.jpg)
<p align="center">AMD Pollara 400 Hot Chips 2025 大会幻灯片</p>

AMD 推出了一款全新的 AI 网卡（NIC），命名为 AMD Pensando Pollara 400 AI NIC。这是一款速率高达 400GbE、并为超级以太网联盟（Ultra Ethernet Consortium, UEC）标准做好准备的新型网卡。我们去年曾报道过 [AMD Pensando Pollara 400 超级以太网 RDMA 网卡的发布](https://www.servethehome.com/amd-pensando-pollara-400-ultraethernet-rdma-nic-launched/)，而现在我们获得了更多技术细节。

本文内容根据 Hot Chips 大会现场演讲整理，如有笔误，敬请谅解。

## AMD Pollara 400 在 Hot Chips 2025 大会的细节披露

以下是这款网卡的概览。它看起来像是 NVIDIA ConnectX-7 的竞争对手，但实际上提供了一些与众不同的特性。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第4页](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_04-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_04/)
<p align="center">AMD Pollara 400 Hot Chips 2025 大会</p>

既然这是一款 AI 网卡，我们来看看 AMD 对它的定位。NVIDIA 正在力推 PCIe 交换机，而 AMD 则选择拥抱现有的 PCIe 交换机生态，并设想其 GPU 和 Pollara 400 网卡在系统中实现 1:1 的配比，就像我们最近评测过的 [技嘉 G893-ZX1-AAX2](https://www.servethehome.com/gigabyte-g893-zx1-aax2-amd-instinct-mi325x-server-review/) 或 [华硕 ESC A8A-E12U](https://www.servethehome.com/asus-esc-a8a-e12u-8x-amd-instinct-mi325x-gpu-server-review/) 那样（本周晚些时候我们还会评测另一款类似产品）。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第5页，展示了在Instinct系统中的图示](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_05-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_05/)
<p align="center">AMD Pollara 400 在 Instinct 系统中的架构图</p>

这是该芯片的模块框图。值得注意的是，AMD 并未集成 PCIe 交换机，而是采用了 P4 语言来实现可编程性。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第6页，模块框图](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_06-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_06/)
<p align="center">AMD Pollara 400 模块框图</p>

下面这张图展示了其 P4 架构。P4 语言专为构建可编程的数据包处理流水线而设计。我们也在其他产品上看到过它的身影，例如英特尔为谷歌设计的 IPU 产品线，所以 P4 并非 AMD 独有的特性。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第7页，P4架构](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_07-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_07/)
<p align="center">AMD Pollara 400 的 P4 架构</p>

AMD 接下来深入介绍了 P4 流水线的各个组件。首先是表引擎（Table Engine, TE），它负责生成表键（table keys）并发起内存读取操作。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第8页，表引擎](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_08-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_08/)
<p align="center">AMD Pollara 400 表引擎</p>

还有一个是匹配处理单元（Match Processing Unit, MPU）。在网络处理中，经常需要根据数据包中的匹配模式来识别和筛选特定的流量。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第9页，MPU](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_09-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_09/)
<p align="center">AMD Pollara 400 匹配处理单元 (MPU)</p>

现在我们再次看到了前面展示过的 P4 架构图。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第10页，P4架构2](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_10-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_10/)
<p align="center">AMD Pollara 400 P4 架构图 (2)</p>

该芯片还针对虚拟地址到物理地址（VA to PA）的转换等功能进行了增强。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第11页，VA到PA转换](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_11-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_11/)
<p align="center">AMD Pollara 400 虚拟地址到物理地址转换 (va2pa)</p>

同时，它也支持原子内存操作。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第12页，原子操作](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_12-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_12/)
<p align="center">AMD Pollara 400 原子操作</p>

AMD 还实现了流水线缓存一致性。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第13页，缓存](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_13-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_13/)
<p align="center">AMD Pollara 400 缓存</p>

在 AI 的横向扩展网络（East-West Traffic）中，我们面临着一系列挑战。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第14页，AI横向扩展挑战](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_14-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_14/)
<p align="center">AI 横向扩展网络面临的挑战</p>

AMD 展示了网络性能如何直接影响系统整体性能。这一点至关重要，因为当你采用 1:1 的网卡与 GPU 配比时，网络性能的瓶颈会严重影响到成本高昂得多的 GPU 的效率。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第15页，后端AI网络](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_15-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_15/)
<p align="center">后端 AI 网络</p>

在 AI 网络中，高利用率是常态，这推动了对更高速交换机和网卡的需求。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第16页，网络利用率](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_16-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_16/)
<p align="center">网络利用率</p>

有问题的链路会拖慢整个系统。因此，数据包喷洒（packet spraying）和乱序重排（reordering）等技术正变得越来越普遍。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第17页，数据包喷洒](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_17-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_17/)
<p align="center">数据包喷洒</p>

网络和节点层面都可能发生拥塞。AMD 为此设计了专门的拥塞控制机制。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第18页，拥塞控制](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_18-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_18/)
<p align="center">拥塞控制</p>

在大型复杂的 AI 网络中，丢包时有发生，而我们绝不希望这种情况影响到训练任务的正常进行。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第19页，丢包](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_19-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_19/)
<p align="center">丢包问题</p>

正因如此，超级以太网联盟（UEC）正致力于利用以太网技术来解决这些挑战。UEC 的标准不仅限于网卡，它也对新型交换机芯片的设计产生了巨大影响，旨在围绕这些问题建立一个完整的生态系统。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第20页，超级以太网联盟](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_20-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_20/)
<p align="center">超级以太网联盟 (UEC)</p>

AMD 表示其网卡已为 UEC 做好准备。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第21页，UEC Ready](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_21-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_21/)
<p align="center">为 UEC 做好准备</p>

UEC 采用多路径（multipathing）技术来帮助解决前面提到的许多挑战。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第22页，UEC多路径](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_22-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_22/)
<p align="center">UEC 多路径技术</p>

下图展示了在发送端，用于路径选择的熵值是如何工作的。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第23页，熵值网卡发送端](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_23-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_23/)
<p align="center">熵值在网卡发送端的应用</p>

而这是在接收端的情况。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第24页，熵值网卡接收端](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_24-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_24/)
<p align="center">熵值在网卡接收端的应用</p>

UEC 也包含了拥塞控制机制。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第25页，UEC拥塞控制](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_25-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_25/)
<p align="center">UEC 拥塞控制</p>

这是 UEC 拥塞控制在网卡发送端的实现。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第26页，UEC拥塞控制发送端](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_26-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_26/)
<p align="center">UEC 拥塞控制：发送端</p>

这是 UEC 拥塞控制在网卡接收端的实现。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第27页，UEC拥塞控制接收端](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_27-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_27/)
<p align="center">UEC 拥塞控制：接收端</p>

此外，还有一个带有选择性确认（Selective Ack, SACK）的重传功能。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第28页，UEC SACK](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_28-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_28/)
<p align="center">UEC SACK</p>

这是 UEC SACK 在网卡接收端的实现。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第29页，UEC SACK接收端](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_29-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_29/)
<p align="center">UEC SACK：接收端</p>

这是请求方（requester side）的实现：

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第30页，UEC SACK请求方](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_30-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_30/)
<p align="center">UEC SACK：请求方</p>

AMD 还表示，将 RCCL（AMD版的NVIDIA NCCL）与支持UEC的 Pollara 400 网卡结合使用，可以提升性能。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第31页，性能](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_31-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_31/)
<p align="center">性能表现</p>

以下是 Pollara 400 AI 网卡的总结。

[![AMD Pollara 400 Hot Chips 2025 大会幻灯片第32页，总结](https://www.servethehome.com/wp-content/uploads/2025/08/AMD-Pollara-400-Hot-Chips-2025-_Page_32-800x450.jpg)](https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/amd-pollara-400-hot-chips-2025-_page_32/)
<p align="center">总结</p>

总结的核心似乎是：UEC 标准前景广阔，而 Pollara 网卡采用了 P4 技术。

## 结语

总而言之，这是一款令人兴奋的网卡。最近，在我们搭建 Keysight CyPerf 流量发生器的过程中，处理了大量 ConnectX-7 400GbE 网卡。希望我们未来也能在网卡评测中使用上这款新产品。

---

### 技术潮汐，邀你共议

看完了 AMD 在 AI 网络领域的最新布局，相信你一定有很多想法。不妨在这里分享你的见解，让我们一起探讨技术的未来：

1.  **开放 vs. 封闭：** 你如何看待 AMD 领衔的 UEC 开放标准与 NVIDIA 一家独大的 InfiniBand/Spectrum-X 之间的竞争？开放生态最终能撼动后者的护城河吗？
2.  **1:1 的黄金配比？** AMD 推崇在 AI 服务器中实现 GPU 与网卡的 1:1 配比，你认为这会成为未来 AI 集群的标配吗？这对系统设计和成本会带来哪些影响？
3.  **P4 的想象空间：** Pollara 400 的一大亮点是基于 P4 的可编程性。除了文章提到的功能，你认为这种高度灵活性还能在 AI 和高性能计算领域催生出哪些创新的网络应用？
4.  **AMD 的“组合拳”：** 从 EPYC CPU 到 Instinct GPU，再到如今的 Pollara 网卡，AMD 的 AI 平台版图日益完整。你认为这套“组合拳”相比竞争对手，优势和挑战分别在哪里？