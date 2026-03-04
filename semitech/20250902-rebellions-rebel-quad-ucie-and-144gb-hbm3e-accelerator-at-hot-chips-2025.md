
### 译者注

韩国AI芯片初创公司Rebellions在Hot Chips 2025上展示的REBEL-Quad加速器，无疑是今年半导体领域的一大亮点。它不仅是首批公开展示并运行的、采用开放标准UCIe进行芯粒（chiplet）互联的AI芯片之一，更集成了高达144GB的HBM3E内存。这标志着开放生态正在打破以往由巨头（如NVIDIA的NVLink）主导的专有互联壁垒，为芯片设计的未来提供了更多灵活性与可能性，也让Rebellions这家新创公司有了挑战行业巨人的底气。

***

# [Rebellions在Hot Chips 2025大会上展示REBEL-Quad：集成UCIe与144GB HBM3E的AI加速器](20250902-rebellions-rebel-quad-ucie-and-144gb-hbm3e-accelerator-at-hot-chips-2025.mp3)

> 作者：[Patrick Kennedy](https://www.servethehome.com/author/patrick/) - 2025年8月24日
> 原文链接：https://www.servethehome.com/rebellions-rebel-quad-ucie-and-144gb-hbm3e-accelerator-at-hot-chips-2025/

![Rebellions REBEL Quad 封装在 Hot Chips 2025 大会上的大幅照片](https://www.servethehome.com/wp-content/uploads/2025/08/Rebellions-REBEL-Quad-Package-At-Hot-Chips-2025-Large-696x522.jpeg)
*Rebellions REBEL-Quad 封装在 Hot Chips 2025 大会上的大幅照片*

在Hot Chips 2025大会上，Rebellions公司展示了其正在运行的全新AI加速器。值得注意的是，这款名为Rebellions REBEL-Quad的加速器不仅配备了四个HBM3E内存堆栈，提供了惊人的144GB内存，还采用了UCIe作为其芯粒（chiplet）间的互联技术。多年来我们一直在关注UCIe的发展，而这次，我们终于看到了一款现代芯片不仅应用了这项芯粒互联技术，还以此为傲地进行宣传。

## Rebellions REBEL-Quad：UCIe与144GB HBM3E的前沿结合

下图展示的是基于三星SF4X工艺和CoWoS-S封装技术的芯片封装。每个封装上集成了四个计算ASIC、四个HBM3E内存堆栈以及四个集成硅电容器（ISC）。有趣的是，这是一张支持双PCIe Gen5 x16接口的卡。考虑到NVIDIA的GB300即将引领业界进入PCIe Gen6时代，而我们眼前看到的还只是一块REBEL-Quad的开发板，这不禁让人觉得，如果它能直接支持PCIe Gen6来对标NVIDIA，或许会更具前瞻性。另一个重磅特性是，该芯片采用了UCIe-A标准来实现高带宽的内部互联。

![Rebellions REBEL-Quad 在 Hot Chips 2025 大会上的规格参数图](https://www.servethehome.com/wp-content/uploads/2025/08/Rebellions-REBEL-Quad-Specs-At-Hot-Chips-2025-Large-800x600.jpeg)
*Rebellions REBEL-Quad 在 Hot Chips 2025 大会上的规格参数*

这是一块REBEL-Quad PCIe加速卡。

![Rebellions 加速卡在 Hot Chips 2025 大会上的照片](https://www.servethehome.com/wp-content/uploads/2025/08/Rebellions-Card-At-Hot-Chips-2025-Large-800x600.jpeg)
*Rebellions 加速卡在 Hot Chips 2025 大会上的照片*

这是芯片封装的特写。你可以清晰地看到四组硅片，这正是其“Quad”（四核）名称的由来。

![Rebellions REBEL-Quad 芯片封装在 Hot Chips 2025 大会上的照片](https://www.servethehome.com/wp-content/uploads/2025/08/Rebellions-REBEL-Quad-Package-At-Hot-Chips-2025-Large-800x600.jpeg)
*Rebellions REBEL-Quad 芯片封装在 Hot Chips 2025 大会上的照片*

许多公司都喜欢展示芯片封装，但我们这次看到的远不止于此。Rebellions公司在一块开发板上现场运行了他们的新芯片。

![Rebellions REBEL-Quad 在 Hot Chips 2025 大会上运行的照片](https://www.servethehome.com/wp-content/uploads/2025/08/Rebellions-REBEL-Quad-Running-At-Hot-Chips-2025-Large-800x600.jpeg)
*Rebellions REBEL-Quad 在 Hot Chips 2025 大会上运行中*

这是它正在现场运行Llama 3.3 70B模型的演示。对于一些更关注AI加速器的STH读者来说，这是一款崭新的硬件正在实际工作的证明。而对于那些关注芯片技术的读者来说，这更是一个采用UCIe标准的芯片成功运行的实例。

![Rebellions REBEL-Quad 在 Hot Chips 2025 大会上进行 Llama 3.3 70B 模型演示的照片](https://www.servethehome.com/wp-content/uploads/2025/08/Rebellions-REBEL-Quad-llama-3.3-70b-Demo-At-Hot-Chips-2025-Large-800x600.jpeg)
*Rebellions REBEL-Quad Llama 3.3 70B 模型演示现场*

对于关心性能的朋友，这次演示中的Llama 3.3 70B模型，其输出速度为平均每个token 35.5毫秒。不过，正如你所见，这还只是在一块开发板上运行。

## 结语

能亲眼看到它运行起来，真是太酷了。每当我和UCIe标准的相关人士聊天时，我都会问何时能看到实际产品落地。得到的答案通常是，这取决于各家公司自己是否愿意宣传他们在封装内部使用了UCIe。现在，我们终于有了一个绝佳的范例。Rebellions能够将如此多的硅片集成在一个大型封装中，并现场展示其运行，这本身就说明了很多问题。许多AI加速器公司空有想法，但这些想法往往无法转化为能够公开演示的硅片。在此，向Rebellions团队（以及UCIe生态的同仁们）表示祝贺！

***

### 芯海拾贝：聊聊你的看法

Rebellions的REBEL-Quad无疑为AI硬件市场投下了一颗震撼弹。它不仅仅是一款新产品，更是开放标准挑战专有生态的一次重要实践。我们诚邀您一同探讨：

1.  **开放标准 vs. 专有壁垒**：你认为UCIe这样的开放互联标准，能否真正撼动NVIDIA凭借NVLink建立的护城河？它会对未来的AI芯片设计带来哪些深远影响？
2.  **性能与迭代的权衡**：REBEL-Quad采用了PCIe Gen5，而同期NVIDIA已转向Gen6。你认为这对初创公司来说是一个致命的短板，还是一个在成本与上市速度之间做出的合理取舍？
3.  **AI硬件的未来格局**：随着Rebellions这样的“后浪”展示出强大的实力，你如何看待AI加速器市场的未来？是会继续一家独大，还是会迎来一个百花齐放的时代？
4.  **性能速览**：对于Llama 3.3 70B模型跑出35.5毫秒/token的成绩（在开发板上），你有什么看法？这个性能在当今市场处于什么水平？

期待在评论区看到你的真知灼见！