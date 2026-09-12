<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：状态更新的两种实现与缓存代价](../06-Agent%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%9A%E9%80%9A%E8%BF%87%E5%85%83%E4%BF%A1%E6%81%AF%E5%A2%9E%E5%BC%BAAgent%E8%BD%A8%E8%BF%B9%E7%AE%A1%E7%90%86/04-%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0%E7%9A%84%E4%B8%A4%E7%A7%8D%E5%AE%9E%E7%8E%B0%E4%B8%8E%E7%BC%93%E5%AD%98%E4%BB%A3%E4%BB%B7.md) · [下一篇：为什么需要压缩：不只是长度问题](01-%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%E5%8E%8B%E7%BC%A9%EF%BC%9A%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%95%BF%E5%BA%A6%E9%97%AE%E9%A2%98.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L983-L986) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="上下文压缩策略"></a>

## 上下文压缩策略

前面几节讨论了如何往上下文里放内容——提示工程决定写什么，Skills 决定按需加载什么，Agent 状态栏决定注入什么元信息。但随着多轮交互的深入，上下文会不断膨胀。本节讨论的是相反的方向：**如何为上下文做减法**——什么时候压缩、怎么压缩、为什么即使上下文没满也应该压缩。


<!-- 原文结束 -->

## 阅读目录

- [为什么需要压缩：不只是长度问题](01-%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%E5%8E%8B%E7%BC%A9%EF%BC%9A%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%95%BF%E5%BA%A6%E9%97%AE%E9%A2%98.md)
- [上下文学习的内部机制：检索而非推理](02-%E4%B8%8A%E4%B8%8B%E6%96%87%E5%AD%A6%E4%B9%A0%E7%9A%84%E5%86%85%E9%83%A8%E6%9C%BA%E5%88%B6%EF%BC%9A%E6%A3%80%E7%B4%A2%E8%80%8C%E9%9D%9E%E6%8E%A8%E7%90%86.md)
- [压缩与 KV Cache：看似矛盾，实则互补](03-%E5%8E%8B%E7%BC%A9%E4%B8%8EKVCache%EF%BC%9A%E7%9C%8B%E4%BC%BC%E7%9F%9B%E7%9B%BE%EF%BC%8C%E5%AE%9E%E5%88%99%E4%BA%92%E8%A1%A5.md)
- [生产级的分层压缩机制](04-%E7%94%9F%E4%BA%A7%E7%BA%A7%E7%9A%84%E5%88%86%E5%B1%82%E5%8E%8B%E7%BC%A9%E6%9C%BA%E5%88%B6.md)
- [压缩策略的设计原则](05-%E5%8E%8B%E7%BC%A9%E7%AD%96%E7%95%A5%E7%9A%84%E8%AE%BE%E8%AE%A1%E5%8E%9F%E5%88%99.md)
- [隔离优于压缩：子 Agent 上下文隔离](06-%E9%9A%94%E7%A6%BB%E4%BC%98%E4%BA%8E%E5%8E%8B%E7%BC%A9%EF%BC%9A%E5%AD%90Agent%E4%B8%8A%E4%B8%8B%E6%96%87%E9%9A%94%E7%A6%BB.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：状态更新的两种实现与缓存代价](../06-Agent%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%9A%E9%80%9A%E8%BF%87%E5%85%83%E4%BF%A1%E6%81%AF%E5%A2%9E%E5%BC%BAAgent%E8%BD%A8%E8%BF%B9%E7%AE%A1%E7%90%86/04-%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0%E7%9A%84%E4%B8%A4%E7%A7%8D%E5%AE%9E%E7%8E%B0%E4%B8%8E%E7%BC%93%E5%AD%98%E4%BB%A3%E4%BB%B7.md) · [下一篇：为什么需要压缩：不只是长度问题](01-%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%E5%8E%8B%E7%BC%A9%EF%BC%9A%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%95%BF%E5%BA%A6%E9%97%AE%E9%A2%98.md)
