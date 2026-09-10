# KV Cache 的原理与约束

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache-的原理与约束

## 核心直觉

Transformer 在生成新 token 时，要让当前 Query 与历史 token 的 Key/Value 参与注意力计算。历史 token 的 K/V 如果已经算过，就可以缓存并复用，避免每一步都把整个前缀重新前向计算。

## 关键约束

KV Cache 只能复用完全一致的前缀。从第一个发生变化的 token 起，后续位置的状态都需要重新计算。改动越靠前，通常需要重算的内容越多。

## Agent 设计含义

不要把时间戳、余额、工具调用次数等高频变化信息放进系统提示词前部；把它们放在轨迹后部，能最大化前缀复用。