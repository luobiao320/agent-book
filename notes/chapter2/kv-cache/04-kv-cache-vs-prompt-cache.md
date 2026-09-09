# KV Cache 与 Prompt Cache

> 来源章节：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache
> 本文为学习整理与重新讲解。

KV Cache 与 Prompt Cache 有联系，但不是同一个层级。

- **KV Cache**：主要描述一次推理/会话生成过程中，对历史 token 中间 K/V 状态的复用。
- **Prompt Cache / Prefix Cache**：服务系统尝试跨请求复用相同 Prompt 前缀已经完成的 Prefill 计算。

如果很多 Agent 请求都拥有很长、完全相同的 system prompt 和工具定义，Prefix/Prompt Cache 可以显著降低重复 Prefill 成本。要获得这种收益，前缀必须尽量稳定。

## 一句话记忆

KV Cache 偏单次生成状态复用，Prompt Cache 偏跨请求前缀复用。
