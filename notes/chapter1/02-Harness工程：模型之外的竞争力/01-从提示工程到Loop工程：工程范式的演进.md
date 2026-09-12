<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Harness 工程：模型之外的竞争力](README.md) · [下一篇：构建有效 Agent 的核心原则](02-%E6%9E%84%E5%BB%BA%E6%9C%89%E6%95%88Agent%E7%9A%84%E6%A0%B8%E5%BF%83%E5%8E%9F%E5%88%99.md)

> 所属章节：[第1章：AI Agent 入门](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter1.md#L321-L340) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter1/)

<!-- 原文开始 -->

<a id="从提示工程到-loop-工程工程范式的演进"></a>

### 从提示工程到 Loop 工程：工程范式的演进

回顾 AI 应用工程的发展，可以看到一条清晰的演进弧线：

**提示工程**（Prompt Engineering）是第一波创新——通过优化输入给模型的自然语言指令来提升输出质量。

**上下文工程**（Context Engineering）是第二波——人们认识到单纯优化提示词还不够，需要系统性地管理模型能看到的所有信息（系统指令、工具定义、对话历史、外部知识）。

**Harness 工程**是第三波——它将视野从“模型能看到什么”进一步扩展到“Agent 如何组织模型运行并与环境交互”，涵盖上下文与工具接口、约束机制、验证手段、反馈循环和错误恢复等 Agent 边界内、模型之外的运行与治理机制。

随后出现的 **Loop 工程**（Loop Engineering）又把视野从单次运行扩展到跨轮次的持续自主运转：谁来发现下一件该做的事、何时验证、何时才算真正完成（第十章将结合多 Agent 协作系统展开）。

2026 年 7 月，业界又开始用 **Graph 工程**（Graph Engineering）描述一种更高层的编排视角：把 Agent 循环、确定性程序和人工审批组织成显式的执行图，其中节点承担具体能力，边规定路由与依赖，结构化状态沿边传递并在关键边界处持久化[^ch1-graph-engineering]。

[^ch1-graph-engineering]: Josh C. Simmons 在 2026 年 7 月 4 日的文章 *We Are Entering the Graph Engineering Phase* 中较早明确使用这一名称，并将其概括为节点、类型化边和可检查点状态；7 月 18 日，Peter Steinberger 关于“是否已从 loops 转向 graphs”的讨论进一步推动了该名称传播。需要注意的是，相关实践早于这个名称：LangGraph、Microsoft Agent Framework 和 Google ADK 的官方文档分别称其为图编排或 graph-based workflow。参见 https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase、https://x.com/steipete/status/2078277297791189132、https://docs.langchain.com/oss/python/langgraph/overview、https://learn.microsoft.com/en-us/agent-framework/workflows/、https://adk.dev/workflows/。

这五个阶段不是替代关系，而是层层包含的：提示工程是上下文工程的子集，上下文工程是 Harness 工程的子集，Harness 工程是 Loop 工程的子集，Loop 工程又是 Graph 工程的子集——单个 Agent 循环正是执行图中的一个节点。每一层都在前一层的基础上扩展了工程师的关注范围和影响力。**当各家模型的能力越来越接近、不再是决定性的差异因素时，竞争优势就转移到了模型之外的工程实践**。

这一判断在最近的工程实践中得到验证。LangChain 在 Terminal Bench 2.0（一个评估 Agent 在终端环境中完成复杂任务能力的基准测试）上的实践提供了一个有力例证：得分从 52.8% 提升到 66.5%（从排行榜 30 名开外跃升至前 5），改变的不是模型，而是 Harness，具体包括让 Agent 自动检查自己的执行结果、检测是否陷入重复循环、优化思考策略等工程手段。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Harness 工程：模型之外的竞争力](README.md) · [下一篇：构建有效 Agent 的核心原则](02-%E6%9E%84%E5%BB%BA%E6%9C%89%E6%95%88Agent%E7%9A%84%E6%A0%B8%E5%BF%83%E5%8E%9F%E5%88%99.md)
