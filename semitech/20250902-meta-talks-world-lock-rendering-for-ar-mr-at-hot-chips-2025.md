
### 译者注

世界锁定渲染（World-Lock Rendering）是实现沉浸式 AR/MR 体验的核心技术，其目标是让虚拟物体“钉”在真实世界中，无论用户如何移动，都能保持位置稳定。这背后最大的挑战是在眼镜这种微小设备上，以极低延迟和极低功耗完成复杂的计算。Meta 在 Hot Chips 大会上展示的 Orion 原型方案，通过专用芯片（ASIC）和分体式计算（眼镜端+外部计算单元）来攻克这一难题，这代表了行业的一个重要趋势：为特定任务设计专用硬件，以突破通用处理器的能效瓶颈，是通向消费级 AR 眼镜的必经之路。

***

# [Meta 在 Hot Chips 2025 大会探讨用于 AR/MR 的世界锁定渲染技术](20250902-meta-talks-world-lock-rendering-for-ar-mr-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月25日
> 原文链接：https://www.servethehome.com/meta-talks-world-lock-rendering-for-ar-mr-at-hot-chips-2025/

![Meta 在 Hot Chips 2025 大会介绍世界锁定渲染技术](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-3-696x392.jpg "Meta 在 Hot Chips 2025 大会介绍世界锁定渲染技术")

*Meta 在 Hot Chips 2025 大会介绍世界锁定渲染技术*

今天最后一场与图形技术相关的演讲来自 Meta，他们带来的或许是本次图形技术分会场中最新颖的分享。Meta 旗下（前 Oculus）的头显部门并没有讨论那些已经上市数月的 GPU 架构，而是在本届大会上探讨如何使用专用集成电路（IC）来加速**世界锁定渲染（World-Locked Rendering, WRL）**。WRL 技术对 Meta 公司发展 AR/VR 眼镜至关重要，特别是其原型机 **Orion 眼镜**，该项目正在不断挑战如何在小巧的眼镜形态下，突破空间和功耗预算的极限。

![Orion 原型眼镜](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-2-800x450.jpg)

*Orion 原型眼镜*

简而言之，**世界锁定渲染**是一种确保当用户头部移动时，渲染出的图像能够始终锁定在真实世界某个点的技术。正是它，让一个虚拟图像能够稳定地悬浮在你面前，其位置参照物是你周围的真实世界。这项技术同样也涵盖了遮挡关系的处理，即真实世界的物体可以遮挡虚拟物体。

![WRL 体验](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-5-800x450.jpg)

*WRL 体验*

![WRL 原理](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-6-800x450.jpg)

*WRL 原理*

我们来回顾一下 WRL 的几个核心原则：锚定对象、深度计算、真实世界与渲染世界的实际合成，甚至还包括空间音频渲染。这些原则不仅涵盖了渲染的各个步骤，更关键的是，所有这些步骤都必须在极低的延迟下完成，同时还要尽可能地降低功耗。

![WRL 框图](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-7-800x450.jpg)

*WRL 框图*

上图是 WRL 基础算法的框图。数据从惯性测量单元和其他传感器输入，经过多个计算阶段，最终进行合成与投影。

![芯片设计的挑战](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-9-800x450.jpg)

*芯片设计的挑战*

AR 眼镜的物理形态限制意味着 WRL 的功耗预算极其有限。为此，Meta 运用了所有业界顶尖技术，从尖端的工艺节点（在 Orion 项目构思时是 5nm 工艺）、有限的 DRAM 使用、数据压缩技术，到广泛的电源管理策略。即便如此，物理尺寸本身也是一个严峻的挑战，因为眼镜上并没有太多空间来放置芯片。

![Orion 的芯片方案](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-10-800x450.jpg)

*Orion 的芯片方案*

因此，Orion 项目将计算任务拆分到了**眼镜本身**和**一个外部计算单元（Puck）**上。WRL 对延迟极其敏感，所以这部分处理必须在眼镜端实时进行。整体架构包含三颗主要的处理器芯片：**显示处理器**、**眼镜处理器**，以及位于外部计算单元中的**计算协处理器**。

![架构考量](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-11-800x450.jpg)

*架构考量*

WRL 是一种非常特殊的工作负载，因为它需要**持续不断地运行**。这意味着它不像大多数传统计算任务那样可以有突发性的高峰负载。因此，在某些方面，它对硬件的需求也截然不同。

![眼镜处理器](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-13-800x450.jpg)

*眼镜处理器*

**眼镜处理器**负责处理所有的眼动追踪、手势追踪以及摄像头输入。它是一个完整的系统级封装（SiP）芯片，将一颗 SoC、LPDDR4X 内存和 NVMe 闪存都集成在同一个封装中。该芯片共包含 24 亿个晶体管，基于 5nm 工艺制造。Meta 甚至在芯片中内置了安全信任根（Secure Root of Trust），以确保所有进出芯片的数据都经过加密。

从外部计算单元传输过来的图像数据经过 HEVC 编码，因此眼镜处理器需要先对其进行解码。随后，数据会被重新编码为一种专有格式，再传输给显示处理器。

![显示处理器](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-14-800x450.jpg)

*显示处理器*

设备中共有**两颗显示处理器**，每只眼睛对应一颗。**重投影（Reprojection）**，也称时间扭曲（Time Warp），就在这颗芯片上进行。这颗处理器没有外挂内存，所有数据都保存在片上 SRAM 中。这也意味着，这部分 SRAM 的容量设计得异常之大。

![计算协处理器](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-16-800x450.jpg)

*计算协处理器*

最后，是在外部计算单元中的**计算协处理器**。这是整个系统里性能最强、功耗和散热预算也最充裕的处理器。计算机视觉处理、机器学习模型推理、音频渲染、HEVC 编码等繁重任务都在这里完成。这颗芯片同样集成了相对较大的片上 SRAM 缓存。它由 57 亿个晶体管组成，采用 5nm 工艺制造，并与 LPDDR4X 内存封装在一起。

![整体架构](https://www.servethehome.com/wp-content/uploads/2025/08/meta-hc25-17-800x450.jpg)

*整体架构*

将所有这些尖端技术组合在一起，便构成了我们今天看到的 Orion 眼镜。

---

### 未来回响

看完了 Meta 为实现 AR 愿景在芯片层面做出的努力，确实令人印象深刻。从通用计算到专用计算的转变，似乎是推动下一代计算平台发展的必然路径。对此，我们不妨畅想和讨论一下：

1.  **形态之争**：大家觉得 Meta 这种分体式设计（眼镜 + 外部计算单元）会是未来 AR 眼镜的主流形态吗？还是说我们最终能克服功耗和散热的挑战，把所有计算能力都塞进一个独立的眼镜里？
2.  **路线对比**：苹果的 Vision Pro 采用了一体化设计（虽然需要外接电池包供电）。与 Meta 这种将计算任务明确分离的方案相比，在便携性、性能和未来发展潜力上，你更看好哪种路线？
3.  **技术破局点**：你认为除了定制芯片，还有哪些技术（例如电池技术、显示技术、散热材料）的突破，将成为引爆消费级 AR 眼镜市场的关键？

欢迎在评论区留下你的真知灼见，一起探讨 AR 的未来！