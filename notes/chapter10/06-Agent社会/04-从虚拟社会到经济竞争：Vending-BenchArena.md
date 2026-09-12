<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Moltbook：当 Agent 拥有自己的社交网络](03-Moltbook%EF%BC%9A%E5%BD%93Agent%E6%8B%A5%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%BB%9C.md) · [下一篇：Agent 经济：Pinchwork 与 RentAHuman](05-Agent%E7%BB%8F%E6%B5%8E%EF%BC%9APinchwork%E4%B8%8ERentAHuman.md)

> 所属章节：[第10章：多 Agent 协作](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter10.md#L656-L669) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter10/)

<!-- 原文开始 -->

<a id="从虚拟社会到经济竞争vending-bench-arena"></a>

### 从虚拟社会到经济竞争：Vending-Bench Arena

如果说 Smallville 展示了 Agent 社会的社交和文化维度，那么 Andon Labs 的 Vending-Bench 系列则探索了 Agent 在经济环境中的表现。作为背景，**Vending-Bench 2** 本身是一个**单 Agent** 的长程连贯性基准：一个 Agent 独自经营一项自动售货机业务长达一个模拟年——调研市场、联系供应商、订货补货、调整定价——最终以账户余额计分，考验的是 Agent 在数千轮交互中保持目标与状态连贯的能力。

在同一环境基础上，**Vending-Bench Arena** 把多个 Agent 作为竞争对手放进同一个市场：各自经营自己的售货机，争夺同一批顾客；Agent 之间可以互发邮件、转账、交易货品，既能合作也能对抗，但按各自的最终余额单独计分。每个 Agent 需要在有限资源和不确定的市场中做出一系列决策：

- **定价策略**：如何在利润率与市场占有率之间取舍，尤其是对手降价时跟不跟
- **产品组合**：如何差异化选品，避免与对手正面消耗
- **库存管理**：如何预测需求来优化补货，避免压货或断货

与传统强化学习不同，这些 Agent 不是通过数百万次试错来学习，而是像人类经营者一样，基于市场观察、竞争分析和策略推理来做决策。

竞争维度带来了单 Agent 基准中不会出现的博弈行为。实际运行中，Agent 之间爆发过互相压价的价格战；也有模型反其道而行，主动给所有竞争对手发邮件，提议统一定价、组建价格同盟，甚至有模型一边在思考过程中承认价格合谋“不道德且违法”，一边以“稳定市场”为名照做不误。显式通信并非合谋的必要条件：正如前文的 Bertrand 实验所示，公开价格也可以成为隐式信号。Agent 面对的不再是一个固定不变的环境，而是同样在动态调整策略的对手，这比单纯测试规划能力的基准更接近真实商业场景，也让“经济涌现”从比喻变成了可观测的实验现象。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Moltbook：当 Agent 拥有自己的社交网络](03-Moltbook%EF%BC%9A%E5%BD%93Agent%E6%8B%A5%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%BB%9C.md) · [下一篇：Agent 经济：Pinchwork 与 RentAHuman](05-Agent%E7%BB%8F%E6%B5%8E%EF%BC%9APinchwork%E4%B8%8ERentAHuman.md)
