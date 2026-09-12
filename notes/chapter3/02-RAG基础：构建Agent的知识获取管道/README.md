<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：隐私保护：日志脱敏](../01-%E7%94%A8%E6%88%B7%E8%AE%B0%E5%BF%86%E7%B3%BB%E7%BB%9F/08-%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%EF%BC%9A%E6%97%A5%E5%BF%97%E8%84%B1%E6%95%8F.md) · [下一篇：文档分块（Chunking）](01-%E6%96%87%E6%A1%A3%E5%88%86%E5%9D%97%EF%BC%88Chunking%EF%BC%89.md)

> 所属章节：[第3章：用户记忆和知识库](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter3.md#L243-L269) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter3/)

<!-- 原文开始 -->

<a id="rag-基础构建-agent-的知识获取管道"></a>

## RAG 基础：构建 Agent 的知识获取管道

构建共享知识库的核心技术是检索增强生成（Retrieval-Augmented Generation, RAG）。其核心思想是将大型语言模型的思考和生成能力，与外部知识库的广度和时效性相结合。模型本身的训练数据有截止日期，而知识库可以随时更新。

典型的 RAG 系统由两部分构成：检索器负责从知识库里找出相关片段，生成器（通常是 LLM）拿到这些片段作为上下文来生成答案。

先通过一个公司知识库的例子直观感受 RAG 的工作方式。用户问：“我买的东西想退款，流程是什么？”

```python
query = "退款流程"
results = retriever.search(query, top_k=2)
# results = [
# "退款政策：订单签收后7天内可申请全额退款，需提供订单号。退款将在3-5个工作日内...",
# "退款操作步骤：1.进入'我的订单' 2.选择需退款的订单 3.点击'申请退款'..."
# ]
answer = llm.generate(system="你是客服助手。", context=results, question=query)
# → "您可以在签收后7天内申请全额退款。操作步骤：进入'我的订单'→选择订单→点击'申请退款'..."
```

RAG 的核心流程是：**检索相关片段 → 注入上下文 → LLM 基于上下文生成答案**。

下面先看文档进入知识库的第一道工序——文档分块，再重点看检索器的两大技术路线：稠密嵌入和稀疏嵌入，以及如何把二者结合起来。


![图3-5 RAG 查询流程：检索、增强与生成](../../../source/book/images/fig3-5.svg)



<!-- 原文结束 -->

## 阅读目录

- [文档分块（Chunking）](01-%E6%96%87%E6%A1%A3%E5%88%86%E5%9D%97%EF%BC%88Chunking%EF%BC%89.md)
- [稠密嵌入：从词汇关联到语义理解](02-%E7%A8%A0%E5%AF%86%E5%B5%8C%E5%85%A5%EF%BC%9A%E4%BB%8E%E8%AF%8D%E6%B1%87%E5%85%B3%E8%81%94%E5%88%B0%E8%AF%AD%E4%B9%89%E7%90%86%E8%A7%A3.md)
- [稀疏嵌入：精确匹配的关键词检索](03-%E7%A8%80%E7%96%8F%E5%B5%8C%E5%85%A5%EF%BC%9A%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%E7%9A%84%E5%85%B3%E9%94%AE%E8%AF%8D%E6%A3%80%E7%B4%A2.md)
- [混合检索：两全其美的艺术](04-%E6%B7%B7%E5%90%88%E6%A3%80%E7%B4%A2%EF%BC%9A%E4%B8%A4%E5%85%A8%E5%85%B6%E7%BE%8E%E7%9A%84%E8%89%BA%E6%9C%AF.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：隐私保护：日志脱敏](../01-%E7%94%A8%E6%88%B7%E8%AE%B0%E5%BF%86%E7%B3%BB%E7%BB%9F/08-%E9%9A%90%E7%A7%81%E4%BF%9D%E6%8A%A4%EF%BC%9A%E6%97%A5%E5%BF%97%E8%84%B1%E6%95%8F.md) · [下一篇：文档分块（Chunking）](01-%E6%96%87%E6%A1%A3%E5%88%86%E5%9D%97%EF%BC%88Chunking%EF%BC%89.md)
