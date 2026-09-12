<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：从仿真环境到真实机器人](../05-%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%93%8D%E4%BD%9C%EF%BC%9A%E4%BB%A5XLeRobot%E6%95%B4%E7%90%86%E6%A1%8C%E9%9D%A2%E4%B8%BA%E4%BE%8B/07-%E4%BB%8E%E4%BB%BF%E7%9C%9F%E7%8E%AF%E5%A2%83%E5%88%B0%E7%9C%9F%E5%AE%9E%E6%9C%BA%E5%99%A8%E4%BA%BA.md) · [下一篇：思考题](../07-%E6%80%9D%E8%80%83%E9%A2%98/README.md)

> 所属章节：[第6章：交互：观察与动作空间的扩展](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter6.md#L736-L762) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter6/)

<!-- 原文开始 -->

<a id="本章小结"></a>

## 本章小结

顺着**模态**和**执行时机**两根轴看，**异步与事件驱动**把观察从“Agent 主动去取”扩展为“世界主动推来”，把动作从“回合内做完”扩展为“先发起、后续靠事件收尾”，模态没变，变的只有时机。**语音**把尺度压到毫秒，级联、端到端 Omni 与全双工三种范式的演进主线，就是从“轮流说话”逐步走向持续听说，并在前台实时交互与后台深度思考之间做出分工。**Computer Use** 把同一个闭环搬到屏幕上，瓶颈已从“能否完成任务”扩展到操作效率、连续视觉理解和动作后的状态确认。**机器人**则把它推到物理世界，动作分块在平滑性与反应速度之间取舍，而最终是否完成，仍必须由新的观察来判定。

四节共享同一条控制骨架：

```text
持续感知
  → 判断当前状态与时机
  → 选择回复或动作
  → 让输出进入环境
  → 观察反馈
  → 继续、修正、重试、停止或重新规划
```

也共享同一组原语——唤醒、安全点、取消、抢占、快慢分离。

本章完成了“构建 Agent”这一部分的最后一块：观察与动作空间在内容、模态和时机三个方向上都已经展开。接下来，第七章先回答如何判断系统构建得对不对；第八章讨论如何通过后训练更新模型参数；第九章再把运行轨迹、评估与多种更新载体组织成持续进化闭环。第十章则在这个完整的单 Agent 基础上转向多 Agent 协作。

[^ch6-1]: XLeRobot, “Teleop 文档”. https://xlerobot.readthedocs.io/en/latest/software/getting_started/XLeRobot_teleop.html
[^ch6-2]: Google DeepMind, “Gemini Robotics-ER 1.5”. https://deepmind.google/models/gemini-robotics/gemini-robotics-er/；XLeRobot, “LLM Agent 控制”. https://xlerobot.readthedocs.io/en/latest/software/getting_started/LLM_agent.html 。XLeRobot 上游示例展示模型与工具调用的编排方式；本节保持同一编排原则，但把动作工具限定为经过标定的桌面抓取、放置、检查和停止原语。
[^ch6-6]: LeRobot, “Sim2Real 教程”. https://github.com/StoneT2000/lerobot-sim2real/blob/87d6c1d969f6e0ca4dc5697940804e231118a63a/docs/zero_shot_rgb_sim2real.md
[^ch6-15]: Moo Jin Kim et al. *OpenVLA: An Open-Source Vision-Language-Action Model.* arXiv:2406.09246, 2024. https://arxiv.org/abs/2406.09246
[^ch6-16]: Meta AI, “Introducing the V-JEPA 2 world model and new benchmarks for physical reasoning,” 2025-06-11. https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/；V-JEPA 2 技术报告：arXiv:2506.09985, https://arxiv.org/abs/2506.09985
[^ch6-22]: OpenAI, “[Async tool calling](https://developers.openai.com/api/docs/guides/async-tool-calling)”；“[Using GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model)”，核对日期：2026-09-05。
[^ch6-23]: OpenAI, “[Mid-turn steering](https://developers.openai.com/api/docs/guides/steering)”，核对日期：2026-09-05。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：从仿真环境到真实机器人](../05-%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%93%8D%E4%BD%9C%EF%BC%9A%E4%BB%A5XLeRobot%E6%95%B4%E7%90%86%E6%A1%8C%E9%9D%A2%E4%B8%BA%E4%BE%8B/07-%E4%BB%8E%E4%BB%BF%E7%9C%9F%E7%8E%AF%E5%A2%83%E5%88%B0%E7%9C%9F%E5%AE%9E%E6%9C%BA%E5%99%A8%E4%BA%BA.md) · [下一篇：思考题](../07-%E6%80%9D%E8%80%83%E9%A2%98/README.md)
