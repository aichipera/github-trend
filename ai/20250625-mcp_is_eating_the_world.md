# [MCP 正在吞噬世界，且已成定局](20250625-mcp_is_eating_the_world.mp3)

> 作者: Young-jin Park
> 原文: https://www.stainless.com/blog/mcp-is-eating-the-world--and-its-here-to-stay

> **译者注**: MCP（模型上下文协议）的出现，并非技术上的颠覆性革命，而是恰逢其时。在经历了函数调用、ReAct、插件等多种“胶水”方案的探索后，业界亟需一个统一、开放的标准来解决 LLM 与外部工具交互的碎片化问题。MCP 正是这剂良药，它通过一个中立的协议，让智能体（Agent）的构建变得前所未有的简单和通用。这篇文章精准地捕捉到了 MCP 成功的核心：**时机、标准与生态**。

尽管炒作不断，但模型上下文协议（MCP）并非什么魔法或革命性技术。然而，它足够简单，时机恰到好处，且执行得力。在 Stainless，我们坚信它将长存于此。

**“MCP 帮助你在大语言模型（LLM）之上构建智能体和复杂工作流”**。如果你一直关注这个领域，就会知道我们以前也见过类似的尝试。历史上曾有**无数**次尝试，试图以结构化、自动化的方式将现实世界与 LLM 连接起来。

- **函数/工具调用**：编写一个 JSON Schema，模型会选择一个函数。但你必须为每个请求手动配置函数，并承担实现重试逻辑的大部分责任。
- **ReAct / LangChain**：让模型输出一个 `Action:` 字符串，然后自己解析它——这种方式通常不稳定且难以调试。
- **ChatGPT 插件**：虽然很酷，但有准入门槛。你必须托管一个 OpenAPI 服务器并获得批准。
- **自定义 GPTs**：进入门槛更低，但仍然受限于 OpenAI 的运行时环境。
- **AutoGPT, BabyAGI**：这些智能体雄心勃勃，但在配置、循环和错误级联方面一团糟。

咳，就连 MCP 本身也不是什么新鲜事——该规范由 Anthropic 在 11 月发布，但在 3 个月后的 2 月份才突然爆火。

![Google 搜索趋势中 MCP 的热度变化](https://cdn.prod.website-files.com/662240109faccc0cefd740ae/685606fd02172b94e1944b7f_Screenshot%202025-06-13%20at%2014.53.08.png)

[Google 搜索趋势中 MCP 的热度变化](https://trends.google.com/trends/explore?date=2024-10-13%202025-06-13&geo=US&q=MCP&hl=en)

为何 MCP 似乎正在崛起，而之前的尝试都未能成功？

## 为何 MCP 能席卷世界？

### 1. 模型终于足够出色

由于模型不可靠，早期的工具使用往好了说也是一团糟。即使是基本的功能也需要大量的错误处理——仅仅为了让复杂的工作流能够运行，重试、验证和详细的错误信息都必不可少。

在智能体场景中使用工具，对鲁棒性有很高的要求。那些用过早期编码智能体的人都深知“上下文污染”的危害——当你的智能体产生一个无意义的输出后，整个对话就会陷入无法逃脱的恶性循环。当你增加更多工具时，这些危险只会成倍增加。

而伴随着新一代模型的出现，LLM 已经足够优秀，它们不再轻易陷入绝望的深渊，并且通常能够从错误中恢复。当然，模型和智能体还远非完美——更强的模型速度很慢，上下文窗口大小仍然有限，并且当上下文越来越多时，性能会下降。

重要的是，**模型已经足够好**——一旦模型越过这个门槛，集成工具使用的开销就会急剧下降。MCP 恰好在此时应运而生。

### 2. 协议终于足够完善

早期的工具接口都与特定的技术栈绑定：

- OpenAI 的函数调用只在他们的 API 中有效。
- ChatGPT 插件需要它们的运行时环境。
- LangChain 工具与它们的提示循环紧密耦合。

你无法简单地将一个工具从一个环境拿到另一个环境中使用，每个平台都需要为每个工具进行专门的配置。

更糟糕的是，将连接器转换到不同平台并非易事：每个提供商支持的能力略有不同，例如支持不同风格的 JSON Schema。为了支持重试，你必须想办法追加消息并创建一个新的补全请求，而这在不同提供商之间的实现方式又有着细微而恼人的差异。

还有一些不那么明显的隐患，比如同一个大致的提示在不同提供商之间表现差异巨大，原因仅仅在于你组织消息流的微小细节。

MCP 通过提供一个共享的、厂商中立的协议来解决这些问题。你只需定义一次工具，任何支持 MCP 的 LLM 智能体都可以访问它。

当然，兼容性问题并未完全解决。在实践中，[让 MCP 在所有平台上都能正常工作仍然是一个挑战](https://www.stainless.com/blog/what-we-learned-converting-complex-openapi-specs-to-mcp-servers#:~:text=MCP%20Clients%20have%20different%20schema%20limitations)——而且在推出初期缺乏认证标准，也使得集成更具挑战性。

尽管如此，MCP 的承诺依然重要：如果你正在开发一个工具，你只需要遵守 MCP 标准——剩下的问题就是别人代码里的 bug 了。当你[不必为了实现某个东西而与全世界对抗时](https://matklad.github.io/2022/04/25/why-lsp.html)，开发新事物会容易得多。

虽然协议并非完美，但可以说它已经**足够好**。作为一种抽象，该协议在工具和智能体之间设定了清晰的界限，这让工具开发者可以专注于工具，而智能体开发者可以专注于智能体。在 API 中暴露恰到好处的细节听起来容易，但实际上是一门艺术：在 Stainless，我们称之为“在正确的高度进行设计”（designing at the right altitude）。根据我们的经验，当一个 API 在正确的高度被设计出来时，它就不会轻易消失。

### 3. 工具链终于足够好用

MCP 的工具链直观、高质量且相对容易上手。许多语言都有可用的 SDK，这使得无论你使用何种技术栈，集成都变得轻而易举。

我们以 [Python SDK](https://github.com/modelcontextprotocol/python-sdk) 为例，尽管每个 SDK 的大致结构都相似：

- 一个能让你轻松定义工具的东西（比如 Python 函数的装饰器）
- 一个用于启动 MCP 服务器的运行时
- 一个用于与服务器交互的基本 MCP 客户端

**定义一个工具**

~~~python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def get_weather(location: str) -> str:
    """获取给定位置的天气预报。"""
    ...
~~~

**启动一个本地 MCP 服务器**：


~~~shell
mcp dev ... path.to.your.module
~~~


就是这么简单——现在，该模块中的工具对任何 MCP 客户端都可用，无需不必要的脚手架，也无需担心重试和智能体。更低的门槛意味着你可以更快地构建和分享工具——并在不同环境中复用它们，无论是在你的命令行工具、IDE、智能体、Web 服务还是其他地方。

当然，开发出色的 MCP 工具仍然需要大量工作，包括精心编写描述和关注上下文使用，但重要的是，你可以快速上手并立即看到效果。

这里有一个小小的教训：**开发者体验至关重要**。一个平台是获得广泛采用还是在默默无闻中消亡，有时仅仅取决于摩擦力的微小变化。

### 4. 势头终于足够强劲

显而易见，势头是任何平台、协议或标准成功的关键。一个协议的好坏，取决于采纳该框架的客户端和服务器的数量。

在客户端方面，MCP 的采用率已接近普及：OpenAI 已经在其智能体 SDK 中[采纳了 MCP](https://openai.github.io/openai-agents-python/mcp/)，而 Google 的 DeepMind 也在[全力支持它](https://x.com/demishassabis/status/1910107859041271977)。至此，所有主要的基础模型提供商都已加入。此外，还有许多智能体集成，包括 Cursor、Cline 和 Zed。

在服务器端，我们看到 API 优先的公司竞相将其服务作为 MCP 工具暴露出来。即使在没有第一方工具的地方，第三方服务器也填补了空白。

除了驱动 MCP 的核心软件之外，一个丰富的独立资源生态系统正在涌现：

- **注册中心** ([awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers), [smithery.ai](https://smithery.ai/), [postman](https://www.postman.com/explore/mcp-servers), [glama.ai](https://glama.ai/mcp))
- **服务** (Cloudflare, Vercel)
- **教程** ([glama.ai](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart), [towardsdatascience.com](https://towardsdatascience.com/model-context-protocol-mcp-tutorial-build-your-first-mcp-server-in-6-steps/))
- **课程** ([huggingface](https://huggingface.co/learn/mcp-course/unit0/introduction))
- **活动** ([MCP Night](https://workos.com/mcp-night))

势头的建立非一日之功——Anthropic 的团队在推动生态系统方面做得非常出色，例如编写优秀的[第一方文档](https://modelcontextprotocol.io/introduction)、提供[演讲](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)、举办活动，以及[直接与公司合作](https://linear.app/changelog/2025-05-01-mcp)，从而引导和构建一个让 MCP 从一开始就充满吸引力的生态世界。

这股势头激励社区构建和发布工具，这反过来又使智能体变得更强大，从而进一步加速社区的采纳。

随着 MCP 变得越来越普遍，基础模型提供商很可能会开始根据其使用模式进行训练。这些数据的涌入无疑将使模型在智能体任务上表现得更好，从而巩固 MCP 在我们未来思考 API 方式中的地位。

## 我们认为，它将长存于此

MCP 正处于风口浪尖，但从历史上看，站在风口浪尖并不意味着长久，因此以一份健康的怀疑态度来看待 MCP 是合理的。

尽管存在这种怀疑，我们仍然坚信 MCP 将会长存：因为它**足够好**，而且是在以往技术所不具备的那些方面足够好。而且不只是我们这么认为：我们那些 API 优先的客户，已经将 MCP 服务器视为其 API 的核心组成部分。我们正在对 MCP 下注。

---

# Hacker News 热议

> 热议: https://news.ycombinator.com/item?id=44338793

## 对 MCP 价值的争论：是革命性标准还是重复造轮子？

许多网友认为，MCP 的核心价值在于为不受自己控制的中心化AI代理（如 Claude 桌面版）提供访问复杂工具的能力，而不是让终端用户连接自己的本地工具。它通过创建一个通用协议，解耦了工具和 AI 应用，解决了 N 个工具与 M 个 AI 框架集成的“N x M”难题，并降低了非技术人员构建工作流的门槛。一位开发者分享道，他利用 MCP 让业务人员能够轻松地要求 AI 总结 20 个 Jira 工单，AI 会自动调用 50 多次工具在 Jira 和 Confluence 中查询，几秒钟就能完成过去需要数小时的手动工作。有人将其比作“LLM 的 JDBC”。

然而，强烈的反对声音认为 MCP 是在“重复造轮子”。一位经验丰富的开发者直言：“一旦行业确定了更合理的方案，我会立即删掉所有 MCP 相关的东西。”在他看来，MCP 并未带来任何新东西，完全可以用 REST API 和标准工具链实现，而且 LLM 与定义良好的 REST API 交互并不困难。**他批评 AI 领域的新人倾向于忽略业界已有的成熟经验，创造新的、设计欠佳的“约定”。** 另一部分用户则认为，**更简单的命令行工具（CLI）通常是更好的选择**。像 Claude Code 这样的 AI 代理似乎更喜欢使用 CLI，因为它们消耗更少的 token，并且不像 **MCP 那样是一个“黑箱”**。

## 炒作、营销与现实落差

社区**普遍弥漫着对 MCP 过度炒作的疲劳感**。一位用户抱怨道：“每个 AI 网红似乎在同一时间都转向了吹捧 MCP 的帖子，这让人反感。” 许多人指出，MCP 被包装成一个革命性的新概念，但本质上只是工具调用（Tool Calling）的一种标准化实现。这种炒作对于行业新人来说尤其具有误导性。

此外，MCP 在现实应用中暴露出诸多问题。安全是最大的担忧，有评论称其为“一个有趣的远程利用向量”，因为它缺乏明确的安全规范，容易受到提示注入攻击，并且可能导致凭证泄露。在资源消耗方面，为每个小功能都运行一个 Docker 容器的做法被认为是“资源浪费”。同时，协议本身尚不成熟，许多公开的 MCP 服务器质量低下、bug 丛生，反而会“把 LLM 搞糊涂”。一位用户吐槽道，他尝试使用 MCP 的体验更像是“争吵而不是调试”。

## MCP 的定位与未来：谁会真正使用它？

讨论的共识是，**MCP 的真正定位是为那些“不受你控制”的、现成的 AI 客户端（如 Claude、ChatGPT）提供扩展能力**。如果你自己编写和控制 AI 代理的循环逻辑，那么 MCP 并非必需品，直接使用 OpenAI 等提供的原生工具调用 API 会更直接。因此，MCP 对于希望为广大非技术用户提供即插即用工具的开发者，或者希望快速组合工具的“超级用户”来说价值最大。

从生态上看，MCP 目前的应用场景几乎完全集中在 B2B 工作流，如 GitHub、Jira、Slack 等。有评论指出，由于广告驱动的商业模式，大型 B2C 消费级应用（如 Twitter、Facebook）不太可能开放 API，因为这会绕过它们的界面，损害其核心利益。因此，MCP 的未来可能仍将局限于企业和专业工具领域。

## 历史的轮回：从 COM 到 X-Windows

有见识的网友从软件工程史的角度给出了有趣的类比。**一位用户指出，MCP 的动态发现和调用机制，本质上是“重新发明了微软的 COM、OLE 和 ActiveX”**。另一位用户则发出了更深刻的警告，他将 MCP 比作当年的“X-Windows”。他担心，就像功能更强大、更优雅的 NeWS 协议输给了更笨拙但“更糟即是更好”的 X-Windows 协议一样，MCP 这种固定的、效率较低的协议可能会扼杀掉未来可能出现的、更强大的动态方案（例如，直接让 LLM 与工具之间传递可执行代码），最终导致“世界第二大完全模块化的软件灾难”。

---
# 赛博茶馆：聊聊你的看法

这篇文章对 MCP 的前景充满了乐观，认为它解决了过往方案的种种痛点，并将在天时、地利、人和的加持下成为最终标准。那么，屏幕前的你怎么看？

1.  **你的痛点是什么？** 你在工作中是否也遇到了类似 LLM 与外部工具集成的难题？你是如何解决的？
2.  **终局还是过渡？** 你认为 MCP 这种“中间协议”的模式是未来的终极答案，还是又一个过渡方案？
3.  **成功的X因素？** 除了文章提到的，你认为还有哪些因素促成了（或将阻碍）MCP 的成功？
4.  **实践出真知！** 如果你已经上手了 MCP，不妨在评论区分享一下你的“最佳实践”或踩过的“坑”！

欢迎留下你的见解，让我们一起探讨 AI Agent 的未来。