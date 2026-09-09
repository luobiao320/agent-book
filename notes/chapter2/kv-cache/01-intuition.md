# KV Cache 的核心直觉

> 来源章节：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache
> 本文为学习整理与重新讲解。

LLM 自回归生成时，每产生一个新 token 都需要关注历史 token。历史 token 已经计算过的 Key / Value 在后续步骤不会凭空变化，因此可以缓存并复用，避免每一步都重新编码整段历史。

可以把它理解为：**历史 K/V 是生成过程中的可复用中间状态**。Prefill 阶段先处理输入并建立缓存；Decode 阶段每次只计算新 token 的相关状态，再把新的 K/V 追加到缓存。

KV Cache 的价值主要是减少重复计算，但它不会让模型“不再看历史”。当前 Query 仍然要与历史 Key 做注意力计算。

## 一句话记忆

历史 token 的 K/V 算过一次后，后续生成尽量复用。
