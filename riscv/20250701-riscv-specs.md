# [权威指南 | RISC-V 官方技术规范完整汇总](20250701-riscv-specs.mp3)


大家好！作为 RISC-V 生态的参与者、开发者或爱好者，我们深知技术规范的重要性。它们是构建兼容、可互操作硬件和软件的基石，是整个生态系统繁荣发展的蓝图。

为了方便大家查阅和学习，我们特地整理了由 RISC-V International 官方发布的最新技术规范列表。

> 本文档信息**整理于 2025 年 6 月 30 日**，数据来源于官方的 [RISC-V Technical Specifications 页面](https://lf-riscv.atlassian.net/wiki/spaces/HOME/pages/16154769/RISC-V+Technical+Specifications)。

无论您是芯片设计工程师、固件开发者、操作系统专家还是嵌入式系统爱好者，这份清单都将是您工作中不可或缺的宝贵资源。下面，让我们一起来深入了解 RISC-V 世界的构建法则。

---

## ISA Specifications (ISA 规范)

指令集架构（ISA）是 RISC-V 的核心。以下是当前已发布的 ISA 规范，它们定义了处理器如何执行指令。

*   *注：先前的版本以及已批准但尚未合并到主手册中的独立扩展，可以在 [RISC-V 技术规范存档页面](https://wiki.riscv.org/display/HOME/RISC-V+Technical+Specifications+Archive) 和 [RISC-V 已批准扩展页面](https://wiki.riscv.org/display/HOME/RISC-V+Ratified+Extensions) 找到。*

### **[RISC-V 指令集手册第一卷：非特权 ISA (The RISC-V Instruction Set Manual Volume I: Unprivileged ISA)](https://github.com/riscv/riscv-isa-manual/releases/download/20250508/riscv-spec-20250508.pdf)**

这份规范定义了用户级（非特权）指令集，是所有应用程序和普通软件运行的基础。

*   **版本:** 20250508
*   **发布日期:** 2025 年 5 月
*   **RISC-V 社区:** 非特权横向委员会 (Unprivileged Horizontal Committee)
*   **源代码仓库:** [riscv/riscv-isa-manual](https://github.com/riscv/riscv-isa-manual)

### **[RISC-V 指令集手册第二卷：特权架构 (The RISC-V Instruction Set Manual Volume II: Privileged Architecture)](https://github.com/riscv/riscv-isa-manual/releases/download/20250508/riscv-privileged-20250508.pdf)**

这份规范定义了操作系统和虚拟机监视器（Hypervisor）所使用的特权级指令和系统寄存器，是构建安全、稳定操作系统的关键。

*   **版本:** 20250508
*   **发布日期:** 2025 年 5 月
*   **RISC-V 社区:** 特权横向委员会 (Privileged Horizontal Committee)
*   **源代码仓库:** [riscv/riscv-isa-manual](https://github.com/riscv/riscv-isa-manual)

---

## Profile (配置文件)

配置文件（Profile）为特定应用领域定义了一套标准的 ISA 扩展组合，旨在提高软件的可移植性和兼容性。

### **[RVA23 配置文件 (RVA23 Profile)](https://github.com/riscv/riscv-profiles/releases/download/v1.0/riscv-profile-spec-RVA23-v1.0.pdf)**
*   **版本:** 1.0
*   **发布日期:** 2024 年 10 月
*   **配置文件:** RVA23
*   **RISC-V 社区:** 配置文件 SIG (Profiles SIG)
*   **源代码仓库:** [riscv/riscv-profiles](https://github.com/riscv/riscv-profiles)

### **[RVB23 配置文件 (RVB23 Profile)](https://github.com/riscv/riscv-profiles/releases/download/v1.0/riscv-profile-spec-RVB23-v1.0.pdf)**
*   **版本:** 1.0
*   **发布日期:** 2024 年 10 月
*   **配置文件:** RVB23
*   **RISC-V 社区:** 配置文件 SIG (Profiles SIG)
*   **源代码仓库:** [riscv/riscv-profiles](https://github.com/riscv/riscv-profiles)

### **[RISC-V 配置文件 (RISC-V Profiles)](https://github.com/riscv/riscv-profiles/releases/download/v1.0-20230302/riscv-profiles-spec-1.0.pdf)**
*   **版本:** 1.0
*   **发布日期:** 2023 年 3 月
*   **配置文件:** RVA20, RVI20, RVA22
*   **RISC-V 社区:** 配置文件 SIG (Profiles SIG)
*   **源代码仓库:** [riscv/riscv-profiles](https://github.com/riscv/riscv-profiles)

---

## Non-ISA Specifications (非 ISA 规范)

除了核心 ISA，RISC-V 生态还需要一系列非 ISA 规范来定义系统级组件，如调试、中断、IOMMU 等，以确保整个 SoC 的协同工作。

*   *注：如果您在下面没有找到某个规范，可以访问 [RISC-V GitHub riscv-non-isa 组织](https://github.com/riscv-non-isa) 查看所有正在制定或已完成的规范。*

### **[RISC-V 高效追踪 (Efficient Trace for RISC-V)](https://drive.google.com/file/d/1iijHsZB7YXW0A2HuuzHo5QTZSKrO_KbW/view?usp=drive_link)**
> 规定了 RISC-V 核心与编码器之间的信号、压缩分支追踪算法，以及用于封装压缩分支追踪信息以实现处理器追踪的数据包格式。
*   **版本:** 2.0
*   **发布日期:** 2022 年 6 月 (更新于 2025 年 6 月)
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/tech-trace-spec](https://github.com/riscv-non-isa/tech-trace-spec)

### **[RISC-V ABI 规范 (RISC-V ABIs Specification)](https://drive.google.com/file/d/1Ja_Tpp_5Me583CGVD-BIZMlgGBnlKU4R/view?usp=drive_link)**
> 为 RISC-V 提供处理器特定的应用程序二进制接口（ABI）文档，是确保编译后的代码能正确链接和运行的基石。
*   **版本:** 1.0
*   **发布日期:** 2022 年 11 月
*   **RISC-V 社区:** 应用与工具横向委员会 (Application & Tools Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-elf-psabi-doc](https://github.com/riscv-non-isa/riscv-elf-psabi-doc)

### **[RISC-V 高级中断架构 (RISC-V Advanced Interrupt Architecture)](https://drive.google.com/file/d/16life2Y5u7Plebbl4v1fFM1-NK-KHw0Y/view?usp=sharing)**
> 描述了用于 RISC-V 系统的高级中断架构 (AIA)，对于支持复杂中断处理的现代系统至关重要。
*   **版本:** 1.0
*   **发布日期:** 2023 年 6 月
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv/riscv-aia](https://github.com/riscv/riscv-aia)

### **[RISC-V 容量和带宽 QoS 寄存器接口 (RISC-V Capacity and Bandwidth QoS Register Interface)](https://drive.google.com/file/d/1XSKqg6MXEmRdpdUYLj-Q03kZD6TDQhtu/view?usp=drive_link)**
> 规定了用于管理共享资源（如缓存、内存控制器）的服务质量（QoS）的寄存器接口，确保关键任务能获得所需性能。
*   **版本:** 1.0
*   **发布日期:** 2024 年 6 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-cbqri](https://github.com/riscv-non-isa/riscv-cbqri)

### **[RISC-V 调试规范 (The RISC-V Debug Specification)](https://drive.google.com/file/d/1h_f9NgB_8m2fS6uCnKP1Oho-3x1MpBEl/view?usp=drive_link)**
> 概述了 RISC-V 硬件平台的标准调试架构，允许调试工具（如 GDB、J-Link）与各种 RISC-V 核心进行交互。
*   **版本:** 1.0
*   **发布日期:** 2025 年 2 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv/tech-debug-spec](https://github.com/riscv/tech-debug-spec)

### **[RISC-V 功能性固定硬件规范 (RISC-V Functional Fixed Hardware Specification)](https://drive.google.com/file/d/1XzlA0LE4N5_47wJXsU3aqyD69pHGvdcL/view?usp=drive_link)**
> 为使用 ACPI 的 RISC-V 系统提供了额外的系统规范，特别针对 ACPI 对象字段。
*   **版本:** 1.0.1
*   **发布日期:** 2024 年 1 月 (更新于 2024 年 10 月)
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-acpi-ffh](https://github.com/riscv-non-isa/riscv-acpi-ffh)

### **[RISC-V IO 映射表规范 (RISC-V IO Mapping Table Specification)](https://drive.google.com/file/d/1sxQ3iQ1l5Jgq9tukvGMnucRUvY16s8zN/view?usp=sharing)**
> (RIMT) 提供了 RISC-V IOMMU 的信息，并描述了在基于 ACPI 的平台中 IO 拓扑与 IOMMU 之间的关系。
*   **版本:** 1.0
*   **发布日期:** 2025 年 3 月
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-acpi-rimt](https://github.com/riscv-non-isa/riscv-acpi-rimt)

### **[RISC-V IOMMU 架构规范 (RISC-V IOMMU Architecture Specification)](https://drive.google.com/file/d/1kVapIJPXUUNFQv_yauCDgtWzMvpgh6C2/view?usp=drive_link)**
> 描述了一种输入/输出内存管理单元 (IOMMU)，用于保护系统内存免受外围设备的非法访问，并实现虚拟化。
*   **版本:** 1.0
*   **发布日期:** 2023 年 6 月 (更新于 2025 年 6 月)
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-iommu](https://github.com/riscv-non-isa/riscv-iommu)

### **[RISC-V N-Trace (基于 Nexus 的追踪) (RISC-V N-Trace (Nexus-based Trace))](https://drive.google.com/file/d/1UXFptcTjd5akPhKRtn0onBC6t53O61qU/view?usp=drive_link)**
> 实现了为 RISC-V 定制的 IEEE-5001 Nexus 追踪标准，为复杂的 SoC/MCU 设计提供强大的追踪能力。
*   **版本:** 1.0
*   **发布日期:** 2024 年 11 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/tg-nexus-trace](https://github.com/riscv-non-isa/tg-nexus-trace)

### **[RISC-V 平台级中断控制器规范 (RISC-V Platform-Level Interrupt Controller Specification)](https://drive.google.com/file/d/1at94PNJl4v2eAsKIwKOsZWBxsVcY2U2F/view?usp=drive_link)**
> (PLIC) 描述了用于管理来自外部设备中断的平台级中断控制器。
*   **版本:** 1.0.0
*   **发布日期:** 2023 年 2 月
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv/riscv-plic-spec](https://github.com/riscv/riscv-plic-spec)

### **[RISC-V RERI 架构规范 (RISC-V RERI Architecture Specification)](https://drive.google.com/file/d/19gMRFbWDrfDZKyqoO3iFkySPvKpxm26a/view?usp=drive_link)**
> 通过标准的内存映射寄存器接口增强了 SoC 的可靠性、可用性和可服务性 (RAS)，用于错误报告和处理。
*   **版本:** 1.0
*   **发布日期:** 2024 年 5 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-ras-eri](https://github.com/riscv-non-isa/riscv-ras-eri)

### **[RISC-V 半主机 (RISC-V Semihosting)](https://drive.google.com/file/d/1qu74D4_EmjGmc03qzfQ7Pf4g6m0fOtcD/view?usp=sharing)**
> 定义了 RISC-V 平台的半主机二进制接口，允许在开发板上运行的代码与主机调试器进行 I/O 交互。
*   **版本:** 1.0
*   **发布日期:** 2025 年 2 月
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-semihosting](https://github.com/riscv-non-isa/riscv-semihosting)

### **[RISC-V 服务器 SoC 规范 (RISC-V Server SOC Specification)](https://drive.google.com/file/d/1KjewRE0NltEmbKOz7YlgOsTF51lZ6aPL/view?usp=sharing)**
> 定义了一套标准化的功能集，使得操作系统和虚拟机监视器等系统软件可以依赖这些功能在 RISC-V 服务器 SoC 中存在。
*   **版本:** 1.0
*   **发布日期:** 2025 年 2 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/server-soc](https://github.com/riscv-non-isa/server-soc)

### **[RISC-V 监管者二进制接口规范 (RISC-V Supervisor Binary Interface Specification)](https://drive.google.com/file/d/1U2kwjqxXgDONXk_-ZDTYzvsV-F_8ylEH/view?usp=drive_link)**
> (SBI) 定义了运行在 M-Mode 的固件与运行在 S-Mode 的操作系统/虚拟机监视器之间的标准接口。
*   **版本:** 2.0.0
*   **发布日期:** 2024 年 1 月
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-sbi-doc](https://github.com/riscv-non-isa/riscv-sbi-doc)

### **[RISC-V 追踪连接器 (RISC-V Trace Connectors)](https://drive.google.com/file/d/1SMypv0CUL338L-sURMyJuO60WZ7oDi9V/view?usp=drive_link)**
> 为标准的调试连接器添加了追踪信号，并为 MIPI 追踪连接器提供了可选扩展。
*   **版本:** 1.0
*   **发布日期:** 2024 年 11 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/tg-nexus-trace](https://github.com/riscv-non-isa/tg-nexus-trace)

### **[RISC-V 追踪控制接口 (RISC-V Trace Control Interface)](https://drive.google.com/file/d/1ZQvU1WNamY5EHGum4yP1z-WmPrcxH2b8/view?usp=drive_link)**
> 为 RISC-V 追踪基础设施提供了一个标准化的控制接口，允许追踪控制软件与不同实现互换使用。
*   **版本:** 1.0
*   **发布日期:** 2024 年 11 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/tg-nexus-trace](https://github.com/riscv-non-isa/tg-nexus-trace)

### **[RISC-V UEFI 协议规范 (RISC-V UEFI Protocol Specification)](https://drive.google.com/file/d/1rbQDRkoeJyqTKTI6tTCKw8zmh7T9dLUZ/view?usp=drive_link)**
> 详细说明了在 RISC-V 平台上实现 UEFI 固件所需的特有协议。
*   **版本:** 1.0.0
*   **发布日期:** 2022 年 5 月
*   **RISC-V 社区:** 特权软件横向委员会 (Privileged Software Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/riscv-uefi](https://github.com/riscv-non-isa/riscv-uefi)

### **[RISC-V 向量 C 内联函数规范 (RISC-V Vector C Intrinsic Specification)](https://drive.google.com/file/d/1RTZi2iOLKzqaX95JCCnzwOm7iCIN3JEq/view?usp=drive_link)**
> 在 C 语言层面提供标准接口（Intrinsics），使开发者能直接利用强大的 RISC-V 向量（Vector）扩展，而无需编写汇编。
*   **版本:** 1.0
*   **发布日期:** 2025 年 4 月
*   **RISC-V 社区:** 应用与工具横向委员会 (Application & Tools Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/rvv-intrinsic-doc](https://github.com/riscv-non-isa/rvv-intrinsic-doc)

### **[RISC-V 未格式化追踪与诊断数据包封装 (Unformatted Trace & Diagnostic Data Packet Encapsulation for RISC-V)](https://drive.google.com/file/d/1R-_koXIpdb9_qW6jpz74TSnNXOfJGhfn/view?usp=drive_link)**
> 定义了一种适用于多种传输机制的封装格式，用于传输未格式化的追踪和诊断数据。
*   **版本:** 1.0
*   **发布日期:** 2024 年 6 月
*   **RISC-V 社区:** SoC 基础设施横向委员会 (SOC Infrastructure Horizontal Committee)
*   **源代码仓库:** [riscv-non-isa/e-trace-encap](https://github.com/riscv-non-isa/e-trace-encap)

---

## 兼容性测试框架 (Compatibility Test Framework)

为了验证一个 RISC-V 实现是否符合规范，RISC-V International 提供了一套架构兼容性测试框架。该框架能够自动选择和配置测试，并比较待测模型与参考模型的行为。

当前的测试覆盖范围包括 `RV[32|64]IMCFD_Zb\*_zK\*_Zmmul_Zicsr_Zifencei` 等核心扩展。

**更多信息和资源：**
*   **兼容性测试框架 (RISCOF):** [GitHub 仓库](https://github.com/riscv-non-isa/riscof), [文档](https://riscof.readthedocs.io/en/latest/)
*   **测试框架配置工具 (RISCV-CONFIG):** [GitHub 仓库](https://github.com/riscv-non-isa/riscv-config), [文档](https://riscv-config.readthedocs.io/en/latest/)
*   **架构兼容性测试套件 (ACT):** [GitHub 仓库](https://github.com/riscv-non-isa/riscv-arch-test), [测试格式规范](https://github.com/riscv-non-isa/riscv-arch-test/blob/main/spec/TestFormatSpec.adoc)

---

## 总结与展望

这份详尽的列表无疑是 RISC-V 世界的一张藏宝图。从最基础的指令集到复杂的系统级规范，每一份文档都为 RISC-V 的开放、创新和协作精神奠定了坚实的基础。

这么多规范，是不是感觉眼花缭乱，不知从何看起？

别担心！这只是一个开始。为了帮助大家更好地理解和应用这些重要的技术规范，**我们计划在后续的文章中，对这些规范进行逐一的深度解析，并分享打包好的Spec集合**。从 ISA 基础到复杂的 IOMMU 和追踪技术，从 ABI 约定到最新的 RVA23 配置文件，我们将带您一探究竟，解读其背后的设计思想和实际应用。

![](../asserts/wx.jpg)

不想错过任何一篇深度解析？**立即关注我们的公众号**，第一时间获取最新、最硬核的 RISC-V 技术解读！让我们一起在 RISC-V 的开放道路上共同成长！