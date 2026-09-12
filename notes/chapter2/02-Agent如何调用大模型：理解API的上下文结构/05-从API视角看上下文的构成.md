<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：用代码实现 Agent 的核心循环](04-%E7%94%A8%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0Agent%E7%9A%84%E6%A0%B8%E5%BF%83%E5%BE%AA%E7%8E%AF.md) · [下一篇：KV Cache 友好的上下文设计](../03-KVCache%E5%8F%8B%E5%A5%BD%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E8%AE%BE%E8%AE%A1/README.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L370-L434) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="从-api-视角看上下文的构成"></a>

### 从 API 视角看上下文的构成

通过上面的例子，我们可以清晰地看到 Agent 每次调用模型时，上下文的完整构成：

![图2-4 Agent 每次调用模型时的上下文构成](../../../source/book/images/fig2-4.svg)

上半部分（System Prompt + Tool Definitions）在整个对话过程中保持不变，下半部分（对话历史，即第一章所定义的**轨迹**）随着交互的进行不断增长。这正是第一章“上下文的五个组成部分”在 API 层面的具体样子：系统提示词和工具定义构成静态前缀，用户消息、模型回复和工具执行结果构成动态增长的消息历史。这个 “静态前缀 + 轨迹” 的结构，是后续讨论 KV Cache 优化、上下文压缩等技术的基础——理解了这个结构，就能理解为什么“前面不能动、后面可以压缩”。

本章后续将围绕这个结构逐层展开，先从利用静态前缀的不变性加速推理的 KV Cache 讲起。

后续技术虽然名称很多，落到每次请求前其实只是一次上下文构造决策。下面用 Python 风格伪代码保留这个决策的最小骨架；它与前面的完整 API 循环互补，强调上下文布局，不替代消息角色、`tool_call_id` 等协议细节。

```python
stable_prefix = system_message
stable_tools = core_tool_schemas
trajectory = load_message_history(session)
status_message = make_status_message(derive_current_state(trajectory))

if estimated_tokens(stable_prefix, trajectory, status_message) > budget:
    trajectory = compress_old_evidence(
        trajectory,
        preserve = [decisions, constraints, failures, citations]
    )

request.messages = [stable_prefix] + trajectory + [status_message]
request.tools = stable_tools
response = call_model(request)
```

系统提示词和核心工具定义尽量保持稳定；旧工具输出只在接近预算时成批压缩；当前状态放在轨迹尾部，让模型不必从长历史中重新推导。

> **实验 2-1 ★：本地 LLM 服务部署与工具调用**
>
>
> ![图2-5 本地 LLM 工具调用架构](../../../source/book/images/fig2-5.svg)
>
>在深入理解 Agent 上下文之前，让我们先通过一个实际项目来体验小型模型的能力。`local_llm_serving` 项目展示了一个重要的观点：具备思维链（Chain of Thought, CoT）思考和工具调用能力的模型并不一定需要很大的参数量。即使是 0.6B（六亿）参数的超小模型，在合理的提示词（prompt）设计和系统架构下，也能展现出令人满意的工具调用能力。
> 
>通过这个实验，你应该能够观察到：
> 
>1. **小模型的能力**：即使是 0.6B 的模型，在适当的提示工程（prompt engineering，即通过精心设计输入提示词来引导模型行为的技术）下也能准确理解并执行工具调用。
> 2. **性能表现**：在本书作者所用的苹果 M2 芯片上，模型能够以超过每秒 100 个 token 的速度生成响应，对于实时交互应用完全足够。Token 是模型处理文本的基本单位，一个中文字通常对应 1-2 个 token，一个英文单词通常对应 1-3 个 token。
>3. **ReAct 循环**：观察模型如何通过多轮思考和工具调用来解决复杂问题。
> 4. **流式响应的优势**：流式输出让用户能够实时看到模型的思考过程，包括工具调用的决策和结果的处理。
> 5. **KV Cache 的影响（顺带留意）**：保持系统提示词不变，连续发起两次对话，记录第二次的首 token 延迟；然后修改系统提示词开头的任意几个字符，再发起一次对话并对比首 token 延迟。前者因为前缀缓存命中而明显更快，后者则需要重新计算整个前缀——这一现象正是下一节的主题。
> 
> **ReAct 循环的实际案例。**
> 
>项目中的多轮工具调用遵循第一章介绍的 ReAct 思考-行动-观察循环，此处不再重复其原理。上一节已经用 OpenAI API 的 JSON 格式展示了这个过程的完整消息结构。在本地部署的实验中，这些 API 消息会被服务端（如 vLLM、Ollama）自动转换为模型内部的 token 格式。本实验的 `local_llm_serving` 项目允许你直接观察模型的原始输入输出 token 流，包括以下在 API 层面不可见的细节：
> 
>**模型的内部思考过程**：支持思维链的模型（如 Qwen3）在生成工具调用之前，会先在 `<think>` 标签内进行思考——分析用户意图、评估哪些工具适用、规划调用顺序。这个思考过程对调试 Agent 行为非常有价值。
> 
>**输出的顺序结构**：模型的输出 token 按固定顺序生成——先是内部思考（`<think>` 标签内），然后是给用户的文本回复，最后是工具调用请求。理解这个顺序对实现流式响应很关键：当 `<think>` 标签出现时可以切换到“思考中”状态；第一个工具调用的参数一经完整生成并通过校验，即可立即开始执行，无需等待模型生成后续的工具调用。
> 
>**并行工具调用**：在本节的温哥华时间和天气的例子中，模型发现两个子问题之间没有依赖关系，因此在一次输出中同时生成了两个工具调用请求。Agent 框架检测到这一点后可以并行执行两个工具，实现流水线式的加速。
> 
>**模型的终止判断**：当 Agent 框架将工具结果送回后，模型会判断是否已有足够信息回答用户。如果够了，直接输出最终回复（不含工具调用）；如果不够，继续输出新的工具调用请求，触发下一轮 ReAct 循环。
> 
>**实验总结。**
> 
>这个实验最值得记住的一点是：0.6B 的小模型在合理的提示词设计下也能可靠地完成工具调用。模型大小固然重要，但不是唯一的决定因素。一些高端移动设备已经能运行 0.6B 级别的小模型，端侧模型的可用能力也在持续提升——端侧 Agent 的时代比大多数人预期的更近。
> 
>在实验中你可能已经注意到，修改系统提示词后模型的首次响应会变慢——这正是下一节要解释的 KV Cache 机制：改变前缀会导致缓存失效，模型需要重新计算。
> 


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：用代码实现 Agent 的核心循环](04-%E7%94%A8%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0Agent%E7%9A%84%E6%A0%B8%E5%BF%83%E5%BE%AA%E7%8E%AF.md) · [下一篇：KV Cache 友好的上下文设计](../03-KVCache%E5%8F%8B%E5%A5%BD%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E8%AE%BE%E8%AE%A1/README.md)
