<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：从 Benchmark 报告到系统改进](README.md) · [下一篇：从数据到假设：构建改进路线图](02-%E4%BB%8E%E6%95%B0%E6%8D%AE%E5%88%B0%E5%81%87%E8%AE%BE%EF%BC%9A%E6%9E%84%E5%BB%BA%E6%94%B9%E8%BF%9B%E8%B7%AF%E7%BA%BF%E5%9B%BE.md)

> 所属章节：[第7章：Agent 的评估](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter7.md#L728-L733) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter7/)

<!-- 原文开始 -->

<a id="读懂-benchmark-报告发现问题的艺术"></a>

### 读懂 Benchmark 报告：发现问题的艺术

最初的报告记录了 116 项任务各跑一次的结果，总成功率约为 88%。但失败并不是零星散落的：四项 `SystemWifiTurn*` 任务里有三项失败，轨迹中还反复出现来回导航、无法确认最终状态等现象。这里至少有两种解释：可能是 Agent 不知道设置入口，也可能是它拿到的界面信息不完整。

如果只盯着 88% 这个总分，这个小而集中的失败簇很容易被忽略；如果只是增加最大步数，又可能把“看不见界面”误当成“不够耐心”。所以，读报告时应先找失败集中在哪些任务和能力上，再回放轨迹，分清问题出在看、想、做还是验。本例先把范围缩到四项 Wi-Fi 任务，目的只是用较低成本判断病因，不是估算系统的整体水平。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：从 Benchmark 报告到系统改进](README.md) · [下一篇：从数据到假设：构建改进路线图](02-%E4%BB%8E%E6%95%B0%E6%8D%AE%E5%88%B0%E5%81%87%E8%AE%BE%EF%BC%9A%E6%9E%84%E5%BB%BA%E6%94%B9%E8%BF%9B%E8%B7%AF%E7%BA%BF%E5%9B%BE.md)
