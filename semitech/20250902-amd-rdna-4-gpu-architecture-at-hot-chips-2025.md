### 译者注

本文是一篇颇具前瞻性的“未来”报道，时间设定在2025年8月。尽管文章内容为虚构，但其中探讨的技术方向，如光线追踪（RT）性能的深化、AI/ML能力的整合以及对SoC架构的模块化设计，精准地反映了当前业界对下一代GPU的普遍预期。现实中，关于RDNA 4的传闻普遍认为AMD可能会暂时放弃高端旗舰市场，转而聚焦于能效比更优的中端主流产品。这篇文章可以看作是对RDNA 4技术潜力的一次极具想象力的推演，读起来饶有趣味。

---

# [AMD 在 Hot Chips 2025 大会上详解 RDNA 4 GPU 架构](20250902-amd-rdna-4-gpu-architecture-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月25日
> 原文链接: https://www.servethehome.com/amd-rdna-4-gpu-architecture-at-hot-chips-2025/

[![AMD RDNA4 Hot Chips 2025](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_01-696x392.jpg "AMD RDNA4 Hot Chips 2025")](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_01.jpg)
*AMD RDNA4 @ Hot Chips 2025*

今天下午的 Hot Chips 2025 图形技术会议由 AMD 拉开序幕。该公司在今年早些时候已经推出了 RDNA 4 架构及相关的 Radeon RX 9000 系列显卡，并已发布了两款 GPU。

由于 AMD 的这一代 Radeon GPU 已经相当成熟，因此公司在今年的 Hot Chips 大会上并没有什么石破天惊的猛料要爆。不过，他们仍然出席了会议，向与会者更新了 RDNA 4 架构的最新动态，并披露了一些在初次发布时未曾涵盖的细节。

[![RDNA 4 愿景](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_02-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_02.jpg)
*RDNA 4 愿景*

让我们快速回顾一下 AMD RDNA 4 的设计目标。这是一个专注于图形（游戏）的架构，对光线追踪和机器学习（AI）硬件都进行了重大更新。AMD 以一种前瞻性的视角来构建该架构，旨在应对未来的图形工作负载。

其他值得注意的改进包括：压缩技术、媒体和显示引擎。

[![RDNA 4 概览](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_03-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_03.jpg)
*RDNA 4 概览*

回顾一下 AMD 的逻辑设计，单个 GPU 由最多多个着色器引擎（Shader Engines）构成。这一代增大了 L2 缓存，以更好地为光线追踪（RT）工作负载做准备。同时，这也标志着 AMD 的无限缓存（Infinity Cache）技术发展到了第三代。所有这些设计都是为了确保核心能够获得充足的数据供给。

[![RDNA 4 媒体与显示引擎](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_04-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_04.jpg)
*RDNA 4 媒体与显示引擎*

RDNA 4 的一项主要改进在于其媒体与显示引擎。在 Navi 48 GPU 中，AMD 集成了两个这样的媒体引擎。媒体模块在编码器方面获得了重大更新，例如为 AV1 编码增加了 B 帧支持，并全面降低了延迟。

与此同时，显示模块也增加了一些新功能，比如将 Radeon Image Sharpening 2（RIS 2，图像锐化技术）直接集成到硬件模块中，而不是通过着色器特效来处理。

[![RDNA 4 计算引擎](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_05-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_05.jpg)
*RDNA 4 计算引擎*

在数值计算方面，一切始于计算引擎（Compute Engine）。值得注意的是，标量单元（scalar units）增加了对浮点运算的支持。更不用说在机器学习（矩阵运算）方面还有显著的改进（下文将详述）。

[![RDNA 4 光线追踪](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_06-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_06.jpg)
*RDNA 4 光线追踪*

在光线追踪（RT）方面，RDNA 4 将其光线相交性能提升了一倍。此外，还增加了一个专用的硬件实例变换器（hardware instance transformer），将这项任务从着色器程序中解放出来。

BVH（包围盒层次结构）的结构也得到了加宽，从 4-wide 升级到 8-wide，这与翻倍的相交引擎相得益彰。另一方面，通过节点压缩技术减小了 BVH 的体积。

[![包围盒](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_07-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_07.jpg)
*包围盒*

一项新的光线追踪硬件特性是定向包围盒（oriented bounding boxes），它旨在解决几何体与世界坐标轴不一致而导致的“伪正相交”（false-positive intersections）问题。

简而言之：旋转包围盒，使其更好地匹配世界几何体。

上方的热力图显示了重新定向的包围盒如何显著减少了伪正相交。

[![乱序内存访问](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_08-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_08.jpg)
*乱序内存访问*

乱序内存访问（Out-of-order memory accesses）同样是光线追踪性能的关键组成部分，因为光追天然具有极高的发散性（divergent）。

只要请求之间相互独立，一些请求就可以超越其他请求，打破严格的顺序。与其他延迟隐藏技术类似，这有助于通过将已准备就绪的工作排队并执行，而无需等待其他被延迟的工作，从而保持更高的效率。

[![光线遍历架构](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_09-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_09.jpg)
*光线遍历架构*

光线追踪性能简述：BVH 吞吐量翻倍为 RDNA 4 带来了大部分的光追性能提升。但乱序内存访问、硬件实例变换和定向包围盒等技术进一步增强了其性能，使其光追性能相较于 RDNA 3 实现了约 2 倍的提升。

[![动态寄存器](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_10-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_10.jpg)
*动态寄存器*

RDNA 4 还通过动态寄存器分配（dynamic register allocations）对着色器引擎进行了一些更新。

光线追踪往往会消耗大量寄存器，但并非在所有执行阶段都是如此。例如，光线遍历（Traversal）阶段使用的寄存器就相对较少。

RDNA 3 会根据最坏情况来分配寄存器。而 RDNA 4 则能够动态分配寄存器，只使用当前所需的寄存器，并在不再需要时立即释放。

在实践中，这使得 AMD 能够将一个额外的计算波形（wave）塞入被释放的寄存器中，从而增加了相较于 RDNA 3 的“在途波形”（waves in flight）数量。

[![AI & WMMA](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_11-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_11.jpg)
*AI & WMMA*

在机器学习/AI 工作负载方面，RDNA 4 增加了对 FP8 数据格式的支持，以及结构化稀疏（structured sparsity）技术。

[![光线追踪 vs. 路径追踪](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_12-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_12.jpg)
*光线追踪 vs. 路径追踪*

[![AI 降噪](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_14-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_14.jpg)
*AI 降噪*

路径追踪（Path tracing）能产生更优质的图像，但它需要发射海量光线，成本极其高昂，以至于无法真正发射所需数量的全部光线。这时，AI 就派上用场了，它通过神经辐射缓存（neural radiance cache）、神经超采样（neural supersampling）和降噪（denoising）技术来填补因光线不足而产生的画面空白。

[![SoC 架构](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_16-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_16.jpg)
*SoC 架构*

在会议的最后几分钟，AMD 将话题从图形转向了 GPU 的 SoC 架构。具体来说，他们展示了数据如何在着色器引擎、各级缓存和内存控制器之间流动。其 Infinity Fabric 互联技术每时钟周期最高可提供 1KB 的带宽。

[![显著特性](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_17-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_17.jpg)
*显著特性*

RDNA 4 在结构上是模块化的。AMD 在设计 Navi 48 时，使其可以被“一分为二”来制造更小的 GPU，从而减少了开发不同 GPU 型号所需的工作量。

RAS（可靠性、可用性和可服务性）特性也在此发挥作用，以提高产品的可靠性。

[![压缩与解压](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_18-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_18.jpg)
*压缩与解压*

如前所述，RDNA 4 拥有全新的内存压缩/解压功能。这对软件层是完全透明的，所有操作均由硬件处理。AMD 观察到，这使得 Fabric 总线带宽占用降低了约 25%。

[![灵活配置](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_19-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_19.jpg)
*灵活配置*

所有这些设计即便在单个 GPU 内部也具备极高的灵活性，允许通过屏蔽不同的功能模块来创造新的显卡 SKU，或用于挽救存在瑕疵的芯片（die salvaging）。

[![总结](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_21-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/RDNA4_21.jpg)
*总结*

总结一下，凭借其强大的光线追踪和 AI/ML 能力，RDNA 4 专为下一代游戏而生。

---

## 极客洞见

看完了这篇来自“未来”的 RDNA 4 深度解析，不知道大家有何感想？让我们一起畅想和讨论一下吧！

1.  **光追与AI，双管齐下？**
    文章重点介绍了 RDNA 4 在光追和 AI 方面的巨大进步，比如硬件实例变换、乱序内存访问和动态寄存器。大家认为这些技术能让 AMD 在光追赛道上真正追平甚至反超对手吗？
2.  **模块化设计，未来的趋势？**
    Navi 48 “一分为二”的模块化设计思路非常亮眼，这是否意味着未来的 GPU 产品线会更加灵活，甚至出现更多针对特定需求的“定制版”SKU？你期待这样的产品吗？
3.  **游戏为本，还是 AI 优先？**
    RDNA 4 似乎仍将核心放在“为下一代游戏而生”，AI 功能更像是为了提升游戏体验（如AI降噪）而服务。在 AI 计算需求日益增长的今天，你认为消费级 GPU 的发展重心应该放在哪里？是极致的游戏画面，还是更强的通用 AI 能力？

欢迎在评论区留下你的真知灼见！