
### 译者注

谷歌的 TPU 家族再添猛将——Ironwood。这篇文章揭示了其专为大规模推理设计的核心思路，这标志着谷歌 AI 硬件战略的重大转变：从训练与推理并重，到为实际应用（如 Gemini）的推理场景深度优化。高达 9216 颗芯片、42.5 Exaflops 的算力以及对光路交换（OCS）和 RAS 特性的强调，无不彰显其挑战 AI 算力极限的雄心。尽管 Ironwood 是谷歌云的“独门秘籍”不对外销售，但其设计理念，特别是对能效、扩展性和可靠性的极致追求，无疑为整个行业未来 AI 基础设施的发展方向提供了宝贵的参考。

***

# [谷歌 Ironwood TPU 亮相 Hot Chips 2025：剑指推理模型性能王座](20250902-google-ironwood-tpu-swings-for-reasoning-model-leadership-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月26日
> 原文链接: https://www.servethehome.com/google-ironwood-tpu-swings-for-reasoning-model-leadership-at-hot-chips-2025/

![谷歌 Ironwood TPU 机架](https://www.servethehome.com/wp-content/uploads/2025/08/Ironwood_Rack-696x606.jpg "谷歌 Ironwood TPU 机架")

*谷歌 Ironwood TPU 机架*

在 Hot Chips 2025 大会的机器学习议程压轴出场的是谷歌，他们带来了代号为 Ironwood 的最新一代张量处理单元 (TPU) 的深度解析。几个月前由公司首次披露的 Ironwood，是谷歌首款明确为大规模 AI 推理（而非 AI 训练）而设计的 TPU。通过与强大的模型相结合，Ironwood 旨在赋能大型语言模型 (LLM)、混合专家模型 (MoE) 以及推理模型，使其性能达到新的高度。

单个 Ironwood 节点最多可扩展至 9,216 颗芯片，性能高达 42.5 Exaflops（百亿亿次浮点运算）。这样的性能伴随着高达 10 兆瓦的功耗，代价不菲。总体而言，Ironwood 据称相较于谷歌上一代 TPU（Trillium）提供了两倍的每瓦性能。然而，与谷歌所有的 TPU 一样，Ironwood 仅供谷歌内部作为其谷歌云服务的一部分使用，因此外界无法接触到实体。这也使得在 Hot Chips 大会上的技术分享显得尤为珍贵，因为它提供了许多我们平时难以窥见的技术细节。

![Ironwood TPU 系统的突破性创新](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-2-800x450.jpg)

*Ironwood TPU 系统的突破性创新*

Ironwood TPU 带来了多项创新，而今天的演讲也将聚焦于这些创新，而非仅仅罗列一些常规的性能提升。

其中最重大的突破在于 SuperPod（超级集群）的规模。借助光路交换机 (OCS) 在整个集群中共享内存，如今芯片数量已可扩展至 9,216 颗。这使得总共 1.77 PB 的 HBM 高带宽显存能够被直接寻址。

这一代产品也开始重点关注 RAS (可靠性、可用性和可服务性) 特性，以确保系统的稳定运行。

当然，能效也得到了提升。谷歌宣称实现了 2 倍的每瓦性能改进——尽管目前尚不清楚这是否基于同等数据精度下的比较。

![TPUv4: 4096 颗芯片使用 OCS 共享内存](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-3-800x450.jpg)

*TPUv4: 4096 颗芯片使用 OCS 共享内存*

![9216 颗 Ironwood 芯片使用 OCS 共享内存](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-4-800x450.jpg)

*9216 颗 Ironwood 芯片使用 OCS 共享内存*

将使用光路交换（OCS）技术的 Ironwood 与 TPUv4 进行比较，Ironwood 将集群内的芯片数量翻了一番。OCS 允许将集群配置成不同尺寸的矩形拓扑结构，并且能够动态隔离故障节点，通过从检查点恢复，将计算切片（slice）重新配置到其他机架上。（据透露，这种检查点恢复的操作相当频繁——当然，是指恢复操作，而不是节点故障。）

之所以选择 9216 这个略大于 2 的幂的数字，是为了出于 RAS 的考量预留额外的备用机架。（8192 颗芯片则没有任何冗余。）

![机架通过光路交换机 (OCS) 连接](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-5-800x450.jpg)

*机架通过光路交换机 (OCS) 连接*

这张图进一步展示了 OCS，以及它如何将节点组织成一个三维逻辑阵列。

![1.77 PB 可直接寻址的共享 HBM 内存](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-6-800x450.jpg)

*1.77 PB 可直接寻址的共享 HBM 内存*

凭借 1.77 PB 的 HBM 内存，谷歌刷新了共享内存容量的新纪录。

![基于 FP8 精度的 42.5 Exaflops 机器学习算力](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-7-800x450.jpg)

*基于 FP8 精度的 42.5 Exaflops 机器学习算力*

同时，让我们看看在 FP8 精度下的计算性能。Ironwood 在这方面实现了巨大的飞跃。

![业界领先的计算能效](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-9-800x450.jpg)

*业界领先的计算能效*

相较于 TPUv4，其每瓦性能提升了近 6 倍。

![强调 RAS (可靠性、可用性和可服务性)](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-8-800x450.jpg)

*强调 RAS (可靠性、可用性和可服务性)*

再次强调，谷歌在这一代产品中对 RAS 给予了高度重视。云 TPU 实例需要能够长时间（而且是越来越长的时间）无差错地运行。

![第三代液冷基础设施](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-10-800x450.jpg)

*第三代液冷基础设施*

Ironwood 也配备了谷歌的第三代液冷技术。谷歌采用多重循环系统来确保进入冷板的水质极其洁净，以防堵塞冷板。

![第四代 SparseCore：加速嵌入和集合通信](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-11-800x450.jpg)

*第四代 SparseCore：加速嵌入和集合通信*

Ironwood 还提供了谷歌最新一代的 SparseCore 功能。

![大规模预训练与兆瓦级负载波动](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-12-800x457.jpg)

*大规模预训练与兆瓦级负载波动*

除了能效，电源稳定性也是一个关注焦点。谷歌通过软硬件协同，平滑了功耗的剧烈波动，以减轻对电力设施的压力。

一段简短的视频也证实了其超大规模部署正在进行中。

![Ironwood 芯片](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-14-800x450.jpg)

*Ironwood 芯片*

现在，让我们更深入地探讨 Ironwood 的架构。

谷歌更新了其 SoC (片上系统) 架构，使其能够超越单个晶片的限制，不再受光刻掩模版尺寸的束缚。因此，Ironwood 是其首款采用多计算芯粒（chiplet）设计的芯片，每个封装上集成了两个 Ironwood 计算晶片。

为了更好地满足大型语言模型对内存的需求，谷歌重新聚焦于内存子系统，采用了 8 堆栈的 HBM3e 内存，实现了 192GB 内存容量和 7.3TB/s 的带宽。

尽管如此，Ironwood 的亮点远不止于速度和参数。它集成了更多旨在提升可靠性和安全性的功能，例如集成的信任根（root of trust）、内置自检（BIST）以及用于捕捉静默数据损坏（silent data corruption）的功能。甚至还有在工作负载运行时检查算术运算的功能。

“我们在芯片中加入了大量功能，旨在使其成为能效最高的芯片。”

AI 技术如今也已应用于 AI 芯片的设计，形成了一个完整的闭环。AI 被用来设计 ALU 电路和优化芯片的布局规划（floor plan）。在这个项目中，谷歌与 AlphaChip 团队进行了合作。

![Ironwood 架构，主机平面](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-20-800x450.jpg)

*Ironwood 架构，主机平面*

这是一张 Ironwood 的逻辑框图，概述了 TPU 架构的各项主要升级和增强。HBM3e 在此扮演了至关重要的角色，同样重要的还有使其能够扩展至 9216 颗芯片组成一个 SuperPod 的互连硬件。同时，它还可以横向扩展（scale-out）至数十个 SuperPod。

![机密计算支持](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-21-800x450.jpg)

*机密计算支持*

该图列出了为支持 Ironwood 上的机密计算而增加的各项功能，包括集成的信任根、安全启动以及安全的测试/调试功能。

![Ironwood 托盘](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-22-800x450.jpg)

*Ironwood 托盘*

从单个芯片往上一层，这是一个 Ironwood 托盘。每个托盘包含 4 个 Ironwood TPU，并采用液冷散热。

![机架](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-23-800x450.jpg)

*机架*

再往上一层，16 个 TPU 托盘组成一个机架，即每个机架 64 个 TPU。与之配套的还有 16 个 CPU 主机机架。机架内的所有互连都使用铜缆；OCS 则负责提供与其他机架的连接。

![最佳机器学习性能：从芯片到数据中心](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-25-800x450.jpg)

*最佳机器学习性能：从芯片到数据中心*

再次强调，能效在这里至关重要。功耗是限制整体性能的瓶颈。实现高能效不仅意味着制造出色的硬件，还需要将其与数据中心级别的功耗感知和控制相结合，以协调硬件运作，确保整个数据中心都以尽可能高的效率运行。

![Ironwood 延续我们在纵向与横向扩展上的领先地位](https://www.servethehome.com/wp-content/uploads/2025/08/61_Google_Ironwood-Final-26-800x450.jpg)

*Ironwood 延续我们在纵向与横向扩展上的领先地位*

以上就是对 Ironwood 的概述。谷歌不仅在性能和能效上实现了巨大提升，更将重点放在了 RAS 特性上，旨在提供构建大规模 SuperPod 所需的可靠性。

## 结语

这是一场非常精彩的演讲。谷歌在很多年前就预见到了创建高端 AI 计算能力的需求。如今，这家公司正在从芯片、互连到物理基础设施的每一个层面进行创新。即使作为 Hot Chips 2025 的最后一场演讲，谷歌所展示的内容依然让全场观众为之瞩目，紧紧地将目光锁定在舞台上。

---

## 芯海回响，邀您共论

这篇文章为我们揭开了谷歌最新 AI 硬件的神秘面纱，其惊人的规模和性能参数背后，是无数工程技术的结晶。看完之后，你是否也有些想法不吐不快？

1.  **“自研自用” vs “开放市场”**：谷歌坚持 TPU 仅供内部云服务使用，而英伟达则通过向全球销售 GPU 建立了一个庞大的生态。你认为这两种商业策略，哪一种更能引领 AI 时代的未来？为什么？
2.  **功耗的“天花板”**：一个 Ironwood 集群的功耗就高达 10 兆瓦，相当于一个小镇的用电量。你认为功耗和散热问题会成为未来 AI 算力发展的最大瓶颈吗？我们还能从哪些方面寻求突破？
3.  **互联技术的革新**：文章中提到的光路交换（OCS）和芯粒（Chiplet）技术是实现超大规模集群的关键。你如何看待这些技术在未来数据中心和超级计算机中的应用前景？
4.  **AI 设计 AI**：谷歌利用 AI 来辅助设计 Ironwood 芯片，这是否预示着一个新时代的到来——AI 将成为芯片设计乃至更多科研领域的核心驱动力？

欢迎在评论区留下你的真知灼见，让我们一起探讨 AI 硬件的星辰大海！