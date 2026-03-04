# 一、Hot Chips 2023-2025 关键产业界演讲报告概览

## Hot Chips 2023

### 主题：AI全面爆发，Chiplet成为基础

### Keynotes

- **Google (Jeff Dean & Amin Vahdat):** 《Exciting Directions for ML Models and the Implications for Computing Hardware》 - 从顶层应用和模型发展的角度，定义了对未来硬件的需求。

- **NVIDIA (Bill Dally):** 《Hardware for Deep Learning》 - 阐述了NVIDIA为深度学习设计的硬件理念和演进路线。

### AI/ML处理器

- **Google:** 《A Machine Learning Supercomputer With An Optically Reconfigurable Interconnect》 - 展示了其TPU系统的庞大规模和对光学互联的探索。

- **Cerebras:** 《Inside the Cerebras Wafer-Scale Cluster》 - 继续推进其晶圆级计算的独特路线。

- **IBM:** 《IBM NorthPole Neural Inference Machine》 - 展示了其受大脑启发的、注重能效的推理芯片架构。

### CPU架构

- **AMD:** 《AMD Next Generation "Zen 4" Core and 4th Gen AMD EPYCTM 9004 Server CPU》 - 发布了其核心数据中心处理器。

- **Intel:** 《Architecting for Flexibility and Value with future Intel® Xeon® processors》 & 《Intel® Xeon® processors built on Efficient-core (E-Core)》 - 详细阐述了其P-Core和E-Core的混合架构战略。

- **Arm:** 《ARM's Neoverse V2 platform》 - 推出了其面向云和HPC的新一代数据中心平台。

### 系统与互联

- **Tutorial:** 《Chiplets/UCIe》 - 由Intel、AMD、NVIDIA等公司联合主导，标志着Chiplet互联标准UCIe已成为行业共识。

- **Intel:** 《The First Direct Mesh-to-Mesh Photonic Fabric》 - 首次展示了芯片间直接光互联的成果。

## Hot Chips 2024

### 主题：AI芯片"军备竞赛"白热化，系统瓶颈凸显

### Keynotes

- **OpenAI (Trevor Cai):** 《Predictable Scaling and Infrastructure》 - AI模型公司首次登上Keynote舞台，直接向硬件行业提出了对可预测扩展性的需求，影响力巨大。

- **AMD (Victor Peng):** 《The Journey to Life with AI Pervasiveness》 - 描绘了AI从数据中心到边缘和终端的普及化蓝图。

### AI加速器（GenAI旗舰之战）

- **NVIDIA:** 《NVIDIA Blackwell Platform: Advancing Generative AI and Accelerated Computing》 - 发布了其划时代的Blackwell GPU架构。

- **AMD:** 《AMD InstinctTM MI300X Generative AI Accelerator and Platform Architecture》 - 推出了其对标NVIDIA的旗舰AI加速器。

- **Intel:** 《Intel Gaudi 3 AI Accelerator: Architected for Gen AI Training and Inference》 - 展示了其在AI训练和推理市场的核心产品。

- **Microsoft:** 《Inside MAIA 100》 - 作为超大规模数据中心厂商，首次公开其自研AI芯片。

### 客户端AI（AI PC元年）

- **Qualcomm:** 《Snapdragon X Elite Qualcomm Oryon CPU: Design & Architecture Overview》 - 凭借其强大的Oryon CPU和NPU，正式进军PC市场。

- **Intel:** 《Lunar Lake: Powering the Next Generation of AI PCs》 - 发布了其为AI PC设计的全新异构架构。

### 系统与方法学

- **Tutorial:** 《AI Assisted Hardware Design》 - 由NVIDIA、Synopsys等主导，探讨使用AI来设计芯片，标志着行业方法论的变革。

- **Tutorial:** 《The Cooling of Hot Chips》 - 首次将散热作为一个独立的教程，反映了千瓦级芯片带来的巨大物理挑战。

## Hot Chips 2025

### 主题：从芯片到"AI工厂"，光互联和机架级架构成为主角

### Keynotes

- **Google DeepMind (Noam Shazeer):** 《Predictions for the Next Phase of AI》 - 作为Transformer架构的发明者之一，他的预测进一步指引着硬件的未来方向。

- **Rapidus (Dr. Atsuyoshi Koike):** 《Up and Running with Rapidus》 - 关注前沿半导体制造，显示了供应链的重要性。

### AI加速器（持续迭代）

- **NVIDIA:** 《NVIDIA's GB10 SoC: AI Supercomputer On Your Desk》 - 展示了Blackwell架构的进一步产品化和系统化。

- **AMD:** 《4th Gen AMD CDNA™ Generative AI Architecture Powering AMD Instinct™ MI350 Series GPUs》 - 发布其下一代AI GPU架构。

- **Google:** 《Ironwood: Delivering best in class perf...for reasoning model training and serving》 - 推出了其最新一代TPU。

### 系统级架构（焦点转移）

#### Tutorial: 《Datacenter Racks》
整个教程聚焦于**机架级系统设计**，案例研究包括 **NVIDIA的GB200NVL72**、**Meta的Catalina**和**Google的TPU Rack**，这表明设计单元已从芯片扩展到整个机架。

#### 光学互联（成为独立分会场）

- **NVIDIA:** 《Co-Packaged Silicon Photonics Switches for Gigawatt AI Factories》 - 直接将光交换与芯片封装在一起，目标是支撑"吉瓦级"的AI工厂。

- **Celestial AI, Ayar Labs, Lightmatter:** 展示了各自的片上/封装内光I/O方案，标志着光互联技术从前沿探索走向商业落地。

#### AI网络

- **NVIDIA:** 《NVIDIA ConnectX-8 SuperNIC》

- **AMD:** 《AMD Pensando™ Pollara 400 AI NIC Architecture》

这两场演讲展示了专为大规模AI集群设计的下一代智能网卡，重点解决RoCE等协议的性能问题。

# 二、结合演讲报告分析产业技术发展趋势变化

## 趋势一：AI的主导地位从"核心议题"演变为"唯一背景"

AI已经成为驱动所有技术创新的默认前提和最终目标。

### 从应用定义硬件
2023年，**Google的Jeff Dean**还在探讨"ML模型对硬件的启示"。到了2024年，**OpenAI的Trevor Cai**直接登上Keynote，告诉硬件厂商"我们需要什么"。而到2025年，**Google DeepMind的Noam Shazeer**则在预测"AI的下一阶段"，整个行业都在围绕AI模型的演进路线来规划硬件蓝图。

### AI芯片的军备竞赛与常规化
2024年是AI加速器的"发布大年"，**NVIDIA的Blackwell**、**AMD的MI300X**、**Intel的Gaudi 3**和**Microsoft的MAIA 100**同台竞技，这是竞争最激烈的时刻。到了2025年，虽然有**NVIDIA GB10**和**AMD MI350**的更新，但这已成为一种可预期的迭代。行业的兴奋点已经从"你发布了什么AI芯片"转移到了"你如何将成千上万个这样的芯片连接成一个高效的系统"。

## 趋势二：设计尺度的宏大化——从"单芯片"到"AI工厂（AI Factory）"

行业的关注点和设计单元正在以前所未有的速度从芯片级（Chip-level）上升到机架级（Rack-scale）和数据中心级（Datacenter-scale）。

### 奠基（2023）
当年的**《Chiplets/UCIe》教程**为构建大型、异构的计算系统铺平了道路，它是后来一切系统级创新的基础。

### 瓶颈凸显（2024）
随着**Blackwell**等千瓦级芯片的发布，功耗和散热问题变得不可忽视，直接催生了**《The Cooling of Hot Chips》教程**。同时，如何连接这些芯片，让通信不成为瓶颈，也成为了**Tesla DOJO网络**等议题的核心。

### 蓝图成型（2025）
2025年的议程是这一趋势的顶峰。**《Datacenter Racks》教程**以及**NVIDIA GB200NVL72**的案例研究，标志着业界开始以"机架"为单位进行一体化设计。一个机架不再是CPU、GPU和网卡的简单堆砌，而是一个经过整体优化的计算单元。**NVIDIA的"吉瓦级AI工厂"**概念，正是这一趋势的终极体现。

## 趋势三：光进铜退——光互联从"前沿探索"走向"核心支柱"

为了支撑"AI工厂"内部海量的数据流动，光互联技术已经从一个"加分项"变成了"必需品"。

### 萌芽（2023）
**Intel的《Photonic Fabric》**演讲展示了早期的技术可能性，但仍被视为前沿研究。

### 加速（2024）
**Intel**再次展示了其**《4 Tbit/s Optical Compute Interconnect Chiplet》**，性能指标大幅提升，显示技术在快速成熟。

### 爆发（2025）
Hot Chips 2025设立了一个完整的**"Optical"分会场**，这是历史性的变化。**Celestial AI**的"世界首款带in-die光IO的SoC"、**Ayar Labs**的"UCIe光I/O Chiplet"以及**NVIDIA**的"Co-Packaged光交换"，清晰地表明，为了突破带宽、延迟和功耗的限制，将光I/O集成到芯片封装内部或旁边，已经成为行业领袖们的一致选择。

## 趋势四：CPU的演进——拥抱AI PC与数据中心内的角色分化

在AI加速器高歌猛进的同时，CPU也在寻找自己的新定位。

### AI走向客户端（2024）
2024年是AI PC的元年。**Qualcomm的Oryon CPU (Snapdragon X Elite)** 和 **Intel的Lunar Lake**的发布，都强调了其强大的片上NPU能力，旨在将生成式AI体验带到笔记本电脑上。这是CPU从纯粹的通用计算向异构AI平台演进的关键一步。

### 数据中心的专业化分工（2023-2025）
在数据中心，CPU的角色也在分化。一方面，如**AMD Zen 4/5**，继续追求极致的单核性能。另一方面，**Intel的《Next Generation Intel® Xeon® Processor with Efficiency Cores》**（2025）等演讲表明，高密度、高能效的E-Core处理器在云原生、微服务等场景下变得越来越重要，它们将承担大量的基础设施和数据处理任务，从而让昂贵的AI加速器专注于其核心计算。

# 结论

通过梳理Hot Chips 2023至2025年的关键演讲，我们可以清晰地看到一条由生成式AI驱动的技术演进脉络：行业首先在2023年确立了AI的核心地位和Chiplet等基础技术；随后在2024年掀起了AI加速器的"算力军备竞赛"，并开始直面随之而来的散热、网络等系统瓶颈；最终在2025年，将焦点全面转向以**机架级设计**和**光互联**为核心的**"AI工厂"**系统架构。这不仅是芯片性能的提升，更是一场围绕算力、互联、散热和供电的全栈式系统工程革命。
