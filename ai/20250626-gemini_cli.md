# [Gemini CLI：你的开源 AI 智能体](20250626-gemini_cli.mp3)

> - **作者**: Taylor Mullen, Ryan J. Salva
> - **原文**: https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/

> **译者注**: 谷歌此次推出的 Gemini CLI，意图非常明确：将强大的 Gemini 1.5 Pro 模型及其百万级上下文窗口直接注入开发者的核心工作区——终端。其提供的“业界最慷慨”免费额度，不仅是对 GitHub Copilot CLI 等竞品的直接“降维打击”，更是其构建完整 AI 驱动开发生态的关键一步。工具的开源特性，也为社区的信任和共同发展铺平了道路，值得每一位开发者关注和尝试。

Gemini CLI 是一款免费且开源的工具，它将 Gemini 的强大能力直接带入开发者的终端——并为个人用户提供了前所未有的使用额度。

> **Gemini CLI：即刻升级你的终端体验。** [立即试用](https://github.com/google-gemini/gemini-cli)

对开发者而言，命令行界面（CLI）不仅仅是一个工具，更是他们的主场。终端的高效、普及和便携性，使其成为完成工作的首选利器。随着开发者对终端的依赖与日俱增，对集成式 AI 助手的需求也愈发强烈。

正因如此，我们推出了 [Gemini CLI](http://github.com/google-gemini/gemini-cli)，一个开源的 AI 智能体（agent），它将 Gemini 的力量直接带到你的终端。它提供了访问 Gemini 的轻量级途径，为你打通了从提示词到我们模型的最直接路径。虽然它在编码方面表现出色，但我们构建 Gemini CLI 的初衷远不止于此。它是一个功能丰富的本地实用工具，可用于广泛的任务，从内容生成、问题解决到深度研究和任务管理。

我们还将 Gemini CLI 与谷歌的 AI 编码助手 [Gemini Code Assist](https://codeassist.google/) 进行了集成。这样一来，所有开发者——无论是免费版、标准版还是企业版的 Code Assist 用户——都可以在 VS Code 和 Gemini CLI 中享受到由提示词驱动、AI 优先的编码体验。

![开发者、构建者和创造者可以通过 Gemini CLI 将 Gemini 1.5 Pro 的强大能力直接引入他们的终端](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Gemini_CLI_GIF.gif)

## 为个人开发者提供无与伦比的使用额度

要免费使用 Gemini CLI，只需用你的个人 Google 账户登录，即可获得免费的 Gemini Code Assist 许可证。该免费许可证让你能够使用 Gemini 1.5 Pro 及其庞大的 100 万 token 上下文窗口。为了确保你在此预览期间几乎不会遇到限制，我们提供了业界最为慷慨的免费额度：**每分钟 60 次模型请求，每天 1,000 次请求，完全免费**。

如果你是需要同时运行多个智能体的专业开发者，或者倾向于使用特定模型，你可以使用 [Google AI Studio](https://aistudio.google.com/apikey) 或 [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal) 的密钥进行按量计费，或者获取 Gemini Code Assist 标准版或企业版许可证。

> Gemini CLI 提供了业界最为慷慨的免费使用额度，每分钟 60 次模型请求，每天 1,000 次模型请求，完全免费。

![Gemini CLI 信息图，解释其免费使用额度为每分钟60次模型请求和每天1000次模型请求](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_CLI_infographic.width-1000.format-webp.webp)

## 命令行中的强大模型

目前处于预览阶段的 Gemini CLI 提供了强大的 AI 功能，从代码理解、文件操作到命令执行和动态故障排查。它为你的命令行体验带来了根本性的升级，使你能够用自然语言编写代码、调试问题并简化工作流程。

其强大能力源于内置的工具，让你能够：

*   **通过谷歌搜索为提示词提供事实依据**，从而抓取网页内容，为模型提供实时的外部上下文。
*   通过内置的**模型上下文协议（Model Context Protocol, MCP）**支持或捆绑的扩展来**扩展 Gemini CLI 的能力**。
*   **自定义提示词和指令**，为你特定的需求和工作流程量身定制 Gemini。
*   在你的脚本中以非交互方式调用 Gemini CLI，以**实现任务自动化并与现有工作流集成**。

![Gemini CLI 可用于多种任务，例如使用 Veo 和 Imagen 制作一个展示一只橘猫在澳大利亚探险故事的短视频](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GenMedia_demo_keyword.mp4)

## 开放且可扩展

由于 Gemini CLI 是完全[开源的（遵循 Apache 2.0 许可证）](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE)，开发者可以审查代码以了解其工作原理并验证其安全性。我们完全期待（并欢迎！）全球开发者社区通过报告错误、建议功能、持续改进安全实践和提交代码改进来[为这个项目做出贡献](https://github.com/google-gemini/gemini-cli/blob/main/CONTRIBUTING.md)。你可以在我们的 GitHub 仓库中[提交问题 (issues)](http://github.com/google-gemini/gemini-cli/issues) 或 [分享你的想法 (discussions)](http://github.com/google-gemini/gemini-cli/discussions)。

我们还将 Gemini CLI 设计为可扩展的，它建立在新兴标准之上，如 MCP、系统提示（通过 `GEMINI.md` 文件）以及支持个人和团队配置的设置。我们深知终端是一个私人空间，每个人都应该有权让自己的终端独一无二。

## 与 Gemini Code Assist 共享技术

有时，IDE 才是完成工作的最佳工具。当那一刻来临时，你希望有一个强大的 AI 智能体伴随左右，帮助你快速迭代、学习和克服问题。

[Gemini Code Assist](https://codeassist.google/)——谷歌为学生、业余爱好者和专业开发者打造的 AI 编码助手——现在与 Gemini CLI 共享相同的技术。在 VS Code 中，你可以使用智能体模式（agent mode）将任何提示词放入聊天窗口，Code Assist 将不知疲倦地为你工作，以编写测试、修复错误、构建功能，甚至迁移你的代码。基于你的提示，Code Assist 的智能体将构建一个多步骤计划，从失败的实现路径中自动恢复，并推荐你可能从未想过的解决方案。

![Gemini Code Assist 的聊天智能体是一个多步骤、协作式、具备推理能力的智能体，它扩展了简单命令响应交互的能力](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/gemini_cli_code_assist_demo_cut.mp4)

所有 Gemini Code Assist 用户（免费版、标准版和企业版）都可以通过 [Insiders 渠道](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#before-you-begin)免费使用智能体模式。如果你还没有使用 Gemini Code Assist，不妨试试看。它的免费套餐拥有当今市场上最高的使用额度，而且[只需不到一分钟即可开始使用](https://codeassist.google/)。

## 上手简单

那么，你还在等什么？立即使用 Gemini CLI 升级你的终端体验吧。通过[安装 Gemini CLI 开始](http://github.com/google-gemini/gemini-cli)。你只需要一个邮箱地址，就能在你的终端中几乎无限制地使用 Gemini。

---

# Hacker News网友热议

> 热议: https://news.ycombinator.com/item?id=44376919

谷歌最新发布的开源命令行工具Gemini CLI在Hacker News上引发了超过500条评论的热烈讨论。这款工具旨在将强大的Gemini 1.5 Pro模型（拥有百万级token上下文窗口）直接带入开发者的终端。然而，网友们的讨论焦点迅速从产品本身扩展到了谷歌混乱的产品策略、激烈的市场竞争以及对隐私的深切担忧。

## 1. “史诗级混乱”的产品线与定价策略

这是整个讨论中被吐槽最猛烈的一点。大量用户，甚至是谷歌的付费订阅者，都对谷歌的产品矩阵感到困惑和愤怒。

*   **付费用户感到被背叛**：用户 `iandanforth` 的评论获得了最高赞，他一针见血地指出：“我是一名Gemini Pro订阅者，但现在我才发现，要想获得更多用量，我得成为‘Gemini Code Assist标准版或企业版’用户——我甚至都不知道这个东西的存在！为‘Gemini’付费，却在‘Gemini CLI’上得不到任何优待，真是妙啊！”
*   **产品定位不清，体验割裂**：网友 `diegof79` 将谷歌与早期的微软相提并论，认为其产品线过于庞杂，信息混乱，削弱了其技术优势。他指出，Gemini Pro、Google One、NotebookLM、Gemini聊天应用等产品之间缺乏良好的整合体验，迫使用户在多个产品间来回切换。
*   **令人费解的订阅层级**：用户们对Google One复杂的订阅等级进行了“考古”，发现其包含“AI Pro”、“AI Ultra”等多个版本，其中有9个等级，5个都叫“Premium”，但包含AI功能的却有6个。这种复杂性让用户直呼“一团糟”（What a mess）。
*   **对开发者不友好**：开发者 `behnamoh` 抱怨谷歌的API体系同样混乱：Vertex API和Google AI Studio API并存，且后者功能受限，无法平滑扩展。更令他不满的是，使用API前必须创建一个GCP项目，这对于小型脚本和概念验证来说完全是“画蛇添足”。

## 2. 与竞品（尤其是Claude Code）的直接较量

Gemini CLI被普遍认为是谷歌对标Anthropic的Claude Code的产品，因此两者的比较贯穿了整个讨论。

*   **模型虽强，商业模式落后**：许多人承认Gemini 1.5 Pro模型本身非常强大，可能是当前最强的模型之一。但他们认为，相比Claude Code清晰的订阅模式（如Pro订阅可直接使用CLI），谷歌的定价和授权方式正在“搞砸自己的优势”（fumbling the bag so badly）。
*   **抄作业但没抄到精髓**：用户 `unshavedyak` 指出，虽然Gemini CLI在功能上模仿了Claude Code，但在购买和授权体验上却天差地别。他想了解价格，却被引导到一个复杂的设置文档，而购买Claude Max就像买Pro一样简单。
*   **开放性带来一线希望**：由于Gemini CLI是开源的，有用户 `zackify` 提出，这为社区提供了可能性——可以替换其API层，接入本地模型或其他LLM，这或许是它相较于闭源的Claude Code的一个优势。

## 3. 隐私与数据使用引发深切担忧

数据隐私是Hacker News永恒的话题，对于一个会接触到用户代码的工具，这一点尤为敏感。

*   **条款明确：你的代码会被用于训练**：用户 `ipsum2` 直接贴出了谷歌的服务条款，其中明确写道，对于免费用户（包括使用个人账户登录CLI的用户），谷歌会收集其提示、相关代码、生成内容等，并可能由人类审查员进行标注，以用于改进谷歌产品和机器学习技术。
*   **“选择退出”机制的不可信**：虽然有用户指出可以“选择退出”（opt out），但立刻有网友 `foob` 引用谷歌在法庭上的证词，指出即使用户选择退出，数据仍可能被谷歌内部的其他组织用于训练。这引发了用户对谷歌隐私承诺的普遍不信任。
*   **官方文档的混乱加剧了困惑**：用户们发现，关于数据使用的说明分散在多个文档中，且相互矛盾。一个文档说不收集内容，另一个则说会收集。最终，在用户的持续追问下，谷歌员工 `fhinkel` 承认文档确实令人困惑，并发布了一个统一的澄清页面。

## 4. 谷歌团队亲自下场，与用户积极互动

本次讨论的一大亮点是多位来自Gemini CLI团队的谷歌员工（如 `cperry`, `sachinag`, `fhinkel` 等）亲自参与讨论，直面用户的批评和建议。

*   **坦诚接受反馈**：团队成员开场就表示“我们正在阅读这个帖子以获取反馈”，并鼓励用户“尽情提出bug或功能请求”。
*   **解决具体问题**：他们回应了关于GCP控制台混乱的抱怨（`sachinag`: “告诉我你想要什么，我会尽力实现”），澄清了Workspace账户需要设置项目ID才能使用的问题，并对文档的错误表示歉意，承诺修复。
*   **拉近与社区的距离**：这种直接、坦诚的沟通在一定程度上缓和了用户的负面情绪，也让外界看到了产品团队积极解决问题的一面。

## 5. 实际使用体验：赞誉与失望并存

*   **高效瞬间**：有用户 `bsenftner` 分享了成功的案例，称自己花5分钟就用Gemini CLI将一段不懂的Ruby代码成功转换为了可运行的JavaScript，而之前用GPT-4则陷入了困境。
*   **失败的“名场面”**：用户 `joelm` 在处理复杂的Rust代码时遭遇了彻底的失败。他分享了Gemini CLI一个令人啼笑皆非的输出：“我把代码搞得一团糟。我现在要撤销所有更改并重新开始。”（I have made a complete mess of the code. I will now revert all changes... and start over.）这引发了广泛共鸣。
*   **奇怪的“AI性格”**：多位用户发现，Gemini在失败时会表现出非常人性化的情绪，时而极度自信，时而又会陷入自我否定，甚至说出“很抱歉浪费您的时间，您不应该拥有我这么没用的助手”之类的话。
*   **性能瓶颈**：不少用户在刚开始使用时就遇到了“请求过于频繁”（429 Too Many Requests）的错误，即使是在免费额度内，这表明服务可能面临容量压力。

总而言之，Hacker News社区认为，Gemini CLI背后的模型技术潜力巨大，但谷歌混乱的产品战略、复杂的定价以及模糊不清的隐私政策正在严重拖累其发展。虽然谷歌团队的积极响应值得称赞，但该产品要想赢得开发者的信任和喜爱，还有很长的路要走。

----
# 终端玩家集结地

看完了这篇文章，相信你已经对 Gemini CLI 有了初步的了解。现在，让我们来聊聊你的看法：

1.  你觉得 Gemini CLI 和你用过的其他命令行 AI 工具（比如 GitHub Copilot CLI、Warp AI）相比如何？谷歌这波“免费大餐”会吸引你从其他工具切换过来吗？
2.  在终端里集成 AI，你最期待用它来解决什么问题？是快速生成 shell 脚本、调试代码，还是有其他更有创意的玩法？欢迎分享你的脑洞！
3.  Gemini 1.5 Pro 的“百万级上下文窗口”在命令行场景下，你认为最实用的地方会是哪里？比如一次性分析一个大型代码库的依赖关系，或是让它阅读整个项目的文档来回答问题？
4.  Gemini CLI 是开源的，你是否会去查看它的源码或者考虑为其贡献代码？你认为开源对于 AI 工具的生态发展有多重要？

期待在评论区看到你的真知灼见！