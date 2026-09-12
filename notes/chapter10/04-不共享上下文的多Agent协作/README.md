<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：共享上下文的多 Agent 协作](../03-%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C/README.md) · [下一篇：Agent 眼中的文件系统](01-Agent%E7%9C%BC%E4%B8%AD%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.md)

> 所属章节：[第10章：多 Agent 协作](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter10.md#L102-L132) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter10/)

<!-- 原文开始 -->

<a id="不共享上下文的多-agent-协作"></a>

## 不共享上下文的多 Agent 协作

不共享上下文代表真正的多 Agent 协作。在这种架构下，每个 Agent 都是独立的实体，拥有自己的上下文、轨迹和状态；彼此无法直接访问对方的 “内心活动”，协作完全依赖本章开头介绍的三种通信机制（工具调用参数、共享文件系统、消息总线）。

沿着开头那条“通信机制即进程间通信”的线索再往前走一步，会发现多 Agent 系统与操作系统的对应关系相当完整（表10-2）：

表10-2 多 Agent 系统与操作系统的对应关系

| 操作系统 | 多 Agent 系统 |
|----------|----------------|
| 程序（可执行文件） | 静态前缀（系统提示词 + 工具定义） |
| 进程的内存 | 轨迹 |
| CPU | LLM |
| 内核 | Agent 运行时 |
| 系统调用 | 工具调用 |
| fork（创建子进程） | spawn_subagent |
| kill（发送信号） | cancel_subagent |
| ps（列出进程） | list_agents |
| 退出码与 wait() | 子 Agent 返回的结构化摘要 |
| 共享内存 / 消息传递 | 共享文件系统 / 消息 |

这套抽象并不新鲜：私有状态、异步消息、可创建新成员，正是 1970 年代 Actor 模型的基本设定[^actor-model]，多 Agent 系统不妨看作它的 LLM 版本。因此操作系统与分布式系统的成熟经验大多可以直接借用。

[^actor-model]: Hewitt, C., Bishop, P., Steiger, R. *A Universal Modular ACTOR Formalism for Artificial Intelligence.* IJCAI 1973.

进程式的隔离带来了几个切实的工程好处：每个 Agent 可以独立开发和测试，新增能力不需要改动现有代码，某个 Agent 出了故障也不会把错误状态传染给其他 Agent，而且多个 Agent 可以真正并发执行——上下文完全独立，不存在资源竞争。

但不共享上下文也有代价。最明显的是信息同步问题：各 Agent 如何对任务状态保持一致的理解？信息在传递过程中会不会丢失或重复？调试也变得更加困难——出了问题需要翻看多个 Agent 的日志，才能拼出完整的执行过程。这些问题使得接口规范、数据格式和通信协议的设计变得至关重要。

不共享上下文的显式协作依赖两套与拓扑无关的基础设施。其一是**共享文件系统**，作为 Agent 间交换产物、与用户交换文件的持久媒介，构成协作的数据平面；其二是**通信与控制机制**，支持 Agent 间的消息传递、状态查询、执行终止与资源调度，构成协作的控制平面。


<!-- 原文结束 -->

## 阅读目录

- [Agent 眼中的文件系统](01-Agent%E7%9C%BC%E4%B8%AD%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.md)
- [Agent 间的通信与控制](02-Agent%E9%97%B4%E7%9A%84%E9%80%9A%E4%BF%A1%E4%B8%8E%E6%8E%A7%E5%88%B6.md)
- [对等协作模式：相互制衡与迭代改进](03-%E5%AF%B9%E7%AD%89%E5%8D%8F%E4%BD%9C%E6%A8%A1%E5%BC%8F%EF%BC%9A%E7%9B%B8%E4%BA%92%E5%88%B6%E8%A1%A1%E4%B8%8E%E8%BF%AD%E4%BB%A3%E6%94%B9%E8%BF%9B.md)
- [管理者模式：中心化协调](04-%E7%AE%A1%E7%90%86%E8%80%85%E6%A8%A1%E5%BC%8F%EF%BC%9A%E4%B8%AD%E5%BF%83%E5%8C%96%E5%8D%8F%E8%B0%83.md)
- [去中心化模式](05-%E5%8E%BB%E4%B8%AD%E5%BF%83%E5%8C%96%E6%A8%A1%E5%BC%8F.md)
- [跨组织协作：A2A 协议](06-%E8%B7%A8%E7%BB%84%E7%BB%87%E5%8D%8F%E4%BD%9C%EF%BC%9AA2A%E5%8D%8F%E8%AE%AE.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：共享上下文的多 Agent 协作](../03-%E5%85%B1%E4%BA%AB%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E5%A4%9AAgent%E5%8D%8F%E4%BD%9C/README.md) · [下一篇：Agent 眼中的文件系统](01-Agent%E7%9C%BC%E4%B8%AD%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.md)
