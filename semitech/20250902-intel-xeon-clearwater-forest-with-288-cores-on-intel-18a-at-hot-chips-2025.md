
### 译者注

> 随着数据中心对能效和计算密度的要求日益严苛，CPU 市场的“核战”已从单纯的数量比拼，转向了对能效核心（E-core）架构的深度挖掘。英特尔此次发布的 Clearwater Forest 无疑是这场战役中的一枚重磅炸弹。它不仅将核心数推向惊人的 288 核，更关键的是，它首次采用了英特尔寄予厚望的 18A 工艺和背面供电技术。这不仅是对 AMD EPYC 和 ARM 阵营（如 Ampere）高密度计算方案的强力回应，更是英特尔展示其“五年四代工艺”路线图决心、重夺半导体制程领导地位的关键一步。

---

# [Hot Chips 2025：英特尔发布至强 Clearwater Forest，采用 Intel 18A 工艺，集成 288 核心](20250902-intel-xeon-clearwater-forest-with-288-cores-on-intel-18a-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月25日
> 原文链接：https://www.servethehome.com/intel-xeon-clearwater-forest-with-288-cores-on-intel-18a-at-hot-chips-2025/

![Intel Xeon Clearwater Forest](https://www.servethehome.com/wp-content/uploads/2024/09/Intel-Xeon-Clearwater-Forest-696x523.jpg)

*英特尔至强 Clearwater Forest*

在 Hot Chips 2025 大会上，英特尔详细介绍了其下一代拥有 288 个核心的处理器。这款处理器基于 Intel 18A 工艺和 3D 封装技术打造，相较于上一代 Sierra Forest 实现了巨大飞跃，拥有更大的缓存、更快的能效核（E-cores）以及更高的内存带宽。

请注意，本文为现场实时报道，如有笔误，敬请谅解。

## Hot Chips 2025：英特尔至强 Clearwater Forest，288 核与 Intel 18A 工艺的强强联合

作为英特尔 *_Forest_* 系列芯片的第二款产品，Clearwater Forest 继承了 Sierra Forest 的设计理念，专注于多核心设计。与依赖传统性能核（P-cores）的思路不同，Forest 系列芯片完全由尺寸更小的能效核构成。这使得它们特别适用于那些需要以高能效方式运行大量并发线程的工作负载——这些负载不一定追求极致的单线程性能。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Intel Xeon 6 Range](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Intel-Xeon-6-Range-800x445.jpg)

*Clearwater Forest 采用 Intel 18A 工艺，拥有 288 核心，隶属英特尔至强 6 系列*

Clearwater Forest 已经在英特尔的实验室中运行了数月，并将很快投入生产。它是首批采用 Intel 18A 工艺的芯片之一，因此在多个层面上对公司都至关重要。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Overview 1](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Overview-1-800x445.jpg)

*Clearwater Forest 概览 1*

Clearwater Forest 将与英特尔当前的至强 6 系列芯片（Granite Rapids 和 Sierra Forest）使用相同的平台。

能效是 Clearwater 的核心优势。在这次演讲中，英特尔不厌其烦地强调这一点。18A 工艺带来了能效的巨大提升，同时核心架构也得到了改进。

另一项重大变革是采用了 Foveros Direct 3D 技术，实现了 3D 晶片堆叠。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 18A Process](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-18A-Process-800x445.jpg)

*Clearwater Forest 采用的 18A 工艺*

18A 工艺带来了多项创新。英特尔特别强调了背面金属层/背面供电网络（BSPDN），它将供电网络从晶体管上方移至其后方。（这一点对英特尔尤为重要，因为这是他们遥遥领先于台积电的一项技术。）

BSPDN 同时还提升了单元密度，英特尔报告称其单元利用率已超过 90%。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 E Cores Overview](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-E-Cores-Overview-800x445.jpg)

*Clearwater Forest 能效核（E-Cores）概览*

至于架构本身，英特尔表示，架构改进对 Clearwater Forest 能效提升的贡献不容小觑。这主要得益于以下 4 个方面的因素：

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 E Cores Front End](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-E-Cores-Front-End-800x445.jpg)

*Clearwater Forest 能效核前端设计*

与 Sierra Forest 相比，Clearwater 的解码宽度从 6-wide 提升到了 9-wide，这是通过三个 3-wide 解码器实现的。分支预测器也得到了改进，既是为了跟上更宽前端的步伐，也是为了全面提高预测准确性。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Out Of Order Engine](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Out-of-Order-Engine-800x445.jpg)

*Clearwater Forest 乱序执行引擎*

在后端，乱序执行引擎的每时钟周期可分派的操作数从 5 个增加到了 8 个。总计来看，每个时钟周期可以退役 16 个操作，是 Sierra 的两倍。

执行端口的数量也大幅增加，使 Clearwater 的执行端口达到了 26 个——尽管它只是一个小型能效核！

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Execution Engine](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Execution-Engine-800x445.jpg)

*Clearwater Forest 执行引擎*

整数和矢量执行吞吐量翻了一番，存储地址生成能力同样翻倍。唯一没有翻倍的是加载地址生成能力，但也达到了 Sierra 的 1.5 倍。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Core Memory Subsystem Page 10](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-_Page_10-800x445.jpg)

*Clearwater Forest 核心内存子系统*

在内存接口方面，L2 未命中缓冲区（miss buffer）的大小增加了一倍，可以存储 128 个未命中条目。这与 Clearwater Forest 的整体内存带宽直接相关，英特尔必须按比例扩展它以匹配新增的带宽。

此外，虽然只是一个脚注，但该核心还支持多项 RAS（可靠性、可用性和可服务性）特性。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Core Memory Subsystem](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Core-Memory-Subsystem-800x445.jpg)

*Clearwater Forest 模块架构*

从更高层面来看，一个 Clearwater Forest 模块由 4 个核心组成，共享一个 4MB 的统一 L2 缓存，这与 Sierra 的设计相同。不过，L2 缓存带宽翻了一番，达到了 400GB/s。

性能方面，英特尔声称在 SPECint 2017 测试中实现了 17% 的 IPC（每时钟周期指令数）提升。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 3D Construction](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Module-Architecture-800x445.jpg)

*Clearwater Forest 3D 结构*

与 Sierra 的 2.5D 设计不同，Clearwater Forest 是一种 3D 设计，CPU 小晶片（chiplet）堆叠在包含其余非核心（uncore）硬件的更大基础晶片之上。

根据规格进行一些计算，1152MB 的 LLC（末级缓存）意味着每个插槽拥有 576MB 的末级缓存。而在 288 核的 Sierra Forest 中，每个 144 核的 tile 只有 108MB，总共也才 216MB。同时，新平台共有 576 个核心，即每插槽 288 核。

基础晶片（base die）基于 Intel 3 工艺制造，而 I/O 晶片则复用了 Sierra Forest 的设计，该晶片基于 Intel 7 工艺。

英特尔还继续使用 EMIB（嵌入式多芯片互连桥接）技术进行晶片间的互连。

整个封装包含：12 个 CPU 小晶片，3 个基础晶片，2 个 I/O 晶片。

![Intel Clearwater Forest 288 Core Intel 18A Hot Chips 2025 Platform](https://www.servethehome.com/wp-content/uploads/2025/08/Intel-Clearwater-Forest-288-Core-Intel-18A-Hot-Chips-2025-Platform-800x445.jpg)

*Clearwater Forest 平台*

在一个双插槽系统中，每个芯片拥有 12 个 DDR5-8000 内存通道（标准模式，非 MRDIMM）。这使得总内存带宽达到了 1300GB/s（显然这是 100% 读取时的实际能力）。

![Rack Analysis](https://www.servethehome.com/wp-content/uploads/2025/08/IntelCWFRack-800x448.jpg)

*机架分析*

从整个机架的视角来看，由于数据中心受到功率限制，通过整合来降低功耗——从而降低总拥有成本（TCO）——变得至关重要。总而言之，与 Sierra 相比，英特尔声称 Clearwater Forest 机架的每瓦性能将提升 3.5 倍。

---

### 极客茶话会

英特尔的 Clearwater Forest 无疑为数据中心的未来描绘了一幅激动人心的蓝图。288 个能效核、尖端的 18A 工艺和 3D 封装技术，这些听起来就像是科幻小说里的配置。那么，让我们来聊聊这些技术突破背后的真正含义吧！

1.  **核心大战的新篇章：** 你认为英特尔这种“人海战术”般的能效核（E-core）堆叠策略，在面对 AMD EPYC 的传统多核设计和 ARM 阵营（如 Ampere）的能效优势时，胜算几何？它会改变云服务商的采购天平吗？
2.  **18A 工艺的王者归来？** 背面供电（BSPDN）技术听起来非常酷，被英特尔视为反超台积电的“杀手锏”。你觉得这足以让英特尔重回半导体制程的王座吗？
3.  **谁最需要 288 核？** 如此多的核心，究竟什么样的应用场景才能将其性能发挥到极致？是云原生应用、大规模微服务、Web 服务器，还是 AI 推理、数据分析等新兴工作负载？
4.  **“旧瓶装新酒”的智慧：** Clearwater Forest 兼容现有的至强 6 平台，并复用了 I/O 晶片。你认为这种对平台兼容性和成本控制的考量，对于数据中心客户的决策有多大影响？