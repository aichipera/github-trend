# [深入剖析TPU](tpu_deep_dive-podcast-20250622.mp3)

> 作者: **Henry Ko**, 文章来源: https://henryhmko.github.io/posts/tpu/tpu.html

> **译者注**: 本文深入剖析了谷歌TPU的设计哲学。与追求通用性的GPU不同，TPU作为专用集成电路（ASIC），通过软硬件协同设计（如XLA编译器和脉动阵列），在矩阵运算上实现了极致的能效与扩展性。这种“专精”路线虽牺牲了部分灵活性，却构筑了谷歌在超大规模AI训练和推理领域的护城河。对开发者而言，理解其架构差异是发挥其最大潜力的关键。

近来，我频繁地与TPU打交道，发现其与GPU在设计哲学上竟有如此天壤之别，这实在是一件趣事。

TPU最核心的优势在于其无与伦比的可扩展性。这一优势的实现，得益于硬件（如能效与模块化设计）与软件（如XLA编译器）的协同设计。

## 背景

简单来说，TPU是谷歌自主研发的专用集成电路（ASIC），其设计核心聚焦于两大要素：**极致的矩阵乘法吞吐量**与**卓越的能效**。

它的起源可以追溯到2006年的谷歌。当时，公司内部正在评估是应该采用GPU、FPGA还是定制ASIC来满足日益增长的计算需求。那时，需要专用硬件的应用屈指可数，谷歌认为可以利用其庞大数据中心里富余的CPU算力来应对。然而，情况在2013年发生了转变。当时，谷歌的语音搜索功能开始运行在神经网络之上，内部预测显示，一旦该功能流行开来，所需的计算量将呈爆炸式增长。

时至今日，TPU已经为谷歌绝大多数的AI服务提供了动力。这自然包括了像Gemini或Veo这样的大模型训练与推理，也包括了其推荐模型（DLRM）的部署。

接下来，让我们自下而上，深入探究TPU的内部构造。

## TPU单芯片层面

我将以TPUv4为例进行图解，但这种布局或多或少也适用于最新一代的TPU（例如TPUv6p "Trillium"；截至本文撰写时（2025年6月），TPUv7 "Ironwood"的细节尚未公布）。

下图是单个TPUv4芯片的布局：

![芯片图][fig1]
*TPU单芯片及其张量核心（TensorCore）*

在每块芯片上，都有两个负责计算的TPU张量核心（TensorCore）。（请注意：专用于推理的TPU只有一个张量核心）。这两个张量核心共享内存单元：CMEM（128MiB）和HBM（32GiB）。

而在每个张量核心内部，则包含了我们的计算单元和更小的内存缓冲区：

### 1. 矩阵乘法单元 (Matrix Multiply Unit, MXU)

*   这是张量核心的关键组件，是一个128x128的脉动阵列（Systolic Array）。
*   我们将在下文详细介绍脉动阵列。

### 2. 向量单元 (Vector Unit, VPU)

*   负责通用的逐元素操作（如ReLU、逐点加/乘、规约操作等）。

### 3. 向量内存 (Vector Memory, VMEM; 32MiB)

*   内存缓冲区。来自HBM的数据必须先复制到VMEM中，张量核心才能对其进行计算。

### 4. 标量单元 + 标量内存 (Scalar Memory, SMEM; 10MiB)

*   负责向VPU和MXU下达指令。
*   管理控制流、标量运算和内存地址生成。

如果你熟悉NVIDIA的GPU，可能会对以下几点感到困惑：

1.  TPU上的片上内存单元（CMEM, VMEM, SMEM）远大于GPU上的L1、L2缓存。
2.  TPU上的HBM容量也远小于GPU上的HBM。
3.  负责计算的“核心”数量似乎少得多。

这与GPU的设计理念几乎完全相反。以H100为例，其L1、L2缓存较小（分别为256KB和50MB），HBM容量更大（80GB），并拥有数万个计算核心。

在我们继续深入之前，请记住，TPU与GPU一样，都具备极高的吞吐量。单片TPU v5p的算力可达500 TFLOPs/秒，而一个由8960个芯片组成的完整Pod集群，其总算力可达约4.45 ExaFLOPs/秒。据称，最新的"Ironwood" TPUv7每个Pod（9216个芯片）的算力甚至能高达42.5 ExaFLOPS/秒。

要理解TPU如何实现这一切，我们必须先理解其设计哲学。

## TPU的设计哲学

TPU之所以能实现惊人的吞吐量和能效，主要依赖于两大支柱和一个关键假设：**脉动阵列 + 流水线技术**，**预先编译（AoT）**，以及一个核心前提——**绝大多数计算都可以被有效地映射到脉动阵列上**。幸运的是，在当今的深度学习时代，矩阵乘法构成了计算的主体，而这正是脉动阵列的用武之地。

## TPU设计选择#1：脉动阵列 + 流水线

### 问：什么是脉动阵列？

脉动阵列是一种硬件设计架构，由一个网格状的互联处理单元（PE）阵列构成。每个PE执行一个简单的计算（例如乘加运算），并将结果传递给相邻的PE。

![脉动阵列图][fig2]

这种设计的优势在于，一旦数据被送入脉动阵列，就不再需要额外的控制逻辑来指导数据如何处理。此外，只要脉动阵列足够大，除了最初的输入和最终的输出，中间过程几乎没有内存读写操作。

由于其结构化的组织方式，脉动阵列仅能处理具有固定数据流模式的运算，但幸运的是，矩阵乘法和卷积完美地契合了这一模式。

更重要的是，这为通过流水线技术将计算与数据移动重叠起来创造了绝佳的机会。下图展示了TPU上一个流水线化的逐点操作。

![TPU数据流可视化][fig3]
*流水线化的逐点操作（图片来源："How to Scale Your Model" [[4]][1]）*

### 题外话：脉动阵列的短板 - 稀疏性

不难看出，脉动阵列偏爱稠密矩阵（即每个PE在几乎每个时钟周期都处于活动状态）。然而，其缺点在于，对于同样大小的稀疏矩阵，它无法带来性能提升：因为即使是处理值为零的元素，PE仍然需要执行相同数量的时钟周期。

如果深度学习社区未来更青睐不规则的稀疏性结构（例如混合专家模型MoE），那么如何应对脉动阵列这一系统性局限将变得愈发重要。

## TPU设计选择#2：预先编译（AoT）+ 减少对缓存的依赖

本节将解释TPU如何通过TPU硬件与XLA编译器的软硬件协同设计，避免使用缓存，从而实现高能效。

首先，我们回顾一下传统缓存的设计初衷：处理不可预测的内存访问模式。不同应用程序的内存访问模式可能天差地别。本质上，缓存让硬件变得灵活，能够适应各种应用。这也是GPU（相对于TPU而言）具有高度灵活性的重要原因。

然而，缓存访问（以及广义上的内存访问）会消耗大量能源。下图粗略估算了芯片上各种操作的能耗（基于45nm工艺，0.9V电压；[[18]][2]）。这里的关键信息是：**内存访问和控制消耗了我们绝大部分的能源，而算术运算的能耗则要低得多**。

![操作能耗对比图][fig4]

但如果你的应用领域非常特定，其计算和内存访问模式高度可预测，情况又会如何呢？

举一个极端的例子，如果我们的编译器能够提前预知所有需要的内存访问，那么硬件只需要一个高速暂存器（Scratchpad Memory）作为缓冲区就足够了，完全不需要缓存。

这正是TPU的设计哲学所追求的目标，也是TPU与XLA编译器协同设计的根本原因。XLA编译器通过提前分析计算图，生成高度优化的程序。

### 问：但JAX也能很好地与TPU配合，它用的不是`@jit`（即时编译）吗？

JAX+XLA在TPU上的工作模式，实际上是即时编译（JIT）和预先编译（AoT）的混合体，因此容易引起混淆。当我们首次调用一个在JAX中被`jit`修饰的函数时，JAX会对其进行追踪（trace）以创建一个静态计算图。这个计算图随后被传递给XLA编译器，由它转换成一个完全静态的、专为TPU设计的二进制文件。正是在这最后的转换阶段，编译器会进行TPU特定的优化（例如最小化内存访问），使程序完全为TPU量身定制。

但这里有一个警示：如果`jit`函数的输入形状（shape）发生变化，它就必须被重新编译和缓存。这就是为什么JAX在处理任何动态填充（dynamic padding）或包含依赖于输入长度的for循环的层时表现不佳。

当然，这种方法听起来很美好，但也有其不便之处。它缺乏灵活性，并且对编译器的重度依赖是一把双刃剑。

那么，谷歌为何仍然坚持这一设计哲学呢？

### TPU与能效（以TPUv4为例）

前面展示的能耗图并不完全适用于TPU，所以这里是TPUv4的能耗分解图。请注意，TPUv4采用的是7nm工艺，图中的45nm数据仅作对比之用（[[3]][3], [[16]][4]）。

左侧的条形图标示了能耗数值，需要注意的是，现代芯片使用HBM3，其能耗远低于图中所示的DDR3/4 DRAM。尽管如此，该图清晰地表明，内存操作的能耗比计算操作高出几个数量级。

这与现代的规模定律（scaling laws）不谋而合：我们非常乐意通过增加浮点运算（FLOPS）来换取内存操作的减少。因此，减少内存操作具有双重优化效益：它不仅能让程序运行得更快，还能大幅降低能耗。

## TPU多芯片层面

现在，让我们把视野提升一个层次，看看TPU在多芯片配置下是如何工作的。

## 托盘（Tray）层面（又称“板卡”，含4个芯片）

![TPU托盘图][fig5]

一个TPU托盘包含4个TPU芯片，即8个张量核心（通常简称为“核”）。每个托盘都配有自己的CPU主机（Host）。（注意：对于推理型TPU，由于每个芯片只有一个核心，一个主机可以访问两个托盘）。

主机与芯片之间通过PCIe连接，而芯片与芯片之间则通过**核心间互连（ICI）**连接，ICI拥有更高的带宽。

但ICI的连接范围远不止于单个托盘，它可以延伸至多个托盘。为此，我们需要进入机架（Rack）层面。

## 机架（Rack）层面（4x4x4芯片集群）

TPU最激动人心的部分在于其扩展性，这一点从机架层面开始初露端倪。

一个TPU机架由64个TPU组成，它们被连接成一个**4x4x4的3D环面网络（3D torus）**。如果你看过谷歌下面这样的TPU宣传图，那么图中展示的就是8个TPU机架。

![8个TPU机架图][fig6]
*8个TPU机架（TPUv4）*

在深入探讨机架之前，我们需要厘清一些容易混淆的术语：**Rack（机架）**、**Pod** 和 **Slice（切片）**。

### 问：“TPU Rack”、“TPU Pod”和“TPU Slice”之间有什么区别？

不同的谷歌资料对这些术语的使用略有不同，有时甚至将“TPU Pod”和“TPU Slice”互换使用。但在本文中，我们将遵循谷歌TPU论文和GCP TPU文档中的定义（[[3]][5], [[7]][6], [[9]][7]）。

1.  **TPU Rack（机架）**：
    *   一个物理单元，包含64个芯片。也被称为一个“立方体”（cube）。
2.  **TPU Pod**：
    *   通过ICI和光纤可以连接的TPU最大单元。
    *   也称为“Superpod”或“完整Pod”。例如，一个TPUv4的Pod由4096个芯片（即64个TPU机架）组成。
3.  **TPU Slice（切片）**：
    *   介于4个芯片和Superpod规模之间的任意TPU配置。

关键区别在于，**TPU Rack和TPU Pod是物理计量单位，而TPU Slice是一个抽象概念**。当然，设置TPU Slice时有重要的物理约束，但我们暂且将其抽象化。

目前，我们先关注物理单位：TPU Rack和TPU Pod。因为了解TPU系统是如何物理连接的，能帮助我们更好地理解TPU的设计哲学。

现在回到TPU机架（以TPUv4为例）：

一个TPU机架由64个芯片组成，通过ICI和**光路交换（OCS）**连接在一起。本质上，我们通过连接多个托盘来模拟一个64芯片的系统。这种将小部件组合成超级计算机的主题，在后面还会反复出现。

下图是一个TPUv4机架的示意图。它是一个4x4x4的3D环面网络，每个节点代表一个芯片，蓝色箭头是ICI，而立方体表面上的红线是OCS（根据[[7]][8]重绘）。

![单机架与OCS连接图][fig7]
*单个TPU机架与OCS连接*

这张图引发了几个问题。*为什么OCS只用于立方体的表面？* 换言之，*使用OCS有什么好处？* OCS有三大好处，我们将在下文介绍另外两个。

### OCS的好处 #1：环绕式连接（Wraparound）

**通过环绕式连接实现节点间的更快通信**

OCS也为给定的TPU配置提供了环绕式连接。这使得任意两个节点间的最坏情况通信跳数从`N-1`减少到`(N-1)/2`（每轴），因为每个轴都变成了一个环（一维环面）。

随着系统规模的扩大，这个效应变得越来越重要，因为降低芯片间通信延迟对于实现高度并行化至关重要。

### 题外话：并非所有TPU都采用3D环面拓扑

注意：老一代的TPU（如TPUv2、v3）和推理型TPU（如TPUv5e、TPUv6e）采用的是2D环面拓扑，而非下图所示的3D环面。然而，TPUv7 "Ironwood" 尽管被宣传为推理芯片，但似乎也采用了3D环面结构（注：我仅根据其宣传材料做出此推断）。

![2D环面拓扑图][fig8]
*2D环面拓扑*

## 完整Pod层面（又称“Superpod”；TPUv4为4096个芯片）

就像我们将多个芯片连接成一个TPU机架一样，我们也可以将多个机架连接起来，构成一个巨大的Superpod。

Superpod也指TPU（仅使用ICI和OCS）所能达到的最大互连芯片配置。在这之上还有一个多Pod（Multi-Pod）层面，但它需要通过速度较慢的互连方式，我们稍后会讨论。

Superpod的规模因代而异，对于TPUv4来说是4096个芯片（即64个4x4x4的机架）。对于最新的TPUv7 "Ironwood"，则是9216个芯片。

下图展示了一个TPUv4的Superpod。

![TPUv4 Superpod图][fig9]
*TPUv4 Superpod（64个机架）*

请注意每个立方体（即一个TPU机架）是如何通过OCS相互连接的。这也使得我们可以在一个Pod内划分出不同形状的TPU Slice。

### 使用OCS划分TPU Slice

我们可以在一个Pod内请求TPU的子集，这些子集就是TPU Slice。但即使你想要N个芯片，也有多种拓扑结构可供选择。

例如，假设你总共需要512个芯片。你可以请求一个**立方体形（8x8x8）**、一个**雪茄形（4x4x32）**或一个**矩形（4x8x16）**。选择Slice的拓扑结构本身就是一个超参数。

你选择的拓扑结构会影响节点间的通信带宽，而这直接关系到不同并行化方法的性能。

例如，对于**全局到全局（all-to-all）**的通信，如数据并行或张量并行，**立方体形（如8x8x8）**会是首选，因为它具有最高的**对分带宽**。然而，对于**流水线并行**，**雪茄形（如4x4x32）**可能更好，因为它可以更快地与序列中的下一层通信（假设每一层都能装入一个4x4的子切片中）。

![不同TPU拓扑示例图][fig10]
*TPU拓扑示例*

当然，最优拓扑取决于具体的模型，找到它本身就是一项工作。TPUv4的论文[[9]][9]也对此进行了测量，展示了拓扑变化如何提升吞吐量（注：我不确定第一行指的是哪种LLM架构，因为论文中未指明）。

![不同拓扑对吞吐量的提升图][fig11]
*不同拓扑对吞吐量的提升效果*

我们已经讨论了TPU Slice，但还有一个重要特性对TPU的高运行稳定性做出了贡献。

那就是，**得益于OCS，这些Slice不必由物理上连续的机架组成**。这是我们前面没有提到的OCS的第二个——也可能是最大的——好处。

### OCS的好处 #2：（可重构的）非连续多节点Slice

请注意，这与通过硬连线将多个节点连接起来以模拟非连续Slice是不同的。由于OCS是一个交换机而不是硬连线，节点间的物理线路大大减少，从而实现了更高的可扩展性（即更大的TPU Pod规模）。

这使得大规模下的节点配置变得非常灵活。例如，假设我们想在一个Pod上运行三个不同的作业。朴素的调度方法可能无法实现，但OCS连接允许我们抽象掉节点的物理位置，将整个Pod看作一个“**节点池**”（"bag of nodes"）（根据[[6]][10]重绘）。

![多作业共享Pod图][fig12]
*独立作业可将Pod中的TPU机架视为“节点池”*

这提高了Pod的利用率，并且在节点发生故障时可能使维护变得更容易。谷歌将其描述为：“**故障节点的影响范围（‘爆炸半径’）很小**”。不过，我不确定当只有部分节点需要关闭时，其液冷系统会受到怎样的影响。

最后，这种灵活的OCS还有一个有趣的延伸：我们还可以改变TPU Slice的拓扑结构，例如从一个常规环面变成一个**扭曲环面（twisted torus）**。

### OCS的好处 #3：扭曲的TPU拓扑

我们之前看到了如何通过改变（x,y,z）维度来获得固定芯片数量的不同TPU Slice拓扑。而这一次，我们将在固定的（x,y,z）维度下，改变它们的连接方式以实现不同的拓扑。

一个显著的例子是，将一个雪茄形的常规环面变成一个扭曲的雪茄形环面，如下图所示。

![常规环面 vs 扭曲环面][fig13]
*常规环面 vs 扭曲环面（来源：TPUv4论文 [[9]][11]）*

扭曲环面可以实现跨越扭曲二维平面的芯片间更快通信。这对于加速**全局到全局（all-to-all）**的通信操作尤其有用。

让我们更深入一点，想象一个具体的场景来说明它的帮助。

### 使用扭曲环面加速训练

理论上，扭曲环面对**张量并行（TP）**的增益最大，因为每个层都有多次**all-gather**和**reduce-scatter**操作。它对**数据并行（DP）**也可能带来中等程度的好处，因为每个训练步骤都有一次**all-reduce**，但频率较低。

想象一下，我们正在训练一个标准的仅解码器Transformer，并希望采用多种并行策略来加速训练。下面我们来看两种情况。

#### 场景 #1：4x4x16拓扑（TP + PP；共256个芯片）

我们将z轴作为**流水线并行（PP）**维度，我们的2D **张量并行（TP）**维度为4x4。本质上，假设第k层位于z=k，并且每一层都被分片到16个芯片上。如果未明确画出，则假设OCS为标准的近邻连接。

![4x4x16拓扑图][fig14]
*采用TP+PP的4x4x16拓扑*

我们将在每个z=k的位置扭曲这个2D环面，这将使每个TP层内的芯片间通信更快。沿着PP维度进行扭曲则没有必要，因为它们主要依赖点对点通信。

**注意**：在现实中，当芯片数量大于4x4时，扭曲环面才能带来显著好处。我们这里使用4x4仅为了方便可视化。

#### 场景 #2：16x4x16拓扑（DP + TP + PP；共1024个芯片）

作为扩展，我们将在前一个场景的基础上增加一个大小为4的**数据并行（DP）**维度。这意味着沿x轴有4个场景#1中的模型副本。

![16x4x16拓扑图][fig15]
*采用DP+TP+PP的16x4x16拓扑*

注意，扭曲环面仅限于每个DP模型副本的TP维度（即，对于每个z=k，k=1…16，都是一个4x4的2D平面）。DP维度上只有一个环绕连接，使得每一行成为一个大小为16的水平环。

你可能已经注意到，还有一种8x8x16的替代拓扑（即2x2的DP维度），但这会变得更复杂，因为我们将DP和TP维度混合在了一起。具体来说，如何为y轴构建OCS环绕连接，同时又要适应每个TP维度的扭曲环面，就变得不那么明朗了。

## 多Pod层面（又称“Multislice”；TPUv4为4096+芯片）

![多Pod示意图][fig16]

TPU层级结构的顶层是多Pod层面。在这一层，你可以将多个Pod当作一台巨大的机器来使用。然而，Pod之间的通信是通过**数据中心网络（DCN）**进行的，其带宽低于ICI。

![两Pod通过DCN连接图][fig17]
*两Pod通过DCN连接 [[1]][12]*
*展示多Pod训练如何配置的图示*

PaLM模型就是这样训练出来的。它在6144个TPUv4（2个Pod）上花费了56天。下图你可以看到6个Pod上的TPU作业分配情况：绿色代表PaLM，红色代表未分配，其余为其他作业。请注意，每个小方块都是一个4x4x4的TPU立方体。

![PaLM训练时的TPU Pod利用率][fig18]
*训练PaLM时的TPU Pod利用率 [[6]][13]*

实现这一点本身已非易事，但更令人印象深刻的是对开发者体验的关注。具体来说，是聚焦于“**我们如何才能最大程度地抽象掉模型扩展中的系统/硬件部分？**”这个问题。

谷歌的答案是，让XLA编译器负责协调大规模芯片间的通信。研究人员只需提供正确的标志（例如DP、FSDP、TP的并行维度，Slice数量等），XLA编译器就会为当前的TPU拓扑插入合适的层级化集合通信操作（Xu et al, 2021: GSPMD [[2]][14]）。其目标是，**用尽可能少的代码改动来实现大规模训练**。

例如，下面是谷歌博客[[1]][15]中对一个跨多个Slice的**all-reduce**操作的分解。

![XLA对跨Pod的all-reduce操作进行分解][fig19]
*XLA对跨Pod的all-reduce操作进行分解*

这表明XLA编译器同时负责处理Slice之间和Slice内部的通信集合操作。

举个具体的例子，训练一个模型可能采用如下的TPU拓扑。**激活值**的通信发生在Slice内部，通过ICI进行；而**梯度**的通信则发生在Slice之间，通过DCN进行（即跨越DCN DP维度）[[1]][16]。

![多Pod并行通信示意图][fig20]

## 将示意图与现实硬件对应起来

我发现，当你有实际的硬件照片时，将示意图与现实对应起来会很有帮助。下面是一个总结。

如果你看过谷歌TPU的宣传材料，可能见过下面这张图片。

![8个TPU机架][fig21]
*8个TPU机架（TPUv4）*

这是8个TPU机架，每个单元就是我们上面看到的4x4x4的3D环面网络。在每个机架中，每一行有2个托盘，意味着每行有8个TPU芯片。

下面是一个单独的TPUv4托盘：

![TPUv4托盘实物图][fig22]

注意，上文的示意图简化为只有一个PCIe端口，但实际的托盘上有4个PCIe端口（在左侧）——每个TPU一个。

下面是一个单独的芯片：

![TPUv4芯片实物图][fig23]
*TPUv4芯片，中间是ASIC，周围是4个HBM堆栈*

中间部分是ASIC，周围的4个块是HBM堆栈。我们看到的是TPUv4，它内部有2个张量核心，因此总共有4个HBM堆栈。

我没能找到TPUv4的芯片布局图（floorplan），所以这里用TPUv4i的来代替，它很相似，只是因为它是一个推理芯片，所以只有1个张量核心[[3]][17]。

![TPUv4i芯片布局图][fig24]

注意，在TPUv4i的布局上，CMEM占据了相当大的空间。

## 致谢

感谢谷歌TPU研究云（TRC）项目提供的TPU支持！

好的，这是对Hacker News上关于《TPU Deep Dive》文章讨论的总结，可以作为文章译文后的“Hacker News网友热议”部分。

---

## Hacker News 网友热议

这篇文章在 [Hacker News](https://news.ycombinator.com/item?id=44342977) 上引发了热烈的技术和商业讨论。网友们从硬件对比、商业策略、技术优势等多个角度分享了他们的见解。

### 1. 硬件之争：TPU vs. GPU vs. FPGA

讨论从一个有趣的比较开始：**为什么不拿TPU和FPGA（现场可编程门阵列）比？**

- **FPGA的优势**：有网友指出，FPGA可以为任何数据处理任务构建完全流水线的系统，而不仅限于SIMD（单指令多数据流）。其上的每个处理单元（如DSP slice）都能独立工作，理论上可以实现100%的吞吐率，没有内存和缓存开销。

-  **ASIC的压倒性优势**：但其他人很快反驳，FPGA只适合小批量生产。对于谷歌这样规模的公司，开发专用ASIC（如TPU）的成本很快就能被收回。一个绝妙的比喻是：**TPU之于FPGA，就像“注塑件”之于“3D打印件”**。 此外，近年来FPGA在制程工艺上落后于尖端ASIC，导致性能和能效差距越来越大。
-  **结论**：当你有能力做ASIC时，就应该做ASIC。不过最初提问的网友也补充说，与TPU相比，GPU在某种意义上也不是针对AI的“真·ASIC”，因此硬件对比的维度很丰富。

### 2. 谷歌的商业策略：为什么不直接出售TPU？

这是讨论最激烈的话题。一位网友提出了一个核心困惑：如果TPU能与英伟达的芯片竞争，为什么谷歌不直接出售它们，从而在市值上分一杯羹？

-   **保持核心竞争优势**：最普遍的观点是，TPU是谷歌云和内部AI产品的护城河。通过出租算力而非出售硬件，谷歌能将最先进的技术保留给自己，避免为竞争对手（如其他云服务商或AI公司）提供助力。
-   **商业模式与利润**：直接销售硬件需要建立庞大的销售、支持和维护体系。相比之下，通过云平台出租TPU算力的利润率更高，也更符合谷歌现有的商业模式。
-   **生态系统与估值复杂性**：有网友指出，不应简单地将谷歌（一家综合性科技公司）的市值与英伟达（一家芯片公司）直接对比。还有人提到，TPU的成功也离不开其合作伙伴**博通（Broadcom）**，其市值也相当高。这个生态系统的总价值才能更全面地反映TPU的地位。
-   **长期布局 vs. 当前炒作**：部分网友认为，英伟达的市值包含了大量炒作成分。而谷歌通过自研TPU，主要是在进行一项长期的成本节约和战略投资，其价值将在未来AI大规模盈利时才完全显现。

### 3. TPU的技术优势与适用场景

-   **什么算法适合TPU？**：网友们确认，TPU的脉动阵列（systolic array）特别适合**密集的矩阵乘法**（Dense Matmul）和卷积。进一步地，像SVD（奇异值分解）、部分线性方程组求解（如GMRES）等算法，因为其核心计算可以分解为大量的矩阵乘法，所以在TPU上也能高效运行。大家推荐了 **[The Scaling Book by JAX-ML](https://jax-ml.github.io/scaling-book/)**作为理解算法如何映射到TPU硬件的最佳参考。
-   **性能确定性（Performance Determinism）**：一位来自Groq（一家研发类似TPU架构芯片的公司）的网友给出了深刻的见解。TPU和GPU都能保证在给定随机种子的情况下输出确定的*结果*。但TPU的核心优势在于**性能的确定性**——即任务执行的周期数是可预测的。这是因为TPU依赖“足够聪明的编译器”在运行前就安排好所有计算和数据流。相比之下，GPU拥有复杂的片上硬件调度器，这使其更灵活，但也带来了性能上的不确定性。
-   **全栈控制力**：有评论一针见血地指出，TPU成功的关键在于谷歌**控制了从芯片、编译器、运行时到互联网络的整个垂直堆栈**。这种端到端的控制消除了大量不确定性，使得在数据中心规模上进行高效、可预测的作业调度成为可能，这是其他公司难以复制的。

### 4. 其他有趣讨论

-   **作者如何了解这么多内部信息？**：大家猜测作者可能通过谷歌的**TRC研究员计划**或GCP平台接触到了TPU。同时，谷歌公开发表的论文、开源的JAX和XLA代码库也揭示了大量关于TPU工作原理的线索。
-   **硬件细节**：有眼尖的网友在TPU托盘的液冷管线上发现了一个疑似**步进电机**的部件，并对其用途（是泵还是计量阀）感到好奇，感叹其设计的精妙。
-   **浮点数误差**：在讨论LLM的确定性时，有网友补充了一个细节：在分布式训练中，由于浮点数加法的顺序不同，会导致微小的精度差异，这给模型的完全可复现性带来了现实挑战。


## 芯海回响：交流与展望

这篇文章从硬件架构到软件协同，为我们描绘了一幅TPU如何通过“专精”路线实现极致扩展性和能效的宏伟蓝图。现在，我们想听听你的声音：

*   **专用 vs 通用**：TPU的专用设计和GPU的通用灵活性，你认为哪种路线更能代表AI硬件的未来？在你的工作或研究中，更倾向于使用哪种加速器，为什么？
*   **生态博弈**：文章强调了XLA编译器与TPU硬件的协同设计。你认为像CUDA这样成熟开放的生态系统，与TPU这种软硬件深度绑定的封闭生态系统相比，各自的优劣势在未来会如何演变？
*   **未来的挑战**：随着模型越来越趋向于稀疏化（如混合专家模型MoE），你认为基于脉动阵列的TPU将如何应对这一挑战？谷歌会推出新的硬件设计，还是通过编译器技术来弥补？

欢迎在评论区分享你的洞见、经验和大胆的预测！



[fig1]: https://henryhmko.github.io/posts/tpu/images/single_chip.png
[fig2]: https://henryhmko.github.io/posts/tpu/images/systolic_arr.png
[fig3]: https://henryhmko.github.io/posts/tpu/images/pipeline_pointwise.gif
[fig4]: https://henryhmko.github.io/posts/tpu/images/patterson_breakdown.png
[fig5]: https://henryhmko.github.io/posts/tpu/images/tray.png
[fig6]: https://henryhmko.github.io/posts/tpu/images/tpu_racks.png
[fig7]: https://henryhmko.github.io/posts/tpu/images/rack_ocs.png
[fig8]: https://henryhmko.github.io/posts/tpu/images/torus_2d.png
[fig9]: https://henryhmko.github.io/posts/tpu/images/full_pod.png
[fig10]: https://henryhmko.github.io/posts/tpu/images/diff_topo.png
[fig11]: https://henryhmko.github.io/posts/tpu/images/diff_topo_fig.png
[fig12]: https://henryhmko.github.io/posts/tpu/images/multijob.png
[fig13]: https://henryhmko.github.io/posts/tpu/images/twisted_torus.png
[fig14]: https://henryhmko.github.io/posts/tpu/images/twisted_scenario_1.png
[fig15]: https://henryhmko.github.io/posts/tpu/images/twisted_scenario_2.png
[fig16]: https://henryhmko.github.io/posts/tpu/images/multipod.png
[fig17]: https://henryhmko.github.io/posts/tpu/images/multipod_dcn.png
[fig18]: https://henryhmko.github.io/posts/tpu/images/palm_train.gif
[fig19]: https://henryhmko.github.io/posts/tpu/images/xla_reduce.jpg
[fig20]: https://henryhmko.github.io/posts/tpu/images/multipod_many.png
[fig21]: https://henryhmko.github.io/posts/tpu/images/tpu_racks.png
[fig22]: https://henryhmko.github.io/posts/tpu/images/tpu_tray.png
[fig23]: https://henryhmko.github.io/posts/tpu/images/tpu_chip.png
[fig24]: https://henryhmko.github.io/posts/tpu/images/tpuv4i_layout.png

[1]: https://henryhmko.github.io/posts/tpu/tpu.html#ref4
[2]: https://henryhmko.github.io/posts/tpu/tpu.html#ref18
[3]: https://henryhmko.github.io/posts/tpu/tpu.html#ref3
[4]: https://henryhmko.github.io/posts/tpu/tpu.html#ref16
[5]: https://henryhmko.github.io/posts/tpu/tpu.html#ref3
[6]: https://henryhmko.github.io/posts/tpu/tpu.html#ref7
[7]: https://henryhmko.github.io/posts/tpu/tpu.html#ref9
[8]: https://henryhmko.github.io/posts/tpu/tpu.html#ref7
[9]: https://henryhmko.github.io/posts/tpu/tpu.html#ref9
[10]: https://henryhmko.github.io/posts/tpu/tpu.html#ref6
[11]: https://henryhmko.github.io/posts/tpu/tpu.html#ref9
[12]: https://henryhmko.github.io/posts/tpu/tpu.html#ref1
[13]: https://henryhmko.github.io/posts/tpu/tpu.html#ref6
[14]: https://henryhmko.github.io/posts/tpu/tpu.html#ref2
[15]: https://henryhmko.github.io/posts/tpu/tpu.html#ref1
[16]: https://henryhmko.github.io/posts/tpu/tpu.html#ref1
[17]: https://henryhmko.github.io/posts/tpu/tpu.html#ref3
[18]: https://cloud.google.com/blog/products/compute/using-cloud-tpu-multislice-to-scale-ai-workloads
[19]: https://arxiv.org/pdf/2105.04663
[20]: https://gwern.net/doc/ai/scaling/hardware/2021-jouppi.pdf
[21]: https://jax-ml.github.io/scaling-book/tpus/
[22]: https://fleetwood.dev/posts/domain-specific-architectures#google-tpu
[23]: https://hc2023.hotchips.org/assets/program/conference/day2/ML%20training/HC2023.Session5.ML_Training.Google.Norm_Jouppi.Andy_Swing.Final_2023-08-25.pdf
[24]: https://cloud.google.com/tpu/docs/v4
[25]: https://arxiv.org/abs/1704.04760
[26]: https://arxiv.org/abs/2304.01433
[27]: https://www.youtube.com/watch?v=0yPFBxkOKRY
[28]: https://hc33.hotchips.org/assets/program/tutorials/HC2021.Google.Sameer%20Kumar.pdf
[29]: https://hc32.hotchips.org/assets/program/tutorials/HC2020.Google.SameerKumarDehaoChen.v02.pdf
[30]: https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/
[31]: https://old.hotchips.org/hc31/HC31_T3_Cloud_TPU_Codesign.pdf
[32]: https://www.youtube.com/watch?v=XkgtANeDrm8
[33]: https://www.cs.ucla.edu/wp-content/uploads/cs/PATTERSON-10-Lessons-4-TPU-gens-CO2e-45-minutes.pdf
[34]: https://personales.unican.es/vallejoe/Publications/C%C3%A1mara%20-%20TPDS'10%20-%20Twisted%20Torus%20Topologies%20for%20Enhanced%20Interconnection%20Networks.pdf
[35]: https://gwern.net/doc/cs/hardware/2014-horowitz-2.pdf
