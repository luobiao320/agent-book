<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：工具的分类](../01-%E5%B7%A5%E5%85%B7%E7%9A%84%E5%88%86%E7%B1%BB/README.md) · [下一篇：能力的表达形式：专用工具、通用执行器与 Skill](01-%E8%83%BD%E5%8A%9B%E7%9A%84%E8%A1%A8%E8%BE%BE%E5%BD%A2%E5%BC%8F%EF%BC%9A%E4%B8%93%E7%94%A8%E5%B7%A5%E5%85%B7%E3%80%81%E9%80%9A%E7%94%A8%E6%89%A7%E8%A1%8C%E5%99%A8%E4%B8%8ESkill.md)

> 所属章节：[第4章：工具](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter4.md#L34-L37) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter4/)

<!-- 原文开始 -->

<a id="工具设计的通用原则"></a>

## 工具设计的通用原则

工具设计的早期形态是直接的 API 封装——把每个 API 端点包成一个工具，粒度过细，Agent 往往要协调好几个工具才能完成一个目标。今天更成熟的思路被称为 **ACI**（Agent-Computer Interface）：工具应该对应 Agent 的**目标**，而不是底层的 API 操作。ACI 是对标 HCI（人机交互界面）提出的概念——如果说 HCI 研究的是人如何与计算机交互，ACI 研究的就是 Agent 如何与计算机交互，核心是让工具对 Agent 而非对人友好。本节的三条原则——能力用什么形式表达、工具怎么描述、参数如何忠实传递——都是 ACI 的具体展开。


<!-- 原文结束 -->

## 阅读目录

- [能力的表达形式：专用工具、通用执行器与 Skill](01-%E8%83%BD%E5%8A%9B%E7%9A%84%E8%A1%A8%E8%BE%BE%E5%BD%A2%E5%BC%8F%EF%BC%9A%E4%B8%93%E7%94%A8%E5%B7%A5%E5%85%B7%E3%80%81%E9%80%9A%E7%94%A8%E6%89%A7%E8%A1%8C%E5%99%A8%E4%B8%8ESkill.md)
- [工具描述的艺术](02-%E5%B7%A5%E5%85%B7%E6%8F%8F%E8%BF%B0%E7%9A%84%E8%89%BA%E6%9C%AF.md)
- [参数传递的保真性](03-%E5%8F%82%E6%95%B0%E4%BC%A0%E9%80%92%E7%9A%84%E4%BF%9D%E7%9C%9F%E6%80%A7.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：工具的分类](../01-%E5%B7%A5%E5%85%B7%E7%9A%84%E5%88%86%E7%B1%BB/README.md) · [下一篇：能力的表达形式：专用工具、通用执行器与 Skill](01-%E8%83%BD%E5%8A%9B%E7%9A%84%E8%A1%A8%E8%BE%BE%E5%BD%A2%E5%BC%8F%EF%BC%9A%E4%B8%93%E7%94%A8%E5%B7%A5%E5%85%B7%E3%80%81%E9%80%9A%E7%94%A8%E6%89%A7%E8%A1%8C%E5%99%A8%E4%B8%8ESkill.md)
