# 股权激励开放指南

> 翻译自 https://github.com/jlevy/og-equity-compensation/blob/master/README.md
>

❇️ *本指南现已[在 Holloway 上发布](https://www.holloway.com/g/equity-compensation/about)。
请在那里阅读，以获得搜索、书签/高亮、专家评论以及 PDF/EPUB 下载功能。*

> **PPT版本参见**: https://aichipera.github.io/github-trend/daily/2025-04-15/og-equty-ppt.html


## 引言

**股权激励**是指授予公司部分所有权以换取劳动成果的做法。
在其理想形式下，股权激励将个体员工的利益与他们所服务公司的目标结合起来，这可以在团队建设、创新和员工留任方面产生显著效果。
这些因素中的每一个都[有助于](#history-and-significance)创造价值——为公司、为其用户和客户，以及为那些努力使其成功的个人创造价值。

将股权作为薪酬[授予的方式](#how-equity-is-granted)——包括限制性股票、股票期权和限制性股票单位——**极其复杂**。股权激励涉及令人困惑的术语、法律上的模糊之处，以及对授予者和接受者而言许多高风险的决策。

如果你与足够多的员工和招聘经理交谈，你会听到他们或他们的同事因未能事先充分了解而遭遇痛苦后果的故事。
虽然许多人通过个人经验、同事或经历过此事的热心朋友了解到基本概念，但股权激励的复杂细节最好由税务律师、公司律师和其他专业人士来理解。

与[谈判录用邀约](#offers-and-negotiations)和[行使股票期权](#stock-option-scenarios)相关的决策，尤其可能产生**重大的财务后果**。由于员工股权的价值取决于公司的命运，员工的股权可能在很长一段时间内[缺乏流动性](#what-is-private-stock-worth)，或者最终[一文不值](#growth-and-risk)，而税收和行权成本（如果适用）可能无法收回。
即使公司经营良好，员工也可能因未能预见其决策的税务后果而遭遇[灾难性的税务陷阱](#tax-dangers)。

理解股权激励的技术细节并不能保证幸运之神会像眷顾 Facebook 的[早期员工](#history-and-significance)那样温暖地眷顾你。但全面的概述可以帮助你在[与专业人士讨论](#seeking-professional-advice)以寻求进一步帮助时更有见地，为你的个人情况做出更好的决策，并避免一些[常见](#tax-dangers)且[代价高昂](#the-amt-trap)的错误。

### 为何撰写本指南？

本书的第一版由与您正在阅读的这一版相同的首席作者撰写，在
[Hacker News](https://news.ycombinator.com/item?id=10880726)、
[GitHub](https://github.com/jlevy/og-equity-compensation) 以及个别专家那里收到了大量的反馈和讨论。
现在，Holloway 很荣幸发布本指南的新版本。
我们扩展了章节，增加了资源和视觉效果，并填补了空白。

关于股权激励，[有很多信息](#further-reading)分散在各种博客和文章中，这些文章通常关注该主题的特定组成部分，例如归属、股票期权的类型或股权水平。
我们认为有必要建立一个整合共享的资源，由薪酬决策不同方面的人士（包括员工、招聘经理、创始人和学生）撰写并为他们服务。
任何人面对这个主题所涉及的复杂细节和高风险个人选择时，都可能感到不知所措。
本参考资料旨在满足初学者和更有经验者的需求。

Holloway 和我们的贡献者的动机只有一个：
帮助读者充分理解重要细节及其背景，以便他们自己做出更好的决策。
本指南旨在做到**实用**（提供具体建议和应避免的陷阱）、**周到**（提供背景和多个专家观点，包括对有争议话题的不同意见）和**简洁**（内容密集但仅包含值得注意的细节——尽管如此，至少需要三个小时阅读，并链接到三百个来源！）。

本指南并不声称完美或完整。
像这样的参考资料总是在不断完善中。
这就是为什么我们目前正在测试一些功能，以便 Holloway 社区能够提出改进建议、贡献新章节，并指出任何需要修订的地方。
我们欢迎（并将欣然致谢）[您的帮助](#please-help)。

我们特别希望[感谢](#credits)迄今为止以及将来帮助撰写、审阅、编辑和改进本指南的数十位人士——并希望您能经常回来查看其改进情况。

### 范围

本指南**目前涵盖**：

-   **美国** **C 型公司**的股权激励。
-   私营公司（从初创公司到大型私营公司）中大多数员工、顾问和独立承包商的股权激励。
-   对上市公司股权激励的有限覆盖。

**尚未涵盖**的主题：

-   上市公司的股权激励计划，例如 [ESPPs](https://www.investopedia.com/terms/e/espp.asp)（员工股票购买计划）。
    （我们希望将来[看到这方面的改进](#please-help)。）
-   高管股权激励的全部细节。
-   美国境外的薪酬。
-   C 型公司以外的公司（包括 [LLCs](https://en.wikipedia.org/wiki/Limited_liability_company)（有限责任公司）和 [S 型公司](https://en.wikipedia.org/wiki/S_corporation)）的薪酬，这些公司的股权激励方式和实践截然不同。

对于这些情况，请参阅[其他资源](#when-to-turn-elsewhere)并获取[专业建议](#seeking-professional-advice)。

### 谁可能会觉得本指南有用

我们的目标是既对初学者有帮助，也对更有经验的人有帮助。
通过与员工、CEO、投资者和律师的交谈，我们可以向您保证，无论您对股权激励了解多少，您都可能在某个时候遇到困惑。

如果您是**员工**或**求职者**，以下某些情况可能适用于您：

-   您听说过诸如*股票*、*股票期权*、*行权价*、*ISOs*、*RSUs*、*83(b) 选择权*、*409A 估值*、*AMT*或*提前行权*等短语，并且知道它们可能很重要，但对其真正含义或是否适用于您的情况感到困惑。
-   您正在考虑一份工作邀约，但不知道如何[处理或谈判](#offers-and-negotiations)邀约中的股权部分。
-   您是第一次加入初创公司，被所有[文书工作](#documents-and-agreements)弄得不知所措。
-   您即将离职、休假，或者在一家您拥有股票或期权的公司被裁员或解雇，并且正在思考相关的决策和后果。
-   您工作的公司正在经历收购、IPO 或倒闭。
-   您拥有私营公司的股票并[需要现金](#stock-option-scenarios)。

需要与员工或潜在雇员讨论股权激励的**创始人**或**招聘经理**也会发现本指南很有用。
正如许多企业家和招聘经理会告诉您的那样，这个话题在谈判桌的另一边也不容易！
与候选人谈判以及回答候选人和员工的问题，都需要充分理解股权激励的同样复杂的技术细节。

话虽如此，这个主题**并不简单**，我们要求读者愿意投入时间来理解大量令人困惑的细节。
如果您很匆忙，或者您不关心了解细节，本指南可能不适合您。[寻求建议](#seeking-professional-advice)。

### 关于公平性的说明

您读到的关于股权激励的大部分内容都是由单一个人从单一角度撰写的。
本指南的作者和编辑从员工、招聘经理、创始人和律师的角度，都经历过股权激励的领域。
我们确实相信，这里的知识，[结合专业建议](#seeking-professional-advice)，可以为**员工和招聘经理双方**带来显著的差异。

候选人在谈判股权激励时遇到的困难之一是，他们可能比招聘他们的人更少了解自己的价值信息。
公司会与许多候选人交谈，并且通常能够访问或购买昂贵的市场薪酬数据。
虽然一些关于[典型员工股权水平](#typical-employee-equity-levels)的数据已经在网上公布，但其中大部分未能代表具有特定经验、担任特定职位的候选人的价值。
然而，即使没有确切的数据，候选人和招聘经理也可以建立更好的思维框架来思考[录用邀约和谈判](#offers-and-negotiations)。

另一方面，挑战并不仅限于员工。
创始人和招聘经理也常常难以向潜在雇员解释清楚各种技术细节，并且在发出录用邀约时也可能做出同样糟糕的决策。无论是对员工薪酬过高还是过低，都可能产生不幸的后果。

简而言之，在股权激励方面，公司和员工都经常因信息不足的决策和代价高昂的错误而受到损害。
一个共享的资源对双方都有帮助。

## 路线图

### Holloway 阅读器

您现在使用的 Holloway 阅读器旨在帮助您查找和浏览所需的材料。**请使用搜索框。**
它将显示定义、分节结果以及指南中**我们链接到的数百个资源**中包含的内容。
把它想象成一个关于股权激励最佳内容的小型图书馆。
在您阅读时，我们还为**术语定义**、相关章节建议和外部链接提供鼠标悬停（或在移动设备上短按）提示。

### 本指南的组织结构

本指南包含大量材料。
而且内容密集。
有些读者可能希望从头到尾阅读，但您也可以**搜索或直接导航**到您感兴趣的部分，**根据需要参考**基础主题。

股权激励位于公司法、税法和员工薪酬的交叉点，因此需要对这三者都有一些基本的了解。
您可能认为薪酬和税收是两个独立的主题，但它们如此紧密地交织在一起，以至于脱离其中一个来解释另一个会产生误导。
我们按逻辑顺序涵盖材料，因此，如果您确实先阅读了前面的章节，后面关于税收和薪酬相互作用的章节将会更清晰。

我们从[**股权激励基础知识**](#equity-compensation-basics)开始：什么是薪酬和股权，以及为什么使用股权作为薪酬。

但在我们深入探讨之前，我们需要谈谈什么是股票，以及公司是如何组建的。[**股份公司基础知识**](#fundamentals-of-stock-corporations)涵盖了公司如何组织其所有权、如何发行股票、上市公司和私营公司，以及 IPO 和流动性（这决定了股权何时能兑现）。

虽然并非每个阅读本文的人都在早期公司工作，但那些在早期公司工作的人可以通过了解股权在[**初创公司与增长**](#startups-and-growth)中的作用而受益。这对于任何参与已获得风险投资的私营公司的人来说都是很好的背景知识。

[**股权授予方式**](#how-equity-is-granted)是本指南的核心。
我们描述了最常见的股权授予形式，包括限制性股票授予、股票期权和限制性股票单位 (RSU)。

现在情况变得更复杂了——税收：

-   [**税务基础知识**](#tax-basics)：关于税收如何运作的技术摘要。
    股权激励的许多令人头疼的问题都涉及其征税方式，包括普通所得税、长期资本利得税，以及鲜为人知但有时至关重要的替代性最低税 (AMT)。
-   [**股权激励的税收**](#taxes-on-equity-compensation)：您应缴纳多少税款很大程度上取决于您拥有的股权类型（例如限制性股票奖励、股票期权或 RSU）、您选择何时支付（包括 83(b) 选择权）以及您选择何时行使期权。

在讨论了这些技术问题之后，我们将转向如何在实践中思考这一切。这些章节侧重于员工和候选人常见的情景，但也可能引起创始人和招聘经理的兴趣：

-   [**计划与情景**](#plans-and-scenarios)：无论您现在拥有股权还是将来会拥有，学习*如何思考*股权的价值及其税务负担都很有帮助。我们还涵盖了您是否可以[出售私人股票](#can-you-sell-private-stock)。
-   [**录用邀约与谈判**](#offers-and-negotiations)：在您谈判或考虑是否接受工作邀约时，股权问题经常出现。
    这里我们涵盖了预期情况、应询问的问题、技巧和陷阱等等。

最后，我们提供一些额外的资源：

-   [**文件与协议**](#documents-and-agreements)：关于您在谈判和接受录用邀约后可能看到的实际法律文书的更多细节。
-   [**进一步阅读**](#further-reading)：一份精选的关于该主题的其他阅读材料清单，包括许多为本指南提供信息的论文、书籍和文章。

🚧 是否应该增加一个“寻求帮助”部分，概述何时向谁寻求专业帮助？

### 何时寻求其他资源

**首席执行官 (CEO)**、**首席财务官 (CFO)**、**首席运营官 (COO)**，或任何运营公司或有一定规模团队的人，都应确保与股权激励顾问或律师事务所的专家交谈，以了解股权激励计划。

**创始人**如果想初步了解运营公司的法律问题，除了咨询律师外，可能希望查阅 Clerky 的 [*创始人法律概念*](https://handbook.clerky.com/)。
创始人还应向他们的投资者寻求建议，因为投资者可能有额外的经验。

大型或上市公司的**高管薪酬**是一个更加微妙的话题，对谈判双方都是如此。
聘请经验丰富的律师或薪酬顾问。
关于高管薪酬，有广泛的法律[资源](https://www.compensationstandards.com/home/)可供查阅。

### 寻求专业建议

本指南不能替代专业建议。

请阅读完整的[免责声明](#disclaimer)，并在做出重大决策前，向律师、税务专业人士或其他薪酬专家寻求专业建议。

这是否意味着通读这些细节是浪费时间？
完全不是。重要的决策很少应该或能够盲目委托他人。
本指南*补充而非取代*您从专业人士那里获得的建议。
当您自己对主题有所了解并知道该问什么问题时，在专业人士的支持下工作可以帮助您做出更好的决策。

## 股权激励基础知识

### 历史与意义

从两人初创公司到[财富 500 强](http://fortune.com/fortune500/)企业，都发现授予公司部分所有权是吸引和留住杰出人才的最佳方法之一。
在美国，自 20 世纪 50 年代以来，通过[股票期权](#stock-options)实现的部分所有权一直是高管和其他员工薪酬的关键组成部分。[^corpgovlaw.6vw7qt]
根据美国国家员工持股中心 (National Center for Employee Ownership) 的数据，就在 2014 年，私营部门所有员工中有 **7.2%**（**850 万人**）以及拥有股票的公司*所有*员工中有 **13.1%** 持有股票期权。[^nceoorgass.x6588n]
许多人认为员工持股[💰促进了技术创新](https://www.wsj.com/articles/reviving-the-flagging-spirit-of-silicon-valley-1428706671)，尤其是在硅谷，从惠普的[早期](http://www.hp.com/hpinfo/abouthp/histnfacts/publications/measure/pdf/1976_07.pdf)到像 Facebook 这样的近期例子。
股票期权帮助 Facebook 的前 3000 名员工在公司上市时获得了大约 **230 亿美元**的财富。[^ftcomconte.x613np]

🌪 围绕高薪高管使用股权激励存在一些争议。
上市公司向高管提供股权激励，很大程度上是因为存在税收漏洞。1993 年，比尔·克林顿总统试图通过《国内税收法典》的一个新条款[^treasurygo.tbpcyx]来限制高管薪酬。
不幸的是，该立法适得其反；
一个漏洞使得基于绩效的薪酬——包括股票期权——可以完全抵税，从而极大地刺激了通过股票期权支付高管薪酬的做法。[^epiorgpubl.cq5o0o]
从 1970 年至 1979 年，美国 50 家最大公司 CEO 的平均薪酬为 **120 万美元**，其中 **11.2%** 来自股票期权。
到 2000 年至 2005 年，同样的数字分别上升到 **920 万美元**和 **37%**。[^nberorgpap.wtsymr]

### 增长与风险

通常，股权激励与公司的**增长**密切相关。
现金匮乏的初创公司通过提供有意义的[所有权份额](#typical-employee-equity-levels)来说服早期员工接受减薪并加入团队，迎合了人们希望公司有朝一日能发展壮大到足以[上市](#ipos)或以可观的价格[被出售](#sales-and-liquidity)的期望。
对于许多求职者来说，与高额现金薪酬相比，提供与所有权挂钩的薪酬对于更成熟但仍在快速增长的公司更具吸引力。

然而，伴随着增长希望的还有**风险**。大型、快速增长的公司常常遭遇困境。
而[初创公司](#startups-and-growth)经常失败，或者无法为投资者或员工带来任何回报。根据剑桥联合公司 (Cambridge Associates) 和《财富》杂志的[一份报告](http://fortune.com/2017/06/27/startup-advice-data-failure/)，在 1990 年至 2010 年间，**约 60%** 的风险投资支持的公司回报低于原始投资，让员工痛苦地意识到他们的初创公司实际上并非下一个谷歌。在剩下的 **40%** 中，只有少数几家公司能让许多员工致富，就像星巴克[^investoped.aaps6n]、UPS[^moneycnnco.80o8bh]、亚马逊[^techcrunch.9ucopn]、谷歌[^dealbookny.es6h1j]或 Facebook[^enwikipedi.q7bc95] 等标志性的高增长公司那样。

### 薪酬与股权

🄳 **薪酬**是指为个人（包括员工、承包商、顾问、创始人和董事会成员）向公司提供服务或劳动而支付的任何报酬。
薪酬的形式包括现金工资（薪水和任何奖金）以及任何非现金报酬，包括像健康保险、家庭相关保障、福利和退休计划等[福利](https://en.wikipedia.org/wiki/Employee_benefits#United_States)。

公司的薪酬策略[远非简单](http://firstround.com/review/counterintuitive-comp-tips-for-the-unwary-and-uninitiated/)。
风险基金 Homebrew 的人才主管 Beth Scheer 对初创公司的薪酬进行了[周到的概述](https://quip.com/HEB3Ah9dYD6o)。

您可能遇到的另一个术语是
[*全面薪酬 (total rewards)*](https://www.worldatwork.org/total-rewards-model/)，它指的是一种吸引和留住员工的模型，该模型结合了薪水和激励性薪酬（如股权）、福利、对贡献或承诺的认可（如奖励和奖金）、培训计划以及改善工作环境的举措。

🄳 在薪酬和投资的背景下，**股权**广义上指个人（如员工或董事会成员）和其他企业（如风险投资公司）可以持有的公司任何形式的所有权。
一种常见的股权是股票，但股权也可以采取其他形式，例如赋予所有权权利的股票期权或认股权证。
通常，股权还附带某些条件，例如归属或回购权。
注意，术语*股权 (equity)* 在会计和房地产领域还有[其他几个](https://www.investopedia.com/terms/e/equity.asp)技术含义。

🄳 [**股权激励 (Equity compensation)**](http://www.investopedia.com/terms/e/equity-compensation.asp) 是指授予股权以换取工作的做法。

在本指南中，我们重点关注股份公司的股权激励，这种公司的所有权由股票代表。
（我们将在[下一节](#fundamentals-of-stock-corporations)更详细地描述股票。）
以直接授予无附加条件的股票形式进行的股权激励非常罕见。取而代之的是，员工获得的股票附带额外的限制条件，或者被授予日后可能导致拥有股票的合同权利。
这些股权激励形式包括限制性股票、股票期权和限制性股票单位，我们将[详细描述](#how-equity-is-granted)每一种形式。

### 股权激励的目标

股权激励的目的有三个：

-   **吸引和留住人才。**
    当一家公司已经或预计将取得显著的财务成功时，有才华的人会受到其股权未来可能[价值连城](https://www.entrepreneur.com/article/253438)前景的[激励](https://avc.com/2010/10/employee-equity-options/)而为公司工作。
    获得改变生活的财富的实际概率可能很低（或者至少，比您仅仅通过观看《社交网络》而了解的初创公司情况要低）。
    但即使是很小的成功机会，对许多人来说也值得冒险，对某些人来说，风险本身就可能令人兴奋。
-   **统一激励机制。**
    即使是能够支付大量现金的公司也可能更愿意给予员工股权，以便员工努力提高公司的*未来*价值。
    通过这种方式，股权将个人激励与公司利益统一起来。
    在最好的情况下，这种理念培养了团队合作的环境和“水涨船高”的心态。
    它还鼓励所有相关人员进行[长期思考](https://www.cebglobal.com/blogs/equity-compensation-will-stop-short-termism-and-boost-growth/)，这对于公司的成功至关重要。
    正如我们将在[后面讨论](#offers-and-negotiations)的那样，您获得的股权数量通常既反映了您对公司的贡献，也反映了您未来对公司的承诺。
-   **减少现金支出。**
    通过给予股权，公司通常可以减少目前支付给员工的现金薪酬，希望以后能回报他们，并将这笔钱用于其他投资或运营费用。
    这在公司早期阶段或其他可能没有足够收入支付高薪的时期至关重要。
    股权激励还可以帮助招聘那些原本薪酬要求特别高的资深员工或高管。

🚧 提及或链接到锁定期等。

## 股份公司基础知识

在本节中，我们将描述股票和股份使用的基本原理。

熟悉股票、股份公司、上市公司和私营公司的人可以[跳到](#how-equity-is-granted)这些公司如何授予股权的部分。

### 公司类型

🄳 **公司 (company)** 是根据公司法为进行贸易而成立的法律实体。在美国，特定的规则和法规管辖着几种[商业实体类型](https://en.wikipedia.org/wiki/Types_of_business_entity#United_States)。
联邦和州法律对每种类型的公司的责任和税收具有重大影响。
值得注意的公司类型包括独资企业、合伙企业、有限责任公司 (LLC)、S 型公司和 C 型公司。

🄳 **公司 (corporation)** 是法律上被承认为单一实体的公司。
公司本身，而非其所有者，有义务偿还债务，并在合同和法律诉讼中承担责任（也就是说，是一个“[法人 (legal person)](https://en.wikipedia.org/wiki/Legal_person)”）。
最常见的情况是，*corporation* 一词指的是**[股份公司 (stock corporation 或 joint-stock company)](https://en.wikipedia.org/wiki/Joint-stock_company)**，这是一种所有权通过股票进行管理的公司。也存在不发行股票的**非股份公司 (non-stock corporations)**，最常见的是[非营利组织 (nonprofit organizations)](https://en.wikipedia.org/wiki/Nonprofit_organization)。（也存在一些[不太常见](https://en.wikipedia.org/wiki/Non-stock_corporation)的营利性非股份公司。）

在实践中，人们经常使用 *company* 这个词来指代 *corporation*。

🄳 **注册成立 (Incorporation)** 是组建（或**incorporating**）一个新的公司（如企业或非营利组织）的[法律程序](https://en.wikipedia.org/wiki/Incorporation_(business))。
公司可以在任何国家创建。
在美国，注册成立由州法律管辖，涉及向州务卿提交[公司章程 (articles of incorporation)](https://en.wikipedia.org/wiki/Articles_of_incorporation) 和各种其他[所需信息](https://handbook.clerky.com/formation/process)。
（请注意，非公司形式的公司（如合伙企业或有限责任公司）的组建与注册成立不同。）

🄳 [**C 型公司 (C corporation 或 C corp)**](https://en.wikipedia.org/wiki/C_corporation) 是美国的一种股份公司类型，具有特定的联邦[税务处理方式](https://ct.wolterskluwer.com/resource-center/articles/what-c-corporation)。它是最普遍的公司类型。[^investoped.m9wdqp]
大多数大型、知名的美国公司都是 C 型公司。
C 型公司在几个方面不同于[S 型公司](https://www.incorporate.com/starting-a-business/s-corporation)和其他商业实体，包括收入如何征税以及谁可以拥有股票。
C 型公司对允许拥有公司部分股权的股东数量没有限制。它们还允许其他公司以及合伙企业、信托和其他企业拥有股票。

C 型公司在寻求通过向个人和组织（如风险投资公司，通常是合伙企业）出售部分业务以换取投资的早期[私营公司](#public-and-private-companies)中非常受欢迎，也适用于在[公共交易所](https://en.wikipedia.org/wiki/Stock_exchange)向个人和其他公司出售大量股票的老牌上市公司。

在实践中，出于一些原因，这些公司通常在特拉华州成立，因此所有这些法律事务都由特拉华州法律定义。[^quoracomwh.wsnr2b][^nytimescom.67ksyb]
您可以将特拉华州法律视为美国公司法的主要“语言”。
在特拉华州注册公司已演变为高增长公司的全国标准，无论其物理位置在哪里。

🔸 本指南特别关注 C 型公司，并且[未涵盖](#scope)股权激励在有限责任公司 (LLC)、S 型公司、合伙企业或独资企业中的运作方式。
在这些类型的企业中，股权和薪酬的处理方式都大相径庭。

粗略地说，看待公司的一种方式是，它们仅仅是一系列[合同 (contracts)](https://www.law.cornell.edu/wex/contract)，由拥有和经营公司的人们随着时间的推移谈判达成，并由政府强制执行，旨在协调所有参与创造客户愿意付费的产品或服务的人的利益。
这些合同的关键在于一种精确追踪公司所有权的方式；发行股票是公司通常选择这样做的方式。

🚧 提及法院案件如何解决？

### 股票与股份

🄳 **股票 (Stock)** 是一种代表公司所有权的法律发明。**股份 (Shares)** 是股票的一部分，允许公司以灵活的方式向各种个人或其他公司授予所有权。
每个**股东 (shareholder 或 stockholder)**，即这些所有者，持有特定数量的股份。创始人、投资者、员工、董事会成员、承包商、顾问以及其他公司（如律师事务所）都可以成为股东。

🄳 股票所有权通常通过**股票证书 (stock certificates)** 正式确定，这些是证明谁拥有股票的精美纸质文件。

有时您拥有股票但没有实物证书，因为它可能由律师事务所为您保管。

一些公司现在通过称为*所有权管理平台*的在线服务来管理其所有权，例如 [Carta](https://carta.com/)。如果您工作的公司使用所有权管理平台，您将能够在线查看您的股票证书和股票价值。

较年轻的公司也可能选择将其股票保持为*非凭证化 (uncertificated)*，这意味着您所有权的唯一证据是您与公司签订的合同以及您在公司股权结构表上的位置，而没有单独的证书。

🄳 [**已发行在外股份 (Outstanding shares)**](http://www.investopedia.com/terms/o/outstandingshares.asp) 指所有股东持有的总股份数。
这个数字在公司创建时始于一个基本上任意的值（例如 1000 万），之后随着新股份的增加（发行）并授予人们以换取金钱或服务而增加。

已发行在外股份也可能因其他原因增减，例如[股票分割和股份回购 (stock splits and share buybacks)](http://www.investorguide.com/article/11713/splits-and-buybacks-explained/)，我们在此不作深入探讨。

稍后，我们将讨论股份计算中的几个[细微之处](#counting-shares)。

🚧 关于股票分割和股份回购，有哪些好的概述？关键资源？

🄳 任何股东都拥有公司的**所有权百分比 (percentage ownership)**，其计算方法是用他们拥有的股份数除以已发行在外股份数。
尽管股票文件总是列出股份数量，但如果股份价值不确定，所有权百分比通常是一个更有意义的数字，特别是如果您知道或可以估计公司的可能估值。
即使一个人拥有的股份数量是固定的，他们的所有权百分比也会随着已发行在外股份的变化而随时间变化。
通常，这个数字以百分比或[**基点 (basis points)**](https://www.investopedia.com/terms/b/basispoint.asp)（百分之一）表示。

### 上市公司与私营公司

🄳 [**上市公司 (Public companies)**](https://en.wikipedia.org/wiki/Public_company) 是指任何公众成员都可以拥有其股票的公司。
人们可以在公共[证券交易所 (stock exchanges)](https://www.investopedia.com/terms/e/exchange.asp) 上用现金买卖股票。公司股票的价值就是股票市场报告中显示的价值，因此股东知道他们的股票值多少钱。

🄳 大多数小型公司，包括所有初创公司，都是[**私营公司 (private companies)**](https://en.wikipedia.org/wiki/Privately_held_company)，其所有者控制着这些公司的运营方式。
与上市公司不同（任何人都可以买卖股票），私营公司的所有者控制着谁能够买卖股票。
交易可能很少或根本没有，或者它们可能不为公众所知。

🚧 什么是公共交易所？股票实际上是如何买卖的？提及合格投资者？

### 公司治理

🄳 公司设有**董事会 (board of directors)**，这是一个[人群](https://en.wikipedia.org/wiki/Board_of_directors)，其法律义务是监督公司并确保其服务于股东的最佳利益。
上市公司在法律上有义务设立董事会，而私营公司通常选择设立董事会。
董事会通常由**内部董事 (inside directors)**（例如 CEO、一两位创始人或公司雇佣的高管）和**外部董事 (outside directors)**（不参与公司日常运作的人）组成。
这些**董事会成员 (board members)** 是选举产生的个人，在对关键公司决策进行投票时拥有法律上的公司治理权利和义务。
董事会成员据说在公司拥有一个**董事席位 (board seat)**。

董事会成员人数从 3 人到 31 人不等，平均规模为 9 人。[^investoped.fn52lq] 董事会几乎总是奇数人数，以避免投票平局。
值得注意的是，加利福尼亚州要求上市公司董事会中至少有一名女性。[^nytimescom.gec7iw]

董事会的关键决策在*董事会会议 (board meetings)* 上正式做出，或以书面形式做出（称为*书面同意 (written consent)*）。[^dlapiperac.wb4617] 许多关于向员工授予股权的决策都由董事会批准。

🚧 本节可以扩展，并包含更多法律链接。

### 首次公开募股 (IPO)

🄳 私营公司通过一个称为[**首次公开募股 (Initial Public Offering, IPO)**](https://en.wikipedia.org/wiki/Initial_public_offering) 的过程成为上市公司。
历史上，只有那些拥有多年稳健增长记录的私营公司才会考虑采取这一重大步骤。
IPO 有其[利弊](https://www.investopedia.com/university/ipo/ipo.asp)，包括用高昂的监管成本换取巨额资本带来的好处。
在公司“IPO”或“**上市 (goes public)**”后，投资者和普通公众可以购买股票，现有股东也可以比公司私有时更容易地出售他们的股票。

公司成立后需要数年时间才能进行 IPO。
公司成立与其 IPO 之间的时间中位数一直在增加。
根据哈佛大学的一份报告，**2016** 年上市的公司平均花费了 **7.7 年**，而 **1996** 年上市的公司则为 **3.1 年**。[^corpgovlaw.vbw82s]

🚧 在 IPO 时，影响员工出售股票的限制和规定有哪些？什么是锁定期？

### 出售与流动性

❗️ 对于私营公司而言，[很难知道](#what-is-private-stock-worth)股权的价值。
由于私营公司股票的价值并非由公共市场上的常规交易决定，股东只能对其可能的未来价值以及何时能够出售股票做出有根据的猜测。

毕竟，私营公司股票仅仅是一份法律协议，赋予您获得某种价值高度不确定的东西的权利，未来可能一文不值，也可能非常有价值，这取决于公司的命运。

☝️ 我们稍后将讨论公司正式指定[公允市场价值](#409a-valuations)的概念，但即使公司出于税务和会计目的为您提供了股票价值，也并不意味着您可以期望以该价值出售它！

🄳 [**收购 (acquisition)**](https://www.investopedia.com/terms/a/acquisition.asp) 是指一家公司（收购方）购买另一家公司（被收购公司）超过 50% 的股份。这也称为被收购公司的**出售 (sale)**。
在收购中，被收购公司将控制权交给收购方。

🄳 买卖股票的能力称为**流动性 (liquidity)**。在初创公司和许多私营公司中，通常很难在公司被出售或上市之前出售股票，因此在这些事件发生之前，股东几乎没有或根本没有流动性。
因此，出售和 IPO 既被称为**退出 (exits)**，也称为**流动性事件 (liquidity events)**。出售、解散和破产都称为**清算 (liquidations)**。

人们常常希望能够出售私营公司的股票，因为他们更愿意拥有现金。
但这只是偶尔才有可能。
我们将在稍后关于出售私营股票的部分[详细讨论](#can-you-sell-private-stock)。

🄳 [**股息 (dividend)**](http://www.investopedia.com/terms/d/dividend.asp) 是公司经董事会授权向股东分配的利润。
成熟的上市公司和一些私营公司会支付股息，但这在初创公司和专注于快速增长的公司中很少见，因为它们通常希望将利润再投资于扩大业务，而不是将钱返还给股东。例如，亚马逊就[从未支付过](https://www.fool.com/investing/2017/12/28/will-amazon-start-paying-a-dividend-in-2018.aspx)股息。

## 初创公司与增长

如果您正在考虑为一家初创公司工作，我们接下来介绍的关于这些早期公司如何融资和成长的内容，有助于理解您的股权可能价值几何。

如果您只关心大型和成熟的公司，可以跳到[股权授予方式](#how-equity-is-granted)。

### 初创公司

🄳 [**初创公司 (startup)**](https://en.wikipedia.org/wiki/Startup_company) 是一家新兴的公司，通常是私营公司，渴望在规模、收入和影响力方面快速增长。
一旦一家公司在市场上站稳脚跟并成功一段时间后，通常就不再被称为初创公司。

☝️ 与具有法律意义的公司术语不同，*初创公司*这个词是非正式的，并非每个人都一致使用。

初创公司与小企业不同。
小企业，如咖啡店或水管业务，通常打算缓慢有机地增长，同时较少依赖投资资本和股权激励。
著名的初创公司投资者[保罗·格雷厄姆 (Paul Graham)](https://en.wikipedia.org/wiki/Paul_Graham_(programmer)) [强调](http://www.paulgraham.com/growth.html)过，最好将初创公司视为任何打算快速增长的[早期](#stages-of-a-startup)公司。

∑ C 型公司主导着初创企业生态系统。
有限责任公司 (LLC) 往往更适合增长较慢、打算分配利润而不是将其再投资以促进增长的公司。
因此，以及由于其融资方式相关的复杂原因，风险投资家非常倾向于投资 C 型公司。

🚧 关于在初创公司工作的人数与在成熟公司工作的人数相比，有哪些好的统计数据？

### 融资、增长与稀释

许多大型成功公司都是从初创公司起步的。
总的来说，初创公司依赖投资者来帮助资助快速增长。

🄳 **融资 (Fundraising)** 是寻求资本以建立或扩展业务的过程。
向投资者出售企业股份是融资的一种形式，贷款和[首次代币发行 (initial coin offerings)](https://en.wikipedia.org/wiki/Initial_coin_offering) 也是。**融资 (Financing)** 既指从外部来源筹集资金，也指通过销售产品或服务获得收入。

🄳 **风险资本 (Venture capital)** 是早期公司的一种融资形式，由个人投资者或投资公司提供，以换取公司的部分所有权或股权。这些投资者被称为**风险投资家 (venture capitalists 或 VCs)**。风险投资家投资于他们认为能够快速增长并占据显著市场份额的公司。
“风险 (Venture)” 指的是投资于商业模式未经证实的早期企业——通常是初创公司——所具有的风险性。

一家初创公司会经历几个[增长阶段](#stages-of-a-startup)，因为它基于公司未来会增长并赚更多钱的希望和预期来筹集资本。

🄳 公司在融资期间增加（或“发行”）股份，这些股份可以用来换取投资者的现金。
随着已发行在外股份数量的增加，每个股东的所有权百分比会下降。这被称为[**稀释 (dilution)**](http://www.investopedia.com/terms/d/dilution.asp)。

☝️ 稀释并不一定意味着作为股东您正在失去什么。
随着公司发行股票和筹集资金，您所拥有的公司较小比例的股份可能会更有价值。
您的那块蛋糕相对变小了，但是，如果公司在增长，整个蛋糕的尺寸变大了。
例如，一个典型的初创公司可能会有三轮融资，每轮融资增发 20% 的股份。
在三轮融资结束时，已发行在外的股份会更多——在这种情况下大约多出 73%，因为 120% × 120% × 120% 是 173%——并且每个股东拥有的公司比例相应减少。

🄳 公司的[**估值 (valuation)**](https://en.wikipedia.org/wiki/Valuation_(finance)) 是投资者认为公司目前具有的价值。
如果公司经营良好，收入增长或显示出未来收入的迹象（例如用户数量增长或在有前景的市场中获得吸引力），公司的估值通常会上升。
也就是说，投资者购买公司一股股票的[价格 (price)](https://en.wikipedia.org/wiki/Share_price) 会增加。

❗️ 当然，事情并非总是一帆风顺，公司的估值也并非总是上升。可能会发生公司完全失败，所有所有权都变得一文不值的情况，或者估值低于预期，导致[某些类型](#classes-of-stock)的股份变得一文不值，而其他类型的股份仍有一些价值。当公司的投资者和领导层期望公司表现好于实际情况时，可能会给股东带来许多令人失望的后果。

### 稀释图示

这些可视化图表演示了随着融资的进行，风险投资支持的公司的所有权是如何演变的。
一种情景设想了表现良好的初创公司所有权的变化，另一种则大致基于对 Zipcar[^reactionwh.uw835n] 的仔细分析，这是一家共享出行公司，在最终上市并被[收购](#sales-and-liquidity)之前经历了大幅稀释。这些图表简化了该分析中讨论的复杂性，但它们让人们了解所有权是如何被稀释的。

```hlwy-infographics
{
  "name": "CaptableDilution",
  "data": {
    "hypothetical": {
      "label": "假设情况",
      "stages": [
        {
          "label": "创立",
          "postValuation": 1000,
          "captable": [
            {
              "type": "founder1",
              "label": "创始人 #1",
              "shares": 4000000
            },
            {
              "type": "founder2",
              "label": "创始人 #2",
              "shares": 3000000
            },
            {
              "type": "founder3",
              "label": "创始人 #3",
              "shares": 3000000
            }
          ]
        },
        {
          "label": "A 轮融资",
          "captable": [
            {
              "type": "founder1",
              "label": "创始人 #1",
              "shares": 4000000
            },
            {
              "type": "founder2",
              "label": "创始人 #2",
              "shares": 3000000
            },
            {
              "type": "founder3",
              "label": "创始人 #3",
              "shares": 3000000
            },
            {
              "type": "options",
              "label": "期权池",
              "shares": 1500000
            },
            {
              "type": "investment",
              "label": "种子轮",
              "preValuation": 8000000,
              "raised": 2000000
            },
            {
              "type": "investment",
              "label": "A 轮",
              "preValuation": 8000000,
              "raised": 5000000
            }
          ]
        },
        {
          "label": "C 轮融资",
          "captable": [
            {
              "type": "founder1",
              "label": "创始人 #1",
              "shares": 4000000
            },
            {
              "type": "founder2",
              "label": "创始人 #2",
              "shares": 3000000
            },
            {
              "type": "founder3",
              "label": "创始人 #3",
              "shares": 3000000
            },
            {
              "type": "options",
              "label": "期权池",
              "shares": 1500000
            },
            {
              "type": "investment",
              "label": "种子轮",
              "preValuation": 8000000,
              "raised": 2000000
            },
            {
              "type": "investment",
              "label": "A 轮",
              "preValuation": 8000000,
              "raised": 5000000
            },
            {
              "type": "investment",
              "label": "B 轮",
              "preValuation": 20000000,
              "raised": 10000000
            },
            {
              "type": "investment",
              "label": "C 轮",
              "preValuation": 40000000,
              "raised": 20000000
            }
          ]
        }
      ]
    },
    "zipcar": {
      "label": "近似 Zipcar",
      "stages": [
        {
          "label": "创立",
          "postValuation": 1000,
          "captable": [
            {
              "type": "founder1",
              "label": "创始人 #1",
              "shares": 570000
            },
            {
              "type": "founder2",
              "label": "创始人 #2",
              "shares": 570000
            }
          ]
        },
        {
          "label": "A 轮融资",
          "captable": [
            {
              "type": "founder1",
              "label": "创始人 #1",
              "shares": 570000
            },
            {
              "type": "founder2",
              "label": "创始人 #2",
              "shares": 570000
            },
            {
              "type": "options",
              "label": "期权池",
              "shares": 378000
            },
            {
              "type": "investment",
              "label": "A 轮",
              "preValuation": 5800000,
              "raised": 1400000
            }
          ]
        },
        {
          "label": "B 轮融资",
          "captable": [
            {
              "type": "founder1",
              "label": "创始人 #1",
              "shares": 570000
            },
            {
              "type": "founder2",
              "label": "创始人 #2",
              "shares": 570000
            },
            {
              "type": "options",
              "label": "期权池",
              "shares": 378000
            },
            {
              "type": "investment",
              "label": "A 轮",
              "preValuation": 5800000,
              "raised": 1400000
            },
            {
              "type": "investment",
              "label": "A 轮*", (*更正为 B 轮*)
              "preValuation": 2200000, (*应为 B 轮投前估值*)
              "raised": 4700000 (*应为 B 轮融资金额*)
            }
          ]
        }
      ]
    }
  }
}
```
(*译者注：Zipcar B 轮融资的标签和数据在原文中似乎有误，已根据上下文推断标注，但保留了原始数据。*)

### 初创公司的阶段

理解初创公司股票和股权的价值，需要把握其经历的增长阶段。
这些阶段很大程度上反映了已筹集资金的多少——即以股份形式出售的所有权换取了多少资本。

非常粗略地说，[典型阶段](http://blog.eladgil.com/2011/03/how-funding-rounds-differ-seed-series.html)包括：

-   [**自主发展 (Bootstrapped)**](https://www.investopedia.com/terms/b/bootstrapping.asp)（资金很少或自筹资金）：创始人正在确定要构建什么，或者他们正在用自己的时间和资源开始构建。
-   [**种子轮 (Series Seed)**](https://www.investopedia.com/terms/s/seedcapital.asp)（融资额约 25 万至 200 万美元）：确定产品和市场。
    这个范围的低端现在通常被称为**种子前轮 (pre-seed)**。
-   [**A 轮 (Series A)**](https://www.investopedia.com/terms/s/seriesa.asp)（200 万至 1500 万美元）：扩展产品并使商业模式奏效。
-   [**B 轮 (Series B)**](https://www.investopedia.com/terms/s/series-b-financing.asp)（数千万美元）：
    扩展业务。
-   **C 轮、D 轮、E 轮等等**（数千万至数亿美元）：持续扩展业务。

请记住，这些数字对于位于加州的初创公司更为典型。
位于硅谷以外的公司在不同阶段筹集的金额通常较小，在硅谷可能被称为种子轮融资的，在休斯顿、丹佛或哥伦布等地可能被称为 A 轮融资，因为这些地方争夺投资的公司较少，风险投资公司也较少，并且与增长相关的成本（包括提供可维持生活的工资）较低。[^nytimescom.bcfuyu][^chicagotri.fq0msp]

🔸 大多数初创公司走不了多远。
根据 Susa Ventures 普通合伙人 [Leo Polovets](http://codingvc.com) 对[天使投资](https://www.investopedia.com/terms/a/angelinvestor.asp)的分析，**超过一半**的投资失败；**三分之一**是小成功（1 倍至 5 倍回报）；**八分之一**是大成功（5 倍至 30 倍）；**二十分之一**是巨大成功（30 倍以上）。[^codingvcco.bcspni]

🚧 除了天使投资，还有其他统计数据吗？

🔸 每个阶段都反映了风险的降低和稀释的增加。
因此，团队成员获得的股权数量在早期阶段较高（从创始人开始），随着公司的成熟而逐渐降低。
（见上图。）

### 期权池

🄳 在早期某个阶段，通常在招聘第一批员工之前，会预留一定数量的股份用于员工**[期权池 (option pool 或 employee pool)](http://www.investopedia.com/terms/o/option-pool.asp)**。期权池是称为股权激励计划的法律结构的一部分。
期权池的典型规模是公司股票的 20%，但特别是对于早期公司，期权池可以是 10%、15% 或其他规模。

一旦期权池建立，公司董事会就会随着员工加入公司而从池中授予股票。

∑ 受到良好建议的公司只会在期权池中预留他们[预期在未来 12 个月左右使用的数量](http://siliconhillslawyer.com/2014/05/01/option-pool-not-ocean-startups/)；
否则，考虑到股权授予通常的承诺方式，他们可能会过度授予股权。
整个期权池可能永远不会被完全使用，但公司仍应尽量不要预留超过计划使用的数量。
期权池的大小由创始人和投资者之间[复杂的因素](http://venturehacks.com/articles/option-pool-shuffle)决定。员工（以及[创始人](https://www.cooleygo.com/negotiating-option-pool/)）值得理解的是，一个小期权池可能是一件好事，因为它反映了公司在与投资者谈判中保留了所有权。
期权池的规模可能会在以后增加。

### 股份计数

在计算[已发行在外股份](#stock-and-shares)的方式上，您可能会遇到一些关键的细微之处：

🄳 私营公司总是有所谓的**已授权但未发行 (authorized but unissued)** 的股份，
指的是在法律文书中授权但尚未实际发行的股份。在发行之前，这些股份所代表的[未发行股票 (unissued stock)](https://www.investopedia.com/terms/u/unissuedstock.asp) 对公司或股东没有任何意义：
没有人拥有它。

☝️ 例如，一家公司可能有 1 亿股*已授权*股份，但只*发行*了 1000 万股。
在这个例子中，该公司将有 9000 万股*已授权但未发行*的股份。
当您试图确定一定数量的股份代表的百分比时，您*不*参考已授权但未发行的股份。

☝️ 您实际上想知道的是总发行股份数，但即使这个数字也可能令人困惑，因为它可以用[不止一种方式](http://www.mattbartus.com/option-grants-fully-diluted-or-issued-and-outstanding/)计算。
通常，人们用两种方式计算股份：*已发行且在外流通 (issued and outstanding)* 和 *完全稀释 (fully diluted)*。

🄳 **已发行且在外流通 (Issued and outstanding)** 指公司实际发行给股东的股份数量，不包括其他人可能有权购买的股份。

🄳 **完全稀释 (Fully diluted)** 指公司已发行的所有股份、已在股票激励计划中预留的所有股份，以及如果所有可转换证券（如未偿认股权证）被行使可能发行的所有股份的总和。

完全稀释股份与已发行且在外流通股份的一个关键区别在于，完全稀释股份的总数将包括员工期权池中所有已预留但*尚未发行给*员工的股份。

🔹 如果您试图弄清楚一定数量的股份未来可能价值的百分比，最好知道完全稀释后的股份数量。

∑ 即使是完全稀释的数字也可能没有考虑那些*等待*在未来某个里程碑事件时转换为股票的未偿可转换证券（如可转换票据）。
为了更全面地了解，除了询问完全稀释的资本总额外，您还可以询问任何未包含在该数字中的未偿可转换证券。

☝️ 这里提到的术语并非普遍适用。
值得与您的公司讨论这些术语，以确保你们的理解一致。

🄳 **资本结构表 (capitalization table 或 cap table)** 是一个[表格](https://www.investopedia.com/terms/c/capitalization-table.asp)（通常是电子表格或其他官方记录），记录了公司所有股东的所有权份额，包括股份数量和类别。
随着股票授予新股东，它会进行更新。[^cooleygoco.p5v68j]

🚧 更好地讨论未来的稀释来源。
定义可转换证券和可转换票据以及“[完全稀释 (fully diluted)](https://www.lawinsider.com/dictionary/fully-diluted-basis)”
。人们是否会说“完全稀释”但不包括可转换证券？

### 股票类别

🄳 投资者通常要求优先获得偿还权以换取他们的投资。
处理这些不同权利的方式是创建不同的[**股票类别 (classes of stock)**](https://www.upcounsel.com/classes-of-stock)。（这些有时也称为 [**股份类别 (classes of shares)**](https://www.investopedia.com/terms/c/class.asp)，尽管该术语在共同基金的背景下有另一个含义。）

🄳 两种重要的股票类别是[**普通股 (common stock)**](https://en.wikipedia.org/wiki/Common_stock) 和[**优先股 (preferred stock)**](https://en.wikipedia.org/wiki/Preferred_stock)。一般来说，优先股拥有普通股所不具备的“[权利、优先权和特权 (rights, preferences, and privileges)](https://www.americanbar.org/groups/business_law/publications/blt/2014/01/04_bigler/)”。
通常，投资者获得优先股，而创始人和员工获得普通股（或股票期权）。

股票类别的确切数量以及它们之间的差异可能因公司而异，并且在初创公司中，这些可能在[每一轮](#stages-of-a-startup)融资时都有所不同。

☝️ 您可能听到的另一个术语是[*创始人股份 (founders’ stock)*](http://www.alleywatch.com/2013/08/what-is-founders-stock-legally/)，它是（通常）在公司成立时分配的普通股，但在其他方面与普通股没有不同的权利。[^lsvpwordpr.dgym96]

虽然优先股的权利过于复杂无法完全涵盖，但我们可以给出几个关键细节：

🄳 优先股通常具有[**清算优先权 (liquidation preference 或 preference)**](http://www.investopedia.com/terms/l/liquidation-preference.asp)，这意味着当发生[流动性事件](#sales-and-liquidity)时（例如公司被出售或上市），优先股所有者将在普通股所有者之前获得偿付。

🄳 当公司价值未能达到投资者投入的金额时，公司处于[**清算优先权积压 (liquidation overhang)**](https://equityzen.com/blog/startup-valuations-and-liquidation-preference-overhang/) 状态。
由于清算优先权，持有优先股的人（投资者）必须在持有普通股的人（员工）之前得到偿付。
如果投资者向一家公司投入了数百万美元并且该公司被出售，那么如果公司处于清算优先权积压状态且出售价格不超过该金额，员工的股权将一文不值。[^avccom2010.zxzhsl]

☝️ 清算优先权的复杂性是[臭名昭著的](https://venturebeat.com/2010/08/16/beware-the-trappings-of-liquidation-preference/)。
值得理解的是，投资者和企业家会就优先权的许多细节进行谈判，包括：

-   *倍数 (multiple)*，一个指定投资者必须获得多少倍偿还后，普通股股东才能获得收益的数字。
    （通常倍数是 1 倍，但可以是 2 倍或更高。）

-   优先股是否是[*参与分配型 (participating)*](https://en.wikipedia.org/wiki/Participating_preferred_stock)，意味着投资者不仅拿回他们的钱，还参与普通股的收益分配。

-   是否有*上限 (cap)*，如果它是参与分配型的，则限制支付额。

-   ∑
    [🔑这篇入门文章](https://medium.com/@CharlesYu/the-ultimate-guide-to-liquidation-preferences-478dda9f9332)
    由 Charles Yu 撰写，给出了简明的概述。
    创始人 和公司受到这些考虑因素的显著且微妙的影响。
    例如，正如律师 José Ancer 指出的，普通股股东和优先股股东通常截然不同，他们的激励[有时会](http://siliconhillslawyer.com/2017/10/13/common-stock-v-preferred-stock/)
    [分歧](http://siliconhillslawyer.com/2018/02/07/board-works-common-stock/)。

-   🚧 有哪些好的资源可以提及，描述优先股转换为普通股的情况？

🔹 对于**持有普通股的员工而言**，关于优先权最重要的一点是，如果公司长期表现良好，它们可能并不重要。
在这种情况下，每个股东都拥有最终可以出售的有价值的股票。
但如果公司失败或以低于投资者期望的价格[退出](#sales-and-liquidity)，优先股股东通常排在第一位获得偿还。
取决于对投资者有利的条款如何，如果公司以低或中等估值退出，普通股股东很可能只收到很少——甚至什么也得不到。

## 股权授予方式

在本节中，我们将阐述股权在实践中是如何授予的，包括常见股权激励类型的差异、好处和缺点，包括限制性股票奖励、股票期权和限制性股票单位 (RSU)。
我们还将介绍一些不太常见的类型。
虽然每种股权授予的[意图](#the-goals-of-equity-compensation)相似，但它们在许多方面有所不同，特别是在[税收](#taxes-on-equity-compensation)方面。

除非在极少数可以协商的情况下，您获得的股权类型取决于您工作的公司。
总的来说，较大的公司授予 RSU，初创公司授予股票期权，偶尔高管和非常早期的员工会获得限制性股票奖励。

🚧 添加关于何时授予股权的部分，包括追加授予 (plus-ups)。

### 限制性股票奖励

从表面上看，最直接的股权激励方法是公司奖励员工股票以换取工作。
在实践中，事实证明公司只会希望在对股票的完全所有权方式和时间施加限制的情况下这样做。

即便如此，这实际上是获得股权最不常见的方式之一。
我们首先提到它，是因为它是最简单的股权激励形式，在事情变得更复杂时可用于比较。

🄳 **限制性股票奖励 (restricted stock award)** 是指公司授予某人股票作为一种薪酬形式。授予的股票附带额外条件，包括归属时间表，因此被称为**限制性股票 (restricted stock)**。限制性股票奖励也可能简称为**股票奖励 (stock awards)** 或**股票授予 (stock grants)**。

∑ 这里*限制性 (restricted)* 的含义实际上是[复杂的](https://github.com/jlevy/og-equity-compensation/issues/24)。它指的是股票 (i) 具有某些限制（如转让限制），这是私营公司股票所要求的，并且 (ii) 将根据归属时间表以成本价回购。
回购权在基于服务的归属期内逐渐失效，这就是这种情况下股票“归属 (vesting)”的含义。

☝️ 限制性股票奖励与限制性股票单位[不是一回事](https://www.fool.com/knowledge-center/the-difference-between-a-restricted-stock-unit-res.aspx)。

通常，股票奖励仅限于高管或非常早期的雇员，因为一旦股票价值增加，获得它们（而无需向公司支付其价值）的税收负担对大多数人来说可能过高。
通常，员工会获得股票期权而不是限制性股票。

### 股票期权

🄳 [**股票期权 (Stock options)**](https://en.wikipedia.org/wiki/Employee_stock_option) 是一种合同，允许个人以固定价格购买其工作公司指定数量的股份。股票期权是早期公司授予股权的最常见方式。

🄳 获得股票期权授予的人在**行使 (exercise)** 其期权之前不是股东，行权意味着以行权价购买其部分或全部股份。在行权之前，期权持有人没有投票权。

🄳 **行权价 (strike price 或 exercise price)** 是指股票期权协议中设定的、可以购买股票的固定每股价格。
行权价通常设定得低于（通常远低于）人们预期的股票*未来*价值，这意味着将来出售股票可能会盈利。

☝️ *股票期权 (Stock options)* 是一个容易混淆的术语。
在投资中，*期权 (option)* 是在特定时间范围内以特定价格购买某物的权利（但不是义务）。
您经常会在[投资](https://www.investopedia.com/terms/s/stockoption.asp)背景下看到讨论股票期权。金融市场投资者所称的*股票期权*确实是股票的期权，但它们不是为服务而授予的*补偿性*股票期权。
在本指南中，以及很可能在您与雇主的任何对话中，任何说“股票期权”的人都指的是补偿性股票期权。

☝️ 股票期权与股票不同；
它们仅仅是*以特定价格和特定条件下购买股票的权利*，这些条件在员工的股票期权协议中规定。
我们接下来将探讨这些条件。

∑ 尽管每个人通常都使用复数形式“股票期权 (stock options)”，但当您收到一份股票期权授予时，您收到的是购买给定数量股份的*一份期权 (an option)*。
因此，从技术上讲，说某人“拥有 10,000 份股票期权”是不正确的。

最好在决定[何时行权](#stock-option-scenarios)之前了解财务和[税务影响](#taxes-on-isos-and-nsos)。
为了使期权在授予时免税，行权价必须是期权授予日股票的公允市场价值。

∑ 熟悉[股票交易](https://www.investopedia.com/university/stocks/stocks3.asp)的人（或拥有经济学学位的人）会告诉您[**布莱克-斯科尔斯模型 (Black-Scholes model)**](https://www.investopedia.com/university/options-pricing/black-scholes-model.asp)，这是一种用于确定期权价值的通用数学模型。
虽然理论上合理，但这在员工股票期权的背景下没有太多实际应用。

🚧 有没有关于低行权价带来巨大回报的真实案例或统计数据？
另外，我们可以提及并关联术语*员工股票期权 (employee stock options 或 ESOs)*，并消除 ESOs 和 ESPPs（员工股票购买计划）之间的任何混淆。

### 归属与悬崖期

🄳 **归属 (Vesting)** 是指获得某物完全合法权利的过程。
在薪酬背景下，创始人、高管和员工通常随着时间的推移，根据限制条件逐步获得其股权授予的权利。
人们可能会说他们的股份或股票期权正在归属，或者说某人正在归属或已完全归属。

🄳 在大多数情况下，归属根据**归属时间表 (vesting schedule)** 逐步发生。一个人只有在为公司工作期间才会归属。
如果此人立即辞职或被解雇，他们将得不到任何股权；如果他们工作多年，他们将获得大部分或全部股权。

股票、股票期权和 RSU 的授予几乎总是受归属时间表的约束。

🄳 归属时间表可以有一个**悬崖期 (cliff)**，指定一个人必须工作多长时间才能开始归属。

例如，如果您的股权奖励有一个为期一年的悬崖期，而您只为公司工作了 11 个月，那么您将一无所获，因为您的奖励没有任何部分归属。同样，如果公司在您入职一年内被出售，根据您的文件规定，您可能在公司出售时什么也得不到。

一个非常常见的归属时间表是**4 年**归属，带有 **1 年**悬崖期。
这意味着您在最初的 12 个月内归属比例为 0%，在第 12 个月时归属 25%，之后每个月额外归属 1/48（约 2.08%），直到第 48 个月。
如果您在满一年之前离开，您将一无所获，但如果您在 3 年后离开，您将获得 75%。

🄳 在某些情况下，根据称为**加速归属 (accelerated vesting 或 acceleration)** 的合同条款，归属可能会由归属时间表之外的特定事件触发。
两种常见的协商加速归属情况是：公司被出售或进行合并（**单一触发 (single trigger)**），或者公司被出售且该员工被解雇（**双重触发 (double trigger)**）。

🌪 悬崖期是一个重要的话题。
当它们运作良好时，悬崖期对员工和公司来说都是一个有效且相当公平的系统。
但它们可能被滥用，其复杂性也可能导致误解：

-   悬崖期的意图是确保新员工致力于在公司工作一段相当长的时间。
    然而，带悬崖期的归属的另一面是，如果员工在悬崖期即将结束时离开——辞职、被裁员或解雇——他们可能最终完全没有任何股票所有权，有时并非出于自身过错，例如发生家庭紧急情况或疾病。在公司恰好在悬崖期前解雇或裁员的情况下，很容易导致不满甚至诉讼（特别是如果公司经营良好，股票价值很高）。[^inccombusi.oldydy][^bloombergc.a48epn]
-   🔹 作为经理或创始人，如果员工表现不佳或可能需要被裁员，在他们的悬崖期到来之前很久就告知他们情况，既是体贴也是明智的做法。
-   ∑ 创始人自己的股票通常也有归属期。
    正如企业家 Dan Shapiro 所解释的，这通常是出于[充分的理由](http://www.danshapiro.com/blog/2012/04/vesting-is-a-hack/)。
-   🔹 作为员工，如果您在归属悬崖期满之前离开或考虑离开公司，请考虑等待。
    或者，如果您对公司的价值足够高，您可以[谈判](https://www.businessinsider.com/everything-you-need-to-know-about-cliff-vesting-2011-5)让您的一部分股票提前“[归属到位 (vested up)](https://www.foley.com/when-should-vesting-of-equity-grants-accelerate-06-19-2014/)”。
    您的经理很可能同意，对于为公司增加了很多价值的人来说，即使他们比预期更早离开，拥有股票也是公平的，特别是对于像家庭紧急情况这样的原因。
    然而，除非您在雇佣协议中协商了特殊的加速条款，否则这类归属加速完全是酌情决定的。
    这种特殊的加速权利通常保留给那些经过大量谈判获得雇佣合同的高管。
-   🚧 休假，例如请事假，如何影响归属时间表？
-   公司出售时的加速（称为[*控制权变更 (change of control)*](http://stockoptioncounsel.com/blog/change-of-control-terms-for-startup-stock-options-restricted-stock-and-rsus/2018/6/4) 条款）对创始人来说很常见，但对员工来说不太常见。
    了解加速和触发器是值得的，以防它们出现在您的期权协议中，但除非您将担任关键角色，否则这些可能不是您可以谈判的内容。
-   公司可能会对已归属的股票施加额外的限制。
    例如，您的股份很可能受到优先购买权的约束，这意味着您不能在未先向公司提出出售要约的情况下将股票出售给第三方。
    而且可能会发生公司保留在某些事件中[回购](https://www.forbes.com/sites/dianahembree/2018/01/10/startup-employee-alert-can-your-company-take-back-your-vested-stock-options/#75fb48ee6e49)已归属股份的权利。

🚧 能在这里举些例子吗？

### 期权如何到期

🄳 **行权窗口 (exercise window 或 exercise period)** 是指个人可以以行权价购买股份的期间。
期权仅在固定期限内可行使，直到它们到期，只要该人在公司工作，通常是七到十年。
但这个窗口并非总是开放的。

❗️ **终止服务后的到期。**
期权可能在您停止为公司工作后到期。
通常，到期日是服务终止后的 **90 天**，如果您无法在此之前行权，期权实际上将变得毫无价值。
正如我们稍后将讨论的，您需要了解行权的成本、[税收](#taxes-on-isos-and-nsos)和税务[责任](#the-amt-trap)，并提前计划。
事实上，您可以在获得期权时，或者最好在签署录用通知书之前就了解清楚。

🔹 **更长的行权窗口。**
最近（大约自 2015 年以来），一些公司正在寻找方法，在员工离开公司后将行权窗口保持开放多年，并将这种做法宣传为对员工更公平。
拥有[延长行权窗口](https://github.com/holman/extended-exercise-windows)的公司包括 Amplitude[^amplitudec.fvea8b]、Clef[^githubcomc.ygtolb]、Coinbase[^mediumcomb.nqs9mo]、Pinterest[^fortunecom.nnfd6o] 和 Quora[^quoracomwh.4dxi02]。
然而，90 天的行权窗口仍然是常态。

🌪 **行权窗口之争。**
是否应该有延长的行权窗口已经被广泛讨论。
一些人认为延长的行权窗口是[未来的趋势](https://triplebyte.com/blog/extending-stock-option-exercise-window-guide#.12rv7ovrv)，
认为较短的窗口使公司的成功变成对早期员工的[惩罚](http://stockoptioncounsel.com/blog/nc7go8ivzxb1el5rhv6nltrjan0n2t/2017/3/6)。

关键考虑因素包括：

-   所有人都同意，持有即将到期的股票期权的员工如果希望离开，通常不得不做出痛苦的选择：
    支付巨额税单（可能高达五到七位数）外加行权成本（可能需要寻找[二级市场流动性或贷款](#can-you-sell-private-stock)）
    或者放弃期权。
-   许多熟悉这种情况的人[强烈反对](https://zachholman.com/posts/fuck-your-90-day-exercise-window/)较短的行权窗口，认为员工可以为公司价值的增长做出重大贡献——通常是以较低的薪水换取股权——但最终却因为无法或不愿留任[通常需要](#ipos)的几年直到 IPO 或出售而[失去所有权](https://triplebyte.com/blog/fixing-the-inequity-of-startup-equity)。
-   另一方面，一些公司和投资者[坚持](https://a16z.com/2016/06/23/options-timing/)现有体系，认为这样更能激励人们不离开公司，或者认为长窗口实际上是将财富从长期承诺的员工转移给了离开的人。
-   一些关注法律问题的人也认为，ISO 的法律要求就是要有 90 天的行权窗口。
    虽然这在技术上是正确的，但这并非[全部情况](https://news.ycombinator.com/item?id=9254299)。公司可以通过改变期权的性质（将它们从 ISO 转换为 NSO）来延长行权窗口，并且[许多公司](https://github.com/holman/extended-exercise-windows)现在选择这样做。
-   另一种途径是[折中处理](http://stockoptioncounsel.com/blog/early-expiration-of-startup-stock-options-part-2-the-full-10-year-term-solution/2017/3/28)，
    仅给予长期员工延长的窗口。
-   总而言之，很明显许多员工在加入公司时对这其中的细微差别并不清楚，并且有些人因此[🔑遭受了损失](https://medium.com/@ben_mathes/90-days-and-my-six-figure-mistake-a495f4a188e2)。
    随着短行权窗口对员工的风险越来越广为人知，更长的行权窗口正逐渐变得更加普遍。
    作为员工或创始人，事先了解和谈判这些事情，避免不幸的意外，是更公平和明智的做法。

☝️ 授予顾问的期权通常比员工授予的归属期更短，通常为一到两年。
顾问授予通常在服务终止后也有更长的行权窗口，并且通常在收购时会有单一触发加速，因为没有人期望顾问在公司被收购后继续留任。
顾问的典型条款，包括股权水平，可在创始人研究所 (Founder Institute) 的[📥创始人/顾问标准模板 (FAST)](https://fi.co/contents/fast#) 中找到。

### 股票期权的种类

🄳 补偿性股票期权有两种类型：**激励性股票期权 (incentive stock options, ISOs)** 和**非法定股票期权 (non-qualifying stock options, NQOs 或 NQSOs)**。令人困惑的是，律师和美国国税局 (IRS) 对这两种股票期权使用[多个名称](https://www.irs.gov/taxtopics/tc427)，包括**法定股票期权 (statutory stock options)** 和**非法定股票期权 (non-statutory stock options 或 NSOs)**。

在本指南中，我们使用 ISOs 和 NSOs。

| 类型        | 也称为                                        |
| ----------- | --------------------------------------------- |
| 法定        | 激励性股票期权 (Incentive stock option), ISO  |
| 非法定      | 非合格股票期权 (Non-qualifying stock option), NQO, NQSO, NSO |

-   公司通常根据他们获得的法律建议来决定授予 ISO 还是 NSO。
    员工很少能决定他们将收到哪种期权，因此最好同时了解两者。
    从接受者和公司的角度来看，每种期权都有其优缺点。
-   ISO 对员工来说很常见，因为它们在税收方面可能比 NSO 更有利。
-   🔸 ISO 只能授予员工（不能授予独立承包商或非兼任员工的董事）。
-   但 ISO 有许多限制和条件，也可能产生困难的[税务后果](#taxes-on-isos-and-nsos)。

### 提前行权

🄳 有时，为了帮助减轻股票期权的税收负担，公司会允许期权持有人**提前行权 (early exercise 或 forward exercise)**，这意味着他们甚至可以在归属之前就行权。
期权持有人更早成为股东，之后归属适用于实际股票而非期权。
这将产生[税务影响](#83b-elections)。

🔸 然而，如果个人停止为公司工作，公司有权以支付的价格或股票的公允市场价值（以较低者为准）回购*未归属*的股份。
如果该人在其购买的股票归属之前离开公司，公司通常会回购未归属的股份。

### 限制性股票单位 (RSU)

虽然股票期权是小型私营公司最常见的股权激励形式，但 RSU 已成为上市公司和大型私营公司最常见的股权奖励类型。
Facebook 作为一家私营公司率先使用 RSU，使其能够避免更早地注册为上市公司。

🚧 为什么？关于 RSU 历史和 Facebook 故事的更多链接？

🄳
[**限制性股票单位 (Restricted stock units, RSUs)**](http://www.investopedia.com/terms/r/restricted-stock-unit.asp)
指公司同意在未来某个日期向员工发行股票或等值现金。
每个单位代表员工将来会收到的一股股票或一股股票的现金价值。
（它们被称为*单位 (units)*，因为它们既不是股票也不是股票期权，而是与股票价值在合同上相关联的另一种东西。）

🄳 员工收到 RSU 的股票或现金支付的日期称为**结算日 (settlement date)**。

-   🔸 RSU 可以根据归属时间表进行归属。
    结算日可能是基于时间的归属日期，也可能是基于例如公司 IPO 日期的更晚日期。
-   RSU 在初创公司或早期公司中很难处理，因为当 RSU 归属时，股票的价值可能很高，并且在收到股票时需要缴纳税款。[^thestartup.tn6iyt] 当公司有足够的资本帮助员工支付税款，或者公司是一家已建立售股缴税计划的上市公司时，这并非坏结果。
    但对于现金拮据的私营初创公司来说，这两种可能性都不存在。
    这就是大多数初创公司使用股票期权而不是 RSU 或股票奖励的原因。
-   RSU 通常被授予者认为不太理想，因为它们剥夺了对何时纳税的控制权。期权，如果以等于股票公允市场价值的行权价授予，在行权之前不征税，而行权是期权持有人可以控制的事件。
    如果员工获得了按时间归属的 RSU 或限制性股票奖励，他们将按照归属时间表纳税；
    他们在纳税事件的时间安排上被置于“自动驾驶”模式。
    如果股票在归属日价值很高，税收负担可能会很大。
-   ☝️ 您不应将*限制性股票单位 (restricted stock units)* 与*限制性股票 (restricted stock)* 混淆，后者通常指限制性股票奖励。

### 不太常见的股权类型

虽然大多数员工股权激励采取股票、股票期权或 RSU 的形式，但对股权激励的完整介绍必须提及一些不太常见的形式。

🄳 **虚拟股权 (Phantom equity)** 是一种参照股权的薪酬奖励，但并不赋予接受者在公司中的实际所有权。
这些奖励有各种不同的名称，但理解它们的关键在于知道它们实际上只是现金奖金计划，其中现金金额是参照公司股票确定的。
虚拟股权可能具有显著价值，但由于承诺的合同性质，可能被员工认为价值较低。
虚拟股权计划可以设立为纯粹的酌情奖金计划，这不如拥有一部分实物有吸引力。

虚拟股权的两个例子是虚拟股票和股票增值权：

🄳
[**虚拟股票 (phantom stock)**](http://www.investopedia.com/articles/stocks/12/introduction-phantom-stock.asp)
奖励是一种虚拟股权，赋予接受者在某些事件发生时获得等于公司一股股票价值的付款的权利。

🄳
[**股票增值权 (Stock appreciation rights, SARs)**](https://www.nceo.org/articles/phantom-stock-appreciation-rights-sars)
是一种虚拟股权，赋予接受者获得参照公司股权增值计算的付款的权利。

🚧 需要详细说明通常触发虚拟股票的事件。
关于这些有多罕见的更多数据？
什么是增值？

🄳 [**认股权证 (Warrants)**](https://en.wikipedia.org/wiki/Warrant_%28finance%29) 是另一种购买股票的期权，通常用于投资交易（例如，在可转换票据发行中，投资者也可能获得认股权证，或者律师事务所可能要求获得认股权证以换取供应商融资）。
它们与股票期权的不同之处在于，它们是更简略和独立的法律文件，不是根据适用于所有员工的单一法律协议（通常称为“[计划 (plan)](#documents-and-agreements)”）授予的。

员工和顾问可能不会遇到认股权证，但值得了解它们的存在。

## 税务基础知识

股权激励的授予可能给接受者带来多种类型的税收，包括联邦和州所得税以及就业税。
您需要注意很多事情。[跳到](#taxes-on-equity-compensation)以了解股权税收如何运作，但如果您有时间，本节提供了税务基础知识的技术摘要，以防您从未真正弄清楚工资单上的所有数字。

您不需要了解每一个细节，可以依靠软件和专业人士来确定您应缴纳的税款，但我们确实建议您了解不同类型的税收、它们的数额有多大，以及每种税收是如何被不同事件“触发”的。

鉴于其复杂性，大多数纳税人并不清楚他们的税款究竟是如何计算的。
联邦税法确实占据了数千页[^slatecomar.qqwwen]，并且还涉及州税法的复杂多样性。[^gpogovfdsy.clz3vr]

☝️ 如果您已经熟悉税务术语，本节可能不会有任何重大意外。但对于那些不习惯的人来说，请注意：
许多术语听起来像普通英语，但它们不是。*普通收入 (Ordinary income)*、*长期 (long-term)* 和*短期 (short-term)*、*选择权 (election)*、*合格小企业 (qualified small business)* 以及其他短语都有非常具体的含义，我们将尽力阐明。

### 收入类型

🄳 **收入 (Income)** 是个人赚取的钱。
出于税收目的，主要有两种类型的收入，它们的征税方式不同。
[**普通收入 (Ordinary income)**](https://www.investopedia.com/terms/o/ordinaryincome.asp) 包括工资、薪水、奖金和投资利息。
[**资本利得 (Capital gains)**](https://www.investopedia.com/terms/c/capital_gains_tax.asp) 是个人出售资产（包括股票）所获得的利润。

普通收入和资本利得之间的一个关键区别是，在计算资本利得税时，不仅要考虑资产的售价，还要考虑投资产生的总收益或损失，每种结果都有显著不同的税务后果。

🄳 资本利得分为长期或短期。**长期资本利得 (Long-term capital gains)** 是个人出售持有超过一年的资产（如股票、企业、房屋或土地）所获得的利润。**短期资本利得 (Short-term capital gains)** 是出售持有不到一年的资产所获得的利润。

尽管这个话题并非没有[💰争议](https://www.wsj.com/articles/how-should-capital-gains-be-taxed-1425271052)，
但普遍的观点是，如果您出售持有很长时间的东西，您可以享受较低的税率。

所有这些税率都随着时间的推移基于经济和政治因素而演变，[^taxpolicyc.sjye20] 因此您可以确信它们将来会再次改变。

📰 2017 年，国会通过了[《减税与就业法案》(Tax Cuts and Jobs Act, TCJA)](https://en.wikipedia.org/wiki/Tax_Cuts_and_Jobs_Act_of_2017)，
该法案对 **2018** 纳税年度的税率进行了[许多更改](https://heritageinvestment.com/wp-content/uploads/2018/01/TCJA-HIG-Old-vs.-New-Comparison.pdf)。
长期资本利得税没有[显著变化](https://www.marketwatch.com/story/your-simple-guide-to-the-new-capital-gains-tax-rates-2018-04-16)。

🚧 我们能澄清一下术语 *投资收入 (investment income)* 吗？

### 联邦税

🄳 **所得税 (Income tax)** 是个人向联邦、州以及某些情况下的地方政府支付的款项，包括对普通收入和资本利得的征税。
通常，美国公民、居民和一些[外国人](https://www.irs.gov/individuals/international-taxpayers/nra-withholding)必须[申报](https://www.irs.gov/pub/irs-pdf/p17.pdf)并缴纳联邦所得税。

🔹 一般来说，联邦税适用于多种[收入类型](https://www.irs.gov/taxtopics/tc400.html)。如果您是初创公司的员工，您需要考虑四种联邦税，每种税的计算方式都不同。

☝️ 当涉及股权激励时，您可能需要担心*所有这些*，具体取决于您的情况。
这就是为什么我们在这里有很多内容要涵盖：

🄳 **普通所得税 (Ordinary income tax)** 是对工资或薪金收入以及短期投资收入征收的税。术语**短期资本利得税 (short-term capital gains tax)** 可用于对购买后不到一年出售的资产征收的税，但这些销售的利润按普通收入征税。
对于大部分收入来自工作的人来说，普通所得税是他们缴纳的最大一部分税款。

🄳 **就业税 (Employment taxes)** 是除普通所得税之外的另一种联邦税，由从个人工资中预扣的社会保障税和[医疗保险税 (Medicare taxes)](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax)组成。
就业税也称为[**工资税 (payroll taxes)**](https://en.wikipedia.org/wiki/Payroll_tax)，因为它们经常出现在员工工资单上。2018 年的社会保障工资预扣税率是 FICA 工资基数以下的 6.2%。医疗保险部分是 1.45%，并且在 FICA 工资基数以上不会逐步取消。

-   🚧 审查并添加更多关于社保和医疗保险税的链接。

🄳 **长期资本利得税 (Long-term capital gains tax)** 是对持有超过一年的资产出售征收的税。
长期资本利得税通常低于普通所得税。
许多投资者持有资产超过一年，以符合长期资本利得较低的税负。

🄳 **替代性最低税 (Alternative Minimum Tax, AMT)** 是一种[补充所得税](https://en.wikipedia.org/wiki/Alternative_minimum_tax)，适用于某些情况下的某些个人。
这种类型的税对许多纳税人来说不会出现，但收入较高者和处于特殊情况的人可能需要支付大额 AMT 税单。
AMT 最初于 1979 年颁布，是为了回应 1966 年有 155 名富人未缴纳任何所得税的报道。[^taxpolicyc.mgorf1] 它不同于普通所得税或就业税，并根据其[自身规则](https://www.nerdwallet.com/blog/taxes/alternative-minimum-tax-amt/)计算。

🚧 AMT 的历史和动机是什么？

❗️ 如果您正在阅读本文，AMT 与您相关。
理解这一点很重要，因为行使 ISO 可能触发 AMT。在某些情况下，可能会触发*大量* AMT，*即使您还没有出售股票*并且没有钱支付。
我们将在[后面](#the-amt-trap)讨论这个问题。

#### 图：税级、收入与税负

```hlwy-infographics
{
  "name": "TaxRates",
  "data": {
    "rates": [
      {
        "rate": 0.1,
        "single": 0,
        "married": 0,
        "hoh": 0,
        "label": "10% 税率"
      },
      {
        "rate": 0.12,
        "single": 9525,
        "married": 19050,
        "hoh": 13600,
        "label": "12% 税率起点 (单身 > $9,525, 联合 > $19,050, 户主 > $13,600)"
      },
      {
        "rate": 0.22,
        "single": 38700,
        "married": 77400,
        "hoh": 51800,
        "label": "22% 税率起点 (单身 > $38,700, 联合 > $77,400, 户主 > $51,800)"
      },
      {
        "rate": 0.24,
        "single": 82500,
        "married": 165000,
        "hoh": 82500,
        "label": "24% 税率起点 (单身 > $82,500, 联合 > $165,000, 户主 > $82,500)"
      },
      {
        "rate": 0.32,
        "single": 157500,
        "married": 315000,
        "hoh": 157500,
        "label": "32% 税率起点 (单身 > $157,500, 联合 > $315,000, 户主 > $157,500)"
      },
      {
        "rate": 0.35,
        "single": 200000,
        "married": 400000,
        "hoh": 200000,
        "label": "35% 税率起点 (单身 > $200,000, 联合 > $400,000, 户主 > $200,000)"
      },
      {
        "rate": 0.37,
        "single": 500000,
        "married": 600000,
        "hoh": 500000,
        "label": "37% 税率起点 (单身 > $500,000, 联合 > $600,000, 户主 > $500,000)"
      }
    ],
    "deductions": {
      "single": 0,
      "married": 0,
      "hoh": 0
    },
    "title": "2018年美国联邦普通所得税税率（单身、已婚联合申报、户主）"
  }
}
```

```hlwy-infographics
{
  "name": "TaxRates",
  "data": {
    "rates": [
      {
        "rate": 0,
        "single": 0,
        "married": 0,
        "hoh": 0,
        "label": "0% 税率"
      },
      {
        "rate": 0.15,
        "single": 38600,
        "married": 77200,
        "hoh": 51700,
        "label": "15% 税率起点 (应税收入：单身 > $38,600, 联合 > $77,200, 户主 > $51,700)"
      },
      {
        "rate": 0.2,
        "single": 425801,
        "married": 479001,
        "hoh": 452401,
        "label": "20% 税率起点 (应税收入：单身 > $425,801, 联合 > $479,001, 户主 > $452,401)"
      }
    ],
    "deductions": {
      "single": 0,
      "married": 0,
      "hoh": 0
    },
    "title": "2018年美国联邦长期资本利得税税率"
  }
}
```

🄴 *来源：IRS 和[税收基金会 (Tax Foundation)](https://files.taxfoundation.org/20180207142513/TaxFoundation-FF567-Updated.pdf)*

关于这一切如何运作的一些说明：

-   普通所得税适用于您可能已经熟悉的情况，即您为[工资或薪金](https://www.irs.gov/taxtopics/tc401.html)支付税款。税率基于[申报状态](https://www.irs.gov/newsroom/choosing-the-correct-filing-status)（如果您是单身、已婚或供养家庭）以及您属于哪个[**收入等级 (income bracket)**](https://taxfoundation.org/2018-tax-brackets)。
-   **收入等级。**
    对于普通收入，截至 **2018** 纳税年度，收入等级的[边际税率 (marginal tax rates)](http://www.investopedia.com/terms/m/marginaltaxrate.asp) 分别为 **10%**、**12%**、**22%**、**24%**、**32%**、**35%** 和 **37%**——参见[通知 1036](https://www.irs.gov/pub/irs-pdf/n1036.pdf) 或税收基金会的[摘要](https://files.taxfoundation.org/20180207142513/TaxFoundation-FF567-Updated.pdf)。请务必了解这些等级如何运作，以及您可能属于哪个等级。
    -   ☝️ 有一个普遍的误解是，如果您进入更高的等级，您的收入会减少。[^todayyougo.tyjmz8] 实际情况是，当您超过某些阈值时，您赚取的每一个额外的（边际）美元将以略高的税率征税，该税率等于您所在的等级。在您赚取的收入超过您的扣除额（您无需为此纳税）之后，您的税后收入看起来如上图所示。
        （关于此类误解的更多讨论在[这个 Reddit 帖子](https://www.reddit.com/r/personalfinance/comments/2wkbgz/graphing_one_misconception_about_tax_brackets/)中。）
-   投资收益，例如买卖股票，除非是[**长期**](https://www.irs.gov/taxtopics/tc409.html)的（意味着您持有资产超过一年），否则同样以“普通”税率征税。
-   您还需要支付许多其他联邦税（参见[📥所有州的 2018 年摘要](https://www.adp.com/tools-and-resources/compliance-connection/state-taxes/2018-fast-wage-and-tax-facts.aspx)），
    值得注意的有：
    -   您前 118,500 美元收入的 **6.2%** 用于社会保障
    -   **1.45%** 用于医疗保险
    -   对超过 200,000 美元（单身）或 250,000 美元（已婚联合申报）的收入征收 **0.9%** 的[附加医疗保险税 (Additional Medicare Tax)](https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/Questions-and-Answers-for-the-Additional-Medicare-Tax)
    -   对投资收入征收 **3.8%** 的[净投资所得税 (Net Investment Income Tax, NII)](https://www.irs.gov/uac/Newsroom/Net-Investment-Income-Tax-FAQs)
        （作为《平价医疗法案》的一部分颁布，[^taxpolicyc.w7dds7] 也称为“奥巴马医改 (Obamacare)”），如果您收入超过 200,000 美元（单身）或 250,000 美元（已婚联合申报）。[^investoped.s08hcp]
-   普通联邦所得税、社会保障税和医疗保险税由您的雇主从您的工资中预扣，被称为[**就业税 (employment taxes)**](https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/Understanding-Employment-Taxes)。
-   🔹 长期资本利得的税率低于普通所得税：**0%**、**15%** 或 **20%**。[^foolcomtax.ox10ej] 这涵盖了您获得股息或在持有一年后出售股票的情况。如果您处于中间等级（普通收入大约超过 37,000 美元但低于 413,000 美元），您的长期资本利得税率为 15%。您可以在[税收基金会](https://taxfoundation.org/2018-tax-brackets/)找到有关税收等级的更多详细信息。
-   [AMT](http://fairmark.com/general-taxation/alternative-minimum-tax/alternative-minimum-tax-101/)
    是联邦税法中一个[复杂的部分](https://www.irs.gov/taxtopics/tc556.html)，大多数纳税人无需担心。
    但它在[行使 ISO 时](#the-amt-trap)会发挥作用。大多数人不会支付 AMT，除非它被特定的[情况](https://www.marketwatch.com/story/meet-the-new-friendlier-alternative-minimum-tax-2018-02-26)“触发”，通常是高收入（超过 50 万美元）或高额抵扣。
    您是否支付 AMT 还取决于您申报的州，因为您的州税会显著影响您的抵扣。
    如果您受到影响，AMT 税率通常为 **26%** 或 **28%** 的边际税率，但对于某些范围，实际有效税率为 **35%**，这意味着它对某些收入来说高于普通所得税，而对另一些收入来说则较低。[^foolcomtax.3ka4p1]
    AMT 规则非常复杂，如果它们可能适用于您，您通常需要专业的税务帮助。IRS 的[AMT 助手](https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/Alternative-Minimum-Tax-(AMT)-Assistant-for-Individuals)也可能有所帮助。
-   🔹 《国内税收法典》[第 1202 条](https://www.investopedia.com/terms/s/section-1202.asp)为持有超过五年的合格小企业股票提供了特殊的税收优惠。[^blogwealth.3vcf24]
    目前，这项税收优惠是对高达 1000 万美元的收益实行 100% 的收入排除。
    还有一些特殊规则允许您对持有不到五年的合格小企业股票的收益进行展期。
    通过行使期权获得的股票可以符合第 1202 条股票优惠的资格。
-   🚧 填写有关 QSBS（合格小企业股票）的详细信息。将其移至别处？
    关于此内容的好读物？

### 州税

州税率和规则[差异很大](https://taxfoundation.org/state-individual-income-tax-rates-brackets-2018/)。
由于联邦税率远高于州税率，您通常首先考虑联邦税务规划。
但您也应该了解一些关于您所在州的税率。

州长期资本利得税率范围很广。
加利福尼亚州最高，为 **13.3%**；有几个州没有此税。[^foolcomper.bw6uel]

🔹 因此，一些人甚至会[考虑搬家](https://www.forbes.com/sites/robertwood/2016/05/17/can-you-avoid-california-taxes-by-moving/#316bd9471694)到另一个州，如果他们很可能获得意外之财，比如在 IPO 后出售大量股票。

🚧 您如何确定应向哪个州纳税？
关于此内容有好的资源吗？

## 股权激励的税收

股权和税收以复杂的方式相互作用，员工收到限制性股票、股票期权或 RSU 的税务后果截然不同。
本节将涵盖这些复杂的细节，并帮助您做出决策以减轻股权激励的税收负担。

### 83(b) 选择权

本节涵盖了您在处理股票奖励和股票期权时可能需要做出的最重要和最复杂的决定之一：
通过 83(b) 选择权提前纳税。

-   通常，限制性股票在[*归属时*](http://www.investopedia.com/articles/tax/09/restricted-stock-tax.asp?performancelayout=true)作为普通收入纳税。
-   如果股票属于价值较低的初创公司，这可能不会导致高额税收。
    如果自首次授予股票以来已经过去数年，并且公司现在价值很高，那么应缴税款可能会相当可观。

🄳 《国内税收法典》在[第 83(b) 条](https://www.law.cornell.edu/uscode/text/26/83)中，为收到股权以换取工作的纳税人提供了一个选项，即在期权归属前就对其纳税。
如果符合条件，个人可以通过一个称为 **83(b) 选择权 (83(b) election)** 的程序告知 IRS 他们倾向于这种替代方案。
通过 83(b) 选择权提前纳税可能显著减少税收。
如果股票价值上涨，归属时应缴的税款可能远高于收到时应缴的税款。

-   ☝️ 为什么称之为 *选择权 (election)*？因为您正在*选择 (electing)* 提前纳税以换取 IRS 的这种处理方式。IRS 是否暗地里喜欢把简单的概念弄得令人困惑？
    我们不确定。
-   然而，83(b) 选择权并不能保证减少您的税收。
    例如，股票价值可能不会增加。
    而且，如果您在归属前离开公司，您*无法*拿回已经支付的税款。
-   ❗️ 您必须在授予或行权后的[**30 天内**](https://www.irs.gov/irb/2012-28_IRB/ar12.html)自行向 IRS 提交 83(b) 选择权申请，否则机会将不可撤销地丧失。
-   ☝️ 请注意，83(b) 选择权是在收到实际股票时做出的。
    严格来说，它不能在收到股票*期权*本身时做出：
    您必须首先行使该期权，然后提交选择权申请。
-   如果您收到可提前行权的股票期权（即您不必等待股票归属），您可以在收到行权后的股票时进行 83(b) 选择。
-   第 83(b) 条选择权不适用于已归属的股份；
    该选择权仅适用于尚未归属的股票。
    因此，如果您收到的期权*不可*提前行权（意味着您必须等到它们归属才能行权），则 83(b) 选择权将不适用。
-   🔹 创始人和非常早期的员工在收到未归属股份时几乎总是希望进行 83(b) 选择，因为此时股票价值可能很低。
    如果价值确实很低，且应缴税款不多，您可以在不必支付太多税款的情况下做出选择，并开始计算股份的资本利得持有期。
-   🚧 在此澄清 83b 可以适用于哪些类型的股权激励。

📰 随着 2017 年[《减税与就业法案》(Tax Cuts and Jobs Act, TCJA)](https://en.wikipedia.org/wiki/Tax_Cuts_and_Jobs_Act_of_2017) 的通过，国会批准了一项[**新的第 83(i) 条**](https://www.wsgr.com/WSGR/Display.aspx?SectionName=publications/PDFSearch/wsgralert-section-83i.htm)，
旨在允许 RSU 和股票期权持有人推迟纳税，直到他们能够出售股份来支付税单。
公司是否会选择或能够向员工提供这项福利尚[不清楚](http://stockoptioncounsel.com/blog/tax-deferred-option-exercises-under-the-new-section-83i-tax-cuts-and-jobs-act-of-2017)。

### 409A 估值

当个人的股票归属或行使期权时，IRS 会确定该人应缴纳的税款。但如果没有人买卖股票，就像大多数初创公司的情况一样，那么股票的价值——以及因此应缴纳的任何税款——就不明显。

🄳 任何商品或财产的**公允市场价值 (Fair Market Value, FMV)** 指的是买卖双方在双方都愿意、知情且没有直接压力的情况下达成一致的价格。
公司股票的公允市场价值指的是公司向员工发行股票的价格，并被 IRS 用于计算员工因收到的任何股权激励而应缴纳的税款。
公司股票的 FMV 由公司最近的 409A 估值确定。

🄳
[**409A 估值**](http://www.fenwick.com/FenwickDocuments/409_Valuations_Stock_Options.pdf) 是 IRS 要求私营公司对其向员工发行或提供的任何股权的价值进行的评估。
公司希望 409A 估值较低，以便员工从期权中获利更多，但又不能低到 IRS 认为不合理的程度。
为了最大限度地降低 409A 估值被操纵以利于公司的风险，公司会聘请独立公司进行 409A 估值，通常每年一次或在融资等事件之后进行。

员工股权的 409A 估值通常远低于投资者为优先股支付的价格；
通常，它可能只有优先股价格的三分之一或更少。

🌪 尽管 409A 流程是初创公司必需且完全标准化的，但这种做法是形式化和完全猜测的奇怪混合体。
风险投资家比尔·格利 (Bill Gurley) 称其为“相当精确——但极其不准确”。您可以阅读更多关于其[细微差别和争议](https://www.nytimes.com/2017/03/08/business/dealbook/valuation-shell-game-silicon-valleys-dirty-secret.html)的内容。

-   🚧 关于 409A 估值何时进行的更多信息。

    -   409A 确实必须每 12 个月进行一次，以授予公司安全港。
    -   在任何可能被视为“重大事件”的事件之后，必须进行 409A 估值，“重大事件”是一种委婉的说法，指任何可能显著改变公司价格或价值的事件。其他例子可能包括 CEO 离职、公司开始赚大钱或被收购。

-   ∑ “FMV”是在最高法院案例 546，[美国诉卡特赖特案 (United States vs. Cartwright)](https://scholar.google.com/scholar_case?case=4964174066744569590&hl=en&as_sdt=6&as_vis=1&oi=scholarr#p551) 中定义的法律术语。

-   ∑ “409A”是指《国内税收法典》中规定期权在授予时免税要求的[条款](https://en.wikipedia.org/wiki/Internal_Revenue_Code_section_409A)。

### ISO 和 NSO 的税收

通常，早期到中期的公司会授予股票期权，可能是[ISOs 或 NSOs](#kinds-of-stock-options)。

-   ❗️当您获得股票期权并考虑是否以及何时行权时，您需要考虑税收以及**何时需要缴税**。原则上，您需要考虑在三个时间点可能产生的税收：
    -   **授予时**
    -   **行权时**
    -   **出售时**
-   这些事件会以不同的方式触发 NSO 和 ISO 的普通税（高税率）、长期资本利得税（较低税率）或 AMT（可能高税率）。

🄳 行权时的税收将取决于行权价和 FMV 之间的差额，称为**价差 (spread)** 或[**议价部分 (bargain element)**](http://www.investorwords.com/5414/bargain_element.html)。

-   🔹 如果您以低行权价获得 ISO 或 NSO，并且议价部分为零，那么您或许能够以合理的价格行权而根本不触发税收。
    因此，假设公司允许，*立即*提前行权（购买大部分或全部股份，即使它们尚未归属）并同时提交 83(b) 选择权是有意义的。
-   🔸 如前所述，83(b) 选择权是选择在收到财产时纳税，即使您可能不得不放弃或将财产退还给公司。
    您可以在收到股票时做出选择，但不能在收到股票期权或 RSU 时做出选择，因为根据第 83(b) 条的目的，期权和 RSU 不被视为财产。
-   🚧 移动或删除此注释，因为它在前面已涵盖？
-   🔸 ISO 通常受到初创公司的青睐，因为从税收角度看，它们据说对员工更有利。
    这假设 (1) 不会触发 AMT，并且 (2) 您将通过持有股票达到适当的持有期而获得较低的长期资本利得税率。
    然而，通常情况下，您要么陷入 AMT 陷阱，要么未能持有股票足够长的时间以满足复杂的 1 年 + 2 年要求，要么行权时的价差很小或为零，因此差异无论如何都不重要。
    NSO 由于需要缴纳就业税（而 ISO 不需要）而确实具有略高的税收。
-   🌪 总的来说，目前尚不清楚 ISO 对员工是否真的好很多，因此[许多人](http://www.business2community.com/finance/nsos-better-isos-0826167#fz1HTCiOQxRyTr62.97)主张[使用 NSO](http://www.startuplawblog.com/2010/08/11/top-reasons-nqos-over-isos/)。
-   ☝️ 这部分是因为 ISO 可能使满足长期资本利得持有期变得更加困难。[^thestartup.25gj0l]
    许多人期望提前行权，再加上 83(b) 选择权，将帮助他们持有股票足够长的时间以符合长期资本利得的资格。
    虽然这对 NSO 是正确的，但关于 ISO 的规则中一个模糊的部分规定，即使有 83(b) 选择权，资本利得持有期也要到股份实际归属时才开始。因此，如果您想立即行使期权并提交 83(b) 选择权，并且您可能很快就有流动性，那么对于那些可以这样做的人来说，最好选择 NSO。

### AMT 陷阱

在税收和股权激励方面，有一种情况非常危险，我们专门用一节来讨论。

❗️ 如果您收到了 ISO，行使它可能会意外触发巨额 AMT 税单——甚至在您实际通过出售获利之前！
如果行权价和 409A 估值之间存在巨大价差，您可能需要承担巨额税单，即使您无法出售股票。
这曾导致人们破产。
它还导致国会批准了一次性豁免，但这种情况再次发生的几率非常低。

🄳 行使 ISO 触发巨额 AMT 税单，却无法出售股票来缴税的灾难性情景，有时被称为 **AMT 陷阱**。这个[臭名昭著的](https://www.nceo.org/articles/stock-options-alternative-minimum-tax-amt)问题已经困住了许多员工，并在过去的互联网泡沫破灭期间导致一些人[破产](http://blog.sfgate.com/dgreenberg/2012/06/22/tax-advice-from-the-dot-com-bubble-beware-of-isos/)。
现在更多人知道了这个问题，但它仍然是一个需要规划应对的重大障碍。

📰 2017 年，国会通过了[《减税与就业法案》(Tax Cuts and Jobs Act, TCJA)](https://en.wikipedia.org/wiki/Tax_Cuts_and_Jobs_Act_of_2017)，
该法案提高了 AMT 免税额及其逐步取消的门槛。
这意味着 2018 年受 AMT 影响的人数将少于往年。[^mediumcomb.57vdab]

请注意，如果您的 AMT 适用于 2008 年之前的事件，您就[不用担心了](http://www.startuplawblog.com/2009/04/03/whoops-i-didnt-pay-amt-on-my-isos-exercised-prior-to-1108-what-do-i-do/)。

如果您行使 ISO，请了解这个主题并咨询专业人士。
AMT 陷阱不适用于 NSO。

🚧 关于国会豁免的报道链接？

### 股票奖励 vs. ISOs vs. NSOs

由于差异非常细微，以下是从员工角度对限制性股票奖励、ISO 和 NSO 税收的总结。

-   **限制性股票奖励。**
    假设有归属期，您可以通过 83(b) 选择权提前全额纳税，或在归属时纳税：

    -   授予时：
        -   如果提交了 83(b) 选择权，按 FMV 缴纳普通所得税
        -   否则无税
    -   归属时：
        -   如果提交了 83(b) 选择权，则无税
        -   否则按已归属部分的 FMV 缴纳普通所得税
    -   出售时：
        -   如果在计入收入后持有**超过 1 年**，则按收益缴纳长期资本利得税
        -   否则按普通所得税纳税（包括立即出售）

-   **NSOs。** 您在行权时全额纳税，出售就像任何投资收益一样：

    -   授予和归属时：
        -   如果以 FMV 授予，则无税
    -   行权时：
        -   按议价部分缴纳普通所得税
        -   工资单上预扣所得税和就业税
    -   出售时：
        -   如果在行权后持有**超过 1 年**，则按收益缴纳长期资本利得税
        -   否则按普通所得税纳税（包括立即出售）

-   **ISOs。** 您在行权时可能支付较少税款，但情况复杂：

    -   授予和归属时：
        -   如果以 FMV 授予，则无税
    -   行权时：
        -   议价部分产生 **AMT 税务事件**
        -   无普通所得税或资本利得税
        -   工资单上无所得税或就业税预扣
    -   出售时：
        -   如果在行权后持有**超过 1 年**且自授予日起持有**超过 2 年**，则为长期资本利得
        -   否则按普通所得税纳税（包括立即出售）

专门研究股权激励的律师 Mary Russell 建议，在私营公司中，每种形式的股权应在适当的时间使用：
限制性股票奖励用于初创公司的最早阶段，具有较长行权窗口的股票期权用于早期到中期阶段，RSU 用于后期阶段。[^stockoptio.z54l1t]

如果您喜欢税务复杂性，可以从以下来源了解更多信息：

-   IRS 对 ISO 和 NSO 的[税务主题](https://www.irs.gov/taxtopics/tc427.html)报道
-   Joe Wallin 在 Startup Law Blog 上的帖子，“[授予 NQO 而非 ISO 的六大理由](http://www.startuplawblog.com/2010/08/11/top-reasons-nqos-over-isos/)”
    和“[激励性股票期权 vs. 非合格股票期权](http://www.startuplawblog.com/2013/05/15/incentive-stock-options-vs-nonqualified-stock-options/)”
-   Investopedia 的帖子“[充分利用员工股票期权](http://www.investopedia.com/articles/optioninvestor/07/esoabout.asp)”
-   EquityZen 对该主题的总结，“[理解股权激励及其对初创公司员工的意义](https://equityzen.com/blog/understanding-equity-compensation-for-startup-employees/)”

### RSU 的税收

如果您被授予 RSU，每个单位代表一股股票，您将在单位归属时获得这些股票。

-   以下是 RSU 的税务摘要：
    -   授予时：
        -   无税
    -   归属/交付时：
        -   按当前股价缴纳普通所得税
    -   出售时：
        -   如果在归属后持有**超过 1 年**，则按收益缴纳长期资本利得税
        -   否则按普通所得税纳税（包括立即出售）
-   🔸 当您收到股票时，您需要按当时的价值纳税。[^joewallinc.8eaojr]
    如果您是雇员，这意味着您可能需要向公司开具支票以支付您的所得税和就业税预扣款。
    通常，对于美国员工，公司会以股份形式预扣税款，这样员工在归属时无需采取任何行动。[^schwabcomp.94cuxl]
-   如果您在股票价值很低时收到 RSU，您不能选择在收到 RSU 时按该股票的价值纳税——您在归属时纳税，基于当时股票的价值。
-   🔸 RSU 在私营公司中存在一些大问题：
    -   即使股票缺乏流动性，您在收到股票时仍需纳税。
    -   您无法将在收到 RSU 之日到结算之日期间标的股票价值增长的税收影响降至最低。
    -   如果您是雇员，您将需要向公司开具支票以满足您的所得税和就业税预扣要求。
-   🔸 从税收角度来看，RSU 不如股票期权有吸引力，因为您不能对 RSU 进行 83(b) 选择。
    相比之下，如果您收到股票期权，只要它以公允市场价值定价，您在收到期权时将没有收入，您的所得税和就业税后果将推迟到您行权时，而行权在很大程度上是您可以控制的事件。

### 税务比较表

#### 表格：股权激励类型税务比较

此表总结了不同类型股权激励的税收差异。

|                       | 限制性股票奖励                                                                                                    | ISOs                                                                                                                                       | NSOs                                                                                                                               | RSUs                                                                                                                    |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| *授予时纳税*            | 如果提交 83(b) 选择权，按 FMV 缴纳普通所得税。否则无税。                                                                | 如果以 FMV 授予，则无税。                                                                                                                     | 如果以 FMV 授予，则无税。                                                                                                                | 无税。                                                                                                                    |
| *归属时纳税*            | 如果提交 83(b) 选择权，则无税。否则按已归属部分的 FMV 缴纳普通所得税。                                                    | 如果以 FMV 授予，则无税。                                                                                                                     | 如果以 FMV 授予，则无税。                                                                                                                | 按当前股价缴纳普通所得税。                                                                                                 |
| *行权时纳税*            |                                                                                                                   | 议价部分产生 AMT 税务事件。无普通所得税、资本利得税或就业税。                                                                                         | 按议价部分缴纳普通所得税。所得税和就业税。                                                                                              |                                                                                                                         |
| *出售时纳税*            | 如果在计入收入后持有**超过 1 年**，则按收益缴纳长期资本利得税。否则按普通所得税纳税（包括立即出售）。                                    | 如果在行权后持有**超过 1 年**且自授予日起持有**超过 2 年**，则为长期资本利得。否则按普通所得税纳税（包括立即出售）。                                    | 如果在行权后持有**超过 1 年**，则按收益缴纳长期资本利得税。否则按普通所得税纳税（包括立即出售）。                                    | 如果在归属后持有**超过 1 年**，则按收益缴纳长期资本利得税。否则按普通所得税纳税（包括立即出售）。                                    |

### 税务风险

由于它们非常重要，我们列出一些在股权激励税收方面需要注意的代价高昂的错误：

-   ❗️ 如果您要提交 83(b) 选择权，必须在股票授予或期权行权后的 **30 天内**完成。
    律师事务所通常需要一段时间才能将文件发送给您，因此您可能只有一两周的时间。如果您错过了这个窗口期，可能会产生巨大的税务后果，并且这基本上是一个不可撤销的错误——这是 IRS 不会延长的最后期限之一。
    提交时，请从邮局获取文件证明以及送达确认，并附上一个写好地址、贴好邮票的信封，以便 IRS 向您发送回执。
    （有些人对此非常担心，甚至会请朋友陪同去邮局作证！）
-   ❗️ 注意我们已经讨论过的 AMT 陷阱。
-   ❗️ 如果您行使期权，并且您的收入来自咨询而非雇佣（1099 表而非 W-2 表），您将需要缴纳[自雇税 (self-employment tax)](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes)，
    其中包括 FICA 的雇主和雇员两部分。除了缴纳正常的所得税外，这意味着您需要为达到 FICA 工资基数的部分缴纳社会保障税（**6.2%**），并为您所有收入缴纳医院保险部分（**2.9%**）。
-   ❗️ 认真决定何时行使期权。
    如前所述，如果您等到公司业绩非常好时，或者在您离职时才行权，这种延迟可能会带来严重的弊端。

## 计划与情景

### 评估股权激励

一旦您了解了[股权类型](#how-equity-is-granted)及其[税务影响](#taxes-on-equity-compensation)，您就掌握了评估包含股权激励的录用邀约或评估您目前在公司拥有的股权所需的许多工具。

总而言之，您必须确定或对以下几件事做出有根据的猜测：

-   **股权价值。** 这可以通过公司未来可能具有的价值以及您可能拥有的股份数量来估计。
    -   **所有权百分比。**
        正如我们提到的，除非您知道已发行在外的股份数量，否则知道您拥有多少股票或股票期权是毫无意义的。
        重要的是这些股份所代表的公司所有权百分比，包括计算总数方式的[细节](#counting-shares)。
    -   **风险。** 理解业务中的[风险](#stages-of-a-startup)和稀释对于确定股权可能的未来价值至关重要。
        Leo Polovets 的[这篇文章](http://codingvc.com/valuing-employee-options/)提供了一些额外的思考。
-   **归属。** 理解您将在[何时](#vesting-and-cliffs)获得股权，以及您是否能够行使股票期权（并支付相关成本和税款），以及您是否可以在行权窗口到期前完成所有这些。
-   **流动性。** 确定您何时能够[出售您的股份](#sales-and-liquidity)，以及届时是否可能盈利。
    （我们接下来讨论私有股票的流动性。）
-   **税收。** [税务问题](#taxes-on-equity-compensation)与股权价值密不可分。
    了解您可能的授予、行权、归属和出售在普通所得税、就业税、长期资本利得税和替代性最低税方面的税务影响。

这涉及很多方面，即便如此，决策仍充满不确定性，但一旦掌握了这些信息，就有可能做出更加明智的决策。

### 私人股票价值几何？

我们现在转向确定私营公司股票价值的问题。
我们已经看到私营公司的股票通常[无法出售](#can-you-sell-private-stock)，
因此其价值[难以估计](https://www.investopedia.com/articles/fundamental-analysis/11/valuing-private-companies.asp)。

您还不能出售的股权价值反映了三个主要关切点：

1.  公司目前的经营状况——即其盈利能力，或吸引了多少客户。
2.  公司未来的表现如何。
3.  公司作为另一家公司的一部分有多大可能具有价值——即它是否可能被[收购](#sales-and-liquidity)。

第一个关切点相对明确，如果您了解公司的财务状况。
第二个和第三个则归结为预测，并且从不确定。
事实上，重要的是要理解所有这三个估计的不确定性有多大，这取决于公司的发展阶段。

在早期私营公司中，可能很少或没有利润，但由于对其未来盈利或被收购能力的高预期，公司可能看起来很有价值。
如果这样的公司从投资者那里获得资金，投资者会根据这些有根据的猜测和市场条件来确定他们支付的价格。

在初创公司中，股权的未来价值往往存在高度不确定性，而在后期私营公司中，财务状况更容易被理解（至少对投资者和其他了解公司内部情况的人而言），这些预测通常更确定。

### 你能出售私人股票吗？

最终，您的股权价值取决于您是否以及何时能够将其转换为您可以出售换取现金的股票。
对于上市公司而言，答案相对容易估计——只要对您的出售能力没有限制，您就知道您拥有或可能拥有的股票的当前市场价值。
那么私营公司呢？

流动性事件通常使得私营公司的股东能够出售他们的股票。
然而，个人有时可能在公司仍为私有时获得流动性。

🄳 **二级市场（或二级销售、私人销售）(secondary market, secondary sale, or private sale)** 交易是指私营公司股票[被出售](https://www.cooleygo.com/secondary-sales-of-private-company-stock/)给另一个私人方。
这与**一级市场 (primary market)** 交易形成对比，后者是公司直接向投资者出售股票。二级销售并非例行公事，但有时会发生，例如当员工向希望投资该公司的合格投资者出售股票时。

🄳 员工持有的股份通常受公司**优先购买权 (right of first refusal, ROFR)** 的约束，这意味着员工在未先向公司提出出售其股份的要约之前，不能将其股份出售给第三方。

🔸 出于合同和实际原因，私人销售通常需要公司的同意和合作。
虽然持有私人股票的人可能希望或期望他们只需要找到一个愿意购买的买家，但在实践中，二级销售仅在[少数情况下](https://venturebeat.com/2016/12/19/secondary-market-for-shares-in-pre-ipo-unicorns-is-booming/)能够成功。

与公共交易所的交易不同，私营公司股票的买方和卖方并不能完全控制销售。
**公司可能不支持二级销售**有几个原因：

-   历史上，初创公司认为让现有员工出售股票没有什么意义，因为他们更希望员工持有股票并通过提升公司整体价值来使其更有价值。
-   即使员工留存不是问题，也有理由认为私人销售可能不符合公司的利益。
    前员工和其他股东通常难以与公司发起二级交易。[^wsjcomarti.vm6qmp]
    私人买家可能会要求查看公司的内部财务数据，以估计其股票的当前和未来价值；
    公司可能不希望分享这些机密信息。
-   公司必须[考虑](https://www.square1bank.com/insights/new-normal-secondaries-409a-valuation-process/)销售是否会影响其 [409A 估值](#409a-valuations)。
-   二级销售对忙碌的初创公司 CEO 和 CFO 来说是一项行政和法律负担，可能无法排在优先事项列表的首位。

🔹 然而，近年来二级市场的参与情况有所演变，[^techcrunch.qn7usd][^industryve.6prupc][^mediumcomr.ez02hw] **一些选择可能是可行的**：

-   [SharesPost](http://sharespost.com/)、[Equidate](https://www.equidateinc.com/) 和 [EquityZen](https://equityzen.com/) 试图围绕二级销售建立市场，
    特别是针对知名的 IPO 前公司。
-   其他一些二级公司已经出现，它们对某些购买感兴趣，
    特别是来自创始人、早期员工或高管的较大规模二级销售。
    公司可以与一家公司合作以促进多笔交易。
    这些公司包括 [137 Ventures](http://137ventures.com/)、
    [ESO Fund](https://employeestockoptions.com/)、
    [Akkadian Ventures](https://www.akkadianventures.com/)、
    [Industry Ventures](http://www.industryventures.com/)、[Atlas Peak](http://www.atlaspeakcap.com/)
    和 [Founders Circle](http://www.founderscircle.com/)。
-   在某些情况下，员工可能幸运地将股票私下出售给希望增加持股比例的个人，例如董事会成员或前高管。
    更多讨论可以在[Quora](https://www.quora.com/How-do-employees-in-startups-sell-stock-in-the-secondary-markets) 上找到。

### 股票期权情景

围绕股票期权的关键决策是何时行权，以及如果可以的话，何时出售。
这里我们列出一些可能适用于您的常见情景。
考虑这些情景及其结果可以帮助您评估自己的处境并决定应该做什么。

-   **行权并持有。**
    您可以给公司开一张支票并支付价差产生的任何税款。
    然后您就成为一名股东，拥有一份未来可能有价值的股票证书。
    如[讨论](#how-equity-is-granted)过的，您可以行权：
    -   提前行权，甚至在授予后立即行权。
    -   在归属前行权（如果可以提前行权）。
    -   在归属后的某个时间行权。
    -   离开公司后行权，只要行权窗口仍然开放。
        -   🔸 回想一下，窗口很可能在您离开公司后[很快关闭](#how-options-expire)，通常是终止服务后 90 天。
-   **等到被收购。**
    如果公司以远高于行权价的倍数被收购，您届时可以使用您的期权购买有价值的股票。
    然而，如前所述，除非出售价格超过清算优先权积压，否则您的股份可能几乎一文不值。
-   🔸 **二级市场。**
    如[讨论](#can-you-sell-private-stock)过的，在某些情况下，可以行权并将私营公司的股票直接出售给私人方。
    但这通常需要公司的某种合作，并且不是您总能指望的事情。
-   **无现金行权。**
    在 IPO 的情况下，经纪人可以允许您行使所有已归属的期权，并立即将其中的一部分出售到公开市场，从而消除了预先行权和支付税款所需的现金。

🔹 请注意，其中一些情景可能需要大量前期现金，因此尽早进行计算是有意义的。
如果您处境困难，可能因为没有现金行权而完全失去有价值的期权，那么探索上述每种情景或其组合是值得的，例如先行权然后出售一部分以支付税款。
此外，有一些[基金](#can-you-sell-private-stock)和个人投资者可能能够为您垫付行权或支付税款的现金，以换取分享利润的协议。

作者兼程序员 Alex MacCaw [探讨了](https://blog.alexmaccaw.com/an-engineers-guide-to-stock-options#exercising_2)一些更详细的情景。

🚧 信息图：
这些行权选项的可视化。
流程图？“如果这样，那么这样”（带箭头）。

### 风险总结

由于其重要性，我们将总结一些在考虑股权激励时讨论过的关键风险：

-   ❗️ 在股权激励方面，细节至关重要！
    您需要详细了解股票授予或股票期权的类型，以及它对您的税收意味着什么，才能知道您的股权价值几何。
-   ❗️ 因为细节如此重要，向熟悉股权激励的税务顾问或律师（或两者兼有）寻求[专业建议](#seeking-professional-advice)通常是个好主意。
    避免完全自己处理所有事情，但也要避免盲目信任顾问而不让他们以您能理解的方式向您解释细节。
-   ❗️ 对于股票期权，高昂的行权成本或高额税收，包括 AMT 陷阱，可能会阻止您行使期权。
    如果您无法出售股票且行权窗口有限，您实际上可能被迫放弃您的股票期权。
-   ❗️ 如果工作邀约包含股权，您需要大量信息来理解股权部分的价值。
    如果公司足够信任您以至于发出录用邀约，但却不愿意回答关于该邀约的问题，请将其视为一个警告信号。
    接下来，我们将提供更多关于在您的邀约中应询问什么以及如何谈判以获得您想要的答案的细节。

## 录用邀约与谈判

当公司提供任何形式的股权作为其薪酬方案的一部分时，潜在员工需要考虑一系列全新的因素。
本章将帮助您准备谈判包含股权的工作邀约，涵盖谈判技巧和期望，以及关于在股权方面可以询问什么和可以谈判什么的具体提醒。

### 为什么谈判很重要

在接受任何工作邀约之前，您都需要[坚定而公平地](http://cefne.com/en/harvard-method-negotiation)进行谈判。您计划为任何全职职位投入大量的时间和精力；
帮助自己确保这是[💰您想要的](https://hbr.org/2016/12/think-strategically-about-your-career-development)。

☝️ 对谈判感到[焦虑](https://www.pon.harvard.edu/daily/negotiation-skills-daily/the-impact-of-anxiety-and-emotions-on-negotiations-how-to-avoid-misjudgment-in-negotiation-scenarios/)是完全正常的，无论您是第一次还是第十次经历这个过程。这关系重大，要求您需要或想要的东西可能会让人感到不舒服和有压力。
许多[人认为](https://www.forbes.com/sites/tanyatarr/2017/12/31/here-are-five-negotiation-myths-we-can-leave-behind-in-2017/#250ff99b15f9engaging)谈判可能会导致工作邀约被撤销，所以他们会几乎不讨论就接受邀约。
但请记住，谈判是您与新团队合作的第一次体验。如果您感到紧张，提醒自己为什么进行这些对话很重要可能会有所帮助：

-   谈判要求您专注于您真正想要的东西。
    什么对您来说是重要的——个人成长、职业发展、影响力、认可、现金、所有权、团队合作？
    对自己不清楚优先事项是什么，是日后不满的根源。
-   如果您对录用邀约的条款不满意，不经讨论就接受它不仅对您自己，对您的新公司和同事来说也可能很困难。
    没有人愿意招聘一个几个月后有更好机会就离开的人。
    为了所有人的利益，现在花点时间考虑您想要什么——然后[提出来](https://www.earnest.com/decision-making/articles/negotiating-job-offers-science-asking-want)。
-   谈判过程本身可以教会您很多关于公司和您未来经理的信息。讨论像录用邀约这样棘手的话题是了解您将来如何与某人合作的好方法。

像这样的指南无法为您提供关于什么是合理录用邀约的个性化建议，因为这在很大程度上取决于您的技能、候选人市场、您拥有的其他录用邀约、公司能支付多少、公司找到的其他候选人以及公司的需求。
但我们可以涵盖录用邀约的基本预期，并建议候选人如何进行谈判。

### 平等待遇

🔹 公司能够并且应该努力确保所有候选人在招聘过程中获得[平等待遇](https://rework.withgoogle.com/guides/pay-equity/steps/introduction/)，但不平等现象依然存在。[^iwprorgpub.1ukyxt]
工作场所的薪酬和机会差距涉及种族和性别，[^digitalcom.k5w0oc] 相关研究关注美国工作场所的不平等、[^pewresearc.dws8o8] 高管领导层及其有据可查的缺乏多样性[^aflcioorgp.6v6p19][^fortunecom.87hw00] 以及技术行业。[^eeocgoveeo.9aynwh]
谈判本身存在的性别偏见也是一个问题；
许多女性曾被使她们觉得不应该要求自己应得的东西。[^newyorkerc.mdcz9c]

需要付出更多努力来消除偏见和缩小工资差距。
所有候选人都应该花时间了解自己的价值以及他们能为公司带来的具体价值，以便为争取更好的录用邀约做好充分准备。

### 一般期望

-   许多公司会在[谈判](#negotiation-tips)期间给予一定的 leeway（灵活性），让您表明您是偏好[更高薪水](https://hired.com/blog/candidates/salary-vs-equity-how-decide-whats-right/)还是[更高股权](https://www.investopedia.com/articles/personal-finance/041515/equity-vs-salary-what-you-need-know.asp)。
-   拥有竞争性录用邀约的候选人几乎总是有更多筹码并获得更好的录用邀约。[^shrmorgres.qv3vrf]
-   初创公司的薪水通常略低于您在成熟公司获得的薪水，因为早期现金非常宝贵。
    对于非常早期的初创公司，风险更高，录用邀约的可变性可能更大，公司之间的差异也会更大，特别是在股权方面。
-   决定[股权](#typical-employee-equity-levels)的主要因素是公司处于哪个融资[阶段](#stages-of-a-startup)，以及您将在公司扮演的角色。
    如果没有融资，可能需要大量股权才能让早期团队成员以极少报酬甚至免费工作。
    一旦 A 轮融资到位，大多数人会接受典型或适度折扣的薪水。
    种子轮融资的初创公司介于两者之间。

### 录用邀约

🄳 在发出工作邀约时，公司通常会先给候选人一个**口头邀约 (verbal offer)**，以加快进度并促进谈判，如果看起来候选人和公司在邀约条款上接近达成一致，则会随之发出**书面邀约 (written offer)**。书面邀约采用[📥**录用通知书 (offer letter)**](https://www.upcounsel.com/employee-offer-letter) 的形式，这只是发送给候选人的摘要，通常包含截止日期以及其他细节和[文书工作](#documents-and-agreements)。

尽管公司通常希望您立即签署以节省时间和精力，但如果您认真对待，您也会在签署前与公司（通常是招聘经理、您未来的经理或招聘人员，或他们的某种组合）进行多次交谈。这有助于您谈判细节，并让您有机会了解您可能与之共事的人、公司和职位，以便您可以为自己的个人情况做出最佳决定。

当您准备好接受录用通知书的条款时，您就可以签字了。

[录用通知书](https://www.glassdoor.com/blog/how-to-read-offer-letter/)中需要注意的事项包括：

-   **职位和级别 (Title and level)。**
    您的角色的正式名称，向谁汇报，以及您的角色在公司内部的资历级别。
-   **薪水 (Salary)。** 您每年获得的税前现金收入。
-   **股权激励 (Equity compensation)。**
    您现在知道这是什么了。
-   **奖金 (Bonus)。** 如果公司有此计划，您将定期获得的额外现金。
-   **[签约奖金 (Signing bonus)](https://www.investopedia.com/terms/s/signing-bonus.asp)。** 您仅因签约而获得的现金。（签约奖金通常附带一些条件——例如，如果您在 12 或 24 个月内离开公司，您可能需要偿还奖金。）

虽然细节可能不包含在您的录用通知书中，但要获得有关您的全面薪酬的完整信息，您还需要讨论：

-   [福利 (Benefits)](https://en.wikipedia.org/wiki/Employee_benefits)，如健康保险、退休储蓄和小吃。
-   可能对您重要的所有其他工作方面，如休假时间、在家工作的能力、灵活的工作时间、培训和教育等等。

关于这些组成部分的一些一般说明（部分归功于 [Cristina Cordova](https://twitter.com/cjc/status/984094472190349312)）：

-   早期初创公司将专注于薪水和股权以及（如果获得资助）福利。
    提供奖金或签约奖金在规模更大、更繁荣的公司中更为常见。
-   奖金通常根据公司和您的级别标准化，因此不太可能是您可以谈判的内容。
-   签约奖金是高度可协商的。
    这并不意味着任何公司都会提供高额签约奖金，但这是可行的，因为签约奖金金额因候选人而异，并且与薪水和其他奖金不同，它对公司来说是一次性成本。

### 来自初创公司的录用邀约

由于初创公司比许多成熟公司小得多，而且它们可能快速增长，因此在谈判来自初创公司的工作录用邀约时，需要考虑额外的因素：

-   **现金与股权。**
    如果您的[风险承受能力](https://www.investopedia.com/terms/r/risktolerance.asp)
    相当高，您可以要求一份包含更多股权和更少现金的录用邀约。
    如果一家公司开始表现良好，即使您最初获得了更多股权，它也可能会“提升”较低的薪水（使其更接近市场平均水平）。
    另一方面，如果您要求更多现金和更少股权，您以后不太可能谈判获得更多股权，因为随着时间的推移，股权越来越稀缺（至少在成功的公司中是这样！）。企业家兼风险投资家
    [马克·苏斯特 (Mark Suster)](https://en.wikipedia.org/wiki/Mark_Suster) 强调需要通过调整薪酬和支出来
    [升级](https://bothsidesofthetable.com/this-is-how-startups-level-up-after-raising-money-328d17076515)，
    在每个融资阶段适当关注。
    在初创公司的极早期，员工的薪水高于公司创始人并不罕见。[^siliconhil.1wd4aa]
-   🚧 什么是风险？人们应该如何考虑风险承受能力？
    关于此内容的好读物？
-   **职位。** 在小型且不断发展的公司中，早期谈判职位和角色的确切细节可能不那么重要，因为您的角色和他人的角色可能会发生很大变化，而且变化很快。
    更重要的是您尊重公司的创始人和领导者。
    更重要的是您感觉自己受到[尊重](https://blog.shrm.org/blog/respect-and-trust-top-the-list-of-most-important-employee-job-satisfaction)。

### 候选人可以提出的问题

🔹 当您收到包含任何类型股权的录用邀约时，提出问题非常重要。
除了帮助您了解股权邀约的事实外，讨论这些细节的过程还可以帮助您了解公司的透明度和响应能力。
以下是您应该考虑提出的一些问题，特别是如果您正在评估来自初创公司或其他私营公司的录用邀约：

-   **所有权百分比。**
    -   *这些股份代表公司多少百分比？*
    -   *计算该百分比时使用了哪组股份？
        是已发行在外股份还是完全稀释股份？*
    -   *有哪些未偿还的可转换证券（可转换票据、SAFE 或认股权证），我可以预期它们的转换会带来多少稀释？*
-   **估值。**
    -   *上一轮融资对公司的估值是多少？
        （即，优先股股价乘以总已发行在外股份数是多少？）*
    -   *最近的 409A 估值是多少？
        是什么时候进行的，近期会再次进行吗？*
    -   *在普通股具有正价值之前，需要达到什么样的退出估值（即，清算优先权积压是多少）？*
-   **股票期权。**
    -   *你们允许提前行使我的期权吗？*
    -   *在我离职或被解雇后，我是否必须在 90 天内行使我的期权？
        公司是否延长离职员工期权的行权窗口？*
-   **归属。**
    -   *所有员工是否都在同一个归属时间表上？*
    -   *如果公司被收购，我的归属是否有任何加速？*
    -   *你们有关于后续股票授予的政策吗？*
    -   *公司对已归属股份是否有任何回购权？*

这些信息将帮助您考虑可能的[行权情景](#stock-option-scenarios)的利弊。

🔹 如果您正在考虑为一家初创公司工作，还需要提出更多问题来评估公司的业务状况及其计划。
在收到录用邀约之前或之时是进行此操作的正确时机。
初创公司在分享财务信息方面可以理解地持谨慎态度，因此您可能无法获得所有这些问题的完整答案，但您至少应该问：

-   *公司已经筹集了多少资金（包括多少轮融资，以及何时融资）？*
-   *上一轮融资对公司的估值是多少？*
-   *优先股上的总清算优先权是多少？*
    （这将告诉您公司需要以多少价格出售，普通股——即您的股权——才能在退出时有价值。）
-   *公司近期是否可能再次融资？*
-   *公司目前的资金能维持多久？*
    （这很可能按当前的烧钱率给出，即公司消耗资金的速度，因此很可能不包括未来员工工资等计算。）
-   *招聘计划是什么？
    （在多长时间内招聘多少人？）*
-   *目前的收入是多少（如果有的话）？
    收入目标/预测是什么？*
-   *在收入、员工数量和市场地位方面，您认为这家公司在 1 年和 5 年后会是什么样子？*

还有其他一些[资源](https://blog.wealthfront.com/stock-options-14-crucial-questions/)提供了[更多类似的问题](http://www.inc.com/atish-davda/5-questions-you-should-ask-before-taking-a-start-up-job-offer.html)
供考虑。

🚧 总结上述链接中的最佳项目。

### 典型员工股权水平

🚧 本节目前主要涵盖初创公司；有哪些后期阶段的资源可用？

薪酬数据是高度情境化的。
员工在股权、现金和福利方面获得什么，取决于他们担任的角色、他们工作的行业、他们和公司的所在地，以及该特定个人可能为公司带来的潜在价值。

任何薪酬数据都来之不易。
公司通常从[供应商](https://www.advanced-hr.com/products-overview)那里购买这些数据，但候选人通常无法获得。

对于初创公司，更容易获得各种数据。
我们在此提供一些关于早期硅谷科技初创公司的概述；
许多这些数字并不代表全国不同类型公司的普遍情况：

-   🔹 判断特定公司和候选人的合理报价的最佳方法之一是查看 [AngelList](https://angel.co/) 上具有相似背景的公司的报价。
    [**AngelList 薪酬数据**](https://angel.co/salaries) 非常广泛。
-   没有硬性规定，但对于**A 轮融资后的初创公司**在**硅谷**，下表基于 [Babak Nivi 的表格](http://venturehacks.com/articles/option-pool-shuffle#market)，给出了许多人认为合理的 ballpark（大致）股权水平。
    这些通常适用于限制性股票或具有标准 4 年归属时间表的股票期权。
    它们适用于这些职位在 A 轮融资后不久被填补，并且新员工也获得薪水（因此不是创始人或在 A 轮融资前雇用的员工）的情况。
    较高范围适用于具有强大业绩记录的备受追捧的候选人。
    -   首席执行官 (CEO): **5–10%**
    -   首席运营官 (COO): **2–5%**
    -   副总裁 (VP): **1–2%**
    -   独立董事会成员: **1%**
    -   总监 (Director): **0.4–1.25%**
    -   首席工程师 (Lead engineer): **0.5–1%**
    -   高级工程师 (Senior engineer): **0.33–0.66%**
    -   经理或初级工程师 (Manager or junior engineer): **0.2–0.33%**
-   对于**B 轮融资后的初创公司**，股权数字会低得多。
    低多少将显著取决于团队规模和公司估值。
-   种子轮融资的初创公司会提供更高的股权——如果资金很少，有时会高得多，但基本工资会更低。
-   Leo Polovets 创建了一项关于 2014 年 AngelList 职位发布的[调查](http://codingvc.com/analyzing-angellist-job-postings-part-2-salary-and-equity-benchmarks)，
    这是对这些早期初创公司前几十名员工股权水平的极好总结。
    对于硅谷的**工程师**，最高（非典型！）
    股权水平为：
    -   第 1 位雇员：高达 **2%–3%**
    -   第 2 至 5 位雇员：高达 **1%–2%**
    -   第 6 和 7 位雇员：高达 **0.5%–1%**
    -   第 8 至 14 位雇员：高达 **0.4%–0.8%**
    -   第 15 至 19 位雇员：高达 **0.3%–0.7%**
    -   第 21 [原文如此] 至 27 位雇员：高达 **0.25%–0.6%**
    -   第 28 至 34 位雇员：高达 **0.25%–0.5%**
-   José Ancer 为早期招聘提供了另一个很好的[概述](http://siliconhillslawyer.com/2018/05/08/early-startup-employee-compensation/)。
-   *创始人*薪酬是另一个完全不同的话题，但可能仍会引起员工的兴趣。José Ancer 提供了一个周到的[概述](http://siliconhillslawyer.com/2016/06/23/founder-compensation-cash-equity-liquidity/)。

### 谈判技巧

🚧 结构：将谈判要点移到前面？

在谈判工作邀约时，公司总是会问您期望的薪酬，而您应该始终[谨慎](http://review.chicagobooth.edu/strategy/2018/article/how-answer-one-toughest-interview-questions)回答。

如果您说出您能接受的最低数字，您可以相当确定公司不会超过它，至少不会超过很多。

🔸 询问薪资期望是大多数公司招聘过程中的正常部分，但询问**薪资历史**已在越来越多的州、市和县被禁止。[^hrdivecomn.56fguz]
这些法律试图通过禁止公司在向候选人发出录用邀约时询问或考虑其当前或过去的薪酬，来消除女性和少数族裔之间的薪酬差距。[^nytimescom.yev52k]
确保您了解与您情况相关的法律。

关于谈判薪酬的几点建议：

-   一些人认为，谈判中的一个[好策略](http://www.businessinsider.com/how-to-negotiate-make-first-offer-2014-5)是开始时提出高于您愿意接受的数字，这样对方可以通过将您的要求向下谈判一点来“获胜”。
    请记住，这只是一个建议的策略，不是硬性规定。
-   如果您缺乏经验并且不确定公平的报价应该是什么样子，请避免在讨论初期就确切说明您想要的薪酬。
    尽管许多招聘经理和招聘人员在流程早期询问[薪资期望](http://fistfuloftalent.com/2018/01/ask-salary-without-asking-salary-expectations.html)以避免在报价阶段出现风险，但有些人这样做是为了利用那些不太了解[自身价值](https://nuleadership.com/2018/01/08/know-your-worth-compensation-negotiation/)的候选人。
    告诉他们您想在讨论数字之前专注于整个机会以及您的贡献能力。
    请他们在了解您能为公司带来什么之后给您一个公平的报价。
-   如果您经验丰富并且了解自己的价值，通常表明您正在寻找什么样的薪酬和职位以锚定预期符合您的利益。
    您甚至可以在流程早期分享您的期望，以免浪费彼此的时间。
-   讨论您未来的薪酬可能会是什么样子。
    没有人能向您保证未来的股权、薪水或奖金，但*如果*您表现出色并且公司有资金，应该可以就这些可能的样子达成一致。
-   如果您从成熟公司转到初创公司，您可能会被要求接受[降薪](https://www.quora.com/Should-you-take-a-salary-cut-if-you-join-a-startup)。这是合理的，但明智的做法是明确讨论降薪幅度以及何时会重新谈判您的薪水。
    例如，您可以接受比以前薪水低 25% 的水平，但可以达成协议，如果您的表现强劲并且公司获得资金，这将得到纠正。
-   🔹 在同意录用邀约之前，务必谈判[非薪酬](http://www.kennedyexecutive.com/blog/salary-negotiation-33-things-negotiate-money/)方面。
    如果您想要特定的职位、头衔、机会、签证担保、育儿假、特殊待遇（如在家工作），或者有关于何时可以入职的时间限制，请[尽早谈判这些](https://www.nerdwallet.com/blog/loans/student-loans/negotiate-nonsalary-benefits-job-perks/)，而不是在流程后期。
-   🔹 如果您将成为非常早期的员工，考虑要求获得限制性股票授予而不是股票期权，以及等于这些期权税款的现金奖金。
    公司会有一些额外的文书工作（和法律成本），但这意味着您不必支付行权费用。
    然后，如果您提交 83(b) 选择权，您将进一步简化您的情况，消除 ISO 的 [AMT 问题](#the-amt-trap)，并最大化您获得长期资本利得税资格的机会。
-   🚧 还有哪些*具体*建议是有帮助的？

关于谈判过程本身的一些说明：

-   🔹 尽管录用通知书有截止日期，但如果您需要更多时间，通常可以协商。灵活性有多大取决于具体情况。
    有些人批评“限时爆炸性工作邀约 (exploding job offers)”是一种[不良做法](https://www.huffingtonpost.com/adam-grant/its-time-to-eliminate-exp_b_4594222.html)，
    完全[没有意义](https://erikbern.com/2016/03/16/exploding-offers-are-bullshit.html)。如果您很可能是该职位的最佳候选人，或者该职位是专业性强且薪酬高的职位，通常没有足够的优秀候选人来满足需求，那么您很可能有足够的筹码来[要求更多时间](http://www.businessinsider.com/how-to-politely-postpone-accepting-a-job-offer-2015-6#dont-be-afraid-to-negotiate-4)，
    这可能是完成与其他公司的面试过程所必需的。
    科技公司的软件工程职位目前就是这种情况。
-   获得[多个录用邀约](https://www.themuse.com/advice/a-guide-to-juggling-multiple-job-offers-and-coming-out-on-top)
    始终符合您的利益。
    如果您有竞争性录用邀约，与您想去的公司分享这些竞争性录用邀约可能会有所帮助，前提是您的录用邀约具有竞争力。
    -   然而，过度拖延谈判以便您可以将一个录用邀约“货比三家”给其他公司，被一些人认为是不好的行为；
        在可能的情况下，审慎和及时是体贴的做法。
-   ❗️ 如果协议内容未包含在您的录用通知书中，请务必将所有协议以书面形式记录下来。
-   除非您准备信守诺言，否则不要口头或书面接受录用邀约。
    在实践中，人们确实偶尔会接受录用邀约然后反悔，或者[*毁约 (renege)*](https://purduecco.wordpress.com/2016/03/28/the-risks-of-reneging-on-a-job-offer/)。
    这可能会使公司陷入困境（他们可能基于您的接受而拒绝了另一位关键候选人），并且可能在以后以意想不到的方式损害您的声誉。

一些额外的资源：

-   《哈佛商业评论》有各种关于谈判过程的一般[💰建议](https://hbr.org/2014/04/15-rules-for-negotiating-a-job-offer)。
-   Wistia 的副总裁 Robby Grossman 对初创公司的股权激励和谈判建议给出了很好的[概述](http://rob.by/2013/negotiating-your-startup-job-offer)。

### 录用邀约和谈判风险

为了结束我们对录用邀约和谈判的讨论，以下是一些需要注意的关键风险和错误：

-   ❗️ 不要接受股票或股份的录用邀约，而不要求确切的总股份数（或者等效地，这些股份代表的公司确切百分比）。一些公司提供股票或期权的录用邀约，却只告诉您股份数量，这是相当普遍的。
    没有百分比，股份数量毫无意义。
    不告诉您是一种极不公平的做法。
    即使在您准备签署录用邀约时也拒绝告知您的公司，很可能给您提供了一个非常糟糕的交易。
-   🔸 如果您正在考虑一份录用邀约，请在接受之前计算出您是否可以以及是否应该提前行权，以及行权成本和税费将是多少。
-   ❗️ 如果您在一家初创公司刚完成新一轮融资时加入，并且没有机会立即行权，他们可能会以低行权价向您发行期权，但股票的 409A 估值已经上升。
    这意味着您将无法在不产生巨额税单的情况下提前行权。
    事实上，您可能根本无法在财务上承担行权的费用。
-   ❗️ 归属从归属起始日开始计算。
    有时，股票期权文件在您加入公司数周或数月后才会送达您手中，因为它需要由律师起草并经董事会批准。在您的谈判中，务必确保归属起始日反映的是您加入公司的真实开始日期，而不是股票期权的授予时间。
-   🔸 录用通知书并非您股权的实际授予文件。
    签署录用通知书后，请确保公司在几周内向您交付实际的股权授予文件。
    早期初创公司在股权授予方面草率行事并非罕见。
    如果他们拖延太久才发送您的授予文件，那么在您等待期间，股权的公允市场价值（和行权价）可能会上涨，这对您来说就是金钱损失。
-   🔸 如果您打算提前行权，请像对待任何投资一样对待它。
    不要相信您听到的关于公司价值的所有预测。
    创始人会告诉您最好的情况。
    请记住，大多数初创公司都会失败。
    做好您的研究，并询问他人对公司可能结果的意见。
-   ❗️ 虽然可能不常见，但一些公司保留回购（买回）已归属股份的权利。简单地问一句“公司对*已归属*股份是否有任何回购权？”就足够了。（注意，回购通过提前行权购买的*未归属*股份是不同的，这对您有利。）
    如果您不想问，公允市场价值回购权应包含在要求您签署或确认您已阅读并理解的文件中。
    （Skype 关于回购的[争议](https://techcrunch.com/2011/06/26/skypes-worthless-employee-stock-option-plan-heres-why-they-did-it/)
    让一些初创公司员工[警惕](https://www.quora.com/Which-valley-startups-have-a-Skype-like-repurchase-right)
    具有类似计划的公司。）
    您可能会在股票计划本身、股票期权协议、行权协议、公司章程、公司注册证书或任何其他股东协议中找到已归属股份的回购权。

## 文件与协议

本节涵盖了您在谈判工作邀约和入职公司时可能看到的几种文件类型。
由于标题和细节各不相同，本节并非详尽无遗。

-   当您考虑录用邀约时，请确保您已从公司获得所有需要的文件：
    -   您的 [📥录用通知书 (offer letter)](https://www.upcounsel.com/employee-offer-letter)，其中将详细说明薪水、福利和股权激励。
    -   一份[📥员工创新协议 (Employee Innovations Agreement)](https://recruit.smashfly.com/SmashFlyMedia/Docs/12250/12250_168_United%20States%20-%20EIPIA%20English%20%28Rev%2014%20FEBRUARY%202017%29%202%20pages.pdf)、
        专有信息和发明转让协议 (Proprietary Information and Inventions Assignment Agreement) 或类似文件，涉及知识产权。
-   如果您有股权激励，在某个时候——可能在您加入后数周或数月——您应该收到一份股票授予摘要 (Summary of Stock Grant)、股票期权授予通知 (Notice of Stock Option Grant) 或类似文件，详细说明您的股票或期权授予情况，包括所有细节，如股份数量、期权类型、授予日期、归属起始日期和归属时间表。
    它将附带其他几份文件，这些文件可能是该协议的附件：
    -   [📥股票期权协议 (Stock Option Agreement)](https://www.upcounsel.com/stock-option-agreement)
    -   [📥股票计划 (Stock Plan)](https://www.upcounsel.com/equity-incentive-plan)（有时称为股票期权计划 Stock Option Plan、股票奖励计划 Stock Award Plan 或股权激励计划 Equity Incentive Plan）
    -   [📥法典第 409A 条弃权和豁免 (Code Section 409A Waiver and Release)](https://www.lawinsider.com/clause/code-section-409a-waiver-and-release)
        （有时是股票期权协议的一部分）
-   如果您正在行使期权，您还应该看到协助该购买的文件：
    -   [📥行权协议 (Exercise Agreement)](https://www.upcounsel.com/option-exercise-agreement)
    -   提前行权和 [📥83(b) 选择权](https://www.irs.gov/pub/irs-drop/rp-12-29.pdf) 的说明和模板（如果适用）
-   年终税务文件

    -   如果您在年内行使了 ISO 期权，您应该从公司收到一份表格 [📥3921 或 3922](https://www.irs.gov/uac/form-3921-exercise-of-an-incentive-stock-option-under-section-422-b)。

## 进一步阅读

此处的资源只是《股权激励指南》中引用的全部资源的一小部分，选择标准是其广度、知名度或在特定问题上的深度。

### 一般资源

-   Mark P. Cussen, Investopedia,
    [*激励性股票期权简介*](http://www.investopedia.com/articles/stocks/12/introduction-incentive-stock-options.asp)，
    2017 年更新。
-   Alex MacCaw,
    [*工程师股票期权指南*](http://blog.alexmaccaw.com/an-engineers-guide-to-stock-options)，
    2013 年。
-   Andy Rachleff, Wealthfront,
    [*关于股票期权的 14 个关键问题*](https://blog.wealthfront.com/stock-options-14-crucial-questions)，
    2014 年。
-   Mary Russell, Stock Option Counsel,
    [*初创公司股权标准：员工指南*](http://www.slideshare.net/StockOptionCnsl/startup-standards-stock-option-counsel)，
    2014 年。
-   David Weekly,
    [ 💰*面向科技企业家或初创公司员工的股票与期权简介*](https://www.scribd.com/doc/55945011/An-Introduction-to-Stock-Options-for-the-Tech-Entrepreneur-or-Startup-Employee#scribd)，
    2012 年。
-   Investopedia,
    [*员工股票期权：定义与关键概念*](http://www.investopedia.com/university/employee-stock-options-eso/eso1.asp)。

### 创始人注意事项

-   Matthew Bartus, Cooley GO,
    [*期权授予：完全稀释还是已发行且在外流通*](https://www.cooleygo.com/option-grants-fully-diluted-issued-outstanding/)。
-   Jay Bhatti, Business Insider,
    [*初创公司应如何处理员工的悬崖期归属*](http://www.businessinsider.com/everything-you-need-to-know-about-cliff-vesting-2011-5)，
    2011 年。
-   Tahir J. Naim, Fenwick,
    [*针对初创科技和生命科学公司的 409A 估值和股票期权授予*](http://www.fenwick.com/FenwickDocuments/409_Valuations_Stock_Options.pdf)。
-   Babak Nivi, Venture Hacks
    [*期权池调整*](http://venturehacks.com/articles/option-pool-shuffle)（以及[股权范围表](http://venturehacks.com/articles/option-pool-shuffle#market)），2017 年。
-   Leo Polovets,
    [*分析 AngelList 职位发布，第 2 部分：薪酬和股权基准*](http://codingvc.com/analyzing-angellist-job-postings-part-2-salary-and-equity-benchmarks)，
    2014 年。
-   Beth Scheer, Homebrew, [初创公司薪酬](https://quip.com/HEB3Ah9dYD6o)。
-   Scott Edward Walker, VentureBeat,
    [*警惕清算优先权的陷阱*](http://venturebeat.com/2010/08/16/beware-the-trappings-of-liquidation-preference/)，
    2010 年。
-   Joe Wallin, The Startup Law Blog,[*授予 NQO 而非 ISO 的六大理由*](http://www.startuplawblog.com/2010/08/11/top-reasons-nqos-over-isos/)，
    2010 年。
-   Clerky, [*创始人法律概念*](https://handbook.clerky.com/)。

### 候选人和员工注意事项

-   匿名，
    [*在加入独角兽公司前我希望了解的关于股权的事情*](https://gist.github.com/yossorion/4965df74fd6da6cdc280ec57e83a202d)，
    2017 年。
-   Atish Davda, Inc,
    [*在接受初创公司工作邀约前应问的 5 个问题*](http://www.inc.com/atish-davda/5-questions-you-should-ask-before-taking-a-start-up-job-offer.html)，
    2014 年。
-   Julia Evans,
    [*在谈判录用邀约前您应了解的关于股票期权的事情*](http://jvns.ca/blog/2015/12/30/do-the-math-on-your-stock-options/)，
    2015 年。
-   Guy Kawasaki, [*向初创公司提出的九个问题*](http://guykawasaki.com/nine_questions_/)，
    2006 年。
-   Sheelah Kolhatkar, The New Yorker,
    [*科技行业的性别歧视问题*](https://www.newyorker.com/magazine/2017/11/20/the-tech-industrys-gender-discrimination-problem)，
    2017 年。
-   Eileen Patten, Pew Research Center,
    [*尽管有所进展，美国种族、性别工资差距依然存在*](http://www.pewresearch.org/fact-tank/2016/07/01/racial-gender-wage-gaps-persist-in-u-s-despite-some-progress/)，
    2016 年。
-   Leo Polovets, [*评估员工期权价值*](http://codingvc.com/valuing-employee-options/)，
    2015 年。
-   Andy Rachleff, Wealthfront,
    [*您应该何时行使您的股票期权？*](https://blog.wealthfront.com/when-to-exercise-stock-options/)，
    2015 年。
-   David Weekly, GigaOm,
    [*关于股票期权您不能犯的 5 个错误*](https://gigaom.com/2011/06/05/5-mistakes-you-cant-afford-to-make-with-stock-options/)，
    2011 年。

### 股权激励类型

-   Jeron Paul, Capshare,
    [*RSU 与期权：为什么 RSU（限制性股票单位）可能比您私营公司的股票期权更好*](https://www.capshare.com/blog/rsus-vs-options/)，
    2016 年。
-   Andy Rachleff, Wealthfront,
    [*股票期权和 RSU 有何不同？*](https://blog.wealthfront.com/stock-options-versus-rsu/)，
    2014 年。
-   Mary Russell, Stock Option Counsel,
    [*初创公司股票期权的提前到期 - 第 3 部分 - 按公司阶段划分的良好股权设计示例*](http://stockoptioncounsel.com/blog/early-expiration-of-startup-stock-options-part-3-examples-of-good-startup-equity-design-by-company-stage/2017/8/11)，
    2017 年。
-   Joe Wallin, The Startup Law Blog,
    [*激励性股票期权 vs. 非合格股票期权*](http://www.startuplawblog.com/2013/05/15/incentive-stock-options-vs-nonqualified-stock-options/)，
    2013 年。
-   Joe Wallin,
    [*RSU vs. 限制性股票 vs. 股票期权*](http://joewallin.com/2014/09/13/rsus-vs-restricted-stock-vs-stock-options/)，
    2014 年。

### 税务

-   Steven Ayre, Accelerated Vesting,
    [*什么是 83(b) 选择权以及我何时进行选择？*](http://acceleratedvesting.com/what-is-an-83b-election-and-when-do-i-make-it-part-1-with-graphic/)，
    2013 年。
-   Mark P. Cussen, Investopedia,
    [*限制性股票和 RSU 如何征税*](http://www.investopedia.com/articles/tax/09/restricted-stock-tax.asp?performancelayout=true)。
-   Barry Kramer,
    [🔑*（无意中）重创硅谷员工的税法*](https://medium.com/@barryjk/the-tax-law-that-is-unintentionally-hammering-silicon-valley-employees-894a7b54ba8a)，
    2015 年。
-   Joshua Levy and Joe Wallin, The Startup Law Blog,
    [*可立即行权的 ISO 的问题*](http://thestartuplawblog.com/the-problem-with-immediately-exercisable-isos/)，
    2015 年。
-   Kaye A. Thomas, Fairmark,
    [*AMT 和长期资本利得*](http://fairmark.com/general-taxation/alternative-minimum-tax/amt-long-term-capital-gain/)，
    2014 年。
-   Robert W. Wood, Forbes,
    [*股票期权的十个税务技巧*](http://www.forbes.com/2010/03/10/10-tax-tips-stock-options-personal-finance-robert-wood.html)，
    2010 年。
-   NCEO,
    [*股票期权与替代性最低税 (AMT)*](https://www.nceo.org/articles/stock-options-alternative-minimum-tax-amt)

### 股票期权的归属和到期

-   Babak Nivi, Venture Hacks,
    [*如何制作资本结构表*](http://venturehacks.com/articles/cap-table)，2007 年。
-   Mary Russell, Stock Option Counsel,
    [*公司能收回我已归属的股份吗？*](http://stockoptioncounsel.com/blog/standards-ownership-canthecomanytakebackmyvestedshares)，
    2017 年。
-   Mary Russell, Stock Option Counsel,
    [*初创公司股票期权的提前到期 - 第 1 部分 - 一个价值 100 万美元的问题*](http://stockoptioncounsel.com/blog/nc7go8ivzxb1el5rhv6nltrjan0n2t/2017/3/6)，
    2017 年。
-   Mary Russell, Stock Option Counsel,
    [*初创公司股票期权的提前到期 - 第 2 部分 - 完整的 10 年期限解决方案*](http://stockoptioncounsel.com/blog/early-expiration-of-startup-stock-options-part-2-the-full-10-year-term-solution/2017/3/28)，
    2017 年。
-   Dan Shapiro, [*归属是一种权宜之计 (Vesting is a hack)*](http://www.danshapiro.com/blog/2012/04/vesting-is-a-hack/)，
    2012 年。

### 谈判

-   Robby Grossman,
    [*谈判您的初创公司工作邀约*](http://rob.by/2013/negotiating-your-startup-job-offer)，
    2013 年。
-   Sheelah Kolhatkar, The New Yorker,
    [*精益求精之外：谈判对女性的风险*](https://www.newyorker.com/magazine/2017/11/20/the-tech-industrys-gender-discrimination-problem)，
    2017 年。
-   Deepak Malhotra, Harvard Business Review,
    [谈判工作邀约的 15 条规则](https://hbr.org/2014/04/15-rules-for-negotiating-a-job-offer)，
    2014 年。
-   [CEFNE（商业谈判研究与培训中心）](http://cefne.com/en/harvard-method-negotiation)

### 表格和工具

-   [🔨TLDR 股票期权](https://tldroptions.io/) 和 [OwnYourVenture](http://ownyourventure.com/)
    是演示股权计算和稀释的模拟器
-   Orrick,
    [📥初创公司表格：股权激励](https://www.orrick.com/Total-Access/Tool-Kit/Start-Up-Forms/Equity-Compensation)

## 免责声明

*本指南及所有相关评论和讨论在任何方面均不构成法律或税务建议。
任何读者都不应在未寻求相关司法管辖区法律顾问建议的情况下，基于本文提供的任何信息采取行动或不采取行动。
作者明确声明，对于基于本指南或相关内容的任何内容而采取或未采取的任何行动，不承担任何责任。*

## 致谢

非常感谢本指南的所有[贡献者](https://github.com/jlevy/og-equity-compensation/graphs/contributors)以及那些提供详细反馈的人，包括
[Julia Evans](https://twitter.com/b0rk)、[George Grellas](https://twitter.com/grellas)、
[Chris McCann](https://twitter.com/mccannatron)、[Leo Polovets](https://twitter.com/lpolovets)、
[Srinath Sridhar](https://www.linkedin.com/in/srinath-sridhar-0a16705)、
[Andy Sparks](https://twitter.com/SparksZilla) 和 [David Weekly](https://twitter.com/dweekly)，
以及 [Hacker News 上的众多评论者](https://news.ycombinator.com/item?id=10880726)。
原作者是 [Joshua Levy](https://twitter.com/ojoshe) 和
[Joe Wallin](https://twitter.com/joewallin)。

### 请提供帮助！

本指南是一份持续更新的出版物，虽不完美但持续改进。
如果您有任何想法或贡献可能改进本指南，请在页边空白处添加建议。
我们欣然感谢所有贡献者。

## 许可协议

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

本作品采用[知识共享署名-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-sa/4.0/)进行许可。

[^corpgovlaw.6vw7qt]: <https://corpgov.law.harvard.edu/2014/10/02/what-has-happened-to-stock-options/>

[^nceoorgass.x6588n]: <https://www.nceo.org/assets/pdf/articles/GSS-2014-data.pdf>

[^ftcomconte.x613np]: <https://www.ft.com/content/d6599ae0-5738-11e1-869b-00144feabdc0>

[^treasurygo.tbpcyx]: <https://www.treasury.gov/resource-center/tax-policy/tax-analysis/Documents/Firms-Exceeding-162m.pdf>

[^epiorgpubl.cq5o0o]: <https://www.epi.org/publication/taxes-executive-compensation/>

[^nberorgpap.wtsymr]: <http://www.nber.org/papers/w16585.pdf>

[^investoped.aaps6n]: <https://www.investopedia.com/articles/markets/120215/if-you-had-invested-right-after-starbucks-ipo.asp>

[^moneycnnco.80o8bh]: <https://money.cnn.com/1999/11/10/companies/ups/>

[^techcrunch.9ucopn]: <https://techcrunch.com/2017/06/28/a-look-back-at-amazons-1997-ipo/>

[^dealbookny.es6h1j]: <https://dealbook.nytimes.com/2009/08/19/googles-ipo-5-years-later/>

[^enwikipedi.q7bc95]: <https://en.wikipedia.org/wiki/Initial_public_offering_of_Facebook>

[^investoped.m9wdqp]: <https://www.investopedia.com/terms/c/c-corporation.asp>

[^quoracomwh.wsnr2b]: <https://www.quora.com/Why-do-most-technology-startups-incorporate-in-Delaware>

[^nytimescom.67ksyb]: <https://www.nytimes.com/2012/07/01/business/how-delaware-thrives-as-a-corporate-tax-haven.html>

[^investoped.fn52lq]: <http://www.investopedia.com/articles/analyst/03/111903.asp>

[^nytimescom.gec7iw]: <https://www.nytimes.com/2018/09/30/business/women-corporate-boards-california.html>

[^dlapiperac.wb4617]: <https://www.dlapiperaccelerate.com/knowledge/2017/board-action-meetings-vs-written-consents.html>

[^corpgovlaw.vbw82s]: <https://corpgov.law.harvard.edu/2017/05/25/2017-ipo-report/>

[^reactionwh.uw835n]: <http://reactionwheel.net/2018/05/zipcar-fundraising-breakdown.html>

[^nytimescom.bcfuyu]: <https://www.nytimes.com/2016/08/22/business/economy/bay-area-start-ups-find-low-cost-outposts-in-arizona.html>

[^chicagotri.fq0msp]: <http://www.chicagotribune.com/bluesky/technology/ct-silicon-valley-midwest-startups-20150925-story.html>

[^codingvcco.bcspni]: <http://codingvc.com/valuing-employee-options/>

[^cooleygoco.p5v68j]: <https://www.cooleygo.com/what-is-a-cap-table/>

[^lsvpwordpr.dgym96]: <https://lsvp.wordpress.com/2008/09/15/what-entrepreneurs-need-to-know-about-founders-stock/>

[^avccom2010.zxzhsl]: <https://avc.com/2010/10/employee-equity-the-liquidation-overhang/>

[^inccombusi.oldydy]: <https://www.inc.com/business-insider/tanium-security-startup-orion-hindawi-fired-employees-before-stocks-vested.html>

[^bloombergc.a48epn]: <https://www.bloomberg.com/news/articles/2017-09-19/tesla-worker-says-timing-of-firing-denied-him-lucrative-shares>

[^amplitudec.fvea8b]: <https://amplitude.com/blog/2015/12/01/employee-equity-is-broken-heres-our-fix/>

[^githubcomc.ygtolb]: <https://github.com/clef/handbook/blob/master/Hiring%20Documents/Guide%20to%20Your%20Equity.md>

[^mediumcomb.nqs9mo]: <https://medium.com/@barmstrong/improving-equity-compensation-at-coinbase-8749979409c3>

[^fortunecom.nnfd6o]: <http://fortune.com/2015/03/23/pinterest-employee-taxes/>

[^quoracomwh.4dxi02]: <https://www.quora.com/Why-do-most-startups-force-employees-to-exercise-their-vested-ISO-options-within-90-days-if-they-leave-rather-than-the-option-to-convert-to-NSOs>

[^thestartup.tn6iyt]: <http://thestartuplawblog.com/rsus-the-tax-problems/>

[^slatecomar.qqwwen]: <http://www.slate.com/articles/news_and_politics/politics/2014/04/how_long_is_the_tax_code_it_is_far_shorter_than_70_000_pages.html>

[^gpogovfdsy.clz3vr]: <https://www.gpo.gov/fdsys/pkg/USCODE-2016-title26/content-detail.html>

[^taxpolicyc.sjye20]: <https://www.taxpolicycenter.org/briefing-book/how-are-capital-gains-taxed>

[^taxpolicyc.mgorf1]: <https://www.taxpolicycenter.org/briefing-book/what-amt>

[^todayyougo.tyjmz8]: <https://today.yougov.com/news/2013/01/08/understanding-how-marginal-taxes-work-its-all-part/>

[^taxpolicyc.w7dds7]: <https://www.taxpolicycenter.org/briefing-book/what-tax-changes-did-affordable-care-act-make>

[^investoped.s08hcp]: <https://www.investopedia.com/articles/personal-finance/020714/new-taxes-under-affordable-care-act.asp>

[^foolcomtax.ox10ej]: <https://www.fool.com/taxes/2017/12/11/long-term-capital-gains-tax-rates-in-2018.aspx>

[^foolcomtax.3ka4p1]: <https://www.fool.com/taxes/2018/02/05/how-the-alternative-minimum-tax-is-changing-in-201.aspx>

[^blogwealth.3vcf24]: <https://blog.wealthfront.com/qualified-small-business-stock-2016/>

[^foolcomper.bw6uel]: <http://www.fool.com/personal-finance/taxes/2014/10/04/the-states-with-the-highest-capital-gains-tax-rate.aspx>

[^thestartup.25gj0l]: <http://thestartuplawblog.com/the-problem-with-immediately-exercisable-isos/>

[^mediumcomb.57vdab]: <https://medium.com/@barryjk/the-tax-law-that-is-unintentionally-hammering-silicon-valley-employees-894a7b54ba8a>

[^stockoptio.z54l1t]: <http://stockoptioncounsel.com/blog/early-expiration-of-startup-stock-options-part-3-examples-of-good-startup-equity-design-by-company-stage/2017/8/11>

[^joewallinc.8eaojr]: <http://joewallin.com/2014/09/13/rsus-vs-restricted-stock-vs-stock-options/>

[^schwabcomp.94cuxl]: <https://www.schwab.com/public/eac/resources/articles/rsu_basics.html>

[^wsjcomarti.vm6qmp]: <https://www.wsj.com/articles/former-employee-wins-legal-feud-to-open-up-startups-books-1485435602>

[^techcrunch.qn7usd]: <https://techcrunch.com/2015/10/14/selling-private-company-shares-2-0/>

[^industryve.6prupc]: <http://www.industryventures.com/2014/12/02/employee-liquidity-good-for-private-companies/>

[^mediumcomr.ez02hw]: <https://medium.com/@rizstanford/secondary-sales-in-vc-backed-startups-a-quick-primer-for-entrepreneurs-bdc25ea7f39a>

[^digitalcom.k5w0oc]: <https://digitalcommons.ilr.cornell.edu/cgi/viewcontent.cgi?article=2208&context=articles>

[^pewresearc.dws8o8]: <http://www.pewresearch.org/fact-tank/2016/07/01/racial-gender-wage-gaps-persist-in-u-s-despite-some-progress/>

[^iwprorgpub.1ukyxt]: <https://iwpr.org/publications/gender-wage-gap-2017-race-ethnicity/>

[^aflcioorgp.6v6p19]: <https://aflcio.org/paywatch/company-pay-ratios>

[^fortunecom.87hw00]: <http://fortune.com/2017/06/09/white-men-senior-executives-fortune-500-companies-diversity-data/>

[^eeocgoveeo.9aynwh]: <https://www.eeoc.gov/eeoc/statistics/reports/hightech/>

[^newyorkerc.mdcz9c]: <https://www.newyorker.com/science/maria-konnikova/lean-out-the-dangers-for-women-who-negotiate>

[^shrmorgres.qv3vrf]: <https://www.shrm.org/resourcesandtools/hr-topics/employee-relations/pages/using-a-job-offer-as-leverage-is-no-longer-a-big-no-no.aspx>

[^siliconhil.1wd4aa]: <http://siliconhillslawyer.com/2016/06/23/founder-compensation-cash-equity-liquidity/>

[^hrdivecomn.56fguz]: <https://www.hrdive.com/news/salary-history-ban-states-list/516662/>

[^nytimescom.yev52k]: <https://www.nytimes.com/2018/02/16/business/economy/salary-history-laws.html>