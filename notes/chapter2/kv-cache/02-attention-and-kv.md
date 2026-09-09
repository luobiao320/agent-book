# 从 Attention 理解 Q / K / V

> 来源章节：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache
> 本文为学习整理与重新讲解。

Attention 可以用“检索”来建立直觉：Query 表示当前正在找什么，Key 表示历史信息的匹配特征，Value 表示匹配后真正取回的内容。

历史 token 一旦确定，它们在各层中形成的 K/V 可以被后续生成复用；而当前 token 的 Query 随生成位置变化，所以缓存重点自然落在 K/V。

要避免一个误解：KV Cache 缓存的不是“最终答案”或自然语言片段，而是 Transformer 注意力层内部的中间张量。

## 一句话记忆

Q 是当前查询，历史 K/V 是可复用的检索索引与内容。
