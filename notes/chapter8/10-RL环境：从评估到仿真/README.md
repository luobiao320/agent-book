<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：为什么 LLM RL 通常优先 On-Policy](../09-RL%E7%AE%97%E6%B3%95%EF%BC%9A%E4%BB%8E16%E6%AC%A1rollout%E5%88%B0%E4%B8%80%E6%AC%A1%E5%8F%82%E6%95%B0%E6%9B%B4%E6%96%B0/01-%E4%B8%BA%E4%BB%80%E4%B9%88LLMRL%E9%80%9A%E5%B8%B8%E4%BC%98%E5%85%88On-Policy.md) · [下一篇：环境：模型练习的场地](01-%E7%8E%AF%E5%A2%83%EF%BC%9A%E6%A8%A1%E5%9E%8B%E7%BB%83%E4%B9%A0%E7%9A%84%E5%9C%BA%E5%9C%B0.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L530-L533) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="rl-环境从评估到仿真"></a>

## RL 环境：从评估到仿真

RL 训练的瓶颈往往不在算法，而在**环境是否足够真实、可重置、可并行**。真实 Agent 的电话、付款或文件修改可能昂贵且不可逆，不能靠无限重试弥补一次错误；第七章的评估环境可以提供验证器，但训练还需要让 Agent 反复试错、承受动作副作用，并在数百万次交互中保持稳定。因此环境工程是 RL 的前置条件，不是训练完成后的附属品。


<!-- 原文结束 -->

## 阅读目录

- [环境：模型练习的场地](01-%E7%8E%AF%E5%A2%83%EF%BC%9A%E6%A8%A1%E5%9E%8B%E7%BB%83%E4%B9%A0%E7%9A%84%E5%9C%BA%E5%9C%B0.md)
- [造不出环境怎么办：让模型扮演环境](02-%E9%80%A0%E4%B8%8D%E5%87%BA%E7%8E%AF%E5%A2%83%E6%80%8E%E4%B9%88%E5%8A%9E%EF%BC%9A%E8%AE%A9%E6%A8%A1%E5%9E%8B%E6%89%AE%E6%BC%94%E7%8E%AF%E5%A2%83.md)
- [环境、任务分布与评估隔离](03-%E7%8E%AF%E5%A2%83%E3%80%81%E4%BB%BB%E5%8A%A1%E5%88%86%E5%B8%83%E4%B8%8E%E8%AF%84%E4%BC%B0%E9%9A%94%E7%A6%BB.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：为什么 LLM RL 通常优先 On-Policy](../09-RL%E7%AE%97%E6%B3%95%EF%BC%9A%E4%BB%8E16%E6%AC%A1rollout%E5%88%B0%E4%B8%80%E6%AC%A1%E5%8F%82%E6%95%B0%E6%9B%B4%E6%96%B0/01-%E4%B8%BA%E4%BB%80%E4%B9%88LLMRL%E9%80%9A%E5%B8%B8%E4%BC%98%E5%85%88On-Policy.md) · [下一篇：环境：模型练习的场地](01-%E7%8E%AF%E5%A2%83%EF%BC%9A%E6%A8%A1%E5%9E%8B%E7%BB%83%E4%B9%A0%E7%9A%84%E5%9C%BA%E5%9C%B0.md)
