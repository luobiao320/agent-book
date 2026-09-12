<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：何时选择 Mid-training、SFT 与 RL](../07-%E4%BD%95%E6%97%B6%E9%80%89%E6%8B%A9Mid-training%E3%80%81SFT%E4%B8%8ERL/README.md) · [下一篇：RL 算法：从 16 次 rollout 到一次参数更新](../09-RL%E7%AE%97%E6%B3%95%EF%BC%9A%E4%BB%8E16%E6%AC%A1rollout%E5%88%B0%E4%B8%80%E6%AC%A1%E5%8F%82%E6%95%B0%E6%9B%B4%E6%96%B0/README.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L410-L481) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="单轮强化学习记忆与泛化的对照"></a>

## 单轮强化学习：记忆与泛化的对照

“单轮” 指任务在一次交互中完成：模型接收输入、产出输出、获得奖励，无需维护跨步骤的状态。这种简化设定让我们能够聚焦于 SFT 与 RL 在学习机制上的根本差异，而不被多轮交互的复杂性干扰。单轮场景提供了清晰的对照实验条件：相同任务、相同基础模型、相同计算预算，唯一的变量是训练方法。第一个实验展示 RL 如何学会“何时该思考”这一元策略；第二个实验通过算术推理卡牌游戏系统地量化 “SFT 记忆、RL 泛化”。

在进入实验之前，先建立一点关于 RL 算法的**最小直觉**，以便理解后续实验里出现的术语。本章的 RL 训练大多基于**策略梯度**：让模型对同一个问题多生成几条回答，奖励高的回答就提高它出现的概率、奖励低的就降低——“奖励高的方向多走，奖励低的方向少走”。为抑制单次更新把模型带偏，主流的 **PPO** 算法会在概率比超出指定区间时裁掉代理目标中的额外收益；它会抑制大幅更新，但不是对策略变化的硬约束（后文实验中出现的 “带价值网络的 PPO” 即指此，价值网络用来估计基线、算出更细的优势）。另一种 **GRPO** 则不训练价值网络，而是用 “同一问题的多条回答互相比较” 来判断每条的相对好坏。记住这条直觉，就足以读懂接下来两个实验。

同一机制可以用下面的 Python 风格伪代码表示。它省略采样并行、KL 正则和优化器细节，只标出一次 rollout 到参数更新的因果链：

```python
for prompt in batch:
    group = [rollout(policy, env.reset(prompt)) for _ in range(G)]
    rewards = [verify(trajectory) for trajectory in group]
    advantages = normalize_within_group(rewards)       # GRPO baseline
    update(policy, group, advantages)
```

而 PPO 的价值网络和裁剪目标可以写成：

```python
for trajectory in rollouts:
    returns = discounted_returns(trajectory.rewards)
    values = value_model(trajectory.states)
    advantages = returns - stop_gradient(values)
    ratio = exp(policy.log_prob(trajectory.actions)
                - old_policy.log_prob(trajectory.actions))
    policy_loss = -mean(min(
        ratio * advantages,
        clip(ratio, 1 - epsilon, 1 + epsilon) * advantages
    ))
    value_loss = mean((value_model(trajectory.states) - returns) ** 2)
update(policy, value_model, policy_loss + value_coef * value_loss)
```

GRPO 的“相对”来自同一 prompt 的组内比较；PPO 中的 `old_policy` 是生成这批 rollout 时冻结的策略快照，概率比用它衡量当前策略已经移动了多远。裁剪会抑制大步更新，但不是对策略变化的硬约束；两者都仍依赖可靠环境与奖励，具体训练适配见对应实验。

> **实验 8-10 ★★：AdaptThink——学会 “何时不思考”**
>
> 大型思考模型（如 OpenAI o1、DeepSeek-R1）对所有问题都会生成冗长的思维链，在简单问题上造成不必要的开销。实验首先验证了一个直觉：**NoThinking 模式**（通过 `<think></think>` 跳过思考）在简单问题上性能相当甚至更好，只有面对困难问题时 Thinking 的优势才显现出来。
>
> AdaptThink 通过 RL 训练模型自适应地选择模式。两个核心组件：
>
> - **约束优化目标**：鼓励 NoThinking 的同时确保整体性能不下降。
> - **重要性采样策略**：平衡 Thinking/NoThinking 样本，解决初始模型几乎总选 Thinking 带来的**冷启动**问题（Cold Start，这里特指训练初期模型几乎只产生 Thinking 样本、NoThinking 分支样本极少而学不起来的问题；它与前文 DeepSeek-R1 用少量示范数据做“冷启动 SFT”是不同语境下的用法）。
>
> 这里出现的“重要性采样”是统计学常用的方法——在采样分布偏向某一类样本时，通过给样本加权来“纠正”分布，让学习信号能够公平覆盖所有类别。本书后续讨论的 PPO、DAPO 等 RL 算法都会反复用到这一思想。
>
> 本书对这次历史训练的规范记录是 checkpoint-free [训练报告](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/chapter8/AdaptThink/TRAINING_REPORT.md)。公开 W&B 主运行 [`wubbn5tj`](https://wandb.ai/bojieli-pine-ai/adapt_think_verl/runs/wubbn5tj) 使用 8×NVIDIA H100 80GB；step 0→300 时，MATH500 准确率 0.8100→0.8180（+0.80 pp）、响应长度 4911.46→1576.62（-67.90%），GSM8K 为 0.796816→0.818802（+2.20 pp）、1025.24→477.33（-53.44%），AIME mean@16 则为 0.314583→0.310417（-0.42 pp）、12119.51→6402.23（-47.17%）。对应 NoThinking 比例为 83.80%、84.15%、56.25%，说明数据集汇总层面存在与难度一致的路由信号，但不能称为逐题 “完美难度感知”，也不能声称准确率普遍提升。
>
> 在报告选取的 step 300 之后，训练继续运行到 step 410，累计耗时 36.92 小时，随后 W&B 状态变为 `crashed`；配置的 10 epochs / 3,140 steps 并未完成。Step 300 虽有 checkpoint 计时事件，但 checkpoint 不随书分发，也没有独立回执证明其经 `run_eval_verl_hf.sh` 成功评估或重跑 MMLU。历史源码提交为 `9e588202…`；未来复现固定到其直接子提交 `0033ad172…`，三个入口文件保持不变，但训练脚本生成的 `-fl-` 路径与评估脚本硬编码的 `-fl4096` 路径不兼容，需手工修正。
>
> AdaptThink 可与 Prompt 蒸馏互补，形成 “快—慢双系统”：蒸馏降低需要思考的任务比例，AdaptThink 优化剩余任务的触发策略，共同提高思考效率。

> **实验 8-11 ★★：GeneralPoints——单轮 RL 的 “记忆与泛化” 对照**
>
>
> ![图8-12 GeneralPoints 实验架构（GP-L 与 GP-VL 两个变体的训练与测试设计）](../../../source/book/images/fig8-12.svg)
>
>
> GeneralPoints 是 Chu 等人提出的算术思考卡牌游戏[^ch8-3]，专门用于评估模型的泛化能力。任务目标类似“24 点”游戏：使用四张卡牌上的数字，通过加减乘除运算，每个数字恰好用一次，凑出目标数字 24。实验设计了纯文本 GP-L 与图像 GP-VL 两个变体，使我们能在同一框架下分别考察规则泛化与视觉泛化。
>
> **规则变体**：训练时 J/Q/K 都计为 10，测试时分别计为 11/12/13，确保测试集出现训练未见的数字组合（含 11、12、13 的运算），严格评估泛化能力。**视觉变体**：训练用黑色花色（♠♣），测试用红色花色（♥♦），评估视觉外观变化下的鲁棒性。基于 Llama-3.2-Vision-11B，遵循标准后训练流程：先 SFT 初始化使其具备基本指令遵循能力，然后在相同计算预算下分别扩展 SFT 与 RL 训练（RL 部分采用带价值网络的 PPO 算法），用单一规则（J/Q/K=10）数据训练，在分布内（ID）与分布外（OOD）测试集上评估。
>
> 结果在这一受控设置中显示出明显差异。**规则 OOD**：RL 在 GP-L 上 +3.5%（11.5%→15.0%），SFT **下降** 8.1%（11.5%→3.4%）；GP-VL 上 RL +3.0%，SFT 下降 5.6%。**视觉 OOD**：RL 在 GP-VL 上 **+17.6%**（23.6%→41.2%），SFT 下降 9.9%（23.6%→13.7%）。
>
> 追踪视觉识别准确率后发现：RL 通过结果导向的优化改善了底层视觉编码器，且这种改善与整体性能提升高度相关；而 SFT 因为过度拟合思考过程中的 token 模式，忽视了对视觉 token 的学习，导致识别准确率反而下降。
>
> 实验还说明，在本实验的设定下（Llama-3.2-Vision-11B 这个量级的基础模型，加上严格的结构化输出要求），RL 需要先用 SFT 初始化：未经 SFT 直接做端到端 RL 完全失败，因为基础模型无法产生结构化输出，奖励根本无法计算。注意这是特定设定下的结论而非普适规律：足够强的基础模型可以跳过 SFT 直接 RL 成功（见前文对 DeepSeek-R1-Zero 的讨论）。另一个值得关注的发现是，在这个实验中，验证迭代次数越多，测得的泛化越好：10 次 +5.99% vs 1 次 +0.48%，表明增加测试阶段的计算量是其泛化提升的重要因素。
>
> 为什么在这个实验的分布偏移下 SFT 性能下降，而 RL 表现更好？一种与观察相符的解释是：有限的 SFT 数据强化了“遇到 J/Q/K 就当 10 用”的固定模式；测试时 J=11，模型仍按 10 计算。结果导向的 RL 分支则更可能强化“重新计算直到得到正确答案”的策略，因而在 J 变成 11 时仍能应用。这解释了本实验中的“记忆”与“泛化”对照，但不是说 SFT 必然只能记忆，或 RL 必然学会通用算法。
>
> 本实验的核心贡献，是在有限的 GeneralPoints 设置中系统量化了 SFT 的过拟合倾向与 RL 更好的分布外表现，并在纯语言和视觉—语言两个变体中观察到同一模式：SFT 稳定格式，RL 在此基础上探索策略，两者形成互补。


<!-- 原文结束 -->

<!-- 补齐本页引用的原文定义 -->

[^ch8-3]: Chu, Tianzhe et al., “SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training”, 2025. arXiv:2501.17161. https://arxiv.org/abs/2501.17161

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：何时选择 Mid-training、SFT 与 RL](../07-%E4%BD%95%E6%97%B6%E9%80%89%E6%8B%A9Mid-training%E3%80%81SFT%E4%B8%8ERL/README.md) · [下一篇：RL 算法：从 16 次 rollout 到一次参数更新](../09-RL%E7%AE%97%E6%B3%95%EF%BC%9A%E4%BB%8E16%E6%AC%A1rollout%E5%88%B0%E4%B8%80%E6%AC%A1%E5%8F%82%E6%95%B0%E6%9B%B4%E6%96%B0/README.md)
