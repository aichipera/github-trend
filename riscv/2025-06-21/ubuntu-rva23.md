# Ubuntu 25.10 计划将 RISC-V 支持基准提升至 RVA23 配置文件

> 作者：Michael Larabel，发布于 2025年6月21日 上午 06:55 (EDT)，分类：Ubuntu

> **译者注**: Ubuntu 提升对 RISC-V 架构的支持标准，是该精简指令集走向成熟和标准化的关键一步。此次升级到 RVA23 配置文件，强制要求硬件支持矢量扩展和虚拟化等现代化功能，意在为开发者提供一个更高性能、功能更统一的平台。 这也意味着 Ubuntu 将告别部分早期 RISC-V 硬件，推动生态向更强的规范看齐。此举不仅加速了 RISC-V 在服务器、AI 等高性能领域的应用，也为即将到来的 26.04 LTS 长期支持版奠定了坚实基础。


![UBUNTU][fig1]

在至关重要的 Ubuntu 26.04 LTS 版本周期到来之前，Canonical 正计划为今年晚些时候发布的 Ubuntu 25.10 提高其所需的 RISC-V 指令集架构（ISA）基准。

Canonical 的开发者们正计划将 Ubuntu 25.10 所需的 RISC-V ISA 配置文件基准提升至去年刚刚获得批准的 RVA23。

![RISC-V cpuinfo][fig2]

RISC-V RVA23 配置文件强制要求硬件支持 RISC-V 矢量扩展（Vector extension）、虚拟机管理程序扩展（Hypervisor extension），并包含了针对 RISC-V 生态系统的其他现代化和标准化工作。 然而，这一变更也意味着，缺乏 RVA23 兼容性的老旧 RISC-V 平台将不再受新版 Ubuntu Linux 支持，它们需要继续使用 Ubuntu 24.04 LTS，或者是在 25.10 版本之前最新的非 LTS 版本 Ubuntu 25.04。

![Ubuntu RVA23 requirement][fig3]

Ubuntu 25.10 的 RISC-V 计划强制要求 RVA23 配置文件支持的消息，在[这份 ubuntu-release-upgrader 的工单]中得到了确认：

> “针对 Ubuntu 25.10 版本，我们计划将所需的 RISC-V ISA 配置文件系列提升至 RVA23。
>
> 对于不支持 RVA23U64 配置文件的硬件，ubuntu-release-upgrader（Ubuntu 版本升级程序）应停止其从 Ubuntu 24.04 之后的版本升级。RVA23U64 是与用户空间相关的配置文件。
>
> 由于 RVA20 系统的硬件不存在从 Ubuntu 25.04 Plucky（代号：勇敢的矮胖鸟）升级的路径，我们也应该停止将这些 RISC-V 系统从 Noble（Ubuntu 24.04 代号）升级到 Plucky。”

这些针对 `ubuntu-release-upgrader` 的更新已开始陆续推出，以确保 Ubuntu 的 RISC-V 用户运行在兼容 RVA23 的硬件上，否则将无法进行系统升级。

[fig1]: https://www.phoronix.com/assets/categories/ubuntu.webp
[fig2]: https://www.phoronix.net/image.php?id=2025&image=riscv_cpuinfo
[fig3]: https://www.phoronix.net/image.php?id=2025&image=ubuntu_rva23

: https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/2111715

---

### 极客茶话会

Ubuntu 这次提高 RISC-V 硬件门槛，可以说是 RISC-V 发展道路上的一个“成人礼”。放弃对旧硬件的支持，虽然会让一小部分早期玩家感到不便，但从长远来看，一个统一、高能的硬件基准对整个生态的健康发展至关重要。这不禁让人思考：

*   **对于开发者来说，** 这次标准提升意味着什么？是不是可以更大胆地利用矢量和虚拟化特性来开发高性能应用了？
*   **对于硬件厂商，** 这是否会加速新一代符合 RVA23 标准的 RISC-V 开发板和设备的推出？我们能期待看到哪些激动人心的新产品？
*   **放眼未来，** 你认为这是不是 RISC-V 挑战 ARM 和 x86 地位的一个重要信号？它离主流桌面和服务器市场还有多远？

欢迎在下方分享你的看法，聊聊你对 RISC-V 生态发展的期待和见解！