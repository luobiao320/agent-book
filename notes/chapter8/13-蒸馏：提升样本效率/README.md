<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：结果正确还不够：路径约束与 RLVP](../12-%E5%A5%96%E5%8A%B1%E8%AE%BE%E8%AE%A1%EF%BC%9A%E5%A6%82%E4%BD%95%E6%8A%8A%E4%BB%BB%E5%8A%A1%E7%9B%AE%E6%A0%87%E5%8F%98%E6%88%90%E5%AD%A6%E4%B9%A0%E4%BF%A1%E5%8F%B7/04-%E7%BB%93%E6%9E%9C%E6%AD%A3%E7%A1%AE%E8%BF%98%E4%B8%8D%E5%A4%9F%EF%BC%9A%E8%B7%AF%E5%BE%84%E7%BA%A6%E6%9D%9F%E4%B8%8ERLVP.md) · [下一篇：在轨蒸馏：让一次 rollout 产生密集监督](01-%E5%9C%A8%E8%BD%A8%E8%92%B8%E9%A6%8F%EF%BC%9A%E8%AE%A9%E4%B8%80%E6%AC%A1rollout%E4%BA%A7%E7%94%9F%E5%AF%86%E9%9B%86%E7%9B%91%E7%9D%A3.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L670-L677) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="蒸馏提升样本效率"></a>

## 蒸馏：提升样本效率

前述实验已系统展示了 RL 在 Agent 训练中的核心价值，但都付出了高昂的样本成本。这里的“样本效率”特指：**每次昂贵的环境交互，能带来多少有效的参数更新**，而不只是训练步数或 GPU 时间。ReTool 的 RL 训练时间是 SFT 的 200 倍以上（9 天 vs 1 小时），因此减少环境采样尤其重要。

RL 样本效率低，除了高方差和在轨数据难复用，更根本的原因是反馈太稀疏。主流 model-free RL 通常只在一条 rollout 结束时得到一个成败标量，中间的错误原因、缺少字段、流程提示都没有直接的学习信号。比如客服说“需要信用卡后四位”，模型却只能从最终的 0/1 结果反复试错，可能要数百次交互才偶然学会这一步；人类听到一次就能记住。

**蒸馏则把一次 rollout 变成密集的监督信号**，不必额外探索更多环境轨迹，就能让同一条轨迹贡献大量梯度，这是蒸馏提升样本效率的关键。


<!-- 原文结束 -->

## 阅读目录

- [在轨蒸馏：让一次 rollout 产生密集监督](01-%E5%9C%A8%E8%BD%A8%E8%92%B8%E9%A6%8F%EF%BC%9A%E8%AE%A9%E4%B8%80%E6%AC%A1rollout%E4%BA%A7%E7%94%9F%E5%AF%86%E9%9B%86%E7%9B%91%E7%9D%A3.md)
- [没有更强的教师怎么办：On-Policy 自蒸馏](02-%E6%B2%A1%E6%9C%89%E6%9B%B4%E5%BC%BA%E7%9A%84%E6%95%99%E5%B8%88%E6%80%8E%E4%B9%88%E5%8A%9E%EF%BC%9AOn-Policy%E8%87%AA%E8%92%B8%E9%A6%8F.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：结果正确还不够：路径约束与 RLVP](../12-%E5%A5%96%E5%8A%B1%E8%AE%BE%E8%AE%A1%EF%BC%9A%E5%A6%82%E4%BD%95%E6%8A%8A%E4%BB%BB%E5%8A%A1%E7%9B%AE%E6%A0%87%E5%8F%98%E6%88%90%E5%AD%A6%E4%B9%A0%E4%BF%A1%E5%8F%B7/04-%E7%BB%93%E6%9E%9C%E6%AD%A3%E7%A1%AE%E8%BF%98%E4%B8%8D%E5%A4%9F%EF%BC%9A%E8%B7%AF%E5%BE%84%E7%BA%A6%E6%9D%9F%E4%B8%8ERLVP.md) · [下一篇：在轨蒸馏：让一次 rollout 产生密集监督](01-%E5%9C%A8%E8%BD%A8%E8%92%B8%E9%A6%8F%EF%BC%9A%E8%AE%A9%E4%B8%80%E6%AC%A1rollout%E4%BA%A7%E7%94%9F%E5%AF%86%E9%9B%86%E7%9B%91%E7%9D%A3.md)
