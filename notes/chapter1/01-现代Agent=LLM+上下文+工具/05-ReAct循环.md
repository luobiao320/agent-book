<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：上下文：Agent 的眼睛](04-%E4%B8%8A%E4%B8%8B%E6%96%87%EF%BC%9AAgent%E7%9A%84%E7%9C%BC%E7%9D%9B.md) · [下一篇：Harness 工程：模型之外的竞争力](../02-Harness%E5%B7%A5%E7%A8%8B%EF%BC%9A%E6%A8%A1%E5%9E%8B%E4%B9%8B%E5%A4%96%E7%9A%84%E7%AB%9E%E4%BA%89%E5%8A%9B/README.md)

> 所属章节：[第1章：AI Agent 入门](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter1.md#L161-L262) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter1/)

<!-- 原文开始 -->

<a id="react-循环"></a>

### ReAct 循环

了解了 Agent 的三大组件后，一个自然的问题是：它们如何协同工作？ReAct 循环就是将 LLM、上下文和工具串联起来的核心机制——让我们看看一个 Agent 是如何一步步思考和行动的。

Agent 执行任务的核心模式叫做 **ReAct**（Reasoning + Acting）。虽然名字只体现了思考（Reasoning）和行动（Acting）两个词，但实际循环包含三个环节：模型先**思考**当前应该做什么，然后调用工具**行动**，再**观察**工具返回的结果并继续思考下一步。这个“想→做→看→想→做→看”的循环不断重复，直到任务完成。

让我们通过一个多币种收入汇总的具体例子来理解 Agent 的**轨迹**（trajectory）。轨迹是 Agent 在执行任务过程中不断积累的消息历史——用户消息、模型回复（包括思考过程和工具调用）、工具执行结果。每一次调用 LLM 时，它接收的完整上下文由**静态前缀**（系统提示词 + 工具定义）和**轨迹**（动态消息历史）两部分组成（图1-4）。这揭示了一个关键事实：**Agent 的上下文 = 静态前缀 + 轨迹**。具体地说，静态前缀对应前文五个组件中的前两项（系统提示词 + 工具定义），轨迹对应后三项（用户消息 + 模型回复 + 工具执行结果，随交互不断增长）。基于这个完整上下文，LLM 生成下一步的响应，然后这个响应又追加到轨迹中，供下一次调用使用。

![图1-4 Agent 轨迹——多币种汇总任务的 ReAct 循环](../../../source/book/images/fig1-4.svg)

先看最小运行骨架。它说明的是**机制如何运行**：Model 只负责决定下一步，Harness 负责组装上下文、校验并执行工具，Environment 负责产生真实状态变化和观察。本书后续也沿用 Python 风格伪代码；伪代码不能直接运行，也不对应某个 SDK。具体的可执行代码在本书配套代码仓库中。

```python
trajectory = [user_request]

repeat:
    context = stable_prefix + trajectory
    decision = Model(context)
    trajectory.append(decision)

    if decision has no tool call:
        return decision.answer

    for call in decision.tool_calls:       # independent calls may run in parallel
        validated_call = Harness.validate(call)
        observation = Environment.execute(validated_call)
        trajectory.append(observation)
```

下面再看一次运行后**轨迹中保存了什么**。它是消息数据的结构示意，不是 Agent 循环的实现代码：

```text
轨迹 = [
  {role: "user" , content: "根据公司季度收入：Q1 2.5M 美元，Q2 2.1M 欧元，Q3 1.8M 英镑，Q4 380M 日元，计算公司年度总收入和季度平均收入" },
  
  # 第一次迭代 - LLM 看到上述轨迹，生成响应
  {role: "assistant" ,
   reasoning: "需要将所有货币转换为 USD..." ,
   content: "" ,  # 没有直接回复用户
   tool_calls: [
     {name: "convert_currency" , args: {amount: 2100000, from: "EUR" , to: "USD" }},
     {name: "convert_currency" , args: {amount: 1800000, from: "GBP" , to: "USD" }},
     {name: "convert_currency" , args: {amount: 380000000, from: "JPY" , to: "USD" }}
   ]},
  
  # Agent 框架执行工具，添加结果到轨迹
  {role: "tool" , content: "EUR->USD: 2282608.7" },
  {role: "tool" , content: "GBP->USD: 2278481.01" },
  {role: "tool" , content: "JPY->USD: 2541806.02" },
  
  # 第二次迭代 - LLM 看到完整轨迹，包括工具结果
  {role: "assistant" ,
   reasoning: "已获得转换结果，现在需要汇总计算..." ,
   content: "" ,
   tool_calls: [
     {name: "code_interpreter" , args: {code: "total = 2500000 + 2282608.7 + ..." }}
   ]},
  
  {role: "tool" , content: "Total: $9,602,895.73, Average: $2,400,723.93..." },
  
  # 第三次迭代 - LLM 看到完整轨迹，生成最终答案
  {role: "assistant" ,
   reasoning: "所有计算完成，总结结果..." ,
   content: "FINAL ANSWER: 总收入$9,602,895.73..." }
]
```

注意，轨迹中没有显示系统提示词和工具定义——它们作为静态前缀，在每次 LLM 调用时都会被自动拼接在轨迹前面。

整个过程只用了 3 次迭代、4 次工具调用。

在这种最基本的设计中，上下文是不断追加的：每次调用 LLM 都能看到完整的轨迹，因而它清楚任务进行到了哪一步、此前尝试过什么、得到了什么结果。轨迹的结构化也让系统易于解释和调试——用户消息、模型回复（思考过程 + 工具调用）和工具执行结果彼此分明。更进一步，分析大量轨迹可以发现 Agent 的行为模式、优化决策路径、改进工具设计；轨迹还可以沉淀进知识库，或用于强化学习训练更好的模型，形成从经验中学习的闭环。


理解了 Agent 的运行循环后，让我们通过两个实验来感受不同模型如何驱动这个循环。

> **实验 1-2 ★：Kimi K3 原生 Agent 能力**
>
> 这个实验展示了 **Kimi K3** 的原生 Agent 能力，体现了“模型即 Agent”的新范式。Kimi K3 是一个约 2.8 万亿参数的混合专家（MoE, Mixture of Experts）模型——可以把 MoE 想象成一个专家团队：面对不同类型的问题，系统会自动选择最合适的几位专家来作答，而不需要所有专家同时上阵，这样既保证了能力又提高了效率。它拥有 100 万 token 的上下文窗口、原生的视觉理解能力，以及始终开启的“思考模式”（thinking mode）；模型通过强化学习训练，将工具调用的**决策策略**内化为原生能力——何时调用工具、调用哪个、传什么参数都由模型自主决定，从而能够自主完成网络搜索等任务。
>
> 关键观察包括：模型自己决定何时搜索、搜索什么，展现了真正的自主性；它能根据搜索结果动态调整策略，自主判断信息是否充足。这里需要厘清一个常见的误解，关键在于分清两件事的归属。**强化学习写进参数的是决策**——何时该调用工具、调用哪个、传入什么参数、拿到结果后是否继续、如何把几十上百次调用串联成连贯的推理。**工具本身及其执行则由 Agent 框架（或 API 内置工具）提供**——`web_search`、`code_runner` 的真实实现、代码沙盒环境、调用的发起与结果回传，都在模型之外的基础设施里完成（Kimi 通过名为 Formula 的服务端脚本引擎运行这些官方工具）。因此编排循环并没有消失，而是从客户端移到了服务端，决策权则交给了模型[^ch1-2]。
>
> [^ch1-2]: 感谢读者 asdlem 通过 GitHub Issue #30 指出并厘清了“RL 内化的是工具调用决策策略、而非工具执行机制”这一区分。参见 https://github.com/bojieli/ai-agent-book/issues/30
>
> Kimi K3 在 Agent 任务中的一个突出优势是**长链工具调用的稳定性**——它能够连续执行 200～300 次工具调用而保持思考的一致性，远超多数模型在数十次调用后就开始退化的表现。K3 面向长周期编程与 Agent 工作负载优化，发布时提供 K3 Max（面向对话与 Agent 任务）与 K3 Swarm Max（面向大规模并行处理）两个规格。作为开源模型，它在软件工程和 Agent 基准测试中展现了可与顶尖闭源系统比肩的性能，证明了通过强化学习赋予模型原生 Agent 能力这条路线的有效性。

> **实验 1-3 ★：GPT-5.6 原生 Deep Research 能力**
>
> 第二个实验使用 **OpenAI GPT-5.6**，展示先进模型如何借助 API 内置工具，在服务端形成 Deep Research 的“搜索—阅读—分析”编排闭环。GPT-5.6 的一个便利特性是**自由格式工具调用**（Freeform Tool Calling）。传统方式中，模型调用工具时必须把所有参数打包成严格的 JSON 格式（一种结构化的数据格式），这就像填表格一样有很多格式限制。自由格式工具调用（在 API 中通过 `type: "custom"` 的工具类型声明）允许模型直接向工具发送原始文本（比如一段 Python 代码、一条 SQL 查询），省去了 JSON 转义的麻烦。要说明的是，这是 API 参数格式的演进，而非模型架构的革新——客户端的工具调用循环（检测 `tool_calls` → 执行 → 回传结果）逻辑保持不变，改变的只是参数从 JSON 字符串变成了原始文本。
>
> GPT-5.6 配合 Responses API 的**网络搜索和代码解释器**内置工具——这正是 Deep Research 的核心：模型能够自主搜索网络获取实时信息，并编写代码进行深度分析，实现“搜索 -> 阅读 -> 分析 -> 再搜索”的迭代研究过程。例如，面对 “东盟 10 国首都之间，最近的一对首都距离多少” 这样的问题，GPT-5.6 会自动搜索各国首都的地理坐标，然后编写 Python 代码计算所有首都对之间的大圆距离，最终找出最近的一对。又如 “搜索最近一个月的比特币走势，做技术分析” 任务中，它能从多个金融数据源获取实时价格数据，运用专业的技术分析库计算移动平均线、RSI、MACD 等技术指标，生成可视化图表并给出交易建议。
>
> 更重要的是，GPT-5.6 将 **OpenAI Deep Research** 产品的设计理念内化到了模型层面，引入了**意图澄清过程**。当用户提出研究需求后，GPT-5.6 不会立即动手执行，而是首先通过一系列问题来澄清用户的真实意图。以“搜索最近一个月的比特币走势，做技术分析”为例，它会先问：“你偏好使用哪个数据源？需要分析哪些技术指标？”通过这种交互式的意图澄清，GPT-5.6 能够生成更精准、更符合用户需求的研究报告。
>
> GPT-5.6 是“模型即 Agent”概念的一个成熟实例：网络搜索、代码解释器作为 Responses API 的内置工具在服务端闭环执行，客户端不必再自行搭建“搜索—阅读—分析”的编排框架。而意图澄清的意义在于，它让“用户说了什么”和“用户真正想要什么”之间的差距，在任务执行之前就得到了弥合。
>
> 需要说明的是，这个实验并不绑定某一家厂商。没有 OpenAI 额度的读者完全可以用具备等价托管工具的提供商复现：例如阿里云百炼 qwen3.7-plus 的 Responses API 同样内置 `web_search` 与 `code_interpreter`；Kimi K3 的 Formula 托管搜索与 `code_runner` 也属于同类能力。
>
> 图1-5 展示了“模型即 Agent”范式下原生工具调用的完整架构，以及 Kimi K3 / GPT-5.6 在实际任务中的 ReAct 执行过程。
>
> ![图1-5 “模型即 Agent” 架构——原生工具调用](../../../source/book/images/fig1-5.svg)


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：上下文：Agent 的眼睛](04-%E4%B8%8A%E4%B8%8B%E6%96%87%EF%BC%9AAgent%E7%9A%84%E7%9C%BC%E7%9D%9B.md) · [下一篇：Harness 工程：模型之外的竞争力](../02-Harness%E5%B7%A5%E7%A8%8B%EF%BC%9A%E6%A8%A1%E5%9E%8B%E4%B9%8B%E5%A4%96%E7%9A%84%E7%AB%9E%E4%BA%89%E5%8A%9B/README.md)
