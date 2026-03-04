
### 译者注

这篇文章虽然设定在未来的2025年，但其描述的 Blackwell 架构、神经网络渲染、FP4 计算和 GDDR7 显存等技术趋势，与我们当前（2024年）观察到的行业方向高度吻合。英伟达正全力将 AI 计算融入图形渲染管线的每个角落，从“大力出奇迹”的传统光栅化，转向更智能、更高效的 AI 驱动生成。这不仅是游戏画质的革命，更预示着消费级 GPU 将成为更强大的个人 AI 计算平台，值得我们持续关注。

***

# [NVIDIA GeForce RTX 5090 与神经网络渲染时代：Hot Chips 2025 深度解析](20250902-nvidia-geforce-rtx-5090-and-the-age-of-neural-rendering-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月25日
> 原文链接：https://www.servethehome.com/nvidia-geforce-rtx-5090-and-the-age-of-neural-rendering-at-hot-chips-2025/

![RTX 5090 与神经网络渲染，Hot Chips 大会](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-1-696x392.jpg)

*RTX 5090 与神经网络渲染，Hot Chips 大会*

今天图形技术分会的第二场演讲来自英伟达。与 AMD 类似，英伟达的当前一代图形产品也处于产品周期的中段——其首批产品已于 2024 年末发布。因此，他们在 Hot Chips 大会上的演讲更像是一次回顾，重点介绍了 Blackwell 架构为图形领域——特别是为基于机器学习的神经网络渲染领域——所带来的新特性。

![Blackwell 架构的可扩展性](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-3-800x450.jpg)

*Blackwell 架构的可扩展性*

英伟达设计的 Blackwell 架构旨在实现从数据中心到移动设备的全方位扩展。从某些方面来说，AI 的本质是相通的——无论是为 ChatGPT 生成 token，还是为光线追踪执行神经降噪。因此，英伟达能够根据专业级和消费级 GPU 的需求，灵活地扩展或缩减其架构。在 Blackwell 架构上，英伟达正大力押注 FP4 机器学习计算，以期最大化性能表现。

![神经网络渲染](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-5-800x451.jpg)

*神经网络渲染*

本次演讲的核心焦点是：**神经网络渲染**。即利用机器学习技术来辅助生成图像帧。英伟达希望借此跨越“恐怖谷”——如果沿用传统的光栅化技术，要完成这项任务将需要天文数字般的额外算力。但机器学习技术或许能让我们更快地达成目标。

英伟达在这里展现了一种“手握铁锤，看什么都像钉子”的思维。即便在图灵（Turing）架构发布7年后的今天，他们仍在努力向大众推销机器学习的各种潜能。因此，这不仅关乎图形渲染，还涉及到如何利用这种扩展能力来节省笔记本电脑的功耗，以及如何在游戏内部署机器学习驱动的智能体（AI agents）。

![为神经网络渲染而生的 Blackwell](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-7-800x450.jpg)

*为神经网络渲染而生的 Blackwell*

相应地，Blackwell 架构也带来了多项改进以提升机器学习性能，同时全面优化能效，力求确保每个 SM（流式多处理器）在每个时钟周期都有有效的工作可做，无论是处理图形任务还是各种机器学习模型。为此，它甚至配备了一个专用的 AI 管理处理器，以帮助保持数据流畅通并让 SM 核心时刻保持满载。

尽管如此，这里展示的原始算力依然惊人：高达 360 TFLOPs 的光线追踪（RT）性能、GDDR7 显存，以及海量的 Tensor Core 浮点运算能力。

![Blackwell SM 架构](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-8-800x450.jpg)

*Blackwell SM 架构*

![着色器执行重排序（Shader Execution Reordering）](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-9-800x450.jpg)

*着色器执行重排序*

英伟达大量运用了“着色器执行重排序”（Shader Execution Reordering）技术来帮助 SM 保持高负载。通过对工作负载进行重新排序，可以避免流水线中出现“气泡”（bubbles），从而维持高效运转。这项技术是软件和硬件协同作用的成果。据称，仅为了完成这种排序工作，就需要进行大量的整数数学运算，这也是为什么整数性能在 Blackwell 这一代架构中对英伟达至关重要的原因。

![FP4 数据格式](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-11-800x450.jpg)

*FP4 数据格式*

英伟达正在全力推进 FP4 格式的应用。他们期望该格式在图形模型中仍能提供必要的精度，同时将显存占用和计算资源消耗减半。附带一提：与 INT4 相比，FP4 具有更宽的动态范围，这可能带来一些额外的好处。

![GDDR7 显存](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-12-800x450.jpg)

*GDDR7 显存*

Blackwell 架构加入了对 GDDR7 的支持，这使得总显存带宽实现了显著跃升。与 GDDR6X 使用的 PAM4 信号调制技术相比，GDDR7 的 PAM3 技术虽然每个时钟周期传输的比特数更少，但其更高的信噪比（SNR）允许实现更高的时钟频率，足以弥补并超越这一差异。此外，它还支持更低的工作电压。

![同时处理 AI 与图形任务](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-13-800x450.jpg)

*同时处理 AI 与图形任务*

英伟达希望缩短“首个令牌生成时间”（Time to first token），尤其是在图形与机器学习混合的工作负载中。这基本上是在为使机器学习模型/AI智能体在交互式游戏中更具实用性铺平道路。

![Blackwell AI 管理处理器](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-14-800x450.jpg)

*Blackwell AI 管理处理器*

AI 管理处理器在其中扮演了关键角色，它负责协调工作，将图形和机器学习任务交错执行，从而避免因昂贵的上下文切换（context switches）而导致 GPU 停滞。

![AI 工作负载流式处理](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-15-800x450.jpg)

*AI 工作负载流式处理*

调度需求是复杂的，特别是当不同工作负载具有不同的延迟要求时。例如，机器学习智能体的最后期限（deadline）不像实时图形渲染那样严苛。这些都是 AI 管理处理器需要考虑的因素。

![“争先至空闲”（Race to Idle）策略](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-16-800x450.jpg)

*“争先至空闲”（Race to Idle）策略*

帧生成技术：跳过耗费大量功耗来渲染某一帧的过程，取而代之的是用一个插值帧来替代，而功耗成本仅为前者的零头。这种方式最多可将功耗降低 2 倍。

![通用 MIG（多实例 GPU）](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-17-800x450.jpg)

*通用 MIG（多实例 GPU）*

消费级的 Blackwell 架构 GPU 也开始支持通用 MIG（Multi-instance GPU），这项功能以前是数据中心 GPU 独有的。它通过为每个客户端（例如云游戏服务）分配一组不同的 SM，改进了将单个 GPU 分割给多个用户的使用方式。

![MIG 的性能扩展](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-18-800x450.jpg)

*MIG 的性能扩展*

与简单的“时间切片”（time slicing）方法相比，英伟达发现 MIG 技术能带来高达 60% 的性能提升。性能增益的原因在于，单个 1080p 的客户端工作负载太小，不足以完全占满一块完整的 RTX Pro 6000 专业卡；而通过将其分割成更小的虚拟GPU（vGPU），并并行执行多个工作负载，可以使 GPU 始终保持在饱和的工作状态。

![结论](https://www.servethehome.com/wp-content/uploads/2025/08/nvidia_hc2025-19-800x450.jpg)

*结论*

---

### Geek 观点碰撞

看完了英伟达对未来的构想，你是否也心潮澎湃？我们为你准备了几个话题，期待听到你的真知灼见：

1.  **AI 渲染的未来**：你认为“神经网络渲染”会彻底改变我们玩游戏和创作内容的方式吗？它会是下一个“光线追踪”级别的技术飞跃，还是仅仅是锦上添花？
2.  **精度 vs. 性能**：文章中提到的 FP4 计算格式，用一半的资源换取性能，你觉得这种“精度换速度”的策略在未来游戏和应用中是否可行？会担心画质细节的损失吗？
3.  **消费级 GPU 的新玩法**：MIG 这样的数据中心技术“下放”到消费级显卡，你觉得除了云游戏，它还能为我们的个人电脑带来哪些前所未有的应用场景？（比如一边玩游戏，一边让 AI 助手处理复杂任务？）
4.  **畅想 RTX 5090**：结合文中的技术爆料，你对未来的旗舰显卡 RTX 5090 有什么样的性能、价格和功能期待？它会成为你下一块升级的显卡吗？

欢迎在评论区留下你的想法，让我们一起探讨图形技术的未来！