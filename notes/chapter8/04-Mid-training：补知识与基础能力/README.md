<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：模型预训练基础 \[可选阅读\]](../03-%E6%A8%A1%E5%9E%8B%E9%A2%84%E8%AE%AD%E7%BB%83%E5%9F%BA%E7%A1%80%5B%E5%8F%AF%E9%80%89%E9%98%85%E8%AF%BB%5D/README.md) · [下一篇：Mid-training 数据如何构造](01-Mid-training%E6%95%B0%E6%8D%AE%E5%A6%82%E4%BD%95%E6%9E%84%E9%80%A0.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L276-L286) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="mid-training补知识与基础能力"></a>

## Mid-training：补知识与基础能力

本章所说的 **Mid-training**，是指从已有基础模型出发，在目标数据分布上继续开展一个阶段的语言模型训练。它通常仍采用与预训练相同的预测下一个词任务，对文档、代码或推导的全部 token 计算损失。经典的 DAPT/TAPT 研究已经表明，在领域语料或任务相关的无标注语料上做第二阶段预训练，可以继续改善下游任务表现[^ch8-30]。名称里的 “Mid” 描述的是它在能力开发流水线中的位置，其数据格式和损失函数与预训练相同。

Mid-training 主要解决两类缺口：

- **知识缺口**：通用预训练没有充分覆盖目标语言、金融/医疗/法律领域、企业内部文档或某类代码库，模型连概念与术语都不能理解。
- **基础能力缺口**：目标任务要求基础模型尚未形成的长上下文、代码模式、数学推导或跨模态表征。此时不只是回答格式不对，而是模型在足够多次采样下也几乎得不到正确解。

这也说明为什么不应把 SFT 当成主要的知识注入工具。SFT 当然可以记住少量事实，也常被放在 Mid-training 之后教模型如何回答领域问题；但少量 QA 对只覆盖有限问法，更擅长训练“如何访问与表达”，不适合承载大规模、相互关联的原始知识。反过来，Mid-training 降低了领域文本的语言模型损失，也不保证模型会自动按用户问题取出知识；已有研究发现，继续预训练与指令训练的顺序和数据组织会显著影响知识能否被问答形式访问[^ch8-31]。稳健配方通常是 Mid-training 吸收知识与能力 → 小规模 SFT 建立输出格式 → 有非零成功率后再 RL 提升成功率和泛化性。


<!-- 原文结束 -->

## 阅读目录

- [Mid-training 数据如何构造](01-Mid-training%E6%95%B0%E6%8D%AE%E5%A6%82%E4%BD%95%E6%9E%84%E9%80%A0.md)

<!-- 补齐本页引用的原文定义 -->

[^ch8-30]: Gururangan, Suchin et al., “Don't Stop Pretraining: Adapt Language Models to Domains and Tasks”, ACL, 2020. https://aclanthology.org/2020.acl-main.740/

[^ch8-31]: Jiang, Zhengbao et al., “Instruction-tuned Language Models are Better Knowledge Learners”, ACL, 2024. https://aclanthology.org/2024.acl-long.296/

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：模型预训练基础 \[可选阅读\]](../03-%E6%A8%A1%E5%9E%8B%E9%A2%84%E8%AE%AD%E7%BB%83%E5%9F%BA%E7%A1%80%5B%E5%8F%AF%E9%80%89%E9%98%85%E8%AF%BB%5D/README.md) · [下一篇：Mid-training 数据如何构造](01-Mid-training%E6%95%B0%E6%8D%AE%E5%A6%82%E4%BD%95%E6%9E%84%E9%80%A0.md)
