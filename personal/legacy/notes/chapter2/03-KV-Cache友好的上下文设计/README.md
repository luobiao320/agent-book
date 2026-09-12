# KV Cache 友好的上下文设计

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache-友好的上下文设计

## 三条先记住的规则

1. 稳定的 System Prompt 和核心工具定义尽量不要改。
2. 时间、状态等动态信息追加到后部，不要改写前缀。
3. 使用标准消息/API 格式，不要随意把结构化消息拼成自定义纯文本。

KV Cache 的本质是复用已经计算过的前缀状态；从首个不同 token 开始，后面的缓存需要重新计算。