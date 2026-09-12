<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：RL 算法：从 16 次 rollout 到一次参数更新](README.md) · [下一篇：RL 环境：从评估到仿真](../10-RL%E7%8E%AF%E5%A2%83%EF%BC%9A%E4%BB%8E%E8%AF%84%E4%BC%B0%E5%88%B0%E4%BB%BF%E7%9C%9F/README.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L504-L529) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="为什么-llm-rl-通常优先-on-policy"></a>

### 为什么 LLM RL 通常优先 On-Policy

先区分两个容易混用的词。**Online（在线）**只表示数据在训练过程中不断通过与环境交互产生；**On-policy（在轨）**要求生成 rollout 的行为策略 $\mu$ 与当前要优化的策略 $\pi_\theta$ 相同或足够接近。异步集群即使持续在线生成，只要 rollout worker 落后了几个 checkpoint，数据就已经陈旧，训练在统计意义上也已经带有 off-policy（离轨）成分。回放旧轨迹、使用旧模型数据或教师完整生成的数据，则是更明显的 off-policy。本章的 PPO/GRPO 配方通常每个 step 都用最新策略重新生成 rollout，因而以近似 on-policy 为目标；PPO 在同一批数据上做多轮 minibatch 更新时，后几轮已经开始偏离生成数据的 `old_policy`，这正是它需要概率比与 clipping 的原因。

策略梯度要估计当前策略 $\pi_\theta$ 下的期望奖励。如果数据由另一个策略 $\mu$ 采样，就要用重要性比率纠正：

$$
\rho_t=\frac{\pi_\theta(a_t\mid s_t)}{\mu(a_t\mid s_t)}
=\exp\left(\log\pi_\theta(a_t\mid s_t)-\log\mu(a_t\mid s_t)\right).
$$

真正的新鲜 on-policy rollout 在**参数更新之前**应满足 $\pi_\theta=\mu$，所以 $\rho_t=1$。这使训练集中在“当前模型实际会进入的状态”，也避免为分布错位付出高方差修正。Off-policy 的优点是旧数据可复用、采样与训练可异步，吞吐量更高；代价是策略越陈旧，$\rho_t$ 的分布越重尾。对自回归长序列，严格的前缀或轨迹修正还会连乘许多 token 比率：少量偏差可能累积成极大或极小权重。PPO 的 clipping 能限制离群更新，却不能无损恢复丢失的分布覆盖；裁得太多会丢梯度，不裁又可能被少数样本主导。因此，“On-policy 更好”不是普遍定理，而是在当前 LLM 策略梯度中通常意味着**更低的分布偏差和更稳定的优化**；稳定大模型 RL 的实证研究也发现，减少策略陈旧度与训练—推理差异是代理目标有效的重要条件[^ch8-32]。


<a id="看似-on-policy为什么仍会被数值误差拖垮"></a>

#### 看似 On-Policy，为什么仍会被数值误差拖垮

大规模 LLM RL 往往用 vLLM/SGLang 一类推理引擎生成 rollout，再用 FSDP/Megatron 一类训练引擎重算 log probability 和梯度。即使两边加载同一份权重，浮点精度、归约顺序、张量并行方式、批大小、KV cache 与 fused kernel 的差异，也可能让同一 token 的 log probability 略有不同。于是更新前本应为 1 的 $\rho_t$ 已经偏离 1：系统名义上同步了权重，数值上却把 on-policy 训练变成了 off-policy。已有受控实验表明，单独存在的微小 token 级训练—推理差异就可能引发训练崩溃[^ch8-33]。

敏感性来自一个放大链条：**log probability 小误差 → 指数化的概率比偏差 → 长前缀上的累积 → clipping/优势加权改变 → 梯度方向与有效样本数改变**。例如，若 4,000 个 token 的 log ratio 都有同方向的 $10^{-3}$ 偏差，轨迹级比率会累积到 $e^4\approx54.6$；真实误差未必同号，但这个例子说明长序列为何会把“每个 token 看起来很小”的误差放大。早期 token 的微小概率差还可能改变实际采样出的 token，使后续整条状态轨迹分叉。最终表现不只是“同一提示偶尔生成不同答案”，还可能是重要性比率尖峰、大量 token 被裁剪、梯度或响应长度突变，继而奖励和熵一起坍塌。批大小改变计算归约方式、破坏数值的 batch invariance，也已被直接观察到会把本应 on-policy 的 RL 变成隐式 off-policy；使用匹配的采样—训练数值或显式 off-policy 修正都能改善稳定性[^ch8-34]。

工程上应把它当作核心问题，而不是普通的浮点噪声：

- 在**任何参数更新之前**，用同一批轨迹比较 sampler 与 trainer 的 token log probability，监控 $\rho_t$ 的均值、分位数、最大值、近似 KL 和被裁剪比例；这是最直接的 on-policy 单元测试。
- 同步的不只是权重，还包括 LoRA adapter、tokenizer、chat template、模型 revision 和位置编码配置；rollout 应保存生成时的 behavior log probability，不能事后拿当前模型冒充。
- 尽可能对齐采样与训练的精度、并行布局和关键计算内核；若不能做到，就把差异明确视作 off-policy，采用重要性修正并监控有效样本数，而不是假设 PPO clipping 会自动兜底。
- 保持 rollout 新鲜，限制每批数据上的更新轮数和异步 staleness。重用旧数据能换吞吐，但应作为经过测量的偏差—效率取舍，而不是免费的加速。


<!-- 原文结束 -->

<!-- 补齐本页引用的原文定义 -->

[^ch8-32]: Zheng, Chujie et al., “Stabilizing Reinforcement Learning with LLMs: Formulation and Practices”, 2025. arXiv:2512.01374. https://arxiv.org/abs/2512.01374

[^ch8-33]: Zhong, Tianle et al., “Diagnosing Training Inference Mismatch in LLM Reinforcement Learning”, 2026. arXiv:2605.14220. https://arxiv.org/abs/2605.14220

[^ch8-34]: He, Horace and Thinking Machines Lab, “Defeating Nondeterminism in LLM Inference”, 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：RL 算法：从 16 次 rollout 到一次参数更新](README.md) · [下一篇：RL 环境：从评估到仿真](../10-RL%E7%8E%AF%E5%A2%83%EF%BC%9A%E4%BB%8E%E8%AF%84%E4%BC%B0%E5%88%B0%E4%BB%BF%E7%9C%9F/README.md)
