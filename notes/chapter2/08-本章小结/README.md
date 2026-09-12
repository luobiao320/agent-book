<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：隔离优于压缩：子 Agent 上下文隔离](../07-%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8E%8B%E7%BC%A9%E7%AD%96%E7%95%A5/06-%E9%9A%94%E7%A6%BB%E4%BC%98%E4%BA%8E%E5%8E%8B%E7%BC%A9%EF%BC%9A%E5%AD%90Agent%E4%B8%8A%E4%B8%8B%E6%96%87%E9%9A%94%E7%A6%BB.md) · [下一篇：思考题](../09-%E6%80%9D%E8%80%83%E9%A2%98/README.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L1087-L1092) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="本章小结"></a>

## 本章小结

上下文工程的主线是显式管理信息：API 消息结构定义骨架；稳定前缀提高 KV Cache 命中；Prompt、Skills 和状态栏分别承载规则、按需知识与当前状态；压缩则在保留决策、约束、失败和来源的前提下，提高历史信息密度。

本章处理**一次任务之内**的状态更新与上下文腐化。下一章把同一思路扩展到跨任务的用户记忆和共享知识库。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：隔离优于压缩：子 Agent 上下文隔离](../07-%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8E%8B%E7%BC%A9%E7%AD%96%E7%95%A5/06-%E9%9A%94%E7%A6%BB%E4%BC%98%E4%BA%8E%E5%8E%8B%E7%BC%A9%EF%BC%9A%E5%AD%90Agent%E4%B8%8A%E4%B8%8B%E6%96%87%E9%9A%94%E7%A6%BB.md) · [下一篇：思考题](../09-%E6%80%9D%E8%80%83%E9%A2%98/README.md)
