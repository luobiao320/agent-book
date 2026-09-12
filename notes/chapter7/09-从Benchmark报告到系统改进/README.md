<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：Agent 的可观测性](../08-Agent%E7%9A%84%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/README.md) · [下一篇：读懂 Benchmark 报告：发现问题的艺术](01-%E8%AF%BB%E6%87%82Benchmark%E6%8A%A5%E5%91%8A%EF%BC%9A%E5%8F%91%E7%8E%B0%E9%97%AE%E9%A2%98%E7%9A%84%E8%89%BA%E6%9C%AF.md)

> 所属章节：[第7章：Agent 的评估](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter7.md#L718-L727) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter7/)

<!-- 原文开始 -->

<a id="从-benchmark-报告到系统改进"></a>

## 从 Benchmark 报告到系统改进

下面来看配套仓库里一次真实的 AndroidWorld 调优过程。实验只跑了 API 35 模拟器上的 4 个 Wi-Fi 设置任务，每项任务做一次配对对照。这个案例的价值不在于证明系统整体提高了多少，而在于展示如何根据一轮结果，决定下一轮只改什么。

![图7-8 Benchmark 到改进闭环](../../../source/book/images/fig7-8.svg)

从 Harness 工程的视角看，这一节本质上讲的是 Harness 迭代优化的方法论——通过评估数据定位 Harness 中的薄弱环节（上下文不足？约束缺失？验证不够？反馈不及时？），有针对性地改进，再重新评估，形成 Harness 持续进化的闭环。

在开始分析 Benchmark 报告之前，有一条容易被忽视的原则：**看到 Agent 表现下降时，应先检查评测系统本身，再动 Agent**。一个常见误区是看到分数下降就立刻修改 Agent 代码，而忽略了评测系统本身可能先出了问题——基于失真的信号调整方向，修改方向可能从一开始就是错的。评测系统常见的错误来源包括：运行环境的资源不足导致进程被杀（表现为随机失败）、验证器本身有 bug 把正确答案判为失败、测试用例与生产场景之间存在脱节。这些问题在结果数字上都跟模型退化一模一样，只有审查完整的轨迹才能区分。


<!-- 原文结束 -->

## 阅读目录

- [读懂 Benchmark 报告：发现问题的艺术](01-%E8%AF%BB%E6%87%82Benchmark%E6%8A%A5%E5%91%8A%EF%BC%9A%E5%8F%91%E7%8E%B0%E9%97%AE%E9%A2%98%E7%9A%84%E8%89%BA%E6%9C%AF.md)
- [从数据到假设：构建改进路线图](02-%E4%BB%8E%E6%95%B0%E6%8D%AE%E5%88%B0%E5%81%87%E8%AE%BE%EF%BC%9A%E6%9E%84%E5%BB%BA%E6%94%B9%E8%BF%9B%E8%B7%AF%E7%BA%BF%E5%9B%BE.md)
- [从结果到决策：数据驱动的权衡](03-%E4%BB%8E%E7%BB%93%E6%9E%9C%E5%88%B0%E5%86%B3%E7%AD%96%EF%BC%9A%E6%95%B0%E6%8D%AE%E9%A9%B1%E5%8A%A8%E7%9A%84%E6%9D%83%E8%A1%A1.md)
- [持续迭代：从第一次改进到系统演化](04-%E6%8C%81%E7%BB%AD%E8%BF%AD%E4%BB%A3%EF%BC%9A%E4%BB%8E%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%94%B9%E8%BF%9B%E5%88%B0%E7%B3%BB%E7%BB%9F%E6%BC%94%E5%8C%96.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：Agent 的可观测性](../08-Agent%E7%9A%84%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/README.md) · [下一篇：读懂 Benchmark 报告：发现问题的艺术](01-%E8%AF%BB%E6%87%82Benchmark%E6%8A%A5%E5%91%8A%EF%BC%9A%E5%8F%91%E7%8E%B0%E9%97%AE%E9%A2%98%E7%9A%84%E8%89%BA%E6%9C%AF.md)
