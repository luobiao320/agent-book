<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Agent 状态栏的构成](02-Agent%E7%8A%B6%E6%80%81%E6%A0%8F%E7%9A%84%E6%9E%84%E6%88%90.md) · [下一篇：状态更新的两种实现与缓存代价](04-%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0%E7%9A%84%E4%B8%A4%E7%A7%8D%E5%AE%9E%E7%8E%B0%E4%B8%8E%E7%BC%93%E5%AD%98%E4%BB%A3%E4%BB%B7.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L912-L942) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="agent-状态栏在上下文中的具体位置"></a>

### Agent 状态栏在上下文中的具体位置

![图2-15 Agent 状态栏在 API 消息列表中的插入位置](../../../source/book/images/fig2-15.svg)

一个重要的实现细节是：Agent 状态栏在 API 层面实际上是作为**一条 user 角色的消息**插入到上下文末尾的——而不是修改开头的 system 消息。原因正是前面讨论的 KV Cache 约束：修改 system 消息会破坏整个前缀的缓存。这里需要澄清一个容易混淆的地方：这里的 user 角色只是 API 协议层面的技术选择，并不等同于第一章定义的“来自终端用户的输入”。换句话说，Harness 是在借用 user 角色这个消息槽位，向模型注入由 Agent 框架自动生成的系统状态信息——内容并非来自真实用户，只是复用了 user 角色的消息格式来挂到上下文末尾。

以下是 Agent 框架在第 N 次 API 调用时实际构建的消息列表：

```text
messages: [
  { role: "system",    content: "You are a customer service assistant..." }  ← Fixed (KV Cache cached)
  { role: "user",      content: "Help me cancel my Xfinity plan" }  ← Original user request
  { role: "assistant", content: null, tool_calls: [...] }   ← Round 1: model decides to call
  { role: "tool",      content: "Call log..." }             ← Round 1: call result
  { role: "assistant", content: null, tool_calls: [...] }   ← Round 2: model decides to call again
  { role: "tool",      content: "Call log..." }             ← Round 2: call result
  ...(more rounds)
  { role: "user",      content: "Can you call them again to follow up?" }  ← User follow-up
  { role: "user",      content: "<agent_status>             ← Status bar injected by Agent framework
      Current State:                                           (as a user message)
      - phone_call invoked 3 times (Xfinity: 3/3 max)
      - Current time: 2025-09-14 10:30:45
      - TODO: [1] Cancel plan (in_progress)
    </agent_status>" }
]
```

注意最后一条消息：它的 role 是 `user`，但内容是 Agent 框架自动生成的元信息，用 `<agent_status>` 标签包裹以便模型识别其特殊性质。这条消息在上下文的最末尾，紧邻模型即将生成的新 token，因此能获得最高的注意力权重。同时，因为它是追加而非修改，前面所有已缓存的内容都不受影响。

这个设计正是 KV Cache 一节核心结论中“动态信息追加末尾、静态信息保持不动”原则在状态栏场景的应用。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Agent 状态栏的构成](02-Agent%E7%8A%B6%E6%80%81%E6%A0%8F%E7%9A%84%E6%9E%84%E6%88%90.md) · [下一篇：状态更新的两种实现与缓存代价](04-%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0%E7%9A%84%E4%B8%A4%E7%A7%8D%E5%AE%9E%E7%8E%B0%E4%B8%8E%E7%BC%93%E5%AD%98%E4%BB%A3%E4%BB%B7.md)
