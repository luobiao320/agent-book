### 没有更强的教师怎么办：On-Policy 自蒸馏

On-Policy Distillation 的威力来自教师，但它也因此背上了一个硬前提：**必须有一个明显强于学生的教师模型。** 这在很多场景里并不成立。如果你要训练的是垂直领域模型，现有模型的能力都存在不足，那就没有教师模型可用。没有更强的教师，稠密信号的红利就与我们无缘了吗？

一个巧妙的破题思路是 **On-Policy Self-Distillation（OPSD，在轨自蒸馏）**[^ch8-15]：**同一个模型分饰教师和学生两角，但看到的上下文不同。** 教师版能看到“特权信息”——如标准答案或已验证的正确解答；学生版只看到问题本身，却在自己采样的轨迹上向教师版的逐 token 分布对齐。对着答案解释学生刚走过的路径，通常比独立探索更容易，因此一条 rollout 仍能产生密集监督。

OPSD 可以看成上一段伪代码的一个受限变体：

```python
student_trajectory = rollout(model, task_without_answer)
loss = 0
for state in student_trajectory:
    privileged_state = add_verified_answer(state)
    teacher_logits = stop_gradient(model(privileged_state))
    loss += KL(model(state), teacher_logits)
update(model, loss + retention_regularizer)
```

其中，`privileged_state` 只能在训练侧构造，不能泄露给部署时的 Agent；`retention_regularizer` 代表保留集/风格约束，而不是某个固定超参数。训练流程还必须检查数据权限、答案遮蔽和遗忘风险。

相比 RLVR，OPSD 不要求奖励一定能被自动验证：特权信息可以是标准答案、人工示范或领域文档。它用这些信息替代更强的外部教师，同时保留“在轨采样 + 逐 token 监督”的样本效率优势。但它不会凭空创造新知识——如果模型拿着答案也讲不清过程，自蒸馏就没有额外信号；朴素 OPSD 还可能让模型丢失原有思考风格，需要额外正则稳定[^ch8-16]。
