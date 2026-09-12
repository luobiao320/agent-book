<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：上下文：决定 Agent 能力上限的关键](../01-%E4%B8%8A%E4%B8%8B%E6%96%87%EF%BC%9A%E5%86%B3%E5%AE%9AAgent%E8%83%BD%E5%8A%9B%E4%B8%8A%E9%99%90%E7%9A%84%E5%85%B3%E9%94%AE/README.md) · [下一篇：消息的四种角色](01-%E6%B6%88%E6%81%AF%E7%9A%84%E5%9B%9B%E7%A7%8D%E8%A7%92%E8%89%B2.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L41-L44) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="agent-如何调用大模型理解-api-的上下文结构"></a>

## Agent 如何调用大模型：理解 API 的上下文结构

本节以 OpenAI 的 Chat Completions API 为例（Anthropic、Google 等厂商的 API 结构大同小异），详细拆解 Agent 每次调用大模型时的完整请求构成。理解这个结构，是掌握后续所有上下文工程技术的基础。


<!-- 原文结束 -->

## 阅读目录

- [消息的四种角色](01-%E6%B6%88%E6%81%AF%E7%9A%84%E5%9B%9B%E7%A7%8D%E8%A7%92%E8%89%B2.md)
- [单轮对话：最简单的 API 调用](02-%E5%8D%95%E8%BD%AE%E5%AF%B9%E8%AF%9D%EF%BC%9A%E6%9C%80%E7%AE%80%E5%8D%95%E7%9A%84API%E8%B0%83%E7%94%A8.md)
- [带工具调用的多轮交互：Agent 的核心循环](03-%E5%B8%A6%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8%E7%9A%84%E5%A4%9A%E8%BD%AE%E4%BA%A4%E4%BA%92%EF%BC%9AAgent%E7%9A%84%E6%A0%B8%E5%BF%83%E5%BE%AA%E7%8E%AF.md)
- [用代码实现 Agent 的核心循环](04-%E7%94%A8%E4%BB%A3%E7%A0%81%E5%AE%9E%E7%8E%B0Agent%E7%9A%84%E6%A0%B8%E5%BF%83%E5%BE%AA%E7%8E%AF.md)
- [从 API 视角看上下文的构成](05-%E4%BB%8EAPI%E8%A7%86%E8%A7%92%E7%9C%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E6%9E%84%E6%88%90.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：上下文：决定 Agent 能力上限的关键](../01-%E4%B8%8A%E4%B8%8B%E6%96%87%EF%BC%9A%E5%86%B3%E5%AE%9AAgent%E8%83%BD%E5%8A%9B%E4%B8%8A%E9%99%90%E7%9A%84%E5%85%B3%E9%94%AE/README.md) · [下一篇：消息的四种角色](01-%E6%B6%88%E6%81%AF%E7%9A%84%E5%9B%9B%E7%A7%8D%E8%A7%92%E8%89%B2.md)
