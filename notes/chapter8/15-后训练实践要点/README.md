## 后训练实践要点

这一章从预训练的“预测下一个词”出发，走了很长一段路：Mid-training 在目标分布上补知识与基础能力，SFT 高效学习格式与协议，结果导向的 RL 在本章的对照实验中改善了分布外泛化；多轮任务引入信用分配难题，奖励设计从结果奖励延伸到“奖励结果、约束过程”的路径信号，工具使用则带来组合爆炸。贯穿其中的线索只有一条——模型学到什么，取决于训练信号教了它什么；而信号的质量主要由数据和环境决定，不是由算法决定。

以下**常见陷阱**值得警惕，识别这些问题往往比掌握技术细节更能避免资源浪费：

1. **用 SFT 硬塞知识库，或把所有知识都交给参数**——大量稳定领域知识与基础能力可以用 Mid-training 写入参数，SFT 再教模型如何访问和表达；需要动态更新、引用、权限控制或删除的事实应由 RAG 管理。
2. **格式未稳定就引入 RL**——如果模型不能稳定生成奖励计算所需的 JSON，训练信号会变得稀疏或失真。可接受的解析失败率取决于任务与奖励设计，不应把固定阈值当作普遍标准；先用小规模评估设定格式稳定性门槛，必要时通过 SFT 或约束解码稳定输出后再应用 RL。
3. **把标称窗口当成有效窗口**——位置编码允许 128K 输入，不代表模型在 128K 上仍会检索、推理和规划。扩窗前应完成当前长度的能力门禁，每个阶段保留短数据和前序阶段 replay，并用“能力 × 长度”矩阵检查退化。
4. **`pass@k` 近零仍直接上 RL**——全失败的 rollout 没有正向轨迹，GRPO 组内优势也会消失。先用 Mid-training 补能力、用 SFT/蒸馏扩大有效支持，或构造与最终目标一致且可达的课程和部分奖励。
5. **奖励函数设计不当**导致奖励黑客——模型学会钻奖励的漏洞来获得高分，而非真正完成任务（比如只看回复长度就生成冗长无意义的文本）。应该评估最终目标而非中间指标。
6. **忽视仿真保真度**——若仿真过于简化（客服总按固定模式回复）或环境响应不真实（错误信息与生产环境不一致），训练出的策略在真实场景中会完全失效。高保真仿真环境的构建成本可能高于训练本身。
7. **过度训练导致泛化下降**——训练损失持续下降但验证集性能反而恶化时，模型正在死记训练细节。Mid-training 会造成通用能力遗忘，SFT 会过拟合示范，RL 过度优化也会让策略过拟合当前奖励与任务分布；三者都需要独立保留集和早停。
8. **价值函数崩溃与探索不足**——PPO 中价值估计不准确会导致优势计算出现偏差，表现为训练曲线剧烈震荡。温度参数过低或随机性不足会使 Agent 陷入局部最优。
9. **把训练—推理数值失配当成小噪声**——更新前 sampler/trainer 的概率比已经偏离 1，会把 on-policy 训练悄悄变成 off-policy。应监控 log probability 差异、近似 KL、裁剪比例和策略 staleness。
10. **低估 RL 的计算成本**——SFT 上表现良好的任务转 RL 可能需要 10-100 倍训练时间。如果测试分布与训练高度一致，SFT 可能已经足够。
11. **训练数据质量低下**——Mid-training 会吸收语料中的错误关联，SFT 会直接学习示范噪声，RL 的奖励若有系统性偏差则会把策略朝错误方向放大。

核心原则：**在投入大规模资源前，先用小规模实验验证关键假设**——小批 Mid-training 语料检查知识/能力与遗忘曲线，少量 SFT 数据测试格式能否稳定，小批 rollout 检查 `pass@k`、奖励差异和 sampler/trainer 数值一致性。快速失败比大规模失败更可接受。

**与 RAG/ICL（上下文学习）的协同**：三者不是互斥方案，而是作用于不同位置。ICL 用示例、规则和当前状态实现零参数的即时适应，但随着上下文增长，延迟与费用也会上升；RAG 把事实与证据放在可动态更新、可追溯的外部知识中；后训练则把高维感知、生成风格和隐式决策策略写入参数。选择依据不只是任务是否长期稳定，更重要的是能力能否被外部符号充分表达。医疗影像识别、自然语气等能力即使面对持续变化的领域，仍往往需要参数更新；反过来，长期稳定的转账审批规则也应由代码提供确定性保障，而不能只靠模型记忆。

稳健的系统通常组合使用这些方法：用 RAG 管理动态事实与证据，用 ICL 快速试验可用语言描述的策略，用程序固化确定性流程与硬约束，用 Mid-training 吸收稳定领域知识和基础能力，再用 SFT/RL 塑造难以由外部规则完整表达的行为。蒸馏还可以把高能力大模型的行为迁移到成本更低的小模型中。

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

## 思考题

1. ★★ 灾难性遗忘——一次针对特定任务的微调破坏了模型原有的通用能力（如通用工具调用）——在 Agent 场景下尤其棘手。相比全参微调，LoRA 冻结基座权重、遗忘风险更低，但并非免疫。有哪些策略可以进一步缓解微调带来的能力遗忘？
2. ★★ 后训练将能力固化为模型权重（“肌肉记忆”），而上下文学习将知识放在推理时的输入中。但有些能力（如领域知识）既可以通过后训练学习，也可以通过 few-shot 示例提供。你会用什么标准来决定某项能力应该走哪条路径？
3. ★★ 模型蒸馏让小模型学习大模型的行为。按能力层次，被蒸馏的模型大致可分为三级——**Chat 模型**（单轮对话、直接作答）、**Reasoning 模型**（带长链思考再作答）、**Agentic 模型**（多轮调用工具、与环境交互）。分别蒸馏这三类模型，难点有什么不同？（提示：从“要蒸馏的到底是什么”入手——是输出的风格、完整的思考轨迹，还是与环境交互的决策策略；轨迹里哪些 token 该学、哪些是环境返回的不该学；以及成败信号出现得有多晚、有多稀疏。）
4. ★★★ 在多轮 Agent 交互中，奖励的归因（credit assignment）问题比单轮更严重——一个最终的成功或失败很难归因到第 3 轮还是第 7 轮的决策。你会如何设计奖励分配策略？
5. ★★★ 如果你有固定预算（比如 $10,000），要提升一个客服 Agent 的性能，你会如何在上下文与知识、Prompt/Skills、程序约束和参数训练之间分配预算？你的决策取决于哪些因素？
6. ★★★ 让模型在没有明确奖励函数、样本稀少的情况下自主学习，被一些人认为是后训练的终极目标。当前的 RL 训练方法距离这个目标还有多远？你认为下一个突破最可能来自哪个方向？
7. ★★ 本章指出 LoRA 微调的成本并不高。那么，是否有可能给每个用户（或每个客户公司）训练一个专属的 LoRA，将用户记忆或企业知识写入参数，而非像第三章那样存储在外部知识库中？在什么场景下，“记忆写入参数” 比 “记忆存入知识库” 更有优势？又在什么场景下会适得其反？
8. ★★★ On-Policy Distillation 依赖更强的教师模型来监督学生。但 OpenAI 的 Weak-to-Strong Generalization 研究提出了一个反直觉的发现：弱模型的监督信号有时能激发强模型本身潜在但未被激活的能力。如果将这一思路应用到 Agent 训练，是否可能实现 “小模型教大模型” 的逆向蒸馏？
9. ★★ 过程奖励模型（PRM）评估每个思考步骤，而结果奖励模型（ORM）只看最终结果。但“正确的过程导致错误结果”和“错误的过程侥幸得到正确结果”哪个更值得奖励？在 Agent 的多步工具调用场景中，你会如何权衡？
10. ★★★ 本章讨论的评估数据集（如 SWE-Bench Verified、τ²-bench、AndroidWorld）既可以用于评估也可以用于后训练。但如果将评估集用于训练，它就不再是独立的评估集——这是否违反了训练集与测试集必须分离的基本原则？τ²-bench 的动态参数生成和 AndroidWorld 的参数化模板在一定程度上缓解了这个问题，但模板结构本身仍然是固定的。如何在充分利用评估数据的训练价值与维护评估独立性之间找到平衡？
11. ★★★ 面对一个目标任务，基模的 `pass@1` 很低。你会怎样联合 `pass@k`、格式解析率、部分进展率和失败归因，判断应该先做 Mid-training、SFT，还是可以直接进入 RL？这些指标达到什么条件时才值得切换阶段？
12. ★★★ ReTool 的训练动态显示（见实验 8-14），少数超长响应会显著拖长整个训练周期——一批 rollout 里绝大多数已经生成完毕，却要等那几条最长的响应收尾，其间集群的 GPU 利用率很低。如何提升这种长尾响应场景下训练集群的资源利用率？
13. ★★★ 用 LLM 模拟环境（如模拟搜索引擎、模拟用户）训练 Agent 时，Agent 钻空子的对象从 “真实环境的规则” 变成了 “模拟器本身的偏见与漏洞”。这类训练中可能出现哪些具体的 reward hacking 行为？又该如何防范？
