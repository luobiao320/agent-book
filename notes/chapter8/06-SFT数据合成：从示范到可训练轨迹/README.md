<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：SFT（监督微调）](../05-SFT%EF%BC%88%E7%9B%91%E7%9D%A3%E5%BE%AE%E8%B0%83%EF%BC%89/README.md) · [下一篇：何时选择 Mid-training、SFT 与 RL](../07-%E4%BD%95%E6%97%B6%E9%80%89%E6%8B%A9Mid-training%E3%80%81SFT%E4%B8%8ERL/README.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L370-L385) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="sft-数据合成从示范到可训练轨迹"></a>

## SFT 数据合成：从示范到可训练轨迹

SFT 的上限首先由数据决定。实际项目很少能靠人工逐条写出足够多的示范，通常要把**少量人工种子、教师模型生成和验证器筛选**组合起来：人工示范定义格式与边界，教师模型放大规模，规则验证或人工抽检守住质量。模型自举时，可以对同一题采样多条候选，只保留验证通过的轨迹，这就是拒绝采样微调（RFT）。

合成数据的目标不是复述线上日志，而是从日志中提炼可复用的**任务结构**：用户意图、初始状态、可用工具、业务约束、常见失败方式和成功条件。去除身份信息后，为每种任务重新生成虚构人物、订单、文件和状态，放进可重置的隔离环境。这样既保留真实难点，也避免模型记住客户数据或内部凭据。

一条稳妥的流水线是：**线上数据 → 任务蓝图 → 合成任务 → 多次候选轨迹 → 任务验证与轨迹验证 → SFT 数据**。任务验证检查题目本身是否可完成、难度是否合适、参考结果是否正确；轨迹验证检查最终状态、工具调用和业务约束。能写成单元测试、数据库断言或状态差异检查的条件，优先使用确定性代码；开放式的沟通质量再由模型评价器补充，并用人工抽样校准。技能图、可执行环境和独立验证器可以进一步扩大任务覆盖并过滤无效轨迹[^ch8-12][^ch8-17][^ch8-18][^ch8-19][^ch8-20]。

同一套任务和验证设施之后还可以转成 RL 环境，但两阶段的用法不同：SFT 只保留验证通过的成功轨迹，学习稳定的格式、流程和基本动作；RL 让当前策略重新 rollout，利用环境奖励探索示范之外的路径。失败轨迹不应直接当作正确示范，可以用来构造偏好对、发现任务覆盖缺口，或补上诊断与修复后再加入训练。

数据合成的关键不是数量，而是覆盖面、多样性和准确性。训练集还应按任务模板、客户或时间段去重划分，评估集必须来自不重叠的任务类型；参考解法、隐藏测试和验证器反馈不能泄露给模型。

第七章的问题案例也可以在这里转成训练数据。以 Coding Agent “过早结束”为例，先把“准备宣称完成”的轨迹前缀截出来，再把当时的过早宣称作为 rejected，把“先运行测试、逐条核对验收条件，再下结论”作为 chosen。这类数据适合做 DPO 或决策边界示范，而不是直接当作正确的 SFT 轨迹；失败原因、适用条件和验证器应随样本保存，方便追溯和复查。实验 8-17 的 `build_preference_data.py` 提供了确定性模板和教师模型两条构造路径，训练数据与后面的评估集分开保存。这样，问题案例不只是被“记住”，还可以用来定义模型需要改进的决策边界。

本章新增的两个问题案例实验分别展示了两种不同的监督目标。中文弯引号案例先把反馈提炼成作用域敏感的文档 Skill，再用结构化合成数据做 SFT；特殊字符串案例则把 `old_string` mismatch 转成 byte-exact 复制任务，重点训练逐 token 的保真度。二者共享第七章的失败归因和训练/评估隔离协议，但采用不同的评分标准：前者测“该改才改、该留则留”，后者测“必须逐字复制”。


<!-- 原文结束 -->

<!-- 补齐本页引用的原文定义 -->

[^ch8-12]: Kulikov, Ilia, et al. *Autodata: An Agentic Data Scientist to Create High Quality Synthetic Data.* arXiv:2606.25996, 2026.

[^ch8-17]: Tan, Zelin, et al. “SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation”, 2026. arXiv:2608.02287.

[^ch8-18]: Wei, Yifan, et al. “Towards Compositional Generalization of LLMs via Skill Taxonomy Guided Data Synthesis”, 2026. arXiv:2601.03676.

[^ch8-19]: Zhu, Kaijie, et al. “TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents”, 2026. arXiv:2602.07274.

[^ch8-20]: Hua, Zhanbo, et al. “CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents”, 2026. arXiv:2606.22883.

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：SFT（监督微调）](../05-SFT%EF%BC%88%E7%9B%91%E7%9D%A3%E5%BE%AE%E8%B0%83%EF%BC%89/README.md) · [下一篇：何时选择 Mid-training、SFT 与 RL](../07-%E4%BD%95%E6%97%B6%E9%80%89%E6%8B%A9Mid-training%E3%80%81SFT%E4%B8%8ERL/README.md)
