
# 当AI遇上Linus: 重现那场著名的RISC-V内核补丁评审风波

近期，Linux内核的创始人兼首席维护者Linus Torvalds对一个RISC-V架构相关的补丁提出了尖锐的批评。这个补丁原本计划在Linux 5.17版本中合并，但由于存在一些严重问题，Linus要求开发团队必须对代码进行彻底修改，并在Linux 5.18版本的早期合并窗口重新提交。这一引人关注的事件的详细信息可以在 https://www.phoronix.com/news/Linux-6.17-RISC-V-Rejected 查看。
这让我产生了一个有趣的想法：如果让AI来模拟Linus的代码审查风格，会产生怎样的效果呢？让我们来做一个有趣的实验。

> **特别说明**：本文纯粹出于学习和研究目的。我们对补丁作者怀有最崇高的敬意 - 他们都是Linux内核社区的杰出贡献者。通过这种方式模拟Linus的代码审查风格，我们希望能更深入地理解Linux内核的开发流程和质量标准，同时也探索AI在技术评审领域的潜在应用价值。

**实验提示词如下**

```
学习linus的风格来review下下面的代码

From 0f2705c52e4a9fc19be7a622eb44244a57db877f Mon Sep 17 00:00:00 2001
From: Anup Patel <apatel@ventanamicro.com>
Date: Mon, 28 Jul 2025 15:10:11 +0530
Subject: RISC-V: Add defines for the SBI message proxy extension

Add defines for the new SBI message proxy extension which is part
of the SBI v3.0 specification.

Reviewed-by: Atish Patra <atishp@rivosinc.com>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Co-developed-by: Rahul Pathak <rpathak@ventanamicro.com>
Signed-off-by: Rahul Pathak <rpathak@ventanamicro.com>
Signed-off-by: Anup Patel <apatel@ventanamicro.com>
Link: https://lore.kernel.org/r/20250728094032.63545-4-apatel@ventanamicro.com
Signed-off-by: Palmer Dabbelt <palmer@dabbelt.com>
---
 arch/riscv/include/asm/sbi.h | 63 ++++++++++++++++++++++++++++++++++++++++++++
 include/linux/wordpart.h     |  8 ++++++
 2 files changed, 71 insertions(+)

diff --git a/arch/riscv/include/asm/sbi.h b/arch/riscv/include/asm/sbi.h
index 341e74238aa04e..22f6e70cd32e40 100644
--- a/arch/riscv/include/asm/sbi.h
+++ b/arch/riscv/include/asm/sbi.h
@@ -10,6 +10,7 @@
 #include <linux/types.h>
 #include <linux/cpumask.h>
 #include <linux/jump_label.h>
+#include <linux/wordpart.h>
 
 #ifdef CONFIG_RISCV_SBI
 enum sbi_ext_id {
@@ -36,6 +37,7 @@ enum sbi_ext_id {
 	SBI_EXT_STA = 0x535441,
 	SBI_EXT_NACL = 0x4E41434C,
 	SBI_EXT_FWFT = 0x46574654,
+	SBI_EXT_MPXY = 0x4D505859,
 
 	/* Experimentals extensions must lie within this range */
 	SBI_EXT_EXPERIMENTAL_START = 0x08000000,
@@ -430,6 +432,67 @@ enum sbi_fwft_feature_t {
 
 #define SBI_FWFT_SET_FLAG_LOCK			BIT(0)
 
+enum sbi_ext_mpxy_fid {
+	SBI_EXT_MPXY_GET_SHMEM_SIZE,
+	SBI_EXT_MPXY_SET_SHMEM,
+	SBI_EXT_MPXY_GET_CHANNEL_IDS,
+	SBI_EXT_MPXY_READ_ATTRS,
+	SBI_EXT_MPXY_WRITE_ATTRS,
+	SBI_EXT_MPXY_SEND_MSG_WITH_RESP,
+	SBI_EXT_MPXY_SEND_MSG_WITHOUT_RESP,
+	SBI_EXT_MPXY_GET_NOTIFICATION_EVENTS,
+};
+
+enum sbi_mpxy_attribute_id {
+	/* Standard channel attributes managed by MPXY framework */
+	SBI_MPXY_ATTR_MSG_PROT_ID		= 0x00000000,
+	SBI_MPXY_ATTR_MSG_PROT_VER		= 0x00000001,
+	SBI_MPXY_ATTR_MSG_MAX_LEN		= 0x00000002,
+	SBI_MPXY_ATTR_MSG_SEND_TIMEOUT		= 0x00000003,
+	SBI_MPXY_ATTR_MSG_COMPLETION_TIMEOUT	= 0x00000004,
+	SBI_MPXY_ATTR_CHANNEL_CAPABILITY	= 0x00000005,
+	SBI_MPXY_ATTR_SSE_EVENT_ID		= 0x00000006,
+	SBI_MPXY_ATTR_MSI_CONTROL		= 0x00000007,
+	SBI_MPXY_ATTR_MSI_ADDR_LO		= 0x00000008,
+	SBI_MPXY_ATTR_MSI_ADDR_HI		= 0x00000009,
+	SBI_MPXY_ATTR_MSI_DATA			= 0x0000000A,
+	SBI_MPXY_ATTR_EVENTS_STATE_CONTROL	= 0x0000000B,
+	SBI_MPXY_ATTR_STD_ATTR_MAX_IDX,
+	/*
+	 * Message protocol specific attributes, managed by
+	 * the message protocol specification.
+	 */
+	SBI_MPXY_ATTR_MSGPROTO_ATTR_START	= 0x80000000,
+	SBI_MPXY_ATTR_MSGPROTO_ATTR_END		= 0xffffffff
+};
+
+/* Possible values of MSG_PROT_ID attribute as-per SBI v3.0 (or higher) */
+enum sbi_mpxy_msgproto_id {
+	SBI_MPXY_MSGPROTO_RPMI_ID = 0x0,
+};
+
+/* RPMI message protocol specific MPXY attributes */
+enum sbi_mpxy_rpmi_attribute_id {
+	SBI_MPXY_RPMI_ATTR_SERVICEGROUP_ID = SBI_MPXY_ATTR_MSGPROTO_ATTR_START,
+	SBI_MPXY_RPMI_ATTR_SERVICEGROUP_VERSION,
+	SBI_MPXY_RPMI_ATTR_IMPL_ID,
+	SBI_MPXY_RPMI_ATTR_IMPL_VERSION,
+	SBI_MPXY_RPMI_ATTR_MAX_ID
+};
+
+/* Encoding of MSG_PROT_VER attribute */
+#define SBI_MPXY_MSG_PROT_VER_MAJOR(__ver)	upper_16_bits(__ver)
+#define SBI_MPXY_MSG_PROT_VER_MINOR(__ver)	lower_16_bits(__ver)
+#define SBI_MPXY_MSG_PROT_MKVER(__maj, __min)	make_u32_from_two_u16(__maj, __min)
+
+/* Capabilities available through CHANNEL_CAPABILITY attribute */
+#define SBI_MPXY_CHAN_CAP_MSI			BIT(0)
+#define SBI_MPXY_CHAN_CAP_SSE			BIT(1)
+#define SBI_MPXY_CHAN_CAP_EVENTS_STATE		BIT(2)
+#define SBI_MPXY_CHAN_CAP_SEND_WITH_RESP	BIT(3)
+#define SBI_MPXY_CHAN_CAP_SEND_WITHOUT_RESP	BIT(4)
+#define SBI_MPXY_CHAN_CAP_GET_NOTIFICATIONS	BIT(5)
+
 /* SBI spec version fields */
 #define SBI_SPEC_VERSION_DEFAULT	0x1
 #define SBI_SPEC_VERSION_MAJOR_SHIFT	24
diff --git a/include/linux/wordpart.h b/include/linux/wordpart.h
index 5a7b97bb7c9569..ed871773003707 100644
--- a/include/linux/wordpart.h
+++ b/include/linux/wordpart.h
@@ -31,6 +31,14 @@
  */
 #define lower_16_bits(n) ((u16)((n) & 0xffff))
 
+/**
+ * make_u32_from_two_u16 - return u32 number by combining
+ * two u16 numbers.
+ * @hi: upper 16 bit number
+ * @lo: lower 16 bit number
+ */
+#define make_u32_from_two_u16(hi, lo)	(((u32)(hi) << 16) | (u32)(lo))
+
 /**
  * REPEAT_BYTE - repeat the value @x multiple times as an unsigned long value
  * @x: value to repeat
-- 
cgit 1.2.3-korg
```

**下面是AI给的回复**

好的，没问题。我会戴上我的“Linus Torvalds”帽子，用他的标志性风格来 review 这段代码。

---

**主题：Re: [PATCH] RISC-V: Add defines for the SBI message proxy extension**

各位，

这代码有些地方看起来还行，但有些地方简直是在浪费我的时间。我们一个个来看。

**首先，最让我恼火的是对 `include/linux/wordpart.h` 的改动。**

```c
+/**
+ * make_u32_from_two_u16 - return u32 number by combining
+ * two u16 numbers.
+ * @hi: upper 16 bit number
+ * @lo: lower 16 bit number
+ */
+#define make_u32_from_two_u16(hi, lo)	(((u32)(hi) << 16) | (u32)(lo))
```

搞什么鬼？

你为了在一个 *特定架构* 的头文件里用一次，就往一个 *通用* 的头文件里塞一个新宏？绝对不行。

这个宏完全是多余的垃圾。`(((u32)(hi) << 16) | (u32)(lo))` 这行代码本身就足够清晰了，任何一个合格的C程序员都看得懂。你加一个宏，除了让代码更难追踪之外，没有任何好处。我们不需要为这种鸡毛蒜皮的小事发明新的“帮助”宏。

把它从 `wordpart.h` 里删掉。彻彻底底地。如果你们在 RISC-V 的代码里实在懒得打那几个字符，那就在你们自己的 `asm/sbi.h` 里定义一个静态内联函数或者本地宏。**不要污染全局命名空间。**

这是基本常识，犯这种错误简直不可原谅。

**其次，再看看 `arch/riscv/include/asm/sbi.h` 里的东西。**

```c
enum sbi_mpxy_attribute_id {
	/* Standard channel attributes managed by MPXY framework */
	SBI_MPXY_ATTR_MSG_PROT_ID		= 0x00000000,
	SBI_MPXY_ATTR_MSG_PROT_VER		= 0x00000001,
	SBI_MPXY_ATTR_MSG_MAX_LEN		= 0x00000002,
    ...
```

这些 `0x00000000` 是什么玩意儿？你在搞笑吗？

这是一个简单的枚举，值是 0, 1, 2... 编译器会自动帮你做这件事。你非要手动写上这些丑陋的、带着一堆零的十六进制数，是想证明什么？这只会让代码变得臃肿不堪，毫无意义。

删掉那些 ` = 0x...` 的部分，让它回归一个正常 `enum` 该有的样子。像下面这样：

```c
enum sbi_mpxy_attribute_id {
	SBI_MPXY_ATTR_MSG_PROT_ID,
	SBI_MPXY_ATTR_MSG_PROT_VER,
	...
```
这不干净多了吗？

还有，命名不一致的问题：

```c
	SBI_MPXY_ATTR_STD_ATTR_MAX_IDX,
```
和
```c
enum sbi_mpxy_rpmi_attribute_id {
    ...
	SBI_MPXY_RPMI_ATTR_MAX_ID
};
```

一个是 `_MAX_IDX`，一个是 `_MAX_ID`。你们就不能统一一下吗？这种小细节反映了代码的质量和作者的用心程度。挑一个，然后坚持用下去。

最后，回到那个让我火大的宏：

```c
/* Encoding of MSG_PROT_VER attribute */
#define SBI_MPXY_MSG_PROT_VER_MAJOR(__ver)	upper_16_bits(__ver)
#define SBI_MPXY_MSG_PROT_VER_MINOR(__ver)	lower_16_bits(__ver)
#define SBI_MPXY_MSG_PROT_MKVER(__maj, __min)	make_u32_from_two_u16(__maj, __min)
```

`upper_16_bits` 和 `lower_16_bits` 的用法没问题，它们是已有的、合理的抽象。但 `SBI_MPXY_MSG_PROT_MKVER` 又用了那个本不该存在的 `make_u32_from_two_u16`。

按照我上面说的，删掉 `wordpart.h` 的改动，然后把这里直接改成：

```c
#define SBI_MPXY_MSG_PROT_MKVER(maj, min)	(((u32)(maj) << 16) | (u32)(min))
```

另外，`__maj` 和 `__min` 这种双下划线的参数名是想干嘛？你以为你在写内核内部的什么魔法吗？别这么做。普通的 `maj` 和 `min` 就够了。别耍小聪明。

**总结一下：**

1.  **必须** 撤销对 `include/linux/wordpart.h` 的所有改动。这是不可协商的。
2.  清理 `sbi.h` 里的 `enum` 定义，去掉那些多余的、丑陋的赋值。
3.  统一 `_MAX_IDX` 和 `_MAX_ID` 的命名。
4.  直接在 `SBI_MPXY_MSG_PROT_MKVER` 中实现组合逻辑，并使用正常的参数名。

其他的定义（比如 `BIT()` 的使用）看起来是合理的，说明你们至少在某些地方还是清醒的。

把这些愚蠢的问题改好再发过来。别再浪费大家的时间了。

   Linus


如果Linus能鼓励向的Review这个代码，他可能会怎么说呢。

**提示词**: `能不能让Linus鼓励向的Review这个代码`

当然可以！这是一个非常有意思的尝试。

要让 Linus 的风格变得“鼓励”，关键在于保留他那种**一针见血、注重代码原则和简洁性**的核心特质，但把攻击性的语言换成**建设性的指导**和**对开发者努力的肯定**。他不会说“你写的真棒”，而会说“这个方向是对的，但我们可以做得更好”。

下面，我将用这种“严师出高徒”式的鼓励风格，重新 review 一遍代码。

---

### 鼓励向的“Linus”风格 Review

**主题：Re: [PATCH] RISC-V: Add defines for the SBI message proxy extension**

各位，

很高兴看到 RISC-V 对新 SBI 规范的支持工作在稳步推进。这个 Message Proxy 扩展很重要，感谢你们为此付出的努力。

我看了一下代码，整体思路是正确的，为新功能加入了必要的定义。不过，为了让这个补丁更好地融入内核，我有几个建议，希望能帮助你们在下个版本中把它打磨得更出色。

**我们先来看看对 `include/linux/wordpart.h` 的改动。**

```c
+/**
+ * make_u32_from_two_u16 - return u32 number by combining
+ * two u16 numbers.
+ * @hi: upper 16 bit number
+ * @lo: lower 16 bit number
+ */
+#define make_u32_from_two_u16(hi, lo)	(((u32)(hi) << 16) | (u32)(lo))
```

我明白你们想创建一个帮助宏来提高代码可读性的初衷，这个想法是好的。

**但是，** 我们对通用头文件（比如 `wordpart.h`）的修改需要非常谨慎。一个好的原则是：**不要为了单一的、特定于某个架构的用途，而向一个全局的、通用的头文件里添加新东西。** 这会让通用头文件变得臃肿，也可能在未来引发意想不到的冲突。

更简洁的做法是，直接在你们的 `arch/riscv/include/asm/sbi.h` 文件里处理它。`(((u32)(maj) << 16) | (u32)(min))` 这个表达式本身已经足够清晰，或者如果你们真的非常希望有一个宏，可以在 `sbi.h` 本地定义它。

所以，我的建议是：**请撤销对 `wordpart.h` 的改动。** 这样做能让你的补丁更聚焦于它本身要解决的问题，也更容易被接受。

**接下来，是 `arch/riscv/include/asm/sbi.h` 里的一些小细节。**

```c
enum sbi_mpxy_attribute_id {
	/* Standard channel attributes managed by MPXY framework */
	SBI_MPXY_ATTR_MSG_PROT_ID		= 0x00000000,
	SBI_MPXY_ATTR_MSG_PROT_VER		= 0x00000001,
	...
```

这里有一个提升代码整洁度的小机会。对于像这样从 0 开始连续递增的 `enum`，你其实不需要显式地给它们赋值。编译器会自动处理得很好。

如果去掉这些 `= 0x...` 的部分，代码会变成这样：

```c
enum sbi_mpxy_attribute_id {
	SBI_MPXY_ATTR_MSG_PROT_ID,
	SBI_MPXY_ATTR_MSG_PROT_VER,
	...
```
你看，这样是不是更干净、更易读了？这是内核编码风格中我们所推崇的简洁性。

另外，我注意到命名上有一个微小的不一致：
`SBI_MPXY_ATTR_STD_ATTR_MAX_IDX` 和 `SBI_MPXY_RPMI_ATTR_MAX_ID`。

一个是 `_MAX_IDX`，一个是 `_MAX_ID`。为了保持代码的整体一致性，建议你们统一一下风格。细节决定成败，对吧？

**最后一点，关于宏的参数命名：**

```c
#define SBI_MPXY_MSG_PROT_MKVER(__maj, __min)	...
```
在内核代码中，我们通常会避免使用双下划线开头的参数名（比如 `__maj`），因为这通常是为编译器或库的内部实现保留的。直接使用 `maj` 和 `min` 这样的普通名字就可以了，它们清晰明了，也符合我们的编码习惯。

**总结一下：**

1.  **撤销对 `wordpart.h` 的修改**，保持通用头文件的纯净。
2.  **清理 `enum` 定义**，移除不必要的显式赋值，让代码更简洁。
3.  **统一 `_MAX_ID` / `_MAX_IDX` 的命名**，提升代码一致性。
4.  **调整宏参数的命名风格**，使用常规的参数名。

这些都是小调整，但它们共同构成了高质量内核代码的基础。

总的来说，这是一个很好的补丁，它正在做正确的事情。把上面提到的这些小细节打磨一下，再提交一版，我相信它会变得非常出色。

期待看到你们的 v2 版本！

   Linus
