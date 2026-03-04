# 香山 RISC-V 处理器：一场深刻的开源实验能否撼动 Arm 与 x86 的围墙？

在被 Arm 和 x86 架构长期固化的全球处理器版图上，一个源自中国的开源项目——香山（XiangShan）RISC-V 处理器，正以一种近乎理想主义的姿态，试图撬动这看似坚不可摧的产业格局。它不仅是一款对标世界顶尖水平的高性能处理器 IP，更承载着一场宏大的技术和社会实验：以彻底的开源模式，团结中国乃至全球的 RISC-V 力量，向服务器、移动终端，尤其是新兴的 AI 市场发起冲击。

这场实验的核心问题是，香山的开源策略能否真正奏效？它能否在弥合国内 RISC-V 产业碎片化的同时，构建一个足以与 Arm、x86 相抗衡的强大生态？这不仅是对技术路线的考验，更是对产业协作模式与地缘政治格局的深刻反思。

## 技术雄心：从对标 A76 到比肩 Neoverse N2

香山项目的起点，源于一个清晰的判断：彼时 RISC-V 社区虽充满活力，但缺乏一个能被工业界和学术界广泛应用的高性能开源处理器核心。[^1] [^2] 为填补这一空白，由中国科学院计算技术研究所（ICT, CAS）牵头，香山项目于 2020 年 6 月正式启动。[^3] [^4] 其目标明确——打造一个像 Linux 那样至少能存活 30 年的开源处理器主线。[^1] [^5]

香山的发展路径以迭代迅速、目标远大为特征，每一代架构都以北京的地名命名，极具象征意义：

- **第一代“雁栖湖 (Yanqihu)”**：作为项目的开端，这代架构采用了 11 级流水线、6 发射的超标量乱序设计。[^3] 在 28nm 工艺下实现了 1.3GHz 的主频，SPEC CPU2006 得分约为 7 分/GHz，性能对标 Arm Cortex-A72/A73 级别。[^6] “雁栖湖”的成功流片与点亮，验证了团队的技术实力和敏捷开发流程的可行性。[^7]
    
- **第二代“南湖 (Nanhu)”**：性能目标直接对标 Arm Cortex-A76。[^6] [^8] 通过采用更先进的微架构设计，如解耦的分支预测和指令获取、更优的调度器等，“南湖”的 SPEC CPU2006 分数提升至约 10 分/GHz。[^3] [^9] 计划采用中芯国际 14nm 工艺，目标频率 2GHz。[^9] 基于“南湖”核心的开发板已成功运行《云·原神》等复杂应用，展示了其在实际场景中的潜力。[^10] [^11]
    
- **第三代“昆明湖 (Kunminghu)”**：这是香山迈向服务器与数据中心市场的关键一步，性能直接对标 Arm 的高性能服务器核心 Neoverse N2。[^8] [^12] [^13] “昆明湖”是一个重大的架构重构，采用了更复杂的 13 级流水线、6-wide 解码/重命名/分派的后端设计，并支持 RISC-V 的矢量（Vector）和虚拟化（Hypervisor）扩展。[^8] [^14] 在 7nm 工艺下，其目标主频达到 3GHz，SPECint2006 基础得分预计约 45 分，性能达到 15 分/GHz，已步入全球高性能处理器的第一梯队。[^13] [^15] [^16] 负责人包云岗研究员透露，经过持续优化，“昆明湖”与 Neoverse N2 在 PPA（性能、功耗、面积）上的差距已缩至 8% 以内。[^17]
    

香山的技术实现并非闭门造车，它站在了巨人的肩膀上。项目文档中明确致谢了多篇经典的体系结构论文。[^18] 同时，它在技术选型上十分现代，采用了 Chisel 这一高层级的硬件描述语言，以提升开发效率和设计的可配置性，使其更像一个“处理器生成器”而非固定的设计。[^4] [^19] [^20]

## 开源策略：一场关于“公地”与“联盟”的实验

香山最引人瞩目的特质，是其彻底的开源策略。它开源的不仅仅是约 6 万行 Chisel 设计代码和 3 万行验证代码，还包括一整套名为“敏捷”的开发基础设施和工具集。[^2] [^20] 这套工具链涵盖了差分测试框架、仿真快照、性能验证等，旨在大幅降低高性能处理器的开发和验证门槛。[^2] [^4] [^15]

这背后是一种深刻的战略考量：

1. **打造开源“公地”，团结国内力量**：香山团队希望通过提供一个高性能的开源“公地”，避免国内 RISC-V 发展的低水平重复和碎片化，形成合力。[^1] 这一策略得到了产业界的积极响应。2021 年，北京市与中科院战略合作，成立了非营利性的北京开源芯片研究院（BOSC，简称“开芯院”）。[^9] [^21] [^22] 开芯院承接了香山的后续开发，并联合腾讯、阿里巴巴、中兴通讯等 16 家企业组成了开源芯片创新联合体，共同围绕香山进行开发与应用。[^10] [^16] [^22]
    
2. **“协同开发瀑布模型”，加速产业化**：依托开芯院，香山探索出一种“协同开发瀑布模型”。[^16] 该模型体系化地拉通了产学研协作链条：由研究院牵头，与企业共同定义产品规格，与多家企业组成联合开发团队进行研发，并将学术界的创新成果融入其中。[^16] 第三代“昆明湖”的开发就是这一模式的成功实践，仅用一年半时间就完成了开发。[^16] 目前，已有多家企业基于“香山”的 IP 核研发数据中心 AI 芯片、服务器芯片和 GPU 等高端产品，有望在 2025 年形成集体突破。[^16]
    
3. **效仿 Linux，构建全球生态**：项目负责人包云岗多次表示，希望香山能成为 CPU 领域的 Linux，建立一个既能被工业界广泛应用，又能支持学术界创新的开源主线。[^1] [^23] 这意味着香山的目标不仅是中国，更是全球。项目代码托管在 GitHub 上，获得了全球开发者数千星标和数百复刻，成为最受关注的开源硬件项目之一。[^19] [^22] 同时，其相关成果也在 MICRO、Hot Chips 等国际顶级学术会议上发表，积极融入全球学术和开源社区。[^15] [^18]
    

然而，这种理想化的开源策略也面临着严峻的现实挑战。其中最核心的便是**商业模式**。包云岗曾提出效仿红帽（Red Hat）之于 Linux 的模式，但成功的路径仍在探索中。[^12] 此外，如何平衡开源社区的开放性与商业合作伙伴的利益，如何在地缘政治日益紧张的背景下维持全球合作，都是香山必须回答的问题。

## 直面围墙：在 Arm 与 x86 的领地寻求突破

香山若想成功，终将要在 Arm 和 x86 统治的市场中夺取份额。这注定是一场非对称的持久战，其突破口极有可能在以下几个领域：

- **服务器与数据中心市场**：“昆明湖”对标 Neoverse N2 的性能，使其具备了进军服务器市场的基本资格。[^8] [^12] 在这个领域，单纯的 CPU 性能比拼并非唯一路径。异构计算是 RISC-V 的重要机会。算能科技（Sophgo）基于 64 核 RISC-V 处理器 SG2042 实现了数据中心级的算力，验证了 RISC-V 在该场景下的潜力。[^24] 香山作为高性能的通用 CPU 核，可以与国产的 GPU、DPU 和 AI 加速器等形成异构方案，满足特定应用场景的需求。
    
- **AI 市场：最大的变量与机遇**：AI 的崛起为 RISC-V 带来了千载难逢的机遇。[^25] [^26] AI 工作负载的多样性和快速演进，恰好能发挥 RISC-V 指令集灵活、可扩展的优势。[^27] 许多观点认为，RISC-V 正在成为构建高效 AI 加速器的首选标准。[^27] [^28] 中国开放指令生态（RISC-V）联盟秘书长包云岗也指出，“RISC-V+AI”将成为未来的新组合。[^29] 中兴微电子等公司认为，RISC-V 在大模型推理领域有大量机会。[^29] 目前，多家企业已基于“香山”开发面向 AI 的芯片。[^16] 更重要的是，当 NVIDIA 宣布其 CUDA 生态将全面拥抱 RISC-V 时，无疑为整个 RISC-V 在 AI 计算领域的发展注入了最强劲的动力。[^27]
    
- **移动与桌面市场：最艰难的战场**：这是 Arm 与 x86 根基最深、生态壁垒最高的领域。尽管 Google 已宣布 Android 将原生支持 RISC-V，但软件生态的成熟度、兼容性与迁移成本依然是巨大的障碍。[^5] 包云岗也坦言，RISC-V 要想走进手机、电脑等传统领域，至少还需要 5 到 10 年的时间。[^5]
    

## 各方观点与深层反思

香山项目自诞生之日起，就伴随着业界的期待与审视。

- **支持者与参与者**：以中科院计算所、开芯院为代表的研发团队，以及阿里、腾讯等联合开发企业，将其视为打破国外技术垄断、实现高端芯片自主可控的重要路径。他们强调开源协作的模式，认为这是凝聚产业力量、加速创新的唯一可行方式。[^16]
    
- **行业观察者**：普遍认为香山的技术水平值得肯定，是全球开源 RISC-V 处理器中当之无愧的性能领跑者。[^13] [^19] 但对其商业化前景和生态建设的长期挑战持谨慎态度。[^5] [^24] 许多人指出，RISC-V 生态“专用有余、通用不足”的特征依然明显，需要标杆性的产品来建立行业信心。[^24]
    
- **国际视角**：香山在国际上获得了相当的关注。硅谷知名黑客 George Hotz 的发问——“为什么最强的开源 CPU 来自中国？”，在海外社交媒体引发热议，并为香山的 GitHub 仓库带来了大量关注。[^10] [^30] 这从侧面反映出，国际社区认可香山的技术成就，并对这种由国家力量支持的开源模式感到好奇和些许敬畏。
    
- **质疑与反思**：面对“雷声大、雨点小”、“PPT 造芯”等质疑，项目负责人包云岗回应称，“2025 年将是香山的交付年”，并坦言很多人低估了开发一款与世界顶尖水平竞争的高端 CPU IP 核的难度。[^17] 这种难度不仅在于性能，更在于要在面积和功耗上取得平衡，这对 IP 核的商业竞争力至关重要。[^17]
    

**结论：一场超越芯片本身的深刻实验**

香山处理器项目，早已超越了一款硬件的范畴。它是一场在中国特定产业环境下，探索核心技术突破路径的深刻实验。它试图回答一个根本性问题：在处理器这一技术、资本和生态高度密集的领域，开源协作能否成为对抗商业巨头封锁的有效武器？

目前来看，香山的开源策略在“团结中国 RISC-V 玩家”方面已初见成效，开芯院的成立和产业联盟的协同开发是明确的证据。[^16] [^22] 然而，要真正冲击 Arm 和 x86 的统治地位，尤其是在服务器和手机市场，依然任重道远。生态系统的构建，非一日之功，它需要漫长的时间、持续的投入以及数个“杀手级”应用的出现来引爆市场。[^24]

真正的突破口，或许在于 AI。AI 市场的颠覆性力量正在重塑计算架构，这为相对年轻的 RISC-V 生态提供了一个换道超车的历史性机遇。[^27] [^29] 香山若能抓住这个窗口，与中国的 AI 芯片产业深度绑定，形成强大的“CPU+AI”异构计算平台，便有可能在新的战场上建立自己的根据地。

最终，香山的成败，不仅取决于其技术迭代的速度，更取决于其开源社区的活力、商业模式的创新，以及能否在一个日益复杂的国际环境中，保持开放与协作的初心。这场实验的最终结果尚不可知，但它所激起的涟漪，已足以让我们深刻反思全球芯片产业的未来格局以及开源模式在其中的无限可能。

---

[^1]: 开源高性能处理器“香山”研发骨干来自国科大一生一芯计划 https://news.ucas.ac.cn/jxyd/2ff17a31f40945d8a4022b141c83bae6.htm
[^2]: 香山开源高性能 RISC-V 处理器设计与实现 https://crad.ict.ac.cn/cn/article/pdf/preview/10.7544/issn1000-1239.202221036.pdf
[^3]: XiangShan: an Open-source High-performance RISC-V Processor - Yungang Bao https://www.youtube.com/watch?v=LSiBKxoszz4
[^4]: 香山项目总体介绍 - XiangShan 官方文档 https://xiangshan-doc-en.readthedocs.io/en/latest/
[^5]: 向Linux看齐，立志存活三十年：包云岗团队开源高性能RISC-V处理器「香山」-腾讯云开发者社区-腾讯云 https://cloud.tencent.com/developer/article/2252116
[^6]: 中科院发布国产RISC-V处理器“香山”|雁栖湖|处理器_新浪科技_新浪网 https://finance.sina.com.cn/tech/2021-07-01/doc-ikqciyzk2854051.shtml
[^7]: XiangShan 官方文档 https://xiangshan-doc-en.readthedocs.io/en/latest/
[^8]: XiangShan High-Performance RISC-V Processors at Hot Chips 2024 https://www.servethehome.com/xiangshan-high-performance-risc-v-processors-at-hot-chips-2024/
[^9]: “北京开芯院”成立，中科院包云岗团队开源RISC-V处理器“香山”有了新归属_澎湃号·湃客_澎湃新闻-The Paper https://www.thepaper.cn/newsDetail_forward_17557571
[^10]: 「为啥最强开源CPU是中国的」，硅谷大V灵魂发问，震动50万人在线围观 | 量子位 https://www.qbitai.com/2025/01/241088.html
[^11]: 「为啥最强开源CPU是中国的」，硅谷大V灵魂发问，震动50万人在线围观 https://www.pconline.com.cn/focus/1866/18661029.html
[^12]: Chinese RISC-V project teases 2025 debut of freely licensed advanced chip design https://www.theregister.com/2025/01/08/chinese_riscv_project_teases_2025/
[^13]: 国产最强开源RISC-V内核“昆明湖”解析：性能比肩Neoverse N2|RISC-V_新浪财经_新浪网 https://finance.sina.com.cn/wm/2024-08-29/doc-incmhrnn1129812.shtml
[^14]: 微架构简介 - 香山开源处理器用户手册 https://docs.xiangshan.cc/projects/user-guide/zh-cn/latest/processor/
[^15]: CSDL | IEEE Computer Society https://www.computer.org/csdl/magazine/mi/2025/03/10980411/26l8Dw4uinm
[^16]: 第三代“香山”开源高性能RISC-V处理器核发布 https://m.bjnews.com.cn/detail/1714012616129159.html
[^17]: 国产开源 RISC-V 芯片香山被质疑“PPT 造芯”，研究员包云岗称今年交付、很多人低估开发高端 CPU IP 核难度|cpu|RISC-V|芯片_新浪科技_新浪网 https://finance.sina.com.cn/tech/digi/2025-01-05/doc-inecwtca9749650.shtml
[^18]: GitHub - OpenXiangShan/XiangShan: Open-source high-performance RISC-V processor https://github.com/OpenXiangShan/XiangShan
[^19]: XiangShan Open-Source High Performance RISC-V Processor Design and Implementation https://crad.ict.ac.cn/en/article/doi/10.7544/issn1000-1239.202221036
[^20]: 香山开源高性能RISC-V处理器设计与实现 https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202221036
[^21]: RISC-V 开源处理器 “香山” 新归属：北京开源芯片研究院 https://www.oschina.net/news/190555/xiangshan-bosc
[^22]: XiangShan 官方文档 https://docs.xiangshan.cc/zh-cn/latest/
[^23]: Dr Yungang Bao - RISC-V in China: Embracing the Era of Open-Source Chip https://www.youtube.com/watch?v=d0UVSAd6NC8
[^24]: RISC-V：迈向高性能计算新征程 https://eu.36kr.com/zh/p/3387914993909248
[^25]: Boosting RISC-V SoC performance for AI and ML applications https://riscv.org/ecosystem-news/2025/05/boosting-risc-v-soc-performance-for-ai-and-ml-applications/
[^26]: RISC-V adoption will be accelerated by AI, according to new Omdia research https://omdia.tech.informa.com/pr/2024/may/risc-v-adoption-will-be-accelerated-by-ai-according-to-new-omdia-research
[^27]: RISC-V and AI https://riscv.org/industries/artificial-intelligence/
[^28]: How RISC-V Changes the Global Landscape of AI and ML https://www.wevolver.com/article/how-risc-v-changes-the-global-landscape-of-aiml
[^29]: RISC-V芯片全球出货量突破百亿颗 AI大模型推理带来新机遇 https://www.cls.cn/detail/2090295
[^30]: "Why is the most powerful open source CPU from China?" A Silicon Valley big V asked a soul-searching question, shocking 500,000 people watching online https://en.eeworld.com.cn/mp/QbitAI/a391647.jspx