<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：后训练实践要点](../15-%E5%90%8E%E8%AE%AD%E7%BB%83%E5%AE%9E%E8%B7%B5%E8%A6%81%E7%82%B9/README.md) · [下一篇：思考题](../17-%E6%80%9D%E8%80%83%E9%A2%98/README.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L820-L863) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="本章小结"></a>

## 本章小结

Mid-training、SFT 和 RL 不是三种可互换的“微调力度”，而是分别处理**底座、协议与策略**。Mid-training 还应通过长度课程、混合数据和逐级门禁，把标称上下文扩展变成不遗忘短程能力的有效上下文。如果合理采样下 `pass@k` 仍接近零，先用 Mid-training 补知识与能力；如果模型偶尔会做却输出不可解析，先用 SFT 稳定格式；只有当当前策略能产生可评分且有奖励差异的轨迹时，RL 才能高效地重新分配概率并探索策略。“SFT 记忆、RL 泛化”概括的是本章受控实验中观察到的倾向，并不是不受数据、模型、奖励与环境影响的普遍规律。

还有两条贯穿全章、比任何算法都值得记住的判断。其一，**数据和环境比算法更重要**：Mid-training 语料决定底座补到了哪里，SFT 示范决定协议是否稳定，环境和奖励决定 RL 能探索并强化什么。造不出真实环境时，用模型模拟环境（合成工具返回值、仿真环境动态）也是一条可行路线，但模拟器的偏差就是训练的天花板。很多场景下，只要底座和示范数据到位，甚至不需要做 RL。

其二，**当前 RL 的主要瓶颈是样本效率与分布一致性**：On-Policy Distillation 把一条 rollout 的终点标量扩展为学生实际状态上的逐 token 监督，RLVP 把被浪费的环境反馈变成可学习信号；真正 on-policy 的 rollout 又减少了重要性修正的偏差与方差。训练—推理数值失配会破坏这个前提，因此 sampler/trainer 一致性应与奖励曲线同等重要。

本章回答了怎样通过更新模型参数来实现 Agent 持续进化的问题。下一章我们将看到，参数只是知识、指令、程序与参数四种 Agent 自我进化的载体之一。

[^ch8-1]: Schulman, John and Thinking Machines Lab, “LoRA Without Regret”, 2025.
[^ch8-2]: 姚顺雨（Shunyu Yao），“The Second Half”，2025 年 4 月 10 日。https://ysymyth.github.io/The-Second-Half/
[^ch8-3]: Chu, Tianzhe et al., “SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training”, 2025. arXiv:2501.17161. https://arxiv.org/abs/2501.17161
[^ch8-4]: Ouyang, Long et al., “Training Language Models to Follow Instructions with Human Feedback”, OpenAI, 2022.
[^ch8-5]: Gao, Leo, John Schulman, and Jacob Hilton, “Scaling Laws for Reward Model Overoptimization”, OpenAI, 2023.
[^ch8-6]: Rafailov, Rafael et al., “Direct Preference Optimization: Your Language Model is Secretly a Reward Model”, 2023.
[^ch8-7]: Lightman, Hunter et al., “Let's Verify Step by Step”, OpenAI, 2023.
[^ch8-8]: Silver, David and Richard S. Sutton, “Welcome to the Era of Experience”, 2025.
[^ch8-9]: Li, Bojie, and Noah Shi, “RLVP: Penalize the Path, Reward the Outcome”, 2026. arXiv:2607.07435. https://arxiv.org/abs/2607.07435
[^ch8-10]: Thinking Machines Lab, “On-Policy Distillation”, 2025. https://thinkingmachines.ai/blog/on-policy-distillation/
[^ch8-11]: Li, Bojie, and Noah Shi, “Agents That Sense Physical Time: Urgency, Persistence, and Vigilance as Missing Controls for LLM Agents”, 2026. https://01.me/research/physical-time-agent
[^ch8-12]: Kulikov, Ilia, et al. *Autodata: An Agentic Data Scientist to Create High Quality Synthetic Data.* arXiv:2606.25996, 2026.
[^ch8-13]: Sun, Hao, et al. “ZeroSearch: Incentivize the Search Capability of LLMs without Searching”, 2025. arXiv:2505.04588.
[^ch8-14]: “DreamGym: Scaling Agent Learning via Experience Synthesis”, 2025. arXiv:2511.01824.
[^ch8-15]: Zhao, Siyan, et al. “Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models”, 2026. arXiv:2601.18734.
[^ch8-16]: Shen, Ziqi, et al. “Purified OPSD: On-Policy Self-Distillation Without Losing How to Think”, 2026. arXiv:2607.02234.
[^ch8-17]: Tan, Zelin, et al. “SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation”, 2026. arXiv:2608.02287.
[^ch8-18]: Wei, Yifan, et al. “Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis”, 2026. arXiv:2601.03676.
[^ch8-19]: Zhu, Kaijie, et al. “TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents”, 2026. arXiv:2602.07274.
[^ch8-20]: Hua, Zhanbo, et al. “CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents”, 2026. arXiv:2606.22883.
[^ch8-21]: Kim, Moo Jin et al., “OpenVLA: An Open-Source Vision-Language-Action Model”, 2024. arXiv:2406.09246. https://arxiv.org/abs/2406.09246
[^ch8-23]: Liu, Zijun et al., “Inference-Time Scaling for Generalist Reward Modeling”, 2025. arXiv:2504.02495. https://arxiv.org/abs/2504.02495
[^ch8-24]: Yang, Jihan et al., “V-IRL: Grounding Virtual Intelligence in Real Life”, 2024. arXiv:2402.03310. https://arxiv.org/abs/2402.03310
[^ch8-25]: Jin, Bowen et al., “Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning”, 2025. arXiv:2503.09516. https://arxiv.org/abs/2503.09516
[^ch8-26]: Feng, Jiazhan et al., “ReTool: Reinforcement Learning for Strategic Tool Use in LLMs”, 2025. arXiv:2504.11536. https://arxiv.org/abs/2504.11536
[^ch8-27]: Yu, Qiying et al., “DAPO: An Open-Source LLM Reinforcement Learning System at Scale”, 2025. arXiv:2503.14476. https://arxiv.org/abs/2503.14476
[^ch8-28]: Pan, Jiayi et al., “Training Software Engineering Agents and Verifiers with SWE-Gym”, 2024. arXiv:2412.21139；Barres, Victor et al., “$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment”, 2025. arXiv:2506.07982；Rawles, Christopher et al., “AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents”, 2024. arXiv:2405.14573.
[^ch8-29]: storm, “长程智能体自我检查与早停行为：Reward Seeking 现象及其缓解措施”，青稞社区，2026 年 8 月 6 日。https://qingkeai.online/archives/Reward-Seeking；原文链接：https://zhuanlan.zhihu.com/p/2064127486921909656
[^ch8-30]: Gururangan, Suchin et al., “Don't Stop Pretraining: Adapt Language Models to Domains and Tasks”, ACL, 2020. https://aclanthology.org/2020.acl-main.740/
[^ch8-31]: Jiang, Zhengbao et al., “Instruction-tuned Language Models are Better Knowledge Learners”, ACL, 2024. https://aclanthology.org/2024.acl-long.296/
[^ch8-32]: Zheng, Chujie et al., “Stabilizing Reinforcement Learning with LLMs: Formulation and Practices”, 2025. arXiv:2512.01374. https://arxiv.org/abs/2512.01374
[^ch8-33]: Zhong, Tianle et al., “Diagnosing Training Inference Mismatch in LLM Reinforcement Learning”, 2026. arXiv:2605.14220. https://arxiv.org/abs/2605.14220
[^ch8-34]: He, Horace and Thinking Machines Lab, “Defeating Nondeterminism in LLM Inference”, 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：后训练实践要点](../15-%E5%90%8E%E8%AE%AD%E7%BB%83%E5%AE%9E%E8%B7%B5%E8%A6%81%E7%82%B9/README.md) · [下一篇：思考题](../17-%E6%80%9D%E8%80%83%E9%A2%98/README.md)
