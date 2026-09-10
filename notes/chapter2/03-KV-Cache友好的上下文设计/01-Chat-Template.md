# 从 API 消息到模型 Token：Chat Template

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#从-api-消息到模型-tokenchat-template

## 核心结论

API 中的角色消息最终要被转换成模型真正处理的线性 token 序列。这个转换由 Chat Template 完成，不同模型家族使用不同的特殊 token 和边界格式。

## 为什么重要

- 标准 API 角色能让服务端套用模型训练时一致的模板。
- 错误地把工具结果当作 user 消息，可能破坏模型对多轮工具调用和历史思考的处理。
- KV/Prompt Cache 最终匹配的是 token 前缀，因此 Chat Template 的稳定性直接影响缓存命中。