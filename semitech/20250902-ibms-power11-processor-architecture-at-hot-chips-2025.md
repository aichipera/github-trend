
### 译者注

在 x86 和 ARM 架构主导的今天，IBM 的 Power 架构依旧是关键任务领域（如大型机、高性能计算）不可或缺的中坚力量。Power11 延续了 IBM“少而精、大核心”的设计哲学，在 AI 时代通过集成矩阵数学引擎和创新的 OMI 内存架构，巧妙地平衡了性能、带宽与成本。它没有盲目追随先进制程，而是选择在成熟的 7nm 工艺上深挖潜力，这体现了 IBM 对客户需求和系统稳定性的深刻理解，也展示了其在后摩尔时代独特的系统级创新思路。

***

# [IBM 在 Hot Chips 2025 大会上发布 Power11 处理器架构](20250902-ibms-power11-processor-architecture-at-hot-chips-2025.mp3)

> 作者：[Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月25日
> 原文链接：https://www.servethehome.com/ibms-power11-processor-architecture-at-hot-chips-2025/ 

[![IBM Power 架构路线图](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_03-696x538.jpg "IBM Power 架构路线图")](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_03.jpg)
*IBM Power 架构路线图*

今天 CPU 主题的第三场演讲来自 IBM。这家蓝色巨人（Big Blue）在大会上讨论了其最新一代的 Power 架构芯片——Power11。

[![](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_02-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_02.jpg)

IBM 的演讲首先回顾了 Power 架构的历史、它存在的意义，以及 IBM 对这款处理器和其架构设定的目标。与仅仅销售 CPU 的厂商不同，IBM 极度关注整个系统。其产品线覆盖了从单路（1P）、双路（2P）系统，一直到高达 16 路的“无胶水”多路互联（glueless）系统。

*我们正在进行现场报道，如有拼写错误，敬请谅解。*

## IBM Power11 亮相 Hot Chips 2025

回顾 Power 的发布历史，Power10 对 IBM 来说被证明是非常成功的，其成就“远超我们最大胆的想象”。因此，Power11 并非对 Power10 的颠覆性改变；它更多是在 Power10 的基础上进行构建，而不是大规模替换其核心部分。这也意味着，与过去的 Power 发布会，甚至是本次 Hot Chips 大会上的其他演讲相比，Power11 的新内容并没有那么多。

值得注意的是：搭载 Power11 的系统已经发布。所以这次在 Hot Chips 上的演讲，更多的是为了让与会者了解最新进展，而不是用爆炸性新闻来震撼全场。

IBM 的设计哲学是采用更少但更强大的核心，然后根据需要扩展核心数量。

[![](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_06-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_06.jpg)

相较于 Power10，最大的变化之一？那就是将 AI 功能集成到处理器核心中的迫切需求。

[![](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_08-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_08.jpg)

从某些方面来看，IBM 在 Power10 中集成的矩阵乘法引擎已经让他们在这方面走在了行业前沿。但显然，这还远远不够。

[![](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_09-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_09.jpg)

Power10 构建于三星的 7LPE 工艺之上。而 Power11 则（根据客户的反馈）继续沿用 7nm 工艺，因此优化的重点放在了提升速度而非堆砌密度上。最终，它采用了三星 7nm 技术的更新迭代版本。

[![](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_10-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_10.jpg)

Power11 还采用了堆叠设计。IBM 使用了同样由三星代工的硅中介层（silicon interposer）。

[![](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_13-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_13.jpg)

除了对核心架构进行一系列调整外，Power11 的另一个重点是整个系统堆栈的优化。这意味着 IBM 致力于全方位的改进，从抵御未来攻击的量子安全（quantum safety），到改进系统更新的部署方式。

[![Power11 OMI 内存](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_21-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_21.jpg)
*Power11 的 OMI 内存*

更重大的升级在于 Power11 的内存子系统，IBM 称之为 OMI 内存架构（OMI Memory Architecture）。这种分层内存架构意味着单个芯片最多可拥有 32 个 DDR5 内存端口。其互联速度高达 38.4Gbps，并最终催生了一种定制化的内存形态——OMI D-DIMM。

[![OMI 内存架构](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_23-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_23.jpg)
*OMI 内存架构*

顺便一提，IBM 对 HBM（高带宽内存）并不十分看好。倒不是说它速度不快（它确实很快），而是其容量相对较小。IBM 希望鱼与熊掌兼得：他们既想要 8TB 的 DRAM 容量，也想要超过 1TB/s 的内存带宽。而 OMI 架构正是在传统的 DDR5 内存基础上实现了这一目标。据 IBM 称，这些 OMI 缓冲器（buffer）会增加 6 到 8 纳秒的延迟。

[![Power11 对 AI 加速器的连接支持](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_25-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_25.jpg)
*Power11 对 AI 加速器的连接支持*

Power11 还将为外部 PCIe 加速器带来更好的支持。图中展示了 IBM 自家的 Spyre 加速器。

[![IBM Power 的未来展望](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_29-800x618.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/23_ibm_starke_v2_29.jpg)
*IBM Power 的未来展望*

当然，IBM 的脚步不会止于 Power11。下一代 Power——“Power Future”——已在开发之中。IBM 在设计下一代芯片时，必须考虑到行业的变化趋势，包括应用场景的演变以及未来可用于芯片制造的技术。简而言之，和其他所有厂商一样，IBM 也无法再仅仅依赖于更先进的制程节点来获得巨大的性能和密度提升。

除了眼下的制造工艺问题，带宽也是一个焦点。芯粒（Chiplet）技术的使用带来了新的挑战，即芯片边缘可用的宝贵空间（即所谓的“黄金海岸线”，beachfront property）非常有限。当大量的带宽需要被用于芯粒之间的互联时，这个问题就变得更加复杂。OMI 被视为解决这一问题的方案之一。

> *对于那些更关注大众市场，并希望了解英特尔 2026 年 CPU 计划的读者，我们在本文发布后，已在我们的 Substack 专栏中对此进行了深入探讨。*
>
> *《英特尔 2026 年的 Diamond Rapids 和 Clearwater Forest 面临的挑战》by Patrick Kennedy*
>
> *英特尔的产品路线图与其 CEO 的目标并不一致。*

---

### 极客观点碰撞

看完了 IBM 对 Power11 的解读，相信你一定有很多想法。不妨在这里分享你的观点，让我们一起探讨技术的未来：

*   **坚守还是另辟蹊径？** 在 x86 与 ARM 架构日益普及的今天，你如何看待 IBM Power 架构坚持“少而精的大核心”策略？这在未来的 AI 和数据中心市场中是优势还是劣势？
*   **内存的终极方案？** IBM 的 OMI 内存架构通过 DDR5 实现了超大容量和高带宽，但牺牲了一点延迟。你认为它与 HBM 相比，哪种方案更能代表未来高性能计算的趋势？
*   **后摩尔时代的创新？** Power11 没有追逐最新的 3nm 或 2nm 工艺，而是选择在成熟的 7nm 上进行架构和系统级创新。你认为这种策略是否明智？这对于整个芯片行业有什么启示？
*   **生态系统的挑战：** 尽管 Power 架构性能强大，但其生态系统相对封闭。你认为 IBM 应如何吸引更多的开发者和用户，以应对开放生态的挑战？