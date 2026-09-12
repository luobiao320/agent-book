<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：全书结构](../01-%E5%85%A8%E4%B9%A6%E7%BB%93%E6%9E%84/README.md) · [下一篇：前置知识](../03-%E5%89%8D%E7%BD%AE%E7%9F%A5%E8%AF%86/README.md)

> 所属章节：[引言](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/introduction.md#L54-L76) · [在线原书](https://bojieli.github.io/ai-agent-book/book/introduction/)

<!-- 原文开始 -->

<a id="如何阅读本书"></a>

## 如何阅读本书

本书的各章节相对独立，你可以根据自己的需求选择不同的阅读路径：

- **如果你是 Agent 开发者**，建议按顺序阅读全书：第一至六章建立完整的 Agent 构建方法，第七至十章则从评估、模型后训练、持续进化和多 Agent 协作四个方向讨论能力提升。
- **如果你时间有限**，优先阅读第一章（建立全局认知）和第二章（掌握最关键的上下文工程）。第二章中 KV Cache 的底层原理较为技术化，初次阅读可先跳过原理部分、只记住开头给出的三条核心结论，不影响后续理解。
- **如果你关注模型训练**，可以直接阅读第八章（模型后训练）；其中评估方法（第七章）是训练的前提，建议一并阅读，并先读第一至二章以建立整体认知。

每章都包含大量的**实验**和**思考题**，编号格式为“实验 X-Y”（X 为章节号，Y 为章节内序号）。实验和思考题的标题中用星级标注难度：★ 表示入门级，适合所有读者；★★ 表示中等难度，需要一定的工程实践基础；★★★ 表示进阶挑战，通常涉及开放性问题或复杂的系统设计。大部分实验配有完整的可运行代码，组织在配套的开源仓库中：

> **配套代码仓库**：[https://github.com/bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

可以使用 Git 获取全部配套代码：

```bash
git clone https://github.com/bojieli/ai-agent-book.git
cd ai-agent-book
```

不熟悉 Git 的读者也可以在仓库页面点击 **Code → Download ZIP** 下载。实验代码按章节组织在 `chapter1/` 至 `chapter10/` 中；要查找“实验 X-Y”，请先打开对应的 `chapterX/README.md`，根据实验编号找到项目目录，再按照项目自身的 README 安装依赖并运行。部分标为“复现指南”的实验依赖外部仓库，具体获取方式也会在相应的 README 中说明。

我强烈建议你动手跑一遍这些实验。AI Agent 是一个实践性极强的领域，很多设计上的直觉需要在动手调试的过程中才能真正建立起来。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：全书结构](../01-%E5%85%A8%E4%B9%A6%E7%BB%93%E6%9E%84/README.md) · [下一篇：前置知识](../03-%E5%89%8D%E7%BD%AE%E7%9F%A5%E8%AF%86/README.md)
