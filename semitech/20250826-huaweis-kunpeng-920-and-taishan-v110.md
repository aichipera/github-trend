> **译者注**
> 华为鲲鹏920发布于2019年初，是其在面临外部技术压力下，加速自主研发之路上的关键一步。本文作者在2025年对其进行[深度技术剖析](https://chipsandcheese.com/p/huaweis-kunpeng-920-and-taishan-v110)，视角独特。鲲鹏920不仅是华为首款自研的服务器CPU核，更承载了构建自主可控计算生态的重任。尽管在单核性能上与同时期顶级产品存在差距，但其在多核、能效及创新的Chiplet和小核集群设计上的探索，为后续产品迭代和整个国产服务器芯片产业的发展奠定了坚实基础，其战略意义远超单纯的性能跑分。

---

# [深入解析华为鲲鹏920及其泰山v110 CPU架构](20250826-huaweis-kunpeng-920-and-taishan-v110.mp3)

### 探究华为独特的L3缓存设计及其首款自研核心

> 原文: Chester Lam, 2025年7月22日, https://chipsandcheese.com/p/huaweis-kunpeng-920-and-taishan-v110

华为是中国最大的科技公司之一，其企业产品线覆盖了从服务器到网络设备的方方面面。所有这些产品都需要先进的芯片来保持竞争力。为此，华为通过其子公司海思（HiSilicon）投入巨资研发自有芯片，这既能让华为根据自身需求定制芯片设计，又能保障其业务免受供应链中断的风险。鲲鹏920（Kunpeng 920）就是一款基于Chiplet（芯粒）的CPU设计，旨在面向云服务器、AI加速器和无线基站等多种企业级应用。

在本文中，我们将深入探究一块华为网卡中所搭载的24核鲲鹏920 CPU子系统。

[![](https://substackcdn.com/image/fetch/$s_!o1U3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc70063cb-bc34-45de-b3d6-e5e3525c6f67_790x523.png)](https://substackcdn.com/image/fetch/%24s_%21o1U3%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/c70063cb-bc34-45de-b3d6-e5e3525c6f67_790x523.png)
<center>图片来源：华为研究出版物³</center>

特别感谢 Brutus 为本次测试所做的准备工作！

## 系统架构

鲲鹏920采用台积电（TSMC）的CoWoS封装技术，将多个Die（裸片）整合在一起，实现了海思所谓的“乐高式生产”。海思的Chiplet策略是使用等高的裸片并排摆放，计算裸片（Compute Die）居中，IO裸片（IO Die）置于两侧。计算裸片被称为“超级CPU集群”（SCCL），其顶部和底部分布着DDR4控制器，从而将芯片所有的边缘区域都用于片外接口。SCCL采用台积电的7nm工艺制造，最多包含32个泰山v110（TaiShan v110）CPU核心及L3缓存。独立的IO裸片则使用台积电16nm节点，负责连接PCIe、SATA和其他低速IO。所有裸片都安放在一个65nm的中介层（Interposer）之上。

> 裸片间的带宽能够达到400 GB/s，并支持一致性。
>
> *——《鲲鹏920：首款面向云服务的7nm、基于Chiplet的64核ARM SoC》*

海思的“乐高式生产”与英特尔的Chiplet策略有异曲同工之妙，后者同样强调高跨裸片带宽，但代价是更昂贵的封装技术和更严格的裸片间距限制。与英特尔的Sapphire Rapids类似，将内存控制器放置在CPU裸片上，使得核心数较少的SKU（产品型号）也能够直接访问DRAM，无需通过另一个Chiplet来路由内存请求。Sapphire Rapids利用其高跨裸片带宽，使其多裸片配置在软件层面看起来像一个单片（Monolithic）设计。L3和DRAM资源可以在裸片间无缝共享，这与NUMA（非一致性内存访问）架构形成了鲜明对比，后者需要软件来处理不同的内存池。但奇怪的是，我未能找到任何证据表明鲲鹏920能够在多个SCCL之间整合L3和DRAM资源。

[![](https://substackcdn.com/image/fetch/$s_!T-EC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e257a03-81dc-4693-90fc-55c7f5f862c9_1244x664.png)](https://substackcdn.com/image/fetch/%24s_%21T-EC%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/7e257a03-81dc-4693-90fc-55c7f5f862c9_1244x664.png)
<center>一篇论文中的图示⁴，显示裸片被呈现为不同的NUMA节点。其他来源的numactl输出示例也显示每个裸片作为一个独立的节点。</center>

鲲鹏920通过华为自家的“Hydra”互连技术支持双路和四路配置，这有助于进一步扩展核心数量。同时期拥有相似单路核心数的服务器处理器，如Ampere Altra和AMD的Zen 2，仅支持双路配置。

### 计算裸片拓扑与L3缓存

在一个SCCL计算裸片内，泰山v110核心被分组成四核CPU集群（CCL）。一条双向环形总线（Ring Bus）连接着计算裸片上的各个模块，包括CPU集群、L3数据banks、内存控制器以及连接其他裸片的链路。L3数据banks与CPU集群配对，但它们似乎位于独立的环形总线站点（ring stop），而非像Intel和AMD的设计那样与CPU集群共享一个站点。一个满配的SCCL拥有八个CPU集群，共计21个环形总线站点。我们测试的这个24核SKU很可能禁用了两个CPU集群及其对应的L3 banks，不过目前尚不清楚这些环形总线站点是否依然保持活动状态。

[![](https://substackcdn.com/image/fetch/$s_!9aLv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67671ec9-f29d-4dab-9e71-9130be53e49d_1223x785.png)](https://substackcdn.com/image/fetch/%24s_%219aLv%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/67671ec9-f29d-4dab-9e71-9130be53e49d_1223x785.png)

一个不同寻常的设计是，华为将L3标签（L3 tags）放置在CPU集群侧，而不是L3数据banks侧。此外，L3缓存还可以在不同模式下运行。“共享”（Shared）模式的行为类似于AMD、Arm和Intel芯片上的L3，将所有L3 banks组合成一个大型共享缓存。在这种模式下，物理地址空间大概率是被哈希到各个L3 banks上的，从而均匀分配访问请求以扩展带宽，同时避免数据重复。而“私有”（Private）模式则使一个L3 bank专属于距离最近的CPU集群，通过大幅减少互连路径的参与来提升L3性能。第三种“分区”（Partition）模式可以动态调整每个核心集群的私有L3容量。华为的论文暗示，分区模式还可以动态调整L3策略，在共享和私有模式间切换，以应对不同任务、甚至同一任务的不同阶段对私有或共享L3行为的偏好。

[![](https://substackcdn.com/image/fetch/$s_!Ftec!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82d85077-201a-4bb1-8f6c-8b52c9cee5ee_606x544.png)](https://substackcdn.com/image/fetch/%24s_%21Ftec%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/82d85077-201a-4bb1-8f6c-8b52c9cee5ee_606x544.png)
<center>来源：华为论文³</center>

分区模式是默认设置，也是我们测试系统上唯一可用的模式。一些鲲鹏920系统允许在BIOS中设置L3缓存策略，但我们的测试系统没有BIOS界面，并且缓存控制设置也未通过UEFI变量暴露出来。在分区模式下，单个核心在访问接近4MB的数据时，能观测到相当不错的36个周期的L3延迟。随着测试数据量的增大，私有L3部分扩展到包含邻近的L3切片（slice），延迟也随之逐渐增加。最终，当测试数据量接近L3总容量时，延迟超过了90个周期。

[![](https://substackcdn.com/image/fetch/$s_!sxUH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fa180da-8562-4f1a-a3f8-4b8fc1b9aedd_1600x727.png)](https://substackcdn.com/image/fetch/%24s_%21sxUH%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/5fa180da-8562-4f1a-a3f8-4b8fc1b9aedd_1600x727.png)
<center>为简化测试使用了索引寻址，若换用简单寻址，延迟可减去约1.5个周期（~0.58 ns）。</center>

如果让另一个核心遍历相同的测试数组，L3延迟在其整个容量范围内都变得非常高。即使测试数组仅略微超出L2的范围，延迟也会达到90多个周期的水平，这表明L3此时正以共享模式运行。令人惊讶的是，即使是同一集群内的两个核心共享数据，也会触发类似的行为。或许当缓存行（cacheline）处于共享状态时，L3会进入共享模式，或者说它无法在集群的私有L3分区内缓存处于共享状态的数据行。

[![](https://substackcdn.com/image/fetch/$s_!Zk6c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c65d852-a701-4458-adda-85363250497b_486x634.png)](https://substackcdn.com/image/fetch/%24s_%21Zk6c%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/4c65d852-a701-4458-adda-85363250497b_486x634.png)

这并非总是最优策略。例如，两个核心共享一个2MB的数组，如果能将该数组保留在各自的私有L3分区内，效果会更好。只要L3本身没有容量压力，数据重复就不是问题。对于集群内数据共享缺乏特殊处理也让人费解。

[![](https://substackcdn.com/image/fetch/$s_!3WLu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b87e39a-c137-48eb-b500-e513b1ed5ff3_1600x747.png)](https://substackcdn.com/image/fetch/%24s_%213WLu%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/7b87e39a-c137-48eb-b500-e513b1ed5ff3_1600x747.png)

从一个角度看，鲲鹏920的分区模式是一个优势，因为它利用了L3 banks离某些核心更近的物理位置。AMD、Intel和大多数Arm芯片的L3本质上也存在这种非一致性延迟特性，但它们并未尝试将L3数据放置在离使用它的核心更近的位置。然而，从另一个角度看，分区模式似乎是为了弥补其互连性能的不足。当L3以共享模式运行，或单个核心需要使用整个L3时，鲲鹏920的L3延迟比Intel的Sapphire Rapids更差。考虑到每个核心只有512 KB的L2缓存，这种表现堪称惨烈。我更倾向于后一种观点，因为即使是核心私有访问最近的L3切片，其周期数延迟也与Zen 2的L3相当，而后者是将访问请求分散到所有L3 banks的。Zen 2在共享或私有读取模式下，都能在整个L3容量范围内保持一致的低延迟。因此，鲲鹏920的分区模式最好被看作是一种有时能掩盖其高延迟互连的机制。

[![](https://substackcdn.com/image/fetch/$s_!u45P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F448038f4-17c2-4d4f-909d-8b3fae135a86_1600x728.png)](https://substackcdn.com/image/fetch/%24s_%21u45P%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/448038f4-17c2-4d4f-909d-8b3fae135a86_1600x728.png)

一个四核的泰山v110集群可以实现21.7 GB/s的L3读取带宽，因此鲲鹏920在集群级别存在带宽瓶颈，这与Intel的E-Core集群非常相似。然而，鲲鹏920的带宽瓶颈更为严重。来自集群内兄弟核心的带宽争用，可能导致L3延迟超过80 ns。Intel的设计（以Skymont测试为例）也会出现延迟增加的情况，但其总体延迟更低，带宽更高。

[![](https://substackcdn.com/image/fetch/$s_!NSCx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d967ef5-3713-4e33-8e81-90f4a97087bd_1041x600.png)](https://substackcdn.com/image/fetch/%24s_%21NSCx%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/9d967ef5-3713-4e33-8e81-90f4a97087bd_1041x600.png)

DRAM访问由位于计算裸片顶部和底部的两对双通道DDR4控制器提供，在我们的测试设置中，连接的是32 GB的DDR4-2400内存。使用只读模式测得的读取带宽为63 GB/s。对于服务器芯片而言，96 ns的空载延迟表现不错，但在中等带宽负载下，延迟会迅速攀升至100 ns以上。当推至带宽极限时，延迟可能超过300 ns。虽然不算出色，但比高通Centriq那接近600 ns的延迟控制得要好。

[![](https://substackcdn.com/image/fetch/$s_!Vk7r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17ac7fa2-08ba-4fda-b303-99d9bef4a92a_1600x772.png)](https://substackcdn.com/image/fetch/%24s_%21Vk7r%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/17ac7fa2-08ba-4fda-b303-99d9bef4a92a_1600x772.png)

### 核间延迟测试

在一个四核集群内进行缓存行传递时，鲲鹏920的延迟表现尚可。但跨集群访问会产生显著更高的延迟，并且延迟大小可能取决于共享缓存行的归属位置（homed）。

[![](https://substackcdn.com/image/fetch/$s_!c1TO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07ae20e7-0280-4a7b-b086-8daa12fad30f_997x518.png)](https://substackcdn.com/image/fetch/%24s_%21c1TO%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/07ae20e7-0280-4a7b-b086-8daa12fad30f_997x518.png)

与AMD的Zen 2（至少在桌面平台上）相比，鲲鹏920的集群内和跨集群延迟都更高。

[![](https://substackcdn.com/image/fetch/$s_!grrM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F805776d2-1a3e-486e-95e6-ae64bc16d3bb_1319x679.png)](https://substackcdn.com/image/fetch/%24s_%21grrM%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/805776d2-1a3e-486e-95e6-ae64bc16d3bb_1319x679.png)

缓存到缓存的传输在实际应用中很少见，我进行这项测试主要是为了展示系统拓扑，并为缓存一致性的实现方式提供线索。核间延迟不太可能对应用性能产生重大影响。

## 泰山v110核心概览

海思的泰山v110是一款64位ARM（aarch64）核心，具备4发射乱序执行能力。这是华为首款自研核心设计。虽然华为之前曾在服务器SoC中使用过Arm的Cortex A57和A72，但泰山v110似乎与那些旧的Arm设计没有太多共同之处。

[![](https://substackcdn.com/image/fetch/$s_!SiUx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd166b08c-371f-43fe-94d7-76056fc9b7af_780x1005.png)](https://substackcdn.com/image/fetch/%24s_%21SiUx%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/d166b08c-371f-43fe-94d7-76056fc9b7af_780x1005.png)

该核心的重排序能力（reordering capacity）中等，拥有三个整数ALU（算术逻辑单元）、一个双流水线FPU（浮点单元），并且每个周期可以处理两个内存操作。它大致可以与几年前Intel的Goldmont Plus相提并论，但比Goldmont Plus稍大一些，并且得益于一个强大得多的服务器级内存子系统。另一个比较对象是Arm的Neoverse N1，因为它也是一款在台积电7nm节点上实现、针对密度优化的aarch64核心。Neoverse N1同样是4发射，但其乱序引擎规模稍大。

### 分支预测

华为的公开资料称，泰山v110采用“两级动态分支预测器”。两级预测利用分支地址和之前的分支结果来索引一个预测分支结果的表格。这是一种相对简单的预测算法，在2010年代左右逐渐在高性能设计中失宠。华为也可能指的是一种“两级”BTB（分支目标缓冲）设置，或者是一个创建了两个覆盖级别的子预测器。通过一个简单的测试（使用不同长度随机模式的条件跳转，跳转或不跳转），泰山v110的行为有点像Arm的Cortex A73。

[![](https://substackcdn.com/image/fetch/$s_!hnGH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6de38300-8412-4388-9096-ecf1855860d0_1600x849.png)](https://substackcdn.com/image/fetch/%24s_%21hnGH%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/6de38300-8412-4388-9096-ecf1855860d0_1600x849.png)

一个64项的BTB能以单周期延迟提供已跳转分支的目标地址，从而实现零气泡（zero-bubble）的跳转。超出这个范围后，只要代码能装入32KB并且分支间隔不太近，分支预测器能以3周期延迟处理分支。分支间隔为16字节或更小时会产生一个额外的惩罚周期，更密集的分支则表现不佳。代码超出L1指令缓存（L1i）会急剧增加跳转延迟。当每64字节缓存行有一个分支时，从L2获取的延迟达到11-12个周期，而当代码必须从L3获取时，延迟甚至超过38个周期。这大致与数据侧L2和私有L3的延迟相符，表明分支预测器无法领先于指令获取的其他部分来驱动预取。

[![](https://substackcdn.com/image/fetch/$s_!tQUG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90a8aa9d-486c-4371-ad40-5aff254d3701_1313x644.png)](https://substackcdn.com/image/fetch/%24s_%21tQUG%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/90a8aa9d-486c-4371-ad40-5aff254d3701_1313x644.png)

一个31项的返回栈（return stack）负责处理返回指令。对于更普遍的间接分支，一个间接预测器可以为每个分支追踪多达16个目标，或者在出现显著惩罚之前，总共能追踪约256个间接目标。

[![](https://substackcdn.com/image/fetch/$s_!Nx-9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89b51fdd-ff76-45d8-a939-c3450e0640a0_1198x857.png)](https://substackcdn.com/image/fetch/%24s_%21Nx-9%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/89b51fdd-ff76-45d8-a939-c3450e0640a0_1198x857.png)

在SPEC CPU2017测试中，其分支预测准确率大致与Intel的Goldmont Plus相当，尽管Goldmont Plus以微弱优势胜出。同时期AMD的Zen 2表现更强，展示了台积电7nm节点上高性能核心应有的水平。

[![](https://substackcdn.com/image/fetch/$s_!nDdS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F553250dd-9dbe-4f0e-bcda-9cf18cb1cb76_1011x1600.png)](https://substackcdn.com/image/fetch/%24s_%21nDdS%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/553250dd-9dbe-4f0e-bcda-9cf18cb1cb76_1011x1600.png)

### 指令获取

泰山v110拥有一个64 KB的指令缓存，每周期可向核心提供四条指令。指令侧地址转换使用一个32项的iTLB，其后备是一个1024项的L2 TLB。该L2 TLB可能与数据访问共享，但我目前没有编写测试来验证这一点。当代码溢出L1i时，指令获取带宽急剧下降，平均每周期只有6-7字节。这使得从L2读取代码的带宽比Intel的Goldmont Plus或Arm的Neoverse N1稍差。从L3获取代码的带宽非常糟糕，几乎和Goldmont Plus或Neoverse N1从DRAM获取指令一样差。

[![](https://substackcdn.com/image/fetch/$s_!SO9d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60b1c81d-b423-4551-8d0e-357b35205760_1600x715.png)](https://substackcdn.com/image/fetch/%24s_%21SO9d%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/60b1c81d-b423-4551-8d0e-357b35205760_1600x715.png)

指令由一个4发射的解码器解码，并翻译成微操作（micro-ops）。然后，核心进行寄存器重命名并分配其他后端资源来跟踪它们，以实现乱序执行。重命名器可以执行移动消除（move elimination）。

### 执行引擎

泰山v110采用基于物理寄存器文件（PRF-based）的执行方案，其中寄存器值存储在物理寄存器文件中，而其他结构则存储指向这些寄存器文件条目的指针。重排序缓冲（Reorder buffer）的容量与Intel的Goldmont Plus相似，但泰山v110更大的整数寄存器文件和内存排序队列应该使其更具优势。调度器（scheduler）的布局将微操作分为ALU、内存访问和FP/向量三类，并为每一类使用一个独立的统一调度器。每个调度器大约有33个条目。Goldmont Plus在整数侧使用分布式调度器布局，而Arm的Neoverse N1则使用纯粹的分布式调度器布局。

[![](https://substackcdn.com/image/fetch/$s_!qEWd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fa2a6b3-a421-4d02-8218-502993a3bcf8_1717x488.png)](https://substackcdn.com/image/fetch/%24s_%21qEWd%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/7fa2a6b3-a421-4d02-8218-502993a3bcf8_1717x488.png)

SPEC CPU2017的工作负载给泰山v110的调度器带来了巨大压力。调度器条目在任何核心上通常都是“热门”资源，所以这并不奇怪。整数寄存器文件的容量很少成为问题，因为该核心的整数寄存器几乎足以覆盖ROB的容量。泰山v110在一个独立的寄存器文件中对标志位（条件码）进行重命名，大约有31个重命名可用。标志位重命名也基本不成问题，除非在分支非常密集的负载中，如文件压缩和505.mcf。

[![](https://substackcdn.com/image/fetch/$s_!zORv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d2b087b-9bc6-4e9e-a170-8441c1faccfd_1104x577.png)](https://substackcdn.com/image/fetch/%24s_%21zORv%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/2d2b087b-9bc6-4e9e-a170-8441c1faccfd_1104x577.png)

浮点工作负载除了给FPU的调度器带来压力外，还会对FP/向量寄存器文件造成压力。泰山v110的FP/向量寄存器文件容量可能与Goldmont Plus相似，但由于aarch64定义了32个FP/向量寄存器（x86-64为16个），可用于重命名的寄存器更少。更大的寄存器文件将有助于更好地平衡核心在FP和向量工作负载下的表现。

#### 执行端口

泰山v110的整数执行侧有四个端口。三个是通用ALU，处理简单的常见操作，如整数加法和位运算。分支可以走其中两个端口，但与同时代其他核心一样，该核心每周期只能维持一个已跳转的分支。第四个端口专门用于多周期整数操作，如乘法和除法。整数乘法的执行延迟为四个周期。Goldmont Plus和Neoverse N1同样采用3+1的整数端口配置，但它们都将分支放在第四个端口，而不是用它来执行多周期操作。将分支放在第四个端口可能对吞吐量略有好处，因为分支通常比多周期操作更常见。将分支放在专用端口上也能自然地赋予它们高优先级，因为没有其他指令类别与它们竞争同一个端口。这有助于更快地发现错误预测，减少无效功耗。另一方面，泰山v110的布局可能通过按延迟特性对端口进行分组，从而简化了调度。

泰山v110的FPU有两个端口，这在当时期的低功耗和密度优化设计中很常见。两个端口都能处理128位向量长度的浮点融合乘加（FMA）操作（FP32）。FP64操作的执行速率为四分之一。FP32 FMA操作的延迟为5个周期。奇怪的是，FP32加法和乘法每个只能由一个端口处理，尽管它们的延迟与FMA操作一样都是5个周期。向量整数加法可以使用两个端口，延迟为2个周期。只有一个端口有向量整数乘法器。

### 加载/存储

两个AGU（地址生成单元）端口生成内存地址，对于L1D（一级数据缓存）命中，提供4周期的加载到使用（load-to-use）延迟。使用索引寻址时，延迟会增加1-2个周期。来自AGU的虚拟地址由一个32项全相联的数据TLB转换为物理地址。一个1024项的L2 TLB负责处理更大的内存足迹。命中L2 TLB会增加11个周期的延迟，对于一个低时钟频率的核心来说，这算比较慢了。AMD的Zen 2和Intel的Goldmont Plus的L2 TLB延迟分别为7和8个周期。值得注意的是，Zen 2的TLB容量是其两倍，达到2048项，并且能达到高得多的时钟速度。

[![](https://substackcdn.com/image/fetch/$s_!YXIE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20615c9f-4217-4be3-8b97-7830e9a3fa85_1600x776.png)](https://substackcdn.com/image/fetch/%24s_%21YXIE%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/20615c9f-4217-4be3-8b97-7830e9a3fa85_1600x776.png)

加载地址必须与之前的存储地址进行检查，以检测内存依赖关系。存储转发（Store forwarding）的延迟为6-7个周期，值得称道的是，即使当一个存储只部分重叠于随后的加载时，这个延迟也能保持。该核心的L1D似乎在16字节对齐的块上操作。当跨越16字节边界时，转发延迟会增加1-2个周期。只要加载和存储都不跨越16字节边界，它们就可以并行进行。

泰山v110的64 KB数据缓存是4路组相联的，每周期可处理两个128位的访问。这两个访问都可以是加载，其中一个可以是存储。其数据缓存带宽优于Intel的Goldmont Plus，后者每周期也能进行两次128位访问，但仅限于一次加载和一次存储。加载操作通常远多于存储操作，因此泰山v110在实践中应该具有带宽优势。Neoverse N1作为一款更新的密度优化设计，其L1D带宽与泰山v110相似。

### L2缓存

泰山v110的L2缓存容量为512 KB，为每个核心私有。尽管核心以四核集群的方式排列，但并没有像Intel E-Cores那样的集群级共享缓存。L2的延迟为10个周期，以周期数计算，比Neoverse N1或Zen 2更快。

[![](https://substackcdn.com/image/fetch/$s_!zHk2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8af8f797-fbb0-4e23-9315-f63633000386_1600x712.png)](https://substackcdn.com/image/fetch/%24s_%21zHk2%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/8af8f797-fbb0-4e23-9315-f63633000386_1600x712.png)

L2平均每周期可提供约20字节的数据，这表明核心的L2和L1D之间可能有一个每周期32字节的接口。使用读-改-写模式并没有增加带宽，所以L2到L1D的接口可能不是双向的。尽管如此，考虑到该核心拥有较大的L1D和中等的向量能力，L2带宽是足够充裕的。

泰山v110的L2似乎是为了追求高性能而牺牲了容量。Goldmont Plus则采取了相反的设计，使用了一个巨大的4 MB共享L2，因为其L2也充当了末级缓存。华为可能希望依靠动态L3分区来降低平均L2未命中延迟，从而让L2的设计可以专注于速度。

## 性能表现：SPEC CPU2017

华为选择SPEC CPU2017的整数套件作为评估泰山v110的指标，因为其目标市场包括了“涉及大量整数运算”的工作负载。在单核测试中，泰山v110分别领先Arm的Cortex A72和Intel的Goldmont Plus 22.5%和7%。毫无疑问，它比前几代的核心要好。但考虑到泰山v110在制程节点、更大的末级缓存和更好的DRAM控制器方面的优势，其对Goldmont Plus的领先优势并不算大。

[![](https://substackcdn.com/image/fetch/$s_!TPyT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb7bd629-e208-4f0f-8029-373e63066174_1003x777.png)](https://substackcdn.com/image/fetch/%24s_%21TPyT%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/fb7bd629-e208-4f0f-8029-373e63066174_1003x777.png)

与同为台积电7nm工艺的同辈相比，泰山v110的处境就比较艰难了。Arm的Neoverse N1比泰山v110快52.2%。AMD的Zen 2则大幅领先，但这对于一款高性能设计来说是意料之中的。

[![](https://substackcdn.com/image/fetch/$s_!HjhK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61edee50-031b-471a-a016-07c8eef38ead_852x1600.png)](https://substackcdn.com/image/fetch/%24s_%21HjhK%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/61edee50-031b-471a-a016-07c8eef38ead_852x1600.png)

虽然泰山v110总体上优于Goldmont Plus，但在505.mcf、525.x264和503.bwaves这几个项目上落后了。在这三个测试中，泰山v110每条指令的错误预测次数更多，分支预测准确率也更差。不知何故，这些测试对泰山v110的预测器构成了挑战，尽管在其他同样考验分支预测器的子测试（如541.leela）中，它的分支预测器取得了与Goldmont Plus相当的准确率。

[![](https://substackcdn.com/image/fetch/$s_!MEJE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde69ecce-f662-49c9-94cb-ab2f0c3bbef0_752x452.png)](https://substackcdn.com/image/fetch/%24s_%21MEJE%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/de69ecce-f662-49c9-94cb-ab2f0c3bbef0_752x452.png)

Neoverse N1在每个子测试中都战胜了泰山v110。Neoverse N1最大的胜利来自505.mcf和525.x264。在前者中，Neoverse N1的每千条指令分支错误预测数（MPKI）为15.03，而泰山v110为16.64。505.mcf除了受分支错误预测的限制外，还严重受后端内存访问的限制，这对任何CPU核心来说都是一场噩梦。Ampere Altra的缓存设置和更好的分支预测器可能共同作用，使其性能超出鲲鹏920 100%以上。525.x264的情况则更难理解。我怀疑在获取分数报告时，鲲鹏920的运行结果不佳，因为随后使用性能计数器的一次运行表明，根据实现的IPC、实际指令数和时钟速度，分数差距不应该这么大。然而，由于时间和远程测试设置的限制，没有机会再跟进验证。

无论525.x264发生了什么，Neoverse N1的优势是显而易见的。N1拥有一个出色的分支预测器，如果取所有子测试中分支预测准确率的几何平均值，它几乎与Zen 2中的预测器不相上下。它的乱序执行引擎仅比泰山v110中的略大，但N1的后端资源平衡得更好。它有更多的整数侧调度器条目和更大的FP/向量寄存器文件。泰山v110在这两个方面都常常感到压力。在内存子系统方面，鲲鹏920分区模式带来的任何优势似乎都被Neoverse N1更大的L2所抵消。

## 结语

鲲鹏920集结了一系列引人入胜的特性。它是服务器领域台积电7nm节点的早期采用者，比Ampere Altra和Zen 2的服务器版本更早上市。它使用了台积电的CoWoS封装技术，而当时AMD选择了更简单的封装上走线，Ampere则坚持单片设计。动态L3行为是一个突出的特性，而其他人（除了IBM）的L3缓存只以相当于“共享”模式的方式运行。我相信许多技术爱好者都曾审视过Intel和AMD CPU上的多bank L3设计，并好奇他们是否会尝试将L3数据保存在离使用它的核心更近的地方。嗯，华为正是这样做的。

[![](https://substackcdn.com/image/fetch/$s_!omdW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1451d473-870a-43eb-b807-1cf30638793c_581x495.png)](https://substackcdn.com/image/fetch/%24s_%21omdW%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/1451d473-870a-43eb-b807-1cf30638793c_581x495.png)

然而，鲲鹏920很难将这些特性转化为优势。如果芯片没有被设置为在软件层面表现得像一个单片设计，那么CoWoS的高跨裸片带宽似乎被浪费了。L3的分区模式根据数据共享行为的不同，提供了不一致的性能。当单个核心需要使用大部分L3容量或核心间共享数据时，L3性能很差。Zen 2的一致性高速L3即使没有利用bank/核心的局部性，也表现得更稳定、性能更高。Neoverse N1使用更大的L2来隔离核心免受L3延迟影响的做法，在实践中也看起来是一个更好的选择。也许唯一体现出来的优势是其Chiplet设计的灵活性，这让华为能够通过复用裸片来覆盖更广泛的产品类别。

[![](https://substackcdn.com/image/fetch/$s_!8Xkl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d4e78a4-ac22-4f1e-8fed-6365881a80fa_714x422.png)](https://substackcdn.com/image/fetch/%24s_%218Xkl%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/3d4e78a4-ac22-4f1e-8fed-6365881a80fa_714x422.png)

在核心层面，我们很难不得出这样的结论：台积电7nm的优势也被浪费了。Neoverse N1在同一节点上瞄准了类似的目标，并且做得更好。Arm在密度优化设计方面的才华在此尽显。他们能够将更大的结构塞进相同的面积，包括一个拥有6K条目BTB的分支预测器和一个更大的向量寄存器文件。他们能够更好地调整核心结构，以减少延迟受限工作负载中的后端资源停顿。最后，他们能够给予Neoverse N1两倍的L2容量，同时将其全部保持在与泰山v110相同的面积足迹内。与AMD的比较要困难得多，因为设计目标不同。但有趣的是，即使增加核心宽度和重排序能力会遇到收益递减的问题，Zen 2在作为桌面核心运行时也实现了相似的面积效率。

[![](https://substackcdn.com/image/fetch/$s_!uQXY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e704217-b1aa-4929-836c-05b2d64c31b9_646x481.png)](https://substackcdn.com/image/fetch/%24s_%21uQXY%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/7e704217-b1aa-4929-836c-05b2d64c31b9_646x481.png)

这些核心之间的比较给人的印象是，AMD和Arm充分利用了台积电的7nm节点，而海思仅仅是做了一份合格的工作。但一份合格的工作可能就足够了。华为不需要泰山v110与Neoverse N1和Zen 2正面硬刚。它需要一个能维持其业务运转的、不错的核心。泰山v110完全有能力扮演这个角色。也许更重要的是，海思对先进台积电技术的早期采纳，以及愿意尝试动态L3行为的意愿，表明海思的工程师们不惧怕采取激进的策略。这意味着泰山v110可以作为未来设计的跳板，为保障华为的未来铺平道路。

## 参考文献

1.  泰山v110针对各种指令的微操作端口分配: <https://github.com/qcjiang/OSACA/blob/feature/tsv110/osaca/data/tsv110.yml>
2.  一款鲲鹏920服务器的BIOS设置，表明L3可以被静态设置为使用共享或私有模式: <https://support.huawei.com/enterprise/zh/doc/EDOC1100088653/98b06651>
3.  华为研究关于鲲鹏920的出版物（从第126页开始）: <https://www-file.huawei.com/-/media/corp2020/pdf/publications/huawei-research/2022/huawei-research-issue1-en.pdf>
4.  Shanghao Liu 等人, *ARM处理器上模板计算的高效局部性感知的指令流调度*
5.  关于更大规格鲲鹏920的NUMA行为描述，表明每个计算裸片作为一个NUMA节点: <https://www.hikunpeng.com/document/detail/en/perftuning/progtuneg/kunpengprogramming_05_0004.html>

---

### 芯海拾贝：交流与探讨

这篇文章对华为鲲鹏920进行了一次深入的技术“考古”，揭示了其设计的亮点与权衡。读完之后，相信你也有自己的思考，欢迎在评论区分享你的观点：

1.  **关于L3缓存设计**：你如何看待鲲鹏920在L3缓存上“分区/私有/共享”模式的创新？这种复杂性在实际应用中是“锦上添花”还是“画蛇添足”？
2.  **首款自研核心的意义**：文章将泰山v110与同期的Neoverse N1和Zen 2对比，虽有差距但仍不失为一份“合格”的答卷。考虑到这是华为首款服务器核心，你认为这体现了怎样的设计能力和发展潜力？
3.  **技术自主的视角**：在技术自立自强的宏大背景下，像鲲鹏920这样的产品，即使在某些性能指标上未能登顶，其战略价值体现在何处？
4.  **你的实践经验**：你是否接触或使用过基于鲲鹏平台的服务器或开发板？欢迎分享你的第一手经验和感受！