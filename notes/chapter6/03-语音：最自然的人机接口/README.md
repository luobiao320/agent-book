<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：从“能接收异步消息”到“可靠处理异步任务”](../02-%E5%BC%82%E6%AD%A5%E4%B8%8E%E4%BA%8B%E4%BB%B6%E9%A9%B1%E5%8A%A8%EF%BC%9A%E5%BD%93%E4%B8%96%E7%95%8C%E4%B8%BB%E5%8A%A8%E6%89%BE%E4%B8%8A%E9%97%A8/09-%E4%BB%8E%E2%80%9C%E8%83%BD%E6%8E%A5%E6%94%B6%E5%BC%82%E6%AD%A5%E6%B6%88%E6%81%AF%E2%80%9D%E5%88%B0%E2%80%9C%E5%8F%AF%E9%9D%A0%E5%A4%84%E7%90%86%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E2%80%9D.md) · [下一篇：交互时序：从级联到全双工](01-%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%EF%BC%9A%E4%BB%8E%E7%BA%A7%E8%81%94%E5%88%B0%E5%85%A8%E5%8F%8C%E5%B7%A5.md)

> 所属章节：[第6章：交互：观察与动作空间的扩展](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter6.md#L307-L312) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter6/)

<!-- 原文开始 -->

<a id="语音最自然的人机接口"></a>

## 语音：最自然的人机接口

语音的价值不只是把文字换成声音。正常说话的速度约为打字的四倍，而且不占用双手与视线，因此它天然适合把 Agent 放进持续工作、随时可能被打断的输入输出回路。语音输入法把口述转成文字，语音 Agent 则让用户直接与 Agent 协作；两者都可以支持引言中提到的 whisper coding。

本节同时讨论两个方向：用户对 Agent 说话，以及 Agent 代替用户对外部世界说话。语音模型决定“能回答什么”，交互架构决定“能否听清、及时回应、自然换手，并在通话中完成确认和工具调用”。后文先讨论交互时序，再讨论深度思考和表达质量。


<!-- 原文结束 -->

## 阅读目录

- [交互时序：从级联到全双工](01-%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%EF%BC%9A%E4%BB%8E%E7%BA%A7%E8%81%94%E5%88%B0%E5%85%A8%E5%8F%8C%E5%B7%A5.md)
- [范式一 · 级联流水线（Cascading）](02-%E8%8C%83%E5%BC%8F%E4%B8%80%C2%B7%E7%BA%A7%E8%81%94%E6%B5%81%E6%B0%B4%E7%BA%BF%EF%BC%88Cascading%EF%BC%89.md)
- [范式二 · 端到端全模态模型（Omni）](03-%E8%8C%83%E5%BC%8F%E4%BA%8C%C2%B7%E7%AB%AF%E5%88%B0%E7%AB%AF%E5%85%A8%E6%A8%A1%E6%80%81%E6%A8%A1%E5%9E%8B%EF%BC%88Omni%EF%BC%89.md)
- [范式三 · 全双工交互模型](04-%E8%8C%83%E5%BC%8F%E4%B8%89%C2%B7%E5%85%A8%E5%8F%8C%E5%B7%A5%E4%BA%A4%E4%BA%92%E6%A8%A1%E5%9E%8B.md)
- [认知时序：实时交互与深度思考](05-%E8%AE%A4%E7%9F%A5%E6%97%B6%E5%BA%8F%EF%BC%9A%E5%AE%9E%E6%97%B6%E4%BA%A4%E4%BA%92%E4%B8%8E%E6%B7%B1%E5%BA%A6%E6%80%9D%E8%80%83.md)
- [更像人的语音合成](06-%E6%9B%B4%E5%83%8F%E4%BA%BA%E7%9A%84%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：从“能接收异步消息”到“可靠处理异步任务”](../02-%E5%BC%82%E6%AD%A5%E4%B8%8E%E4%BA%8B%E4%BB%B6%E9%A9%B1%E5%8A%A8%EF%BC%9A%E5%BD%93%E4%B8%96%E7%95%8C%E4%B8%BB%E5%8A%A8%E6%89%BE%E4%B8%8A%E9%97%A8/09-%E4%BB%8E%E2%80%9C%E8%83%BD%E6%8E%A5%E6%94%B6%E5%BC%82%E6%AD%A5%E6%B6%88%E6%81%AF%E2%80%9D%E5%88%B0%E2%80%9C%E5%8F%AF%E9%9D%A0%E5%A4%84%E7%90%86%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E2%80%9D.md) · [下一篇：交互时序：从级联到全双工](01-%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%EF%BC%9A%E4%BB%8E%E7%BA%A7%E8%81%94%E5%88%B0%E5%85%A8%E5%8F%8C%E5%B7%A5.md)
