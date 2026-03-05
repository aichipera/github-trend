---
title: 绿联NAS部署OpenClaw保姆级教程：打造飞书AI机器人
date: 2026-03-04
tags:
    - OpenClaw
    - Docker
    - 绿联NAS
    - 飞书
    - AI机器人
---

# 绿联NAS部署OpenClaw保姆级教程：打造飞书AI机器人

## 前言

如果你想在飞书里拥有一个属于自己的AI机器人，OpenClaw是一个很不错的选择。它是一个强大的AI工具代理网关，支持多种IM平台接入，并且集成了代码助手、浏览器自动化等实用功能。

![](./asserts/openclaw.jpg)

**本教程将手把手教你**如何在**绿联NAS**上部署OpenClaw，并对接飞书，使用SiliconFlow提供的LLM API服务。

> 💡 **推荐模型提供商**：本教程使用 [SiliconFlow](https://cloud.siliconflow.cn/i/ym4c1Vqm) 的API服务。注册后可获得赠金额度，支持多种大模型，性价比很高！

![](./asserts/pasted_image_20260303-33.png)

---

## 一、OpenClaw是什么？

[OpenClaw](https://docs.openclaw.ai/)是一个开源的AI工具调度代理网关，专注于将各种AI能力（如大模型、代码助手、浏览器自动化等）通过统一的接口对外提供服务。

本教程使用的是预装了中国主流IM平台的定制Docker镜像 [**OpenClaw-Docker-CN-IM**](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM)，其特性如下：

| 特性              | 说明                             |
| --------------- | ------------------------------ |
| 🚀 **开箱即用**     | **飞书、钉钉、QQ、企业微信**等主流IM平台插件全部预装 |
| 🐳 **Docker部署** | 一键启动，无需复杂配置                    |
| 💻 **AI代码助手**   | 内置OpenCode AI，支持智能代码生成和分析      |
| 🎭 **浏览器自动化**   | 预装Playwright，支持网页操作和截图         |
| 🎙️ **中文TTS**   | 支持中文语音合成                       |

---

## 二、准备工作

### 2.1 硬件要求

- 一台已联网的**绿联NAS**（需要支持Docker的型号）
- 绿联NAS管理员权限

### 2.2 申请API Key

1. 绿联NAS 且 使能 Docker 功能

2. 注册SiliconFlow账号获取API Key
   - 访问 [https://cloud.siliconflow.cn/i/ym4c1Vqm](https://cloud.siliconflow.cn/i/ym4c1Vqm) 注册
   - 完成实名认证后可获得赠金额度

注册完成后，建议充值几块钱，然后创建**API Key**： https://cloud.siliconflow.cn/me/account/ak 

![](./asserts/pasted_image_20260302-18.png)

创建成功后，把API Key复制下来，记录为 `API_KEY` 变量的值，后面要用到。
### 2.3 飞书机器人

1. 访问 [飞书开放平台](https://open.feishu.cn)
2. 点击「创建企业自建应用」
3. 填写应用名称（如「AI助手」）
4. 选择应用类型为「机器人」
![](./asserts/pasted_image_20260302-8.png)
![](./asserts/pasted_image_20260302-9.png)
![](./asserts/pasted_image_20260302-10.png)
在 **机器人** 页面，修改这里的 **如何开始使用**
![](./asserts/pasted_image_20260302-15.png)
在 **凭证与基础信息** 这里 点击一下，然后复制记住这里的 **App ID** 和 **App Secret** ，这是**非常重要**的。 这里记录为 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 变量的值。
![](./asserts/pasted_image_20260302-12.png)

然后点击「权限管理」，点击「批量导入/导出权限」，复制下面的JSON内容粘贴导入：

~~~json
{
  "scopes": {
    "tenant": [
      "contact:contact.base:readonly",
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "cardkit:card:read",
      "cardkit:card:write",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "event:ip_list",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource"
    ],
    "user": [
      "aily:file:read",
      "aily:file:write",
      "im:chat.access_event.bot_p2p_chat:read"
    ]
  }
}
~~~

![](./asserts/pasted_image_20260302-13.png)
![](./asserts/pasted_image_20260302-14.png)

然后创建机器人，发布一个版本，版本号填写「1.0.0」，更新记录可以随意填写，**务必点击确认发布**。
![](./asserts/pasted_image_20260302-16.png)
![](./asserts/pasted_image_20260302-17.png)


---

## 三、OpenClaw项目介绍

本教程基于 [OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) 项目进行部署。这是一个预装了所有中国主流IM平台插件的Docker镜像，开箱即用。

### 项目特点

| 优势     | 说明                  |
| ------ | ------------------- |
| 预装插件   | 飞书、钉钉、QQ、企业微信插件全部预装 |
| 环境变量配置 | 通过 Docker Compose 配置管理，一键部署  |
| 数据持久化  | 配置和工作空间数据自动持久化到NAS  |

### Docker镜像

```
https://hub.docker.com/r/justlikemaki/openclaw-docker-cn-im/
```

---

## 四、绿联NAS部署OpenClaw

### 4.1 登录绿联NAS管理页面

> 📖 绿联NAS提供了详细的[知识中心](https://support.ugnas.com/knowledgecenter/#/)，可以查阅Docker相关教程。

![](./asserts/pasted_image_20260302-2.png)
1. 打开浏览器访问绿联NAS管理入口：[https://ug.link](https://ug.link)
2. 输入你的 **NAS ID**（在绿联NAS APP的「设备信息」里可以查看到）
3. 输入管理员账号密码登录
![](./asserts/pasted_image_20260302.png)

### 4.2 开启并配置Docker

#### 开启Docker功能

1. 登录后进入「应用中心」
2. 找到[「Docker」应用](https://support.ugnas.com/knowledgecenter/#/detail/eyJhcnRpY2xlSW5mb0lkIjoyMzYsImFydGljbGVWZXJzaW9uIjoiMS4wIiwiY2xpZW50VHlwZSI6Ik1PQklMRSIsImN1cnJlbnRQYWdlIjowLCJpZCI6NTY3NiwibGFuZ3VhZ2UiOiJrby1LUiIsInBhdGhDb2RlIjoicHJvMDAyLDlqb3A1dyIsInNpemUiOjEwLCJ0eXBlIjoidGFnMDAxIn0=) 并 打开

#### 配置Docker镜像加速（重要！）

由于国内访问Docker Hub速度较慢，强烈建议配置[镜像加速](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNDUzIn0=)：

1. 进入Docker的「设置」页面
2. 找到「镜像加速器」或「Registry Mirrors」配置项
3. 添加以下镜像源（推荐配置多个以提高稳定性）：

```c
https://docker.1ms.run
https://docker.1panel.live/
```

4. 点击保存并重启Docker服务
![](./asserts/pasted_image_20260302-1.png)

> 💡 不配置镜像加速的话，下载镜像可能会非常慢甚至失败。

### 4.3 下载OpenClaw Docker镜像

1. 进入Docker的「镜像」管理页面
2. 点击「搜索镜像」或「Pull Image」按钮
3. 输入镜像名称：`justlikemaki/openclaw-docker-cn-im`
4. 选择版本（建议选择 `latest` 标签，我当时的版本是 `main-8642ab9`）
5. 点击下载，等待下载完成
![](./asserts/pasted_image_20260302-3.png)
镜像大小约 2-3GB，需要等待几分钟下载完成。

### 4.4 创建OpenClaw Docker项目

在绿联知识中心搜索「Docker Compose」可以查看相关教程：
- https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNDg3In0=

在 **Docker** -> 「**项目**」页面创建一个项目，参考Docker Compose配置如下（**注意将API_KEY、FEISHU_APP_ID和FEISHU_APP_SECRET修改为你自己的**）：

![](./asserts/pasted_image_20260302-20.png)

> ⚠️ **安全提醒**：以下配置中的API Key为示例，请务必替换为你自己创建的凭证。

~~~shell
# Compose配置
version: '3.8'

services:
  openclaw-gateway:
    container_name: openclaw-gateway
    # 如果发现镜像版本太新了，和我部署的时候版本不一样，可以将 latest 换成 main-8642ab9
    image: justlikemaki/openclaw-docker-cn-im:latest
    cap_add:
      - CHOWN
      - SETUID
      - SETGID
      - DAC_OVERRIDE
    # 可选：指定容器运行 UID:GID（例如 1000:1000）
    # 默认保持 root 启动，以便 init.sh 自动修复挂载卷权限后再降权运行网关
    user: 0:0
    environment:
      TZ: Asia/Shanghai
      HOME: /home/node
      TERM: xterm-256color
      # ========== 请务必修改以下配置 ==========
      # 模型配置 第一次需要配置成true，确保配置同步过去了
      # 等openclaw.json生成以后，且配置好了飞书可用了，可以正常聊天了，我建议后面改成false
      # 以后重新部署一次，但是不用删除myclaw文件夹，不然他default的模型又会切错
      SYNC_MODEL_CONFIG: true
      MODEL_ID: siliconflow/Pro/MiniMaxAI/MiniMax-M2.5
      IMAGE_MODEL_ID: Qwen/Qwen-Image-Edit-2509
      BASE_URL: https://api.siliconflow.cn/v1
      # 👇 TODO 在这里填入你在 SiliconFlow 申请的 API Key
      API_KEY: YOUR_API_KEY
      # 👇 TODO 在这里填入你在飞书开放平台申请的 App ID 和 App Secret
      FEISHU_APP_ID: YOUR_FEISHU_APP_ID
      FEISHU_APP_SECRET: YOUR_FEISHU_APP_SECRET
      # ========== 以上配置请务必修改 ==========
      API_PROTOCOL: openai-completions
      CONTEXT_WINDOW: 196608
      MAX_TOKENS: 16384
      # 工作空间配置
      WORKSPACE: /home/node/.openclaw/workspace
      # Gateway 配置
      OPENCLAW_GATEWAY_TOKEN: 123456
      OPENCLAW_GATEWAY_BIND: lan
      OPENCLAW_GATEWAY_PORT: 18789
      OPENCLAW_BRIDGE_PORT: 18790
      OPENCLAW_GATEWAY_MODE: local
      # 允许的 Origin 域，多个用逗号隔开
      OPENCLAW_GATEWAY_ALLOWED_ORIGINS: "*"
      # 允许不安全认证（如 http），可选 true/false
      OPENCLAW_GATEWAY_ALLOW_INSECURE_AUTH: true
      # 危险：禁用设备认证（如在 Docker 环境中无法获取设备信息），可选 true/false
      OPENCLAW_GATEWAY_DANGEROUSLY_DISABLE_DEVICE_AUTH: true
      # 插件全局控制
      OPENCLAW_PLUGINS_ENABLED: true
    volumes:
      - /volume1/docker/myclaw:/home/node/.openclaw
      # 使用匿名卷排除 extensions 目录，使用镜像中预装的插件
      - /home/node/.openclaw/extensions
    ports:
      - "58789:18789"
      - "58790:18790"
    init: true
    restart: unless-stopped
~~~
按照上面的截图标红的位置，在 `docker`目录下创建一个 `myclaw`文件夹，然后创建项目的时候，选择存放位置到这个 `myclaw` 目录，然后将上面的`Compose配置`复制出来，然后把里面的`TODO`位置的**API_KEY**、**FEISHU_APP_ID**和**FEISHU_APP_SECRET**修改成自己的，然后再把修改后的内容复制到这个**Compose配置**下方文本编辑区域里面，然后点击 **立即部署**，然后等待部署完成。
![](./asserts/pasted_image_20260302-21.png)
然后再点击 **容器**，选择 **openclaw-gateway** 这个容器，然后查看 **日志**，然后等出现类似下面标红输出的时候，再到飞书机器人页面继续配置。
![](./asserts/pasted_image_20260303.png)
现在在**飞书开放平台**，这个**机器人配置页面**的事件与回调页面，点击订阅方式，然后选择使用**长连接**，然后把这个事件 `im.message.receive_v1`添加进去保存。

![](./asserts/pasted_image_20260303-1.png)
修改完毕后，需要在**飞书开放平台**发布新版本机器人，然后才能进行后续配置。
![](./asserts/pasted_image_20260303-2.png)

openclaw-gateway docker镜像启动以后，第一次需要等几分钟，然后在和NAS相同的局域网里面打开你NAS的IP，配合设置的端口 http://192.168.1.8:58789/ （**注意**：不要使用绿联转发的网页，那个连不上Gateway）

> 💡 这上面的IP地址换成你自己的NAS局域网IP

![](./asserts/pasted_image_20260303-4.png)

打开以后，设置WebSocket URL为 `ws://192.168.1.8:58789`（替换为你的NAS IP），网关令牌为 `123456`

![](./asserts/pasted_image_20260303-3.png)

然后点击「聊天」，如果发消息报错：

```
⚠️ Agent failed before reply: Unknown model: pro/MiniMaxAI/MiniMax-M2.5.
Logs: openclaw logs --follow
```

![](./asserts/pasted_image_20260303-5.png)

然后在 **容器 -> openclaw-gateway -> 终端 -> 新增**，然后运行如下命令：

> [!NOTE]
> 如果你是在命令行上，如WSL或者Linux上，可以使用 `docker ps` 查看运行的镜像，然后使用 `docker exec -it <容器名或ID> /bin/bash` 连接进去。

~~~shell
# 安装一下vim，后面可能需要编辑
apt update
apt install -y vim
# **重要** 必须切到 node 用户
su node
~~~
![](./asserts/pasted_image_20260303-7.png)
![](./asserts/pasted_image_20260303-8.png)
**下面执行的命令务必确保**切到了 `node`用户，然后运行如下命令

~~~shell
# 修复一下配置文件
openclaw doctor --fix
~~~
![](./asserts/pasted_image_20260303-9.png)
然后再运行 `openclaw onboard`, 按照下面的步骤标红的选择，注意里面的API Key填你的，API Base URL配置成 `https://api.siliconflow.cn/v1`
![](./asserts/pasted_image_20260303-10.png)
![](./asserts/pasted_image_20260303-11.png)
这里就可以配置出 `siliconflow/Pro/MinimaxAI/MiniMax-M2.5`模型
![](./asserts/pasted_image_20260303-12.png)
![](./asserts/pasted_image_20260303-15.png)
![](./asserts/pasted_image_20260303-16.png)

配置好Model和API Key以后，就可以正常通过Dashboard跟模型交互了

![](./asserts/pasted_image_20260303-17.png)

飞书可能遇到权限问题，需要重新导入一些新的权限，点击链接完成授权即可。
![](./asserts/pasted_image_20260303-18.png)
 **飞书配对**：在飞书APP上给机器人发送消息，它会回复配对命令，输入到这个终端里面执行执行即可，然后他会返回 `Approved feishu sender xxx`
![](./asserts/pasted_image_20260303-20.png)

但是在飞书里面给机器人发消息，也会报前面出现的这个`Unknown model: pro/MiniMaxAI/MiniMax-M2.5. Logs: openclaw logs --follow` 模型错误，同时在docker界面的日志里面也会报错，如下图所示：
![](./asserts/pasted_image_20260303-19.png)
然后在命令行里面输入 `openclaw channels list` 可以查看一下
![](./asserts/pasted_image_20260303-22.png)
执行 `openclaw models` 发现还是模型没有配置好
![](./asserts/pasted_image_20260303-26.png)

需要执行以下命令强制设置默认模型：

~~~shell
openclaw models set-image siliconflow/Qwen/Qwen-Image-Edit-2509
openclaw models set siliconflow/Pro/MiniMaxAI/MiniMax-M2.5
~~~

![](./asserts/pasted_image_20260303-27.png)

然后手动编辑 `vim .openclaw/openclaw.json` 文件，修改context和maxTokens大小分别为`196608` 和 `16384`：

> 关于配置各项含义参见 https://docs.openclaw.ai/concepts/model-providers#local-proxies-lm-studio-vllm-litellm-etc

![](./asserts/pasted_image_20260303-28.png)

重启OpenClaw Gateway Docker后，即可正常使用：
![](./asserts/pasted_image_20260304.png)

> 如果发现重启以后用不了，就需要将前面提到的 `SYNC_MODEL_CONFIG` 从 `true` 改成 ``false``。
> 然后重新部署一下，但是不需要删除 `myclaw` 目录，只需要重新用 `node` 用户执行以下，上面的 默认模型设置。
> openclaw models相关的命令应该就可以了。

然后飞书也可以正常工作了。


## 五、总结

通过以上步骤，你已经成功在绿联NAS上部署了OpenClaw，并对接了飞书机器人。现在你可以：

- ✅ 在飞书中随时与AI对话
- ✅ 在群聊中@机器人获取回复
- ✅ 利用AI助手处理各种任务
- ✅ 根据需要添加更多IM平台

> 💡 **小提示**：当一切配置完毕、正常运行后，建议将 `/volume1/docker/myclaw/openclaw.json` 文件备份一份。日后如果不小心配置弄坏了，可以直接用备份文件恢复，省去重新配置的麻烦。

部署过程中如果遇到问题，欢迎在评论区交流讨论~

---

## 📮 交流群

如果你对 OpenClaw 感兴趣，欢迎加群一起来**煲小龙虾🍤**！

![](./asserts/wechat_group.jpg)

**如果觉得不错，可以扫描关注一下公众号。**

![](../asserts/wx.jpg)

或者可以通过 GitHub 提交 Issue 与开发者社区交流：

| 项目/服务                 | 链接                                                                               |
| --------------------- | -------------------------------------------------------------------------------- |
| OpenClaw官方文档          | [官方手册](https://docs.openclaw.ai/start/getting-started)                           |
| OpenClaw飞书配置          | [飞书配置指南](https://github.com/openclaw/openclaw/blob/main/docs/channels/feishu.md) |
| OpenClaw-Docker-CN-IM | [GitHub](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM)                  |
| SiliconFlow注册（有赠金）    | [立即注册](https://cloud.siliconflow.cn/i/ym4c1Vqm)                                  |
| 飞书开放平台                | [https://open.feishu.cn](https://open.feishu.cn)                                 |

---

> 💡 本教程基于实际部署经验编写，如果对你有帮助，欢迎点赞、分享！有问题欢迎在评论区交流~
