<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：没有更强的教师怎么办：On-Policy 自蒸馏](../13-%E8%92%B8%E9%A6%8F%EF%BC%9A%E6%8F%90%E5%8D%87%E6%A0%B7%E6%9C%AC%E6%95%88%E7%8E%87/02-%E6%B2%A1%E6%9C%89%E6%9B%B4%E5%BC%BA%E7%9A%84%E6%95%99%E5%B8%88%E6%80%8E%E4%B9%88%E5%8A%9E%EF%BC%9AOn-Policy%E8%87%AA%E8%92%B8%E9%A6%8F.md) · [下一篇：案例 1：Coding Agent 过早结束](01-%E6%A1%88%E4%BE%8B1%EF%BC%9ACodingAgent%E8%BF%87%E6%97%A9%E7%BB%93%E6%9D%9F.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L733-L745) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="从问题案例到后训练"></a>

## 从问题案例到后训练

这一节回到第七章留下的问题：基于生产问题案例构建的评估数据集，如何真正变成后训练的输入。第七章结尾把评估环境和验证器比作后训练的基石。失败归因记录、端到端回归任务、轨迹前缀回归任务、Rubric 评分各自对应不同的训练用法：

表8-5 第七章评估数据集到第八章训练用法的映射

| 第七章的评估数据集                     | 第八章的训练用法                                             |
| -------------------------------------- | ------------------------------------------------------------ |
| 端到端回归任务（含验证器）             | RL rollout 任务与可验证奖励（RLVR）；拒绝采样（RFT）的采样池 |
| 轨迹前缀回归任务                       | DPO 偏好对、决策边界的 SFT 示范、On-Policy Distillation 的教师状态 |
| 失败归因记录（首个错误步骤与错误类别） | 过程监督的负标签（PRM）、RLVP 路径惩罚的规则来源             |
| Rubric 多维评分与人工金标集            | 向量奖励的各维度、生成式奖励模型（GRM）的训练与校准数据      |


<!-- 原文结束 -->

## 阅读目录

- [案例 1：Coding Agent 过早结束](01-%E6%A1%88%E4%BE%8B1%EF%BC%9ACodingAgent%E8%BF%87%E6%97%A9%E7%BB%93%E6%9D%9F.md)
- [案例 2：中文引号](02-%E6%A1%88%E4%BE%8B2%EF%BC%9A%E4%B8%AD%E6%96%87%E5%BC%95%E5%8F%B7.md)
- [案例 3：编辑文件经常失败](03-%E6%A1%88%E4%BE%8B3%EF%BC%9A%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6%E7%BB%8F%E5%B8%B8%E5%A4%B1%E8%B4%A5.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：没有更强的教师怎么办：On-Policy 自蒸馏](../13-%E8%92%B8%E9%A6%8F%EF%BC%9A%E6%8F%90%E5%8D%87%E6%A0%B7%E6%9C%AC%E6%95%88%E7%8E%87/02-%E6%B2%A1%E6%9C%89%E6%9B%B4%E5%BC%BA%E7%9A%84%E6%95%99%E5%B8%88%E6%80%8E%E4%B9%88%E5%8A%9E%EF%BC%9AOn-Policy%E8%87%AA%E8%92%B8%E9%A6%8F.md) · [下一篇：案例 1：Coding Agent 过早结束](01-%E6%A1%88%E4%BE%8B1%EF%BC%9ACodingAgent%E8%BF%87%E6%97%A9%E7%BB%93%E6%9D%9F.md)
