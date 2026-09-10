# 本章小结

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#本章小结

上下文工程的主线是显式管理信息：

- API 消息结构定义基本骨架。
- 稳定前缀提升 KV/Prompt Cache 命中。
- Prompt 承载长期规则。
- Skills 承载按需能力。
- 状态栏承载当前运行状态。
- 压缩提高旧历史的信息密度。
- 子 Agent 隔离从源头减少主上下文噪声。

这一章关注“一次任务内”的上下文；跨任务的用户记忆和知识库是下一章的主题。