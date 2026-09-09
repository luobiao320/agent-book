# KV Cache 如何工作

> 来源章节：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache
> 本文为学习整理与重新讲解。

推理可粗分为两个阶段：

1. **Prefill**：处理 system prompt、工具定义、历史消息、用户输入等已有 token，并构建这些 token 的 K/V。
2. **Decode**：逐 token 生成。每一步复用已有 K/V，只为新 token 计算并追加新的 K/V。

因此长 Prompt 首 token 延迟通常与 Prefill 有关；生成阶段的逐 token 延迟则与 Decode 和已有上下文长度有关。

KV Cache 是典型的“空间换时间”：上下文越长，需要保存的 K/V 越多，显存/内存压力越大。

## 一句话记忆

Prefill 建缓存，Decode 用缓存并追加。
