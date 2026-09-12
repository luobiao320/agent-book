<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../README.md) · [上级目录](../../README.md) · [上一篇：致谢](../introduction/04-%E8%87%B4%E8%B0%A2/README.md) · [下一篇：现代 Agent = LLM + 上下文 + 工具](01-%E7%8E%B0%E4%BB%A3Agent%3DLLM%2B%E4%B8%8A%E4%B8%8B%E6%96%87%2B%E5%B7%A5%E5%85%B7/README.md)

> 所属章节：[第1章：AI Agent 入门](README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter1.md#L1-L10) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter1/)

<!-- 原文开始 -->

<a id="ai-agent-入门"></a>

# AI Agent 入门

如果你用 Cursor 写过代码，看它搜索代码库、编辑多个文件、运行测试直到通过；用 Deep Research 调研过一个课题，看它反复搜索、阅读，总结出一份完整报告；用 Manus 操控浏览器帮你完成在线任务；让豆包手机助手帮你在手机上订票、发消息；或者让 Pine AI 替你打电话给运营商协商降低账单——你已经在使用 AI Agent 了。

这些产品的形态各异，但有一个共同点：它们不再是“你问一句、它答一句”的被动对话，而是能够自主规划执行步骤、调用各种工具完成任务，并根据结果不断调整策略的智能系统。AI Agent 正在成为我们与计算机交互的一种全新方式。

本章将带你从实践出发理解 AI Agent 的核心组成。我们将直接动手体验现代 Agent 的能力，理解其背后的架构原理，掌握构建 Agent 系统的设计模式与最佳实践。

> **阅读提示**：本章是全书的概念地图——它会快速引入 Agent 的核心公式、运行循环、工程框架和设计模式，为后续章节提供统一的术语和参照坐标。初次阅读时不必逐一记住所有概念，建议先建立整体印象；后续每一章都会展开讲解本章提到的某一个方面，届时可随时回来对照。


<!-- 原文结束 -->

## 阅读目录

- [现代 Agent = LLM + 上下文 + 工具](01-%E7%8E%B0%E4%BB%A3Agent%3DLLM%2B%E4%B8%8A%E4%B8%8B%E6%96%87%2B%E5%B7%A5%E5%85%B7/README.md)
- [Harness 工程：模型之外的竞争力](02-Harness%E5%B7%A5%E7%A8%8B%EF%BC%9A%E6%A8%A1%E5%9E%8B%E4%B9%8B%E5%A4%96%E7%9A%84%E7%AB%9E%E4%BA%89%E5%8A%9B/README.md)
- [贯穿全书的设计模式](03-%E8%B4%AF%E7%A9%BF%E5%85%A8%E4%B9%A6%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/README.md)

---

[全书目录](../../README.md) · [上级目录](../../README.md) · [上一篇：致谢](../introduction/04-%E8%87%B4%E8%B0%A2/README.md) · [下一篇：现代 Agent = LLM + 上下文 + 工具](01-%E7%8E%B0%E4%BB%A3Agent%3DLLM%2B%E4%B8%8A%E4%B8%8B%E6%96%87%2B%E5%B7%A5%E5%85%B7/README.md)
