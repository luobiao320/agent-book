# 06｜Agent 场景下的 KV Cache 设计原则

KV Cache 不是只属于底层推理引擎的问题。Agent 的上下文组织方式，也会直接影响缓存是否容易复用。

## 原则 1：稳定内容前置

适合放在前面的通常是：

- 长期不变的 System Prompt；
- 固定安全规则；
- 固定角色设定；
- 稳定的工具定义；
- 不经常变化的输出格式约束。

这些内容越稳定，越适合作为可重复利用的公共前缀。

## 原则 2：动态内容后置

适合放在后面的通常是：

- 当前时间；
- 当前用户输入；
- 最新工具执行结果；
- 临时状态；
- 请求级 metadata；
- 当前轮新增信息。

一个理想结构可以是：

```text
[稳定 System Prompt]
[稳定规则]
[稳定 Tool Definitions]
[已有历史消息]
[最新动态状态]
[最新用户输入]
```

## 原则 3：尽量追加，而不是修改历史

Agent 的运行天然适合事件流式组织：

```text
User
 ↓
Assistant tool call
 ↓
Tool result
 ↓
Assistant
 ↓
新的 Tool result
```

如果旧消息内容不变，只在尾部不断追加，就更符合缓存复用的特点。

## 原则 4：保持序列化稳定

即使业务语义相同，下列变化也可能导致 token 序列变化：

- JSON 字段顺序变化；
- 工具顺序变化；
- 空格和模板变化；
- 不必要的格式化差异；
- 每次动态生成不同措辞的说明。

因此 Agent 框架最好让 Prompt 构建过程尽量 deterministic（确定性）。

## 原则 5：不要把所有状态都塞进 Prompt

有些状态只供程序使用，不需要模型知道，比如：

```text
traceId
数据库主键
内部重试次数
内部耗时统计
调度节点 ID
```

这些内容如果进入上下文，不但消耗 token，还可能破坏稳定前缀。

可以保留在应用层状态中，只把模型真正需要的信息传给模型。

## 原则 6：上下文压缩也要考虑稳定性

长时间运行的 Agent 最终还是会遇到上下文过长的问题，需要：

- 截断；
- 摘要；
- 外部记忆；
- RAG；
- checkpoint。

但不要每一轮都重新摘要整段历史，因为这会持续改写旧前缀。

更合理的方法通常是分段固化：

```text
[稳定摘要 checkpoint]
[checkpoint 之后的原始消息，持续追加]
```

到达新的阈值后，再生成下一份 checkpoint。

## 一个推荐的 Agent 上下文模板

```text
1. System Prompt          ← 最稳定
2. Safety / Policy
3. Tool Definitions
4. Memory Checkpoint
5. Conversation History
6. Recent Tool Results
7. Runtime State          ← 动态
8. Current User Message   ← 最动态
```

这不是绝对规则，但提供了一个重要方向：

> **越稳定、越可复用的内容越靠前；越动态、越请求级的内容越靠后。**

## 最后总结

从 Agent 工程角度看，KV Cache 友好的上下文设计可以浓缩成四句话：

1. **固定前缀。**
2. **动态后置。**
3. **历史追加。**
4. **减少无意义变化。**

当 Agent 的 System Prompt、工具定义和历史前缀很长时，这些设计习惯可能对整体推理延迟和成本产生非常明显的影响。

---

原章节：
https://bojieli.github.io/ai-agent-book/book/chapter2/#kv-cache
