<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：持续迭代：从第一次改进到系统演化](../09-%E4%BB%8EBenchmark%E6%8A%A5%E5%91%8A%E5%88%B0%E7%B3%BB%E7%BB%9F%E6%94%B9%E8%BF%9B/04-%E6%8C%81%E7%BB%AD%E8%BF%AD%E4%BB%A3%EF%BC%9A%E4%BB%8E%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%94%B9%E8%BF%9B%E5%88%B0%E7%B3%BB%E7%BB%9F%E6%BC%94%E5%8C%96.md) · [下一篇：消融基础设施：理解每个特性的真实贡献](01-%E6%B6%88%E8%9E%8D%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD%EF%BC%9A%E7%90%86%E8%A7%A3%E6%AF%8F%E4%B8%AA%E7%89%B9%E6%80%A7%E7%9A%84%E7%9C%9F%E5%AE%9E%E8%B4%A1%E7%8C%AE.md)

> 所属章节：[第7章：Agent 的评估](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter7.md#L777-L780) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter7/)

<!-- 原文开始 -->

<a id="从外部评估到内部评估生产级-agent-的评估基础设施"></a>

## 从外部评估到内部评估：生产级 Agent 的评估基础设施

前面几节讨论了如何从外部评估 Agent 系统——搭建评估环境、设计数据集、分析 Benchmark 报告。但最优秀的 Agent 产品不仅接受外部评估，还**内建了持续自我评估的基础设施**。下面以第五章介绍的开源通用 Agent OpenClaw 为例，并结合头部 Coding Agent 产品的公开技术分析与从业者分享，展示一套值得借鉴的内部评估体系——它将 ML 研究中的实验方法论系统性地嵌入到了产品工程中。


<!-- 原文结束 -->

## 阅读目录

- [消融基础设施：理解每个特性的真实贡献](01-%E6%B6%88%E8%9E%8D%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD%EF%BC%9A%E7%90%86%E8%A7%A3%E6%AF%8F%E4%B8%AA%E7%89%B9%E6%80%A7%E7%9A%84%E7%9C%9F%E5%AE%9E%E8%B4%A1%E7%8C%AE.md)
- [AB 测试方法论：区分机制与目标](02-AB%E6%B5%8B%E8%AF%95%E6%96%B9%E6%B3%95%E8%AE%BA%EF%BC%9A%E5%8C%BA%E5%88%86%E6%9C%BA%E5%88%B6%E4%B8%8E%E7%9B%AE%E6%A0%87.md)
- [双层特性开关系统](03-%E5%8F%8C%E5%B1%82%E7%89%B9%E6%80%A7%E5%BC%80%E5%85%B3%E7%B3%BB%E7%BB%9F.md)
- [提示词敏感性评估](04-%E6%8F%90%E7%A4%BA%E8%AF%8D%E6%95%8F%E6%84%9F%E6%80%A7%E8%AF%84%E4%BC%B0.md)
- [以隐私感知分析为评估基础](05-%E4%BB%A5%E9%9A%90%E7%A7%81%E6%84%9F%E7%9F%A5%E5%88%86%E6%9E%90%E4%B8%BA%E8%AF%84%E4%BC%B0%E5%9F%BA%E7%A1%80.md)
- [从外部到内部：评估思维的转变](06-%E4%BB%8E%E5%A4%96%E9%83%A8%E5%88%B0%E5%86%85%E9%83%A8%EF%BC%9A%E8%AF%84%E4%BC%B0%E6%80%9D%E7%BB%B4%E7%9A%84%E8%BD%AC%E5%8F%98.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：持续迭代：从第一次改进到系统演化](../09-%E4%BB%8EBenchmark%E6%8A%A5%E5%91%8A%E5%88%B0%E7%B3%BB%E7%BB%9F%E6%94%B9%E8%BF%9B/04-%E6%8C%81%E7%BB%AD%E8%BF%AD%E4%BB%A3%EF%BC%9A%E4%BB%8E%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%94%B9%E8%BF%9B%E5%88%B0%E7%B3%BB%E7%BB%9F%E6%BC%94%E5%8C%96.md) · [下一篇：消融基础设施：理解每个特性的真实贡献](01-%E6%B6%88%E8%9E%8D%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD%EF%BC%9A%E7%90%86%E8%A7%A3%E6%AF%8F%E4%B8%AA%E7%89%B9%E6%80%A7%E7%9A%84%E7%9C%9F%E5%AE%9E%E8%B4%A1%E7%8C%AE.md)
