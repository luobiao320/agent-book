# 02｜从 Attention 理解 Query / Key / Value

KV Cache 里的 **K** 和 **V**，来自 Transformer 的 Attention 机制。

## Q、K、V 是什么

对于每个 token，模型会通过线性变换得到三组向量：

- Query（Q）：当前 token 想找什么信息；
- Key（K）：这个 token 可以被怎样匹配；
- Value（V）：这个 token 真正携带的信息。

Attention 的简化过程可以理解为：

```text
Query 和所有历史 Key 做匹配
        ↓
得到注意力权重
        ↓
对历史 Value 加权求和
        ↓
得到当前 token 的上下文表示
```

## 为什么历史 K/V 可以缓存

当模型采用因果注意力生成文本时，过去 token 的内容不会发生变化。

例如：

```text
A B C
```

当模型已经算完 A、B、C 的 K 和 V 后，接下来生成 D 时：

- A 的 K/V 不会变；
- B 的 K/V 不会变；
- C 的 K/V 不会变；
- 只需要计算 D 自己的新表示。

因此，A/B/C 的 K/V 很适合直接缓存。

## 一个极简公式

Attention 常写成：

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d))V
```

生成新 token 时，真正变化最大的部分是当前 token 对应的 Query，以及新加入 token 的 K/V。

历史 token 对应的 K/V 可以继续复用。

## 为什么叫 KV Cache

因为缓存的不是原始文本，也不是最终输出，而是每一层 Attention 中历史 token 的 **Key 和 Value 张量**。

所以它叫：

```text
Key + Value Cache
      ↓
   KV Cache
```

## 工程视角

KV Cache 本质上是在做“用显存/内存换计算”。

优点：

- 减少重复计算；
- 降低生成延迟；
- 提升吞吐；
- 对长上下文生成尤其重要。

代价：

- 上下文越长，KV Cache 占用越大；
- 并发请求越多，缓存显存压力越明显。

因此，大模型推理系统往往需要专门优化 KV Cache 的存储和调度。
