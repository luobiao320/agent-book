# KV Cache 与 Prompt Cache：两个层级的缓存

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache-与-prompt-cache两个层级的缓存

## 区别

- KV Cache：模型/推理引擎内部缓存已经处理过 token 的 K/V，主要降低单次生成过程中的重复计算。
- Prompt Cache：跨多次 API 请求复用相同前缀对应的已计算状态，减少重复 prefill。

两者都依赖“前缀稳定”，但作用层级和服务商计费方式不同。

## 工程建议

先把上下文布局设计成“稳定前缀 + 追加式轨迹”，再根据所用服务商的 Prompt Cache 规则做具体优化。