<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：压缩策略的设计原则](05-%E5%8E%8B%E7%BC%A9%E7%AD%96%E7%95%A5%E7%9A%84%E8%AE%BE%E8%AE%A1%E5%8E%9F%E5%88%99.md) · [下一篇：用户记忆和知识库](../../chapter3/README.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L1079-L1086) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="隔离优于压缩子-agent-上下文隔离"></a>

### 隔离优于压缩：子 Agent 上下文隔离

压缩是在信息已经进入上下文之后做减法，而一个更釜底抽薪的思路是：让大体积的中间信息根本不进入主上下文。这就是**子 Agent 上下文隔离**——主 Agent 把 “在代码库中大范围搜索” 这类会产生海量中间内容的任务，委派给一个独立的子 Agent；子 Agent 在自己的上下文中完成探索，只把几百 token 的结论性摘要回传给主 Agent。

对比以下两种做法处理同一个任务：“在代码库中找到处理支付回调的函数”。主 Agent 亲自搜索，可能会将十几个文件中的数万 token 原始代码纳入主上下文，其中绝大部分在找到目标后就沦为永久占据窗口的噪声，还得靠后续压缩来清理。而委派给一个搜索子 Agent，主上下文只增加两条消息：一条任务描述，一条结论（“函数位于 src/payment/callbacks.py 的 handle_callback，另有两处调用点”），而中间过程的数万 token 随子 Agent 的上下文一起被丢弃。

这本质上是**用隔离代替压缩**：压缩是有损的、需要额外 LLM 调用的事后补救；隔离则让噪声从一开始就与主上下文绝缘，主 Agent 的 KV Cache 前缀也完全不受影响。代价是子 Agent 看不到主 Agent 的完整上下文，任务描述必须自包含、目标明确——这又回到了本章的主题：上下文的质量决定能力上限，对子 Agent 同样成立。Claude Code 的 Task 工具、各类深度研究（Deep Research）系统的检索子 Agent，都是这一模式的生产实现。子 Agent 作为一种协作工具的完整设计将在第四章展开，多 Agent 系统的上下文架构则是第十章的主题。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：压缩策略的设计原则](05-%E5%8E%8B%E7%BC%A9%E7%AD%96%E7%95%A5%E7%9A%84%E8%AE%BE%E8%AE%A1%E5%8E%9F%E5%88%99.md) · [下一篇：用户记忆和知识库](../../chapter3/README.md)
