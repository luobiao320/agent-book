<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：工具调用：把环境带进 Agent](../11-%E4%BB%8E%E5%8D%95%E8%BD%AE%E5%88%B0%E5%A4%9A%E8%BD%AE%EF%BC%9A%E4%BB%BB%E5%8A%A1%E5%9C%BA%E6%99%AF%E4%B8%8E%E4%BF%A1%E7%94%A8%E5%88%86%E9%85%8D/02-%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8%EF%BC%9A%E6%8A%8A%E7%8E%AF%E5%A2%83%E5%B8%A6%E8%BF%9BAgent.md) · [下一篇：奖励来自哪里：规则、人类偏好与模型评判](01-%E5%A5%96%E5%8A%B1%E6%9D%A5%E8%87%AA%E5%93%AA%E9%87%8C%EF%BC%9A%E8%A7%84%E5%88%99%E3%80%81%E4%BA%BA%E7%B1%BB%E5%81%8F%E5%A5%BD%E4%B8%8E%E6%A8%A1%E5%9E%8B%E8%AF%84%E5%88%A4.md)

> 所属章节：[第8章：模型后训练](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter8.md#L610-L613) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter8/)

<!-- 原文开始 -->

<a id="奖励设计如何把任务目标变成学习信号"></a>

## 奖励设计：如何把任务目标变成学习信号

前面的单轮、多轮和工具调用场景说明了“要训练什么”；这一节回答“环境应该怎样告诉模型做得好不好”。奖励设计可以沿三个互补维度展开：**奖励来自哪里**、**什么时候给**、**要表达多少信息**。最后再讨论一个额外问题：结果正确时，路径是否也合规。


<!-- 原文结束 -->

## 阅读目录

- [奖励来自哪里：规则、人类偏好与模型评判](01-%E5%A5%96%E5%8A%B1%E6%9D%A5%E8%87%AA%E5%93%AA%E9%87%8C%EF%BC%9A%E8%A7%84%E5%88%99%E3%80%81%E4%BA%BA%E7%B1%BB%E5%81%8F%E5%A5%BD%E4%B8%8E%E6%A8%A1%E5%9E%8B%E8%AF%84%E5%88%A4.md)
- [奖励在什么时候给：结果还是过程](02-%E5%A5%96%E5%8A%B1%E5%9C%A8%E4%BB%80%E4%B9%88%E6%97%B6%E5%80%99%E7%BB%99%EF%BC%9A%E7%BB%93%E6%9E%9C%E8%BF%98%E6%98%AF%E8%BF%87%E7%A8%8B.md)
- [奖励需要表达多少信息：标量、向量与生成式诊断](03-%E5%A5%96%E5%8A%B1%E9%9C%80%E8%A6%81%E8%A1%A8%E8%BE%BE%E5%A4%9A%E5%B0%91%E4%BF%A1%E6%81%AF%EF%BC%9A%E6%A0%87%E9%87%8F%E3%80%81%E5%90%91%E9%87%8F%E4%B8%8E%E7%94%9F%E6%88%90%E5%BC%8F%E8%AF%8A%E6%96%AD.md)
- [结果正确还不够：路径约束与 RLVP](04-%E7%BB%93%E6%9E%9C%E6%AD%A3%E7%A1%AE%E8%BF%98%E4%B8%8D%E5%A4%9F%EF%BC%9A%E8%B7%AF%E5%BE%84%E7%BA%A6%E6%9D%9F%E4%B8%8ERLVP.md)

---

[全书目录](../../../README.md) · [上级目录](../README.md) · [上一篇：工具调用：把环境带进 Agent](../11-%E4%BB%8E%E5%8D%95%E8%BD%AE%E5%88%B0%E5%A4%9A%E8%BD%AE%EF%BC%9A%E4%BB%BB%E5%8A%A1%E5%9C%BA%E6%99%AF%E4%B8%8E%E4%BF%A1%E7%94%A8%E5%88%86%E9%85%8D/02-%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8%EF%BC%9A%E6%8A%8A%E7%8E%AF%E5%A2%83%E5%B8%A6%E8%BF%9BAgent.md) · [下一篇：奖励来自哪里：规则、人类偏好与模型评判](01-%E5%A5%96%E5%8A%B1%E6%9D%A5%E8%87%AA%E5%93%AA%E9%87%8C%EF%BC%9A%E8%A7%84%E5%88%99%E3%80%81%E4%BA%BA%E7%B1%BB%E5%81%8F%E5%A5%BD%E4%B8%8E%E6%A8%A1%E5%9E%8B%E8%AF%84%E5%88%A4.md)
