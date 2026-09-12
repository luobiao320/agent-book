<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：KV Cache 未必是一次性的：可编辑、可组合的“笔记”](../03-KVCache%E5%8F%8B%E5%A5%BD%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E8%AE%BE%E8%AE%A1/05-KVCache%E6%9C%AA%E5%BF%85%E6%98%AF%E4%B8%80%E6%AC%A1%E6%80%A7%E7%9A%84%EF%BC%9A%E5%8F%AF%E7%BC%96%E8%BE%91%E3%80%81%E5%8F%AF%E7%BB%84%E5%90%88%E7%9A%84%E2%80%9C%E7%AC%94%E8%AE%B0%E2%80%9D.md) · [下一篇：语气与风格：系统提示词的“人格”](01-%E8%AF%AD%E6%B0%94%E4%B8%8E%E9%A3%8E%E6%A0%BC%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E2%80%9C%E4%BA%BA%E6%A0%BC%E2%80%9D.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L594-L601) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="提示工程优化系统提示词"></a>

## 提示工程：优化系统提示词

提示工程（Prompt Engineering）的核心对象是**系统提示词（System Prompt）**——API 消息列表中那条 `role: "system"` 的消息。它是 Agent 的“员工手册”，定义了 Agent 的身份、行为规则、约束条件和工作流程。一个精心设计的系统提示词，能让模型在具体任务中充分发挥其通用能力。

系统提示词的设计有一个实用的检验标准：**如果一个聪明的新员工读完你的系统提示词还不知道该怎么做，Agent 也一样不知道。**

下面从几个维度讨论如何优化系统提示词。


<!-- 原文结束 -->

## 阅读目录

- [语气与风格：系统提示词的“人格”](01-%E8%AF%AD%E6%B0%94%E4%B8%8E%E9%A3%8E%E6%A0%BC%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E2%80%9C%E4%BA%BA%E6%A0%BC%E2%80%9D.md)
- [结构化提示：系统提示词的“格式”](02-%E7%BB%93%E6%9E%84%E5%8C%96%E6%8F%90%E7%A4%BA%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E2%80%9C%E6%A0%BC%E5%BC%8F%E2%80%9D.md)
- [流程驱动 vs 规则堆砌：系统提示词的“组织方式”](03-%E6%B5%81%E7%A8%8B%E9%A9%B1%E5%8A%A8vs%E8%A7%84%E5%88%99%E5%A0%86%E7%A0%8C%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E2%80%9C%E7%BB%84%E7%BB%87%E6%96%B9%E5%BC%8F%E2%80%9D.md)
- [业务规则细化：系统提示词的“内容”](04-%E4%B8%9A%E5%8A%A1%E8%A7%84%E5%88%99%E7%BB%86%E5%8C%96%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E2%80%9C%E5%86%85%E5%AE%B9%E2%80%9D.md)
- [Few-shot 示例：何时给模型看例子](05-Few-shot%E7%A4%BA%E4%BE%8B%EF%BC%9A%E4%BD%95%E6%97%B6%E7%BB%99%E6%A8%A1%E5%9E%8B%E7%9C%8B%E4%BE%8B%E5%AD%90.md)
- [工具定义的设计](06-%E5%B7%A5%E5%85%B7%E5%AE%9A%E4%B9%89%E7%9A%84%E8%AE%BE%E8%AE%A1.md)
- [提示注入：上下文安全的核心威胁](07-%E6%8F%90%E7%A4%BA%E6%B3%A8%E5%85%A5%EF%BC%9A%E4%B8%8A%E4%B8%8B%E6%96%87%E5%AE%89%E5%85%A8%E7%9A%84%E6%A0%B8%E5%BF%83%E5%A8%81%E8%83%81.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：KV Cache 未必是一次性的：可编辑、可组合的“笔记”](../03-KVCache%E5%8F%8B%E5%A5%BD%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E8%AE%BE%E8%AE%A1/05-KVCache%E6%9C%AA%E5%BF%85%E6%98%AF%E4%B8%80%E6%AC%A1%E6%80%A7%E7%9A%84%EF%BC%9A%E5%8F%AF%E7%BC%96%E8%BE%91%E3%80%81%E5%8F%AF%E7%BB%84%E5%90%88%E7%9A%84%E2%80%9C%E7%AC%94%E8%AE%B0%E2%80%9D.md) · [下一篇：语气与风格：系统提示词的“人格”](01-%E8%AF%AD%E6%B0%94%E4%B8%8E%E9%A3%8E%E6%A0%BC%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E2%80%9C%E4%BA%BA%E6%A0%BC%E2%80%9D.md)
