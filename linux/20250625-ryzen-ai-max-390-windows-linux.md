# [巅峰对决：AMD 锐龙 AI Max PRO 390 "Strix Halo" 平台上的 Windows 11 vs. Ubuntu Linux 性能评测](20250625-ryzen-ai-max-390-windows-linux.mp3)

> - 作者：[Michael Larabel](https://www.michaellarabel.com/)
> - 原文：https://www.phoronix.com/review/ryzen-ai-max-390-windows-linux


> **译者注**: 本文再次印证了一个长期趋势：**在相同的尖端硬件上，Linux 在多数 CPU 密集型和生产力任务中常常能超越 Windows**。**尤其值得关注的是，AMD 的开源 GPU 驱动（Mesa RADV）已今非昔比，在 Vulkan 乃至光线追踪这类前沿技术上，其性能已能与 Windows 官方驱动分庭抗礼，甚至在某些场景下实现反超**。这对于开发者、数据科学家以及**追求极致性能**的用户来说，无疑是个好消息，**意味着 Linux 桌面正成为一个越来越有吸引力的高性能平台**。

虽然这个结果可能并不出人意料——毕竟我们最近刚发布了 [AMD 锐龙 AI Max+ 395 在 Windows 11 与 Linux 上的测试](https://www.phoronix.com/review/amd-strix-halo-windows-linux)——但当我们拿到这台预装了微软 Windows 11 专业版的 [HP ZBook Ultra G1a](https://www.phoronix.com/review/hp-zbook-ultra-g1a) 时，我们还是抓住了这个机会，在这款定位稍低的 AMD Strix Halo SoC 上，再次进行了一番 Windows 与 Linux 的性能对决。这台笔记本搭载的是 AMD 锐龙 AI Max PRO 390 处理器。

![搭载锐龙 AI MAX PRO 390 的 Windows 笔记本](https://www.phoronix.net/image.php?id=ryzen-ai-max-390-windows-linux&image=ai_max_390_windows_med)

上个月的数据已经显示，在 AMD Strix Halo 平台上，Linux 通常能以不小的优势领先 Windows 11。今天的文章将作为补充，聚焦于惠普 ZBook Ultra G1a 移动工作站上的 Windows 11 专业版与 Ubuntu 25.04 的性能比较。该机型配备了 [AMD 锐龙 AI Max PRO 390](https://www.phoronix.com/review/amd-ryzen-ai-max-390) 12 核 SoC，并集成了 [Radeon 8050S 显卡](https://www.phoronix.com/review/amd-radeon-8050s-graphics)。

![搭载锐龙 AI MAX PRO 390 的 Ubuntu 笔记本](https://www.phoronix.net/image.php?id=amd-ryzen-ai-max-390&image=ryzen_ai_max_390_3_med)

Windows 系统的测试基于 HP ZBook Ultra G1a 开箱即用的 OEM 版 Windows 11 专业版，并安装了截至测试时的所有微软更新。然后，我们将其性能与运行着 Linux 6.14 内核及默认软件配置的 Ubuntu 25.04 进行对比，旨在探究这款 12 核 Strix Halo 笔记本在两大主流操作系统下的表现差异。

![HP ZBook Ultra G1a](https://www.phoronix.net/image.php?id=amd-ryzen-ai-max-390&image=ryzen_ai_max_390_2_med)

我们使用了一系列同时支持 Windows 和 Linux 且质量相近的原生 CPU 和 GPU 测试项目，以确保对比的公平性。其中许多基准测试与上个月的 AMD 锐龙 AI Max+ PRO 395 跨系统测试重合。

![AMD 锐龙 AI MAX PRO 390 在 HP ZBook Ultra 上的 Windows 11 Pro vs. Ubuntu Linux 性能总览](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/result.svgz)

所有基准测试均在同一台 HP ZBook Ultra G1a 上完成。其配置为：锐龙 AI Max PRO 390 处理器、Radeon 8050S 集成显卡、64GB LPDDR5-8000 内存、2TB WD SN810 NVMe 固态硬盘，以及一块 2880 x 1800 分辨率的屏幕。这是一款综合性能极为强大的笔记本，您可以通过我们最近发布的 [HP ZBook Ultra G1a Linux 评测](https://www.phoronix.com/review/hp-zbook-ultra-g1a)了解更多关于这两款 Strix Halo 机型的细节。

![vkpeak 基准测试 - 设置: fp32-scalar。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp32-scalar.svgz)

![vkpeak 基准测试 - 设置: fp32-vec4。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp32-vec4.svgz)

![vkpeak 基准测试 - 设置: fp16-scalar。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp16-scalar.svgz)

![vkpeak 基准测试 - 设置: fp16-vec4。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp16-vec4.svgz)

![vkpeak 基准测试 - 设置: fp16-matrix。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp16-matrix.svgz)

![vkpeak 基准测试 - 设置: fp64-scalar。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp64-scalar.svgz)

![vkpeak 基准测试 - 设置: fp64-vec4。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-fp64-vec4.svgz)

![vkpeak 基准测试 - 设置: int16-scalar。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-int16-scalar.svgz)

![vkpeak 基准测试 - 设置: int16-vec4。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-int16-vec4.svgz)

![vkpeak 基准测试 - 设置: int8-dotprod。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-int8-dotprod.svgz)

![vkpeak 基准测试 - 设置: int8-matrix。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/vkpeak-int8-matrix.svgz)

在使用 vkpeak 测试 Radeon 8050S (Strix Halo, RDNA3.5) 显卡在 Windows 和 Linux 下的原始 Vulkan 计算性能时，采用 Mesa RADV 驱动的 Ubuntu 25.04 赢得了多个项目的胜利，而 Windows 上的 Radeon Software 也在这些综合计算测试中取得了几项领先。无论如何，这都表明开源的 RADV 驱动栈在现代 Strix Halo 平台（RDNA 3.5）上表现强劲。想当年，AMD 开源驱动在新硬件发布之初的性能可是远远落后于 Windows 的。

![GravityMark 基准测试 - 设置: 1920x1080, Vulkan。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/gravitymark-1920-x-1080-vulkan.svgz)

![GravityMark 基准测试 - 设置: 2880x1800, Vulkan。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/gravitymark-2880-x-1800-vulkan.svgz)

![GravityMark 基准测试 - 设置: 1920x1080, Vulkan 光线追踪。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/gravitymark-1920-x-1080-vulkan-ray-tracing.svgz)

![GravityMark 基准测试 - 设置: 2880x1800, Vulkan 光线追踪。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/gravitymark-2880-x-1800-vulkan-ray-tracing.svgz)

在 GravityMark Vulkan 性能基准测试中，Ubuntu 25.04 的表现非常出色。与锐龙 AI Max+ PRO 395 的情况类似，令人惊喜的是，即便在 Vulkan 光线追踪测试中，我们也开始看到 Mesa RADV 驱动在某些情况下超越了 Windows 驱动。

![3DMark Wild Life Extreme 基准测试 - 设置: 1920x1080。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/3dmark-wild-life-extreme-1920-x-1080.svgz)

在 3DMark Wild Life Extreme 这个原生跨平台测试中，Windows 11 确实拥有显著优势。考虑到 3DMark Wild Life Extreme 在 Linux 上的版本仅对部分组织/用户开放，并未广泛普及，这可能是因为 Mesa 开发者根据其有限的访问权限，尚未对其进行充分优化。

![Quake II RTX 基准测试 - 设置: 2880x1800, 低全局光照, 降噪开, VK_KHR_ray_query。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/quake-ii-rtx-2880-x-1800-low-on-vk_khr_ray_query.svgz)

![Quake II RTX 基准测试 - 设置: 2880x1800, 低全局光照, 降噪关, VK_KHR_ray_query。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/quake-ii-rtx-2880-x-1800-low-off-vk_khr_ray_query.svgz)

![Quake II RTX 基准测试 - 设置: 2880x1800, 全局光照关, 降噪关, VK_KHR_ray_query。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/quake-ii-rtx-2880-x-1800-off-off-vk_khr_ray_query.svgz)

![Quake II RTX 基准测试 - 设置: 2880x1800, 全局光照关, 降噪开, VK_KHR_ray_tracing_pipeline。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/quake-ii-rtx-2880-x-1800-off-on-vk_khr_ray_tracing_pipeline.svgz)

![Quake II RTX 基准测试 - 设置: 2880x1800, 低全局光照, 降噪关, VK_KHR_ray_tracing_pipeline。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/quake-ii-rtx-2880-x-1800-low-off-vk_khr_ray_tracing_pipeline.svgz)

![Quake II RTX 基准测试 - 设置: 2880x1800, 全局光照关, 降噪关, VK_KHR_ray_tracing_pipeline。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/quake-ii-rtx-2880-x-1800-off-off-vk_khr_ray_tracing_pipeline.svgz)

在《雷神之锤 II RTX》中，我们进一步压榨了 AMD Radeon 8050S 显卡的 Vulkan 光追性能。Windows 在这里普遍领先，但 RADV 的表现也相差不远。

![Unigine Heaven 基准测试 - 设置: 1920x1080, 全屏, OpenGL。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/unigine-heaven-1920-x-1080-fullscreen-opengl.svgz)

![Unigine Heaven 基准测试 - 设置: 2880x1800, 全屏, OpenGL。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/unigine-heaven-2880-x-1800-fullscreen-opengl.svgz)

![Xonotic 基准测试 - 设置: 2880x1800, 低特效。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/xonotic-2880-x-1800-low.svgz)

![Xonotic 基准测试 - 设置: 2880x1800, 高特效。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/xonotic-2880-x-1800-high.svgz)

![Xonotic 基准测试 - 设置: 2880x1800, 极高特效。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/xonotic-2880-x-1800-ultra.svgz)

![Xonotic 基准测试 - 设置: 2880x1800, 终极特效。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/xonotic-2880-x-1800-ultimate.svgz)

![FurMark 基准测试 - 设置: 2880x1800, FurMark OpenGL, MSAA 关。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/furmark-2880-x-1800-furmark-opengl-off.svgz)

![FurMark 基准测试 - 设置: 2880x1800, FurMark Vulkan, MSAA 关。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/furmark-2880-x-1800-furmark-vulkan-off.svgz)

![FurMark 基准测试 - 设置: 1920x1080, FurMark Knot OpenGL, MSAA 关。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/furmark-1920-x-1080-fko-off.svgz)

![FurMark 基准测试 - 设置: 1920x1080, Furmark Knot Vulkan, MSAA 关。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/furmark-1920-x-1080-fkv-off.svgz)

![FurMark 基准测试 - 设置: 2880x1800, FurMark Knot OpenGL, MSAA 关。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/furmark-2880-x-1800-fko-off.svgz)

![FurMark 基准测试 - 设置: 2880x1800, Furmark Knot Vulkan, MSAA 关。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/furmark-2880-x-1800-fkv-off.svgz)

在各种 OpenGL 测试场景中，Windows 11 和 Ubuntu 25.04 的结果相当混杂，经常互有胜负。

![JPEG-XL libjxl 编码 - 输入: PNG, 质量: 80。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/jpeg-xl-libjxl-png-80.svgz)

![JPEG-XL libjxl 编码 - 输入: PNG, 质量: 90。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/jpeg-xl-libjxl-png-90.svgz)

![JPEG-XL libjxl 解码 - 线程: 全部。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/jpeg-xl-decoding-libjxl-all.svgz)

![WebP 图像编码 - 设置: 默认。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/webp-image-encode-default.svgz)

![WebP 图像编码 - 设置: 质量 100。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/webp-image-encode-quality-100.svgz)

![WebP 图像编码 - 设置: 质量 100, 无损。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/webp-image-encode-q1l.svgz)

![WebP 图像编码 - 设置: 质量 100, 最高压缩。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/webp-image-encode-q1hc.svgz)

![Crafty 国际象棋 - 耗时。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/crafty-elapsed-time.svgz)

![TSCP 国际象棋 - AI 性能。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/tscp-acp.svgz)

当我们转向 CPU 基准测试时，在这台搭载 AMD 锐龙 AI Max PRO 390 的 HP ZBook Ultra G1a 上，Ubuntu 25.04 通常是领跑者。不过，考虑到之前 AMD Strix Halo 的操作系统基准测试以及在英特尔和 AMD 处理器上进行的大量 Windows vs. Linux 测试，这个结果并不令人意外。

![LuxCoreRender - 场景: DLSC, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/luxcorerender-dlsc-cpu.svgz)

![LuxCoreRender - 场景: Danish Mood, CPU 加速。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/luxcorerender-danish-mood-cpu.svgz)

![LuxCoreRender - 场景: Orange Juice, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/luxcorerender-orange-juice-cpu.svgz)

![Embree - Pathtracer ISPC, 模型: Crown。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/embree-pathtracer-ispc-crown.svgz)

![Embree - Pathtracer ISPC, 模型: Asian Dragon。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/embree-pathtracer-ispc-asian-dragon.svgz)

![Embree - Pathtracer ISPC, 模型: Asian Dragon Obj。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/embree-pathtracer-ispc-asian-dragon-obj.svgz)

![Kvazaar 视频编码 - 输入: 4K, 预设: Medium。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/kvazaar-bosphorus-4k-medium.svgz)

![Kvazaar 视频编码 - 输入: 1080p, 预设: Medium。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/kvazaar-bosphorus-1080p-medium.svgz)

![Kvazaar 视频编码 - 输入: 4K, 预设: Ultra Fast。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/kvazaar-bosphorus-4k-ultra-fast.svgz)

![Kvazaar 视频编码 - 输入: 1080p, 预设: Super Fast。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/kvazaar-bosphorus-1080p-super-fast.svgz)

![OpenAPV 视频编码 - 预设: Fast, 输入: 4K。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/openapv-fast-bosphorus-4k.svgz)

![OpenAPV 视频编码 - 预设: Slow, 输入: 4K。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/openapv-slow-bosphorus-4k.svgz)

![OpenAPV 视频编码 - 预设: Medium, 输入: 4K。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/openapv-medium-bosphorus-4k.svgz)

![OpenAPV 视频编码 - 预设: Slow, 输入: 1080p。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/openapv-slow-bosphorus-1080p.svgz)

无论您是从事 3D 建模、视频编解码还是其他创意工作，对于那些考虑购买 HP ZBook Ultra G1a 这款高端移动工作站的用户来说，使用 Linux 通常能获得比 Windows 更好的性能。

![SVT-AV1 视频编码 - 预设: 5, 输入: 4K。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/svt-av1-preset-5-bosphorus-4k.svgz)

![SVT-AV1 视频编码 - 预设: 8, 输入: 4K。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/svt-av1-preset-8-bosphorus-4k.svgz)

![SVT-AV1 视频编码 - 预设: 8, 输入: 1080p。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/svt-av1-preset-8-bosphorus-1080p.svgz)

![x264 视频编码 - 输入: 4K。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/x264-bosphorus-4k.svgz)

![x264 视频编码 - 输入: 1080p。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/x264-bosphorus-1080p.svgz)

![Intel Open Image Denoise - 设备: 纯 CPU。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/intel-open-image-denoise-rtldr_alb_nrm3840x2160-cpu-only.svgz)

![7-Zip 压缩测试 - 压缩评分。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/7-zip-compression-compression-rating.svgz)

![7-Zip 压缩测试 - 解压评分。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/7-zip-compression-dr.svgz)

![Stockfish 国际象棋。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/stockfish-chess-benchmark.svgz)

![asmFish 国际象棋。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/asmfish-1hm2d.svgz)

![OSPRay Studio - 渲染器: Path Tracer, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/ospray-studio-1-1080p-16-path-tracer-cpu.svgz)

![OSPRay Studio - 渲染器: Path Tracer, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/ospray-studio-2-1080p-16-path-tracer-cpu.svgz)

![OSPRay Studio - 渲染器: Path Tracer, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/ospray-studio-3-1080p-32-path-tracer-cpu.svgz)

![LAME MP3 编码 - WAV 转 MP3。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/lame-mp3-encoding-wav-to-mp3.svgz)

![ASTC 编码器 - 预设: Fast。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/astc-encoder-fast.svgz)

![ASTC 编码器 - 预设: Medium。Windows 11 Pro 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/astc-encoder-medium.svgz)

![ASTC 编码器 - 预设: Very Thorough。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/astc-encoder-very-thorough.svgz)

![Blender - 文件: BMW27, 纯 CPU 计算。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/blender-bmw27-cpu-only.svgz)

![Blender - 文件: Junkshop, 纯 CPU 计算。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/blender-junkshop-cpu-only.svgz)

![IndigoBench - 场景: Bedroom, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/indigobench-cpu-bedroom.svgz)

![IndigoBench - 场景: Supercar, CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/indigobench-cpu-supercar.svgz)

![NeatBench - CPU 加速。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/neatbench-cpu.svgz)

![Chaos Group V-RAY - 模式: CPU。Ubuntu 25.04 胜出。](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/chaos-group-v-ray-cpu.svgz)

在数十个不同的创作者工作负载和其他真实软件用例中，这台搭载 AMD 锐龙 AI Max PRO 390 的笔记本（HP ZBook Ultra G1a）上的 Ubuntu 25.04，其性能表现通常都稳固地优于微软 Windows 11。在某些情况下，两者结果不相上下，但更多时候，在这台 AMD Strix Halo 移动工作站上，使用 Ubuntu Linux 能获得更佳的性能。

![胜出项目数量统计 (共 112 项测试)](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/number-of-first-place-finishes-wins-112-tests.svgz)

我们在搭载 [AMD 锐龙 AI Max PRO 390](https://www.phoronix.com/review/amd-ryzen-ai-max-390) 12 核 SoC 和 [Radeon 8050S 显卡](https://www.phoronix.com/review/amd-radeon-8050s-graphics) 的 HP ZBook Ultra G1a 上，分别在 Windows 11 和 Ubuntu 25.04 下进行了 [112 项基准测试](https://openbenchmarking.org/result/2506056-NE-WINDOWSAI25%26sgm%3D1%26ncb%3D1%26sor%26swl#results)。结果显示，**Ubuntu 25.04 在 66% 的测试中速度更快**。而微软 Windows 获胜的项目，通常集中在一部分图形基准测试中。

![所有测试结果的几何平均值](https://phoronix.com/benchmark/result/amd-ryzen-ai-max-pro-390-windows-11-pro-vs-ubuntu-linux-hp-zbook-ultra/geometric-mean-of-all-test-results-result-composite-aramp3w1pvulhzu.svgz)

从几何平均值来看，**Ubuntu 25.04 比 HP ZBook Ultra G1a 笔记本出厂预装的 OEM 版微软 Windows 11 专业版快了约 13%**。

![运行 Ubuntu Linux 的锐龙 AI MAX PRO 390 笔记本](https://www.phoronix.net/image.php?id=ryzen-ai-max-390-windows-linux&image=hp_max_390_med)

请记住，我们使用 Ubuntu 25.04 只是因为它在桌面/笔记本领域最为普及。正如我们之前的测试所示，切换到像 [CachyOS 和 Clear Linux 这样的发行版，可以在 AMD Strix Halo 上获得更大的性能提升](https://www.phoronix.com/review/amd-strix-halo-linux-7)。

对于那些希望购买 Strix Halo 驱动的 HP ZBook Ultra G1a 笔记本作为移动工作站，以处理繁重的创作者工作负载等任务的用户来说，Linux 可以提供相当可观的性能优势。ZBook Ultra G1a 目前的一个小缺点是其网络摄像头驱动尚未合并到上游内核——更多细节请参见我们的 [ZBook Ultra G1a 评测](https://www.phoronix.com/review/hp-zbook-ultra-g1a)，希望这个问题能在今年晚些时候得到解决。

---
# Phoronix网友热议

> 热议: https://www.phoronix.com/forums/forum/hardware/processors-memory/1554335-windows-11-vs-ubuntu-linux-performance-on-the-amd-ryzen-ai-max-pro-390-strix-halo

针对Phoronix发布的AMD Ryzen AI Max PRO 390 "Strix Halo"在Windows 11和Ubuntu Linux下的性能对比测试，网友们展开了激烈讨论。

讨论的核心围绕着测试结果中出现的性能差异。一方面，Linux在许多CPU密集型和部分Vulkan基准测试（如GravityMark和Xonotic）中展现出明显优势。但另一方面，Windows 11在多个3D图形基准测试中，尤其是在Unigine Heaven和FurMark中，取得了压倒性的领先，帧率差距甚至超过一倍。

支持Linux的网友普遍认为，这种图形性能上的落后是暂时的。主要原因是Strix Halo作为全新的硬件平台，其开源的Mesa/RADV驱动程序尚不成熟，不像Windows下的闭源驱动那样能得到厂商的早期优化和支持。他们相信随着时间的推移和社区的努力，Linux下的驱动性能会逐步追平甚至反超。有网友指出，Unigine Heaven和Furmark是两个较为极端的测试例，前者严重依赖曲面细分（Tessellation），后者更像是一个功耗“病毒”，其性能表现并不能完全代表真实游戏场景。

另一派观点则认为，Windows在图形性能上的优势是其生态成熟度的体现。一位名为“avis”的著名Windows支持者（被许多网友认为是“birdie”的马甲）发表长篇大论，详细列举了Windows的优点，如长达30年的API/ABI兼容性、稳定的驱动模型、统一的显示服务器以及庞大的软件和游戏库。他认为，尽管Linux在少数游戏中可能帧率更高，但其碎片化的生态、不稳定的API、以及无法运行所有主流游戏（尤其是有内核级反作弊的游戏）等问题，使其在桌面领域对普通用户毫无吸引力。这一观点引发了激烈的反驳和人身攻击，但也得到了一些用户的赞同。

关于Windows性能的讨论也引出了“系统臃肿”的话题。有网友指出，Windows 11默认开启的HVCI/VBS等安全功能会拖累性能，而微软官方推出的所谓“游戏优化版Windows”（默认不启动explorer.exe）则被Linux爱好者视为其承认自身系统臃肿的证据。对此，Windows支持者反驳称，这与Linux拥有不同用途的发行版是同样道理，是针对特定场景的正常优化。

此外，讨论还涉及了其他方面，例如有网友抱怨测试平台惠普笔记本的做工问题，也有人质疑Linux下高帧率是否以牺牲渲染质量为代价。整个讨论串充满了火药味，从技术辩论迅速升级为操作系统阵营间的“信仰之战”，充斥着对彼此观点的嘲讽和激烈的个人攻击，充分展现了Phoronix论坛一贯的“风貌”。

# 极客观点碰撞

看完了这场精彩的性能对决，你有什么想法？不妨在下方分享你的观点，让我们一起探讨：

1.  **操作系统之选：** 对于开发者和内容创作者来说，面对这样一台全新的高性能移动工作站，您会选择坚守熟悉的 Windows，还是拥抱性能更胜一筹的 Linux？您的决策主要基于哪些考量（如软件生态、易用性、性能、开发环境）？

2.  **开源的逆袭：** AMD 的开源显卡驱动（Mesa RADV）在 Vulkan 甚至光追性能上追平乃至反超 Windows 官方驱动，这在几年前是难以想象的。您如何看待开源驱动近年来的飞速发展？这是否会改变您对 Linux 游戏或专业应用的看法？

3.  **性能的取舍：** 本次测试中，Ubuntu 在 CPU 密集型任务上优势明显，但在部分图形测试中 Windows 仍有领先。您在自己的工作或娱乐场景中，对哪一方面的性能更为敏感？您是否曾因性能问题而切换过操作系统？

4.  **踩坑与成长：** 除了性能，硬件兼容性（如本次测试提到的摄像头）也是 Linux 用户常遇到的挑战。您在笔记本上使用 Linux 时遇到过哪些“坑”？又是如何解决的？欢迎分享您的经验和技巧！