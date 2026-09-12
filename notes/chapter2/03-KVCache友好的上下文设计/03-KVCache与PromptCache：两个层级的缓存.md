<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：KV Cache 的原理与约束](02-KVCache%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E7%BA%A6%E6%9D%9F.md) · [下一篇：缓存作为架构约束](04-%E7%BC%93%E5%AD%98%E4%BD%9C%E4%B8%BA%E6%9E%B6%E6%9E%84%E7%BA%A6%E6%9D%9F.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L556-L559) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="kv-cache-与-prompt-cache两个层级的缓存"></a>

### KV Cache 与 Prompt Cache：两个层级的缓存

在继续之前，需要区分两个容易混淆的概念。**KV Cache** 是模型内部的机制——在一次推理过程中，缓存已计算的 token 的键值对，避免重复计算。**Prompt Cache** 则是推理引擎的优化——在多次 API 请求之间缓存相同前缀的计算结果。两者的优化原理相似（都利用前缀不变性），但作用层级不同：KV Cache 加速单次请求内的 token 生成，Prompt Cache 减少跨请求的重复计算成本。Prompt Cache 的工作方式是：API 服务商对请求的前缀进行匹配，如果多次请求的前缀相同，就直接复用之前计算好的 KV Cache，而不需要重新计算这部分 token 的键值对。缓存读取的成本远低于首次计算，例如 Anthropic、DeepSeek、GPT-5 约为十分之一。不过各家的启用方式和计费细节差异不小，有的能自动启用，有的需要手动指定，使用时需要查询最新文档。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：KV Cache 的原理与约束](02-KVCache%E7%9A%84%E5%8E%9F%E7%90%86%E4%B8%8E%E7%BA%A6%E6%9D%9F.md) · [下一篇：缓存作为架构约束](04-%E7%BC%93%E5%AD%98%E4%BD%9C%E4%B8%BA%E6%9E%B6%E6%9E%84%E7%BA%A6%E6%9D%9F.md)
