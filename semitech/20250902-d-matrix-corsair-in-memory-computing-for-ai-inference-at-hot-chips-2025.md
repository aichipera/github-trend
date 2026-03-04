
## 译者注

> 在AI算力需求爆炸式增长的今天，英伟达GPU一家独大的局面正面临着来自四面八方的挑战。d-Matrix就是这股浪潮中的一个挑战者。它所押注的“内存计算”（In-Memory Computing）架构，旨在颠覆传统冯·诺依曼架构下计算与存储分离的模式，通过在内存单元内直接执行计算，彻底解决AI推理中“内存墙”的瓶颈。其Corsair芯片采用Chiplet（小芯片）和3D堆叠技术，追求极致的低延迟和高能效，这使其在语音交互、AI Agent等实时性要求极高的场景中具备独特的竞争优势。

---

# [d-Matrix 在 Hot Chips 2025 大会发布用于 AI 推理的 Corsair 内存计算芯片](20250902-d-matrix-corsair-in-memory-computing-for-ai-inference-at-hot-chips-2025.mp3)

> 作者: [Ryan Smith](https://www.servethehome.com/author/ryansmith/) - 2025年8月26日
> 原文链接: https://www.servethehome.com/d-matrix-corsair-in-memory-computing-for-ai-inference-at-hot-chips-2025/

[![卡级扩展：16个Chiplet的分层全互联架构](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-8-696x392.jpg "卡级扩展：16个Chiplet的分层全互联架构")](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-8.jpg)
*卡级扩展：16个Chiplet的分层全互联架构*

午后第二场机器学习相关的演讲来自 d-Matrix 公司。这家公司专注于 AI 推理硬件，并且近来一直致力于解决如何利用内存计算来提升推理性能的问题。循着这个思路，该公司在今年的 Hot Chips 大会上展示了其 Corsair 内存计算 Chiplet 架构。顺便一提：几天前我们曾报道过 [d-Matrix Pavehawk 携 3DIMC 技术挑战 HBM 在 AI 推理领域的地位](https://www.servethehome.com/d-matrix-pavehawk-brings-3dimc-to-challenge-hbm-for-ai-inference/)。

d-Matrix 声称，得益于内存计算与低延迟互连技术的结合，Corsair 是市场上能效最高的推理平台。（友情提示：此 Corsair 非彼 [Corsair](https://www.corsair.com/)，请勿与知名硬件厂商海盗船混淆。）

[![“重新思考”AI推理](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-2-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-2.jpg)
*“重新思考”AI推理*

[![大语言模型（LLM）的Token生成受限于内存带宽](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-3-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-3.jpg)
*大语言模型（LLM）的Token生成受限于内存带宽*

在 LLM 中，每一个 Token 的生成都受限于内存带宽。因为所有的权重参数都需要被读取。而批处理（Batching）技术可以分摊这些权重读取的开销。

d-Matrix 的目标是在中等批处理大小（Batch Size）下就能达到算力饱和，从而满足特定的延迟指标。

[![语音应用对延迟极为敏感，且更受限于内存带宽](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-4-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-4.jpg)
*语音应用对延迟极为敏感，且更受限于内存带宽*

实时语音处理要求极低的延迟，这使其成为 d-Matrix 技术的理想目标应用场景。

[![AI Agent：小语言模型（SLM）与推理时计算的兴起](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-5-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-5.jpg)
*AI Agent：小语言模型（SLM）与推理时计算的兴起*

AI Agent（人工智能代理）也面临同样的情况，它需要执行多个小型模型来完成预定任务。

[![d-Matrix Corsair: 基于Chiplet的推理加速平台](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-6-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-6.jpg)
*d-Matrix Corsair: 基于Chiplet的推理加速平台*

这就是 d-Matrix 的加速器——Corsair。它由两颗芯片构成，每颗芯片包含 4 个 Chiplet，基于台积电 6nm 工艺制造。所有 Chiplet 共享 2GB 的 SRAM。这是一块标准的 PCIe 5.0 x16 卡，可以轻松地添加到标准服务器中。

同时，在卡的上边缘设有桥接连接器，用于将多张卡连接在一起。

每个 Chiplet 都与 LPDDR5X 内存连接，每张卡总共配备 256GB 的 LPDDR5X 内存。

[![Corsair Chiplet 架构](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-7-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-7.jpg)
*Corsair Chiplet 架构*

这张图展示了 Chiplet 是如何被组织成多个“切片”（slice）的。边缘部分是 LPDDR 和 D2D（Die-to-Die）连接接口，以及 16 个 PCIe 通道。

[![卡级扩展：16个Chiplet的分层全互联架构](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-8-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-8.jpg)
*卡级扩展：16个Chiplet的分层全互联架构*

两张卡可以通过无源桥接器连接在一起，形成一个拥有 16 个 Chiplet、具备全互联（all-to-all）能力的集群。

[![系统与扩展架构](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-9-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-9.jpg)
*系统与扩展架构*

8 张卡可以部署在一台标准服务器中，例如一台 Supermicro X14 服务器。在此示例中，还配置了 4 张网卡（NIC）以提供横向扩展（scale-out）能力。

[![Corsair 的核心支柱 – 低延迟与批处理吞吐量](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-10-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-10.jpg)
*Corsair 的核心支柱 – 低延迟与批处理吞吐量*

Corsair 是为低延迟、高批处理吞吐量的推理任务而生。

它们支持块浮点（block floating point）数据格式。能效比高达每瓦 38 TOPS。

[![由模块化硬件块构建的 Corsair Chiplet](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-12-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-12.jpg)
*由模块化硬件块构建的 Corsair Chiplet*

每个 Chiplet 内部的调度引擎基于 RISC-V 架构。1 个 Chiplet 被划分为 4 个象限（quads）。D2D 带宽约为 1TB/s。

[![高能效的数字内存计算（DIMC）架构](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-13-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-13.jpg)
*高能效的数字内存计算（DIMC）架构*

深入来看，Corsair 内部的矩阵乘法器可以执行 INT8 格式的 64×64 矩阵乘法，或 INT4 格式的 64×128 矩阵乘法。

[![Corsair 支持5倍权重压缩](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-14-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-14.jpg)
*Corsair 支持5倍权重压缩*

Corsair 还支持带缩放因子的浮点（FP）格式，以及结构化稀疏（structured sparsity）——尽管后者仅用于压缩。总的来说，这使得 d-Matrix 能够实现 5 倍的压缩率。

[![核心架构](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-15-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-15.jpg)
*核心架构*

所有 8 个矩阵单元可以连接在一起协同工作。

[![采用块浮点数值格式的数据流](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-16-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-16.jpg)
*采用块浮点数值格式的数据流*

数据流示意图。数据在计算过程中实时累加，然后转换为所需的输出格式。

[![内存系统：全局内存、暂存内存和LPDDR](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-17-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-17.jpg)
*内存系统：全局内存、暂存内存和LPDDR*

在内存方面，有一个暂存内存（stash memory）为计算核心提供数据。每个暂存内存大小为 6MB。每个 Chiplet 有 2 个 LPDDR 通道。

[![大模型推理的扩展挑战](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-18-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-18.jpg)
*大模型推理的扩展挑战*

当你拥有极高的内存带宽时，集合通信（collective）的延迟就变得至关重要。

[![Corsair 扩展 – 软硬件协同设计](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-19-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-19.jpg)
*Corsair 扩展 – 软硬件协同设计*

为了实现 16 个 Chiplet 的全互联，d-Matrix 将 D2D 延迟降低到了 115 纳秒。即使通过 PCIe 交换机，他们仍能将延迟控制在 650 纳秒。

[![封装级扩展：4个Chiplet的全互联](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-20-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-20.jpg)
*封装级扩展：4个Chiplet的全互联*

这是 Corsair Chiplet 部署在有机封装基板上的另一张特写。

[![透明网卡 – 以太网横向扩展](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-21-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-21.jpg)
*透明网卡 – 以太网横向扩展*

这是 d-Matrix 用于横向扩展网络的网卡，延迟为 2 微秒。

[![机柜级横向扩展：多节点与多机柜](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-22-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-22.jpg)
*机柜级横向扩展：多节点与多机柜*

利用这种技术，d-Matrix 可以将许多服务器堆叠成机柜阵列。

[![Aviator 软件：易于使用并为 Corsair 优化](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-23-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-23.jpg)
*Aviator 软件：易于使用并为 Corsair 优化*

[![Aviator 软件：为LLM加速而协同设计](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-24-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-24.jpg)
*Aviator 软件：为LLM加速而协同设计*

任何推理加速器都离不开配套的软件栈来驱动硬件并释放其特性，Corsair 也不例外。

[![能效比 (TOPS/W)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-25-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-25.jpg)
*能效比 (TOPS/W)*

这是一张功耗表现图。在 800MHz 频率下功耗为 275W。而 1.2GHz 频率下功耗则飙升至 550W。更高的时钟频率对整体能效不利，但影响不算特别巨大。

[![面向不同用例的性能与灵活性](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-26-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-26.jpg)
*面向不同用例的性能与灵活性*

这里展示了一些 Llama3 模型的性能数据。即使是对于较大的 Llama3-70B 模型，每个输出 Token 的生成时间也仅为 2 毫秒。

[![在3D中将逻辑芯片堆叠在DRAM中介层上](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-27-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-27.jpg)
*在3D中将逻辑芯片堆叠在DRAM中介层上*

在芯片下方，d-Matrix 使用了一个带有电容的硅中介层以保证供电的可靠性。d-Matrix 更进一步，将 DRAM 3D 堆叠在他们的 Corsair Chiplet 之下，使得本地内存离计算单元非常非常近。

[![3D DRAM 测试载具](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-28-800x450.jpg)](https://www.servethehome.com/wp-content/uploads/2025/08/24_dMatrix_Bhoja_final-28.jpg)
*3D DRAM 测试载具*

他们已经构建了一个 3D DRAM 测试载具的原型。采用了 36 微米间距的 D2D 堆叠技术。逻辑芯片位于上方，而 DRAM 则位于其下。

d-Matrix 是如何实现 DRAM + 逻辑芯片堆叠的呢？关键在于将热密度控制在 0.3W/mm² 以下，这样可以避免 DRAM 过热。

---

## “芯”潮澎湃，邀您共论

看完了 d-Matrix 这款专为 AI 推理打造的“新式武器”，你有什么想法？欢迎在评论区留下你的真知灼见！

1.  **架构之争**：你认为 d-Matrix 的“内存计算”+ Chiplet 方案，相较于英伟达等传统 GPU 架构，在 AI 推理任务上真正的优势和潜在的挑战分别是什么？它会成为未来的主流吗？
2.  **市场破局**：在 AI 芯片这条拥挤的赛道上，像 d-Matrix 这样的初创公司，凭借架构创新能否真正撼动行业巨头的地位？他们成功的关键会是什么？
3.  **未来应用**：除了文中提到的实时语音和 AI Agent，你认为还有哪些未来的 AI 应用场景，最能从 Corsair 这种低延迟、高能效的推理硬件中受益？