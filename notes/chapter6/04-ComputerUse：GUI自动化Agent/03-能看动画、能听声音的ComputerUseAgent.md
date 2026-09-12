<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：视觉定位（Grounding）](02-%E8%A7%86%E8%A7%89%E5%AE%9A%E4%BD%8D%EF%BC%88Grounding%EF%BC%89.md) · [下一篇：Computer Use 的世界模型](04-ComputerUse%E7%9A%84%E4%B8%96%E7%95%8C%E6%A8%A1%E5%9E%8B.md)

> 所属章节：[第6章：交互：观察与动作空间的扩展](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter6.md#L548-L555) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter6/)

<!-- 原文开始 -->

<a id="能看动画能听声音的-computer-use-agent"></a>

### 能看动画、能听声音的 Computer Use Agent

到目前为止，Computer Use 的感知都建立在一个隐含假设上：**屏幕是静止的**——截一张图、想一步、点一下，再截下一张图。可现实里的屏幕会放视频、会弹出转瞬即逝的通知、会播放会议里的人声。一个每 3–5 秒才睁一次眼、而且完全没有耳朵的 Agent，对这些“两帧之间发生的事”既看不见也听不到。

这里真正该被重新设计的，不是“动作接口”，而是“**观察接口**”[^ch6-9]。核心思想是构建 Agent–电脑观察接口（AOI），把连续的环境观察转换成模型便于处理的离散事件。其中包括几项关键技术：第一，**屏幕关键帧截图**——用一个小模型判断屏幕是否发生了有意义的变化，只在显著变化时截图，变化频繁时每秒截图 1 次就能有不错的效果；第二，**音量门控的语音转写**，有声音时调用语音识别，把识别出的文字放入上下文，让 Agent 能够听到声音；第三，**用文字描述画面**，让模型把捕获到的屏幕截图描述成一句话，这样即使原图之后被清理出上下文，这句文字仍留在上下文里，实现了多模态交互历史压缩的效果。

[^ch6-9]: 论文见 Li, Bojie and Noah Shi. *Agent-Computer Observation Interfaces Enable Dynamic Computer Use.* arXiv:2606.29472, 2026.


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：视觉定位（Grounding）](02-%E8%A7%86%E8%A7%89%E5%AE%9A%E4%BD%8D%EF%BC%88Grounding%EF%BC%89.md) · [下一篇：Computer Use 的世界模型](04-ComputerUse%E7%9A%84%E4%B8%96%E7%95%8C%E6%A8%A1%E5%9E%8B.md)
