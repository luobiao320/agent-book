<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../README.md) · [上级目录](../../README.md) · [上一篇：思考题](../chapter9/05-%E6%80%9D%E8%80%83%E9%A2%98/README.md) · [下一篇：多 Agent 协作的分类框架](01-%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C%E7%9A%84%E5%88%86%E7%B1%BB%E6%A1%86%E6%9E%B6/README.md)

> 所属章节：[第10章：多 Agent 协作](README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter10.md#L1-L10) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter10/)

<!-- 原文开始 -->

<a id="多-agent-协作"></a>

# 多 Agent 协作

前九章围绕单个 Agent 展开：先构建上下文、知识、工具与交互能力，再通过评估、后训练和持续进化让它长期变好。本章把问题从“如何构建和改进一个 Agent”推进到“如何组织多个 Agent”——让它们通过分工、通信与相互验证完成单个 Agent 难以承担的任务。

在 OpenAI 曾提出的五级 AI 能力框架（Level 1 对话者、Level 2 思考者（Reasoners）、Level 3 智能体、Level 4 创新者、Level 5 组织（Organizations））中，多 Agent 协作常被类比为通向第五级的路径之一——需要说明的是，此处 Organizations 指的是“AI 能完成整个组织的工作”这一能力级别，而非对系统架构的要求，足够强大的单个 Agent 理论上也能达到。但就今天的工程现实而言，单个 Agent 终究受限于自身模型的能力边界和上下文窗口。

而让多个 Agent 协同工作，意义远不止让不同专长的 Agent “取长补短”。更根本的一点是：**群体的智能可以高于个体**。人类文明便是明证——单个人的智力有限，但经由分工、协作、辩论和知识的代际累积，人类社会作为整体所展现的智能，远超任何一位天才个体。Agent 群体同样可能涌现出这样的集体智能：哪怕每一个 Agent 都只相当于人类专家的水平，只要组织得当，其整体能力也可能超过所有人类专家的总和。Google DeepMind 在《从 AGI 到 ASI》中正把“大规模多 Agent 集体”列为通往超级智能（ASI）的关键路径之一——正如人类的通用智能能聚合成超越个体的社会与组织实体，众多 AGI 级 Agent 协同形成的“群体智能”，也可能表现出远超其成员简单相加的认知能力[^agi-asi]。因此，多 Agent 协作不只是突破单个模型上下文窗口与能力边界的工程手段，更可能是从“专家级 AI”迈向“超越人类整体”的一条根本路径。

[^agi-asi]: 把“大规模多 Agent 集体”列为从通用人工智能通往超级智能的关键路径之一，见 Google DeepMind, *From AGI to ASI.* arXiv:2606.12683, 2026.


<!-- 原文结束 -->

## 阅读目录

- [多 Agent 协作的分类框架](01-%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C%E7%9A%84%E5%88%86%E7%B1%BB%E6%A1%86%E6%9E%B6/README.md)
- [多 Agent 何时真正优于单 Agent](02-%E5%A4%9AAgent%E4%BD%95%E6%97%B6%E7%9C%9F%E6%AD%A3%E4%BC%98%E4%BA%8E%E5%8D%95Agent/README.md)
- [共享上下文的多 Agent 协作](03-%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C/README.md)
- [不共享上下文的多 Agent 协作](04-%E4%B8%8D%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C/README.md)
- [多 Agent 协作的失败模式](05-%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C%E7%9A%84%E5%A4%B1%E8%B4%A5%E6%A8%A1%E5%BC%8F/README.md)
- [Agent 社会](06-Agent%E7%A4%BE%E4%BC%9A/README.md)
- [本章小结](07-%E6%9C%AC%E7%AB%A0%E5%B0%8F%E7%BB%93/README.md)
- [思考题](08-%E6%80%9D%E8%80%83%E9%A2%98/README.md)

---

[全书目录](../../README.md) · [上级目录](../../README.md) · [上一篇：思考题](../chapter9/05-%E6%80%9D%E8%80%83%E9%A2%98/README.md) · [下一篇：多 Agent 协作的分类框架](01-%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C%E7%9A%84%E5%88%86%E7%B1%BB%E6%A1%86%E6%9E%B6/README.md)
