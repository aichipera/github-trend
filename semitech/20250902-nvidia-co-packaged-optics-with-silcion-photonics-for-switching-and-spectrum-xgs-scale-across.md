
### 译者注

随着 AI 模型和算力需求的爆炸式增长，数据中心内部的通信带宽和功耗已成为关键瓶颈。NVIDIA 在 Hot Chips 2025 上展示的共封装光学（CPO）技术，正是为了解决这一难题。它通过将硅光子引擎与交换芯片封装在一起，极大地缩短了电信号传输距离，从而显著降低延迟和功耗，同时大幅提升带宽密度。这不仅是网络硬件的一次进化，更是支撑未来“万亿参数”级别模型训练、构建“数据中心即计算机”愿景的关键一步，标志着 AI 基础设施正在进入光电融合的新纪元。

***

# [NVIDIA 发布集成硅光子的共封装光学交换芯片，助力 Spectrum-XGS 实现跨域扩展](20250902-nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across.mp3)

> 作者：[Patrick Kennedy](https://www.servethehome.com/author/patrick/) - 2025年8月26日
> 原文链接：https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/

[![NVIDIA 在 Hot Chips 2025 上展示集成硅光子的共封装光学技术](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_14-696x392.jpg "NVIDIA 在 Hot Chips 2025 上展示集成硅光子的共封装光学技术")](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_14.jpg)

这是 Hot Chips 2025 上一个激动人心的议题。我们聆听了 Gilad 关于用于吉瓦（gigawatt）级交换机的共封装硅光子交换芯片的演讲。有趣的是，在这次会议上，我第一次在 Hot Chips 的舞台上被点名了。

*本文为现场实时报道，如有笔误，敬请谅解。*

NVIDIA 认为，**数据中心即计算机**，而不仅仅是单个 GPU 的集合。

[![NVIDIA 在 Hot Chips 2025 展示数据中心即计算单元](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon- Photonics-at-Hot-Chips-2025-_Page_02-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_02/)

BlueField-3 DPU 被设计为接入网络的 NIC（网络接口卡）。

[![NVIDIA BlueField-3 DPU 正面图](https://www.servethehome.com/wp-content/uploads/2024/09/NVIDIA-BlueField-3-DPU-Front-800x537.jpg)](https://www.servethehome.com/?attachment_id=80862)

AI 应用需要**零抖动**的通信，因为它们规模庞大、结构复杂，并且跨越很长的物理距离。

[![NVIDIA 在 Hot Chips 2025 上强调零抖动的重要性](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_03-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_03/)

目前存在多种不同的以太网架构。虽然它们都属于以太网，但各自有不同的需求和目标。

[![NVIDIA 在 Hot Chips 2025 上展示不同的 AI 网络架构](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_04-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_04/)

NVIDIA Spectrum-X 以太网旨在让大型 GPU 集群能够使用以太网进行高效通信。

[![NVIDIA 在 Hot Chips 2025 上介绍 Spectrum-X](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_05-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_05/)

Spectrum-X 专为 AI 工作负载提供低抖动通信。在 AI 网络中，抖动会导致大量 GPU 处于空闲等待状态。这不仅效率低下，而且让昂贵的 GPU 闲置会造成巨大的成本浪费。NVIDIA 正在设计这种端到端的解决方案，以确保所有功能不仅仅局限于交换机本身。

[![NVIDIA 在 Hot Chips 2025 上讲解低抖动的重要性](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_06-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_06/)

Spectrum-X 提供了更高的 NCCL 性能。NVIDIA 希望确保，当多个任务在大型基础设施上同时运行时，它们不会相互干扰。例如，当一台交换机上先有一个任务，后续加入其他任务时，你不希望新任务影响原有任务的性能。

[![NVIDIA 在 Hot Chips 2025 上展示 NCCL 性能](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_07-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_07/)

这张图是今年的新内容，展示了在混合专家模型（MoE）中，Spectrum-X 比标准以太网具有更好的调度性能。

[![NVIDIA 在 Hot Chips 2025 上展示专家调度性能](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_08-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_08/)

这是 Spectrum-X 对多租户数据中心训练任务的影响。

[![NVIDIA 在 Hot Chips 2025 上展示多租户数据中心训练](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_09-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_09/)

这张总结幻灯片展示了 Spectrum-X 以太网与市面上现成的（可能是博通的）以太网有何不同。

[![NVIDIA 在 Hot Chips 2025 上总结 Spectrum-X 的优势](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_10-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_10/)

横向扩展（Scale-out）也成为一个挑战，因为光网络元件可能会消耗大量电力。

[![NVIDIA 在 Hot Chips 2025 上讨论横向扩展的挑战](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_11-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_11/)

这是下一代 Spectrum-X 以太网光子技术。它不再需要耗费电力去驱动一个可插拔光模块，从而节省了大量功耗。

[![NVIDIA 在 Hot Chips 2025 上介绍光子技术](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_12-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_12/)

NVIDIA Photonics 是一款 1.6T 的 CPO（共封装光学）芯片，采用了新型微环调制器。NVIDIA 还专注于可拆卸的光纤连接器。你可能会在照片中看到，Spectrum-X 和 Quantum-X 的 CPO 连接方式有所不同，这是该解决方案不断演进的结果。

[![NVIDIA 在 Hot Chips 2025 上展示 NVIDIA Photonics 技术细节](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_13-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_13/)

有许多组件协同工作才使这一切成为可能。值得注意的是，该设计中包含一个可插拔的激光器。

[![NVIDIA 在 Hot Chips 2025 上展示 CPO 的组件](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_14-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_14/)

NVIDIA 展示了该技术已在其站点上实际运行。

[![NVIDIA 在 Hot Chips 2025 上展示实验室成果](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_15-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_15/)

NVIDIA 推出了一款 102T 交换机——集成了硅光子技术的 Spectrum-6 102T 交换机。

[![NVIDIA 在 Hot Chips 2025 上发布 102T 交换机](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_16-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_16/)

通过这种设计，可靠性得到提升，而功耗则随之下降。

[![NVIDIA 在 Hot Chips 2025 上展示功耗与可靠性优势](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_17-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_17/)

NVIDIA 即将推出同时采用 CPO 技术的 Quantum-X 和 Spectrum-X 交换机。另外，我计划在未来深入研究这些产品。

[![NVIDIA 在 Hot Chips 2025 上展示未来的 CPO 交换机](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_18-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_18/)

从**纵向扩展（Scale-up）**、**横向扩展（Scale-out）**，到如今的**跨域扩展（Scale-across）**。当扩展范围超出单个数据中心站点时，你仍然需要一个高质量的网络，并且需要极高的速度。

[![NVIDIA 在 Hot Chips 2025 上提出跨域扩展概念](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_19-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_19/)

Spectrum-XGS 是该公司将横向扩展网络升级为跨域扩展的方法。这不仅意味着硬件的升级，还包括能感知距离的算法。

[![NVIDIA 在 Hot Chips 2025 上介绍 Spectrum-XGS](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_20-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_20/)

NVIDIA 表示，使用该技术可以获得 1.9 倍的横向扩展性能提升，并且还有进一步优化的空间。

[![NVIDIA 在 Hot Chips 2025 上展示性能提升数据](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_21-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_21/)

这是一个在跨域扩展网络上运行的训练任务示例。

[![NVIDIA 在 Hot Chips 2025 上对比 Spectrum-XGS 与可能是博通的多站点方案](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_22-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_22/)

其目标是实现多站点 AI 训练，使训练任务不再受单个站点的电力和资源限制。

[![NVIDIA 在 Hot Chips 2025 上展望 Giga-Scale AI](https://www.servethehome.com/wp-content/uploads/2025/08/NVIDIA-Co-Packaged-Optics-with-Silicon-Photonics-at-Hot-Chips-2025-_Page_23-800x450.jpg)](https://www.servethehome.com/nvidia-co-packaged-optics-with-silcion-photonics-for-switching-and-spectrum-xgs-scale-across/nvidia-co-packaged-optics-with-silicon-photonics-at-hot-chips-2025-_page_23/)

CoreWeave 很有可能成为首个部署该技术的客户。

## 结语

跨域扩展网络大约从 500 米的距离开始发挥作用。超过这个距离后，就需要对算法进行调整以适应长距离传输。我迫不及待地想看到这些技术成为真正的产品。

---

## 交流与展望

看完了 NVIDIA 最新的“黑科技”，你有什么想法？欢迎在下方分享你的观点！

1.  **CPO（共封装光学）技术**将如何改变未来数据中心的设计、功耗和散热格局？对于运维来说，将光模块直接封装在芯片旁是福是祸？
2.  随着 Spectrum-X 平台集成 CPO 和硅光子技术，你认为**以太网**能否在超大规模 AI 训练集群中，真正挑战 **InfiniBand** 的主导地位？
3.  从可插拔到共封装，你认为这项技术普及面临的最大挑战是什么？是**制造成本、良率**，还是**可维护性**？
4.  NVIDIA 提出的**“跨域扩展”（Scale-across）**概念，让跨数据中心的AI训练成为可能。这对于大模型的未来发展，乃至整个**云计算的版图**意味着什么？