<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：提示注入：上下文安全的核心威胁](../04-%E6%8F%90%E7%A4%BA%E5%B7%A5%E7%A8%8B%EF%BC%9A%E4%BC%98%E5%8C%96%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D/07-%E6%8F%90%E7%A4%BA%E6%B3%A8%E5%85%A5%EF%BC%9A%E4%B8%8A%E4%B8%8B%E6%96%87%E5%AE%89%E5%85%A8%E7%9A%84%E6%A0%B8%E5%BF%83%E5%A8%81%E8%83%81.md) · [下一篇：Skills：领域能力的可组合单元](01-Skills%EF%BC%9A%E9%A2%86%E5%9F%9F%E8%83%BD%E5%8A%9B%E7%9A%84%E5%8F%AF%E7%BB%84%E5%90%88%E5%8D%95%E5%85%83.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L757-L767) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="动态提示词与-agent-skills"></a>

## 动态提示词与 Agent Skills

![图2-11 Skills 渐进式披露机制](../../../source/book/images/fig2-11.svg)

随着 Agent 覆盖的业务场景越来越多，系统提示词会不断膨胀——客服场景的退款规则、编程场景的代码规范、文档场景的格式要求……全部塞进一个提示词，会带来两个问题：

- **浪费 token**：大部分内容与当前任务无关
- **注意力被稀释**：上下文中无关信息过多会稀释模型对关键内容的注意力（这一问题将在后文上下文压缩策略部分以“上下文腐化”的概念详细讨论）

这就是从静态提示工程到动态提示词的自然演进：**不是把所有知识一次性塞给 Agent，而是让它按需加载**。Agent Skills 系统正是这一理念的工程化实现。


<!-- 原文结束 -->

## 阅读目录

- [Skills：领域能力的可组合单元](01-Skills%EF%BC%9A%E9%A2%86%E5%9F%9F%E8%83%BD%E5%8A%9B%E7%9A%84%E5%8F%AF%E7%BB%84%E5%90%88%E5%8D%95%E5%85%83.md)
- [如何编写一份可用的 Skill](02-%E5%A6%82%E4%BD%95%E7%BC%96%E5%86%99%E4%B8%80%E4%BB%BD%E5%8F%AF%E7%94%A8%E7%9A%84Skill.md)
- [Skills 在上下文中的位置](03-Skills%E5%9C%A8%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%E7%9A%84%E4%BD%8D%E7%BD%AE.md)
- [Skills 与工具的关系](04-Skills%E4%B8%8E%E5%B7%A5%E5%85%B7%E7%9A%84%E5%85%B3%E7%B3%BB.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：提示注入：上下文安全的核心威胁](../04-%E6%8F%90%E7%A4%BA%E5%B7%A5%E7%A8%8B%EF%BC%9A%E4%BC%98%E5%8C%96%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D/07-%E6%8F%90%E7%A4%BA%E6%B3%A8%E5%85%A5%EF%BC%9A%E4%B8%8A%E4%B8%8B%E6%96%87%E5%AE%89%E5%85%A8%E7%9A%84%E6%A0%B8%E5%BF%83%E5%A8%81%E8%83%81.md) · [下一篇：Skills：领域能力的可组合单元](01-Skills%EF%BC%9A%E9%A2%86%E5%9F%9F%E8%83%BD%E5%8A%9B%E7%9A%84%E5%8F%AF%E7%BB%84%E5%90%88%E5%8D%95%E5%85%83.md)
