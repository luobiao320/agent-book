<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：用户记忆和知识库](../README.md) · [下一篇：记忆能力的评估：三层次框架](01-%E8%AE%B0%E5%BF%86%E8%83%BD%E5%8A%9B%E7%9A%84%E8%AF%84%E4%BC%B0%EF%BC%9A%E4%B8%89%E5%B1%82%E6%AC%A1%E6%A1%86%E6%9E%B6.md)

> 所属章节：[第3章：用户记忆和知识库](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter3.md#L15-L42) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter3/)

<!-- 原文开始 -->

<a id="用户记忆系统"></a>

## 用户记忆系统

要让 Agent 跨会话提供个性化服务，需要一层持久的用户记忆。它不保存每句对话，而是用额外的 LLM 调用提取、压缩并审查对未来有用的事实；这与只在当前窗口生效的上下文学习不同。

用一个具体的例子来理解这个过程。假设用户和 Agent 有以下对话：

```text
User: Help me book a flight to Tokyo next Friday. I prefer window seats
      and I'm vegetarian, so I'll need a special meal.
Agent: I'll search for flights to Tokyo for next Friday...
       [calls flight_search tool, returns 3 options]
Agent: Here are your options. Based on your preference, I've filtered for
       window seat availability. Shall I book the ANA direct flight?
User: Yes, and use my United MileagePlus number 12345678.
```

这段对话结束后，Agent 框架会调用一次专门的 LLM 来分析对话内容，提取出值得长期记住的信息：

```text
Extracted memories:
- User prefers window seats (preference)
- User is vegetarian, needs special meals on flights (dietary restriction)
- User's United MileagePlus number: 12345678 (loyalty program)
- User has travel plans to Tokyo (recent activity)
```

提取结果应同时满足三条规则：**选择性**（丢弃“搜索返回 3 个选项”这类短期细节）、**抽象化**（把本次“靠窗座位”归纳为长期偏好）和**结构化**（用可检索的字段保存事实）。


<!-- 原文结束 -->

## 阅读目录

- [记忆能力的评估：三层次框架](01-%E8%AE%B0%E5%BF%86%E8%83%BD%E5%8A%9B%E7%9A%84%E8%AF%84%E4%BC%B0%EF%BC%9A%E4%B8%89%E5%B1%82%E6%AC%A1%E6%A1%86%E6%9E%B6.md)
- [记忆的层次结构](02-%E8%AE%B0%E5%BF%86%E7%9A%84%E5%B1%82%E6%AC%A1%E7%BB%93%E6%9E%84.md)
- [用户记忆的四种存储格式](03-%E7%94%A8%E6%88%B7%E8%AE%B0%E5%BF%86%E7%9A%84%E5%9B%9B%E7%A7%8D%E5%AD%98%E5%82%A8%E6%A0%BC%E5%BC%8F.md)
- [进阶知识表示形态：可执行代码](04-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%86%E8%A1%A8%E7%A4%BA%E5%BD%A2%E6%80%81%EF%BC%9A%E5%8F%AF%E6%89%A7%E8%A1%8C%E4%BB%A3%E7%A0%81.md)
- [用户记忆的认知科学基础](05-%E7%94%A8%E6%88%B7%E8%AE%B0%E5%BF%86%E7%9A%84%E8%AE%A4%E7%9F%A5%E7%A7%91%E5%AD%A6%E5%9F%BA%E7%A1%80.md)
- [记忆框架案例](06-%E8%AE%B0%E5%BF%86%E6%A1%86%E6%9E%B6%E6%A1%88%E4%BE%8B.md)
- [记忆压缩与整理机制](07-%E8%AE%B0%E5%BF%86%E5%8E%8B%E7%BC%A9%E4%B8%8E%E6%95%B4%E7%90%86%E6%9C%BA%E5%88%B6.md)
- [隐私保护：日志脱敏](08-%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%EF%BC%9A%E6%97%A5%E5%BF%97%E8%84%B1%E6%95%8F.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：用户记忆和知识库](../README.md) · [下一篇：记忆能力的评估：三层次框架](01-%E8%AE%B0%E5%BF%86%E8%83%BD%E5%8A%9B%E7%9A%84%E8%AF%84%E4%BC%B0%EF%BC%9A%E4%B8%89%E5%B1%82%E6%AC%A1%E6%A1%86%E6%9E%B6.md)
