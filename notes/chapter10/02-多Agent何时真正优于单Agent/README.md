<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：维度二：协作拓扑](../01-%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C%E7%9A%84%E5%88%86%E7%B1%BB%E6%A1%86%E6%9E%B6/02-%E7%BB%B4%E5%BA%A6%E4%BA%8C%EF%BC%9A%E5%8D%8F%E4%BD%9C%E6%8B%93%E6%89%91.md) · [下一篇：共享上下文的多 Agent 协作](../03-%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C/README.md)

> 所属章节：[第10章：多 Agent 协作](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter10.md#L46-L78) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter10/)

<!-- 原文开始 -->

<a id="多-agent-何时真正优于单-agent"></a>

## 多 Agent 何时真正优于单 Agent

在进入具体的协作架构之前，先回答一个更根本的问题：**什么时候真正需要多个 Agent，什么时候一个 Agent 就够了？** 这个问题的答案会成为后文所有工程方案的总体参照。近年的一系列研究给出了一个清晰的判断框架——核心判据只有一条：**协作过程是否引入了单个 Agent 在生成时无法获得的新信息？**

表10-1 汇总了不同协作模式是否引入新信息，用来判断多 Agent 协作相对单 Agent 是否具有实质价值。

表10-1 多 Agent 协作模式的信息增量对比

| 协作模式 | 是否引入新信息 | 效果 |
|---|---|---|
| 同一模型自我审查（重新阅读自己的输出） | 否 | 通常无效甚至有害 |
| 不同 Agent 辩论同一段文本 | 否 | 在等计算量下与单 Agent 持平 |
| 审核者使用测试执行结果审查代码 | 是（执行反馈） | 显著提升 |
| 审核者查看渲染截图审查前端/PPT 代码 | 是（视觉反馈） | 显著提升 |
| 审核者使用外部工具验证事实 | 是（工具反馈） | 显著提升 |

2025 年的 RLEF（Reinforcement Learning from Execution Feedback）[^rlef-2025] 证实了这一点：通过强化学习训练模型利用代码执行反馈来迭代改进代码，效果远超让模型独立多次采样。关键在于每次迭代都引入了**真实的执行结果**（编译错误、测试失败、运行时异常），这些信息在模型写代码时并不存在。2025 年的 WebGen-Agent [^webgen-agent-2025] 在网页生成任务上，通过多层级的视觉反馈（截图 + 视觉语言模型描述）构成的反馈脚手架，据报道使 Claude 3.5 Sonnet 在该基准上的表现从 26.4% 提升到 51.9%——接近翻倍。

[^rlef-2025]: Gehring, J., et al. *RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning.* arXiv:2410.02089, 2025.
[^webgen-agent-2025]: Lu, Z., et al. *WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning.* arXiv:2509.22644, 2025.

这个“新信息”框架解释了一个看似矛盾的现象：一些学术研究认为多 Agent 并不能提升 Agent 能力上限，但在工程实践中，多 Agent 确实表现得更好。矛盾的根源在于两者讨论的是不同类型的 “多 Agent”：学术研究中比较的多是 “多个 Agent 看着同一段上下文互相讨论” 的模式，而工程实践中有效的多 Agent 系统往往包含外部反馈环路（代码执行、视觉渲染、工具调用）。前者没有引入新信息，后者引入了。

Anthropic 2026 年的漏洞挖掘实验给出了一个案例：45 个 Agent 通过共享论坛协调搜索、互相审查，再由独立 Agent 仲裁结果。Agent 集群用 2700 万 token 找到 266 个漏洞，而独立 Agent 并行方案用 650 万 token 只找到 21 个。在开放搜索空间里，多 Agent 通过互相通信，可以动态转移搜索重点、形成专门分工，用更高 token 预算换取更广的覆盖和更多样化的发现路径。[^anthropic-multiagent-2026]

[^anthropic-multiagent-2026]: Anthropic Frontier Red Team, “Patterns and Problems in Emerging Multiagent Systems,” 2026-08-13. https://www.anthropic.com/research/multiagent-systems

**步骤预算与 Agent 性能。** 一个相关的研究方向是：给 Agent 分配不同的步骤预算（即允许的工具调用次数或迭代轮数），会如何影响其表现？直觉上，更多步骤应该带来更好的结果——30 步预算下 Agent 只能快速实现核心功能，300 步预算下它还可以先做规划、再实现、再测试、再改进。但 2025 年 Google 的论文《Budget-Aware Tool-Use Enables Effective Agent Scaling》发现了一个反直觉的结论：**单纯增加 Agent 可用的步骤数并不能保证性能提升**。标准的 Agent 缺乏“预算意识”——即使有 300 步的预算，它们仍然倾向于执行浅层搜索，很快就“饱和”了。要让更多的步骤真正转化为更好的结果，Agent 需要一种显式的预算感知机制，根据剩余资源动态调整策略：前期广泛探索，后期聚焦最有希望的方向。2026 年的 BAVT（Budget-Aware Value Tree Search）进一步提出了步骤级别的价值评估，在每一步根据剩余预算比例调整探索与利用的权重——随着预算减少，Agent 从“广撒网”逐渐切换到“深挖掘”。

这些发现对多 Agent 系统设计有直接的指导意义。比如在管理者模式中，Manager Agent 不应只是简单地将任务分发给子 Agent 然后等待结果，而应该根据任务的复杂度**动态分配步骤预算**——简单子任务给较少的步骤，复杂子任务给充足的步骤。同时还要引导子 Agent 合理利用这些预算（先规划、再实现、再测试、再改进），而不是一头扎进去直接开干。

此外，**成本**是多 Agent 系统必须关注的要点。多 Agent 的并行探索与反复迭代都要消耗大量 token。这意味着多 Agent 带来的收益必须足够大，能够覆盖数倍乃至一个数量级的额外开销，否则一个调校得当的单 Agent 往往是更划算的选择。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：维度二：协作拓扑](../01-%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C%E7%9A%84%E5%88%86%E7%B1%BB%E6%A1%86%E6%9E%B6/02-%E7%BB%B4%E5%BA%A6%E4%BA%8C%EF%BC%9A%E5%8D%8F%E4%BD%9C%E6%8B%93%E6%89%91.md) · [下一篇：共享上下文的多 Agent 协作](../03-%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C/README.md)
