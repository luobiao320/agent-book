<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../README.md) · [上级目录](../../README.md) · [上一篇：思考题](../chapter4/09-%E6%80%9D%E8%80%83%E9%A2%98/README.md) · [下一篇：Coding Agent](01-CodingAgent/README.md)

> 所属章节：[第5章：Coding Agent 与通用 Agent](README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter5.md#L1-L12) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter5/)

<!-- 原文开始 -->

<a id="coding-agent-与通用-agent"></a>

# Coding Agent 与通用 Agent

前面的章节分别深入讨论了上下文工程（第二、三章）和工具设计（第四章）。本章将这些构件组合在一起，回答一个核心问题：**一个能处理任意任务的通用 Agent，它的架构长什么样？**

答案是：**以开放任务为目标的通用 Agent**，其核心是一个 **Coding Agent**（能自主编写、修改和执行代码的 Agent）加上**文件系统**——Agent 用来存储代码、数据、记忆和中间结果的工作空间，类似于程序员在电脑上用文件夹管理项目的方式。从 Manus 到 OpenClaw，成功的开放任务型通用 Agent 都遵循这一范式。

为什么代码生成能担此重任？因为它不只是一个工具，而是一种**元能力**——能在运行时动态创造出新的工具和能力。本章后半部分会完整展开这一概念及其六个应用方向。

代码对 Agent 的价值体现在两个层面。**思考**上，形式化代码让思考高度严谨——“年龄大于 18 且已实名认证”用自然语言描述可能有多种理解，写成代码就毫无歧义。**表达**上，一段能跑通的代码本身就是逻辑自洽的证明，执行结果提供客观的对错标准。

本章先从 Coding Agent 的基础能力和通用 Agent 架构（OpenClaw）讲起，然后展示代码生成在各类场景中的应用——从数学思考、内容创作到系统级的元能力。


<!-- 原文结束 -->

## 阅读目录

- [Coding Agent](01-CodingAgent/README.md)
- [代码：通用 Agent 的元能力](02-%E4%BB%A3%E7%A0%81%EF%BC%9A%E9%80%9A%E7%94%A8Agent%E7%9A%84%E5%85%83%E8%83%BD%E5%8A%9B/README.md)
- [本章小结](03-%E6%9C%AC%E7%AB%A0%E5%B0%8F%E7%BB%93/README.md)
- [思考题](04-%E6%80%9D%E8%80%83%E9%A2%98/README.md)

---

[全书目录](../../README.md) · [上级目录](../../README.md) · [上一篇：思考题](../chapter4/09-%E6%80%9D%E8%80%83%E9%A2%98/README.md) · [下一篇：Coding Agent](01-CodingAgent/README.md)
