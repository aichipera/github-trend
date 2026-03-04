
### 译者注

DPU（数据处理器）或英特尔所称的 IPU（基础设施处理器），已成为继 CPU 和 GPU 之后，数据中心的“第三大支柱”。它旨在从 CPU 手中接管网络、存储和安全等基础设施的繁重任务，从而释放宝贵的计算资源。当前，英伟达（BlueField）、AMD（Pensando）和英特尔（IPU）在此领域展开了激烈角逐。本文介绍的 E2200 是英特尔追赶对手的关键产品，它不仅将网络吞吐量提升至 400G，与竞品看齐，更采用了先进的台积电 5nm 工艺和强大的 Arm Neoverse N2 核心，彰显了英特尔在此赛道上的决心与实力。

***

# [英特尔在 Hot Chips 2025 大会上发布 400G DPU——IPU E2200](20250902-intel-ipu-e2200-400g-dpu-at-hot-chips-2025.mp3)

> 作者：[Patrick Kennedy](https://www.servethehome.com/author/patrick/) - 2025年8月25日
> 原文链接：https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/

[![英特尔 E2200 IPU 在 Hot Chips 2025 上的架构图](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_04-696x392.jpg "Intel E2200 IPU Hot Chips 2025 Architecture")](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_04-scaled.jpg)
> 英特尔 E2200 IPU 在 Hot Chips 2025 大会上展示的架构

现在，让我们来聊聊一个让我非常兴奋的新品——代号为“Mount Morgan”的英特尔新款 IPU E2200。尽管英特尔称之其为 IPU，但业界其他公司普遍称之为 DPU。这是对 [英特尔 IPU E2100 DPU](https://www.servethehome.com/intel-ipu-e2100-dpu-finally-launched-for-the-mass-market-arm/) 的一次重要升级。虽然我曾有幸拍到过 E2100 的照片，但我们从未真正拿到一台用于实验室测试，这一点我至今都感到意外。

[![英特尔 Mount Evans 在 Vision 2022 大会上的展示](https://www.servethehome.com/wp-content/uploads/2022/05/Intel-Mount-Evans-Vision-2022-Top-3-800x534.jpg)](https://www.servethehome.com/new-intel-mount-evans-ipu-asic-dpu-at-intel-vision-2022/intel-mount-evans-vision-2022-top-3/)
> 英特尔 Mount Evans（E2100 的代号）在 Vision 2022 大会上的风采

或许现在想拿到 E2100 已经太晚了，因为下一代产品即将来临。另外，请注意，本文是我们在 Hot Chips 现场实时报道撰写的，如有笔误，敬请谅解。

## 英特尔 IPU E2200：Hot Chips 2025 上的 400G DPU

这是英特尔 IPU E2200 系列的总览幻灯片。该芯片基于台积电（TSMC）的 N5 工艺制造。

[![英特尔 E2200 IPU 在 Hot Chips 2025 上的总览](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_02-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_02/)
> 英特尔 E2200 IPU 在 Hot Chips 2025 大会上的总览

IPU/DPU 的核心目标是卸载和加速通过网络传输的通用基础设施工作负载。举个例子，谷歌就曾使用 E2100 系列作为其 DPU 解决方案。

[![英特尔 E2200 IPU 的基础设施卸载功能](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_03-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_03/)
> 英特尔 E2200 IPU 的基础设施卸载功能

现在我们来深入了解其架构。可以看到，它拥有一个 400G 的 MAC，这非常了不起。计算复合体部分采用了 Arm Neoverse N2 核心。我们还能看到一个 PCIe Gen5 x32 域，并内置了一个 PCIe 交换机。作为对比，英伟达在其 ConnectX-8 上倾向于使用 PCIe Gen6 交换机，而其 BlueField-3 DPU 中的 PCIe Gen5 交换机也是使其 DPU 正常工作的关键特性。

[![英特尔 E2200 IPU 架构图](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_04-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_04/)
> 英特尔 E2200 IPU 架构

在网络子系统中，我们看到了 P4 可编程性、高性能加密等功能。如果你对 NVMe 的部分感到好奇，其设计理念是让这些 DPU 能够通过网络来呈现 NVMe 设备。

[![英特尔 E2200 IPU 网络子系统](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_05-800x454.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_05/)
> 英特尔 E2200 IPU 网络子系统

在计算复合体方面，E2200 最多可搭载 24 个 Arm Neoverse N2 核心，并由四通道 LPDDR5 内存为其提供数据。

[![英特尔 E2200 IPU 的 Arm 计算核心](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_06-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_06/)
> 英特尔 E2200 IPU 的 Arm 计算核心

英特尔表示，该 IPU 支持多主机（multi-host）、无头（headless）和融合（converged）三种模式。无头模式就像我们之前在 [由英伟达 BlueField DPU 驱动的 AIC J2024-04 2U 24盘位 NVMe SSD JBOF](https://www.servethehome.com/aic-j2024-04-2u-24x-nvme-ssd-jbof-powered-by-nvidia-bluefield-dpu/) 一文中展示的那样。在融合模式下，它可以混合运作。这种灵活性非常高。

[![英特尔 E2200 IPU 的平台模式](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_07-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_07/)
> 英特尔 E2200 IPU 支持的平台模式

在数据包处理方面，英特尔详细介绍了其 FXP 数据包处理器，该处理器使用 P4 语言实现可编程性和硬件可配置性。

[![英特尔 E2200 IPU 的 FXP 数据包处理器](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_08-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_08/)
> 英特尔 E2200 IPU 的 FXP 数据包处理器

此外，还有一个内联（inline）加密引擎，可以为每个数据流进行配置。

[![英特尔 E2200 IPU 的加密引擎](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_09-800x454.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_09/)
> 英特尔 E2200 IPU 的加密引擎

英特尔还集成了一个采用时间轮算法（timing wheel algorithm）的流量整形器（traffic shaper）。

[![英特尔 E2200 IPU 的流量整形器](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_10-800x454.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_10/)
> 英特尔 E2200 IPU 的流量整形器

这是关于 RDMA 传输引擎的幻灯片：

[![英特尔 E2200 IPU 的 RDMA 引擎](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_11-800x455.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_11/)
> 英特尔 E2200 IPU 的 RDMA 引擎

一个有趣的细节是，E2200 同时拥有内联加密引擎和旁路（lookaside）加密引擎。幻灯片中没有提到旁路引擎是 P4 可编程的，这揭示了两者之间的一些差异。

[![英特尔 E2200 IPU 的旁路引擎](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_12-800x454.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_12/)
> 英特尔 E2200 IPU 的旁路引擎

E2200 还提供了可编程的卸载选项，用户可以利用不同的加速器和 IP 模块。例如，一些操作可以在网络侧处理，而另一些则可以交由 Arm 核心处理。

[![英特尔 E2200 IPU 的自定义可编程卸载](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_13-800x453.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_13/)
> 英特尔 E2200 IPU 的自定义可编程卸载

英特尔为其 IPU 在数据中心设想了多种用例。

[![英特尔 E2200 IPU 的应用场景](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-E2200-IPU-Hot-Chips-2025_Page_14-800x450.jpg)](https://www.servethehome.com/intel-ipu-e2200-400g-dpu-at-hot-chips-2025/intel-e2200-ipu-hot-chips-2025_page_14/)
> 英特尔 E2200 IPU 的应用场景

当然，最大的挑战在于如何围绕所有这些功能构建应用程序生态。

## 结语

一方面，这款产品非常出色。英伟达在 DPU 领域亟需有力的竞争。凭借其 IPU 已经赢得像谷歌和一些[中国超大规模数据中心](https://www.servethehome.com/this-changes-networking-intel-ipu-hands-on-with-big-spring-canyon/)这样的客户，英特尔在这一领域积累了丰富的经验。希望我们未来能看到更多英特尔 IPU 的身影（并能拿到实验室里来测试！）。至少，随着 E2200 的推出，英特尔将在 400G 吞吐量上与英伟达的 BlueField-3 和 [AMD 的 Pensando Salina 400](https://www.servethehome.com/amd-pensando-salina-400-dpu-arm-neoverse/) DPU 并驾齐驱。

---

### 芯海拾贝：聊聊你的看法

看完了英特尔最新的 IPU E2200，相信你和我一样心潮澎湃。新技术的发布总是能激发我们对未来的无限遐想。在这里，我想邀请大家一起分享观点，碰撞思想的火花：

1.  **三足鼎立，谁主沉浮？** 你如何看待英特尔 IPU、英伟达 BlueField 和 AMD Pensando 在数据中心领域的竞争格局？你认为谁的技术路线或生态策略更具优势？
2.  **IPU vs DPU：名号之争还是实质之别？** 英特尔坚持称其为 IPU，而业界通用 DPU。你觉得这仅仅是市场营销的区别，还是背后有更深层次的技术理念差异？
3.  **400G 开启新纪元？** 随着 400G 网络和强大 Arm 核心成为 DPU 的标配，你认为这将催生哪些新的应用或数据中心架构？AI/ML、云原生、边缘计算等领域会迎来怎样的变革？
4.  **开发者的机遇与挑战：** 文中提到的 P4 可编程性为网络带来了前所未有的灵活性。对于开发者而言，这带来了哪些新的机遇和挑战？你是否接触过 P4 编程？欢迎分享你的经验。

期待在评论区看到你的真知灼见！