# Skills：领域能力的可组合单元

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#skills领域能力的可组合单元

## 三层渐进披露

1. 元数据：先暴露 `name`、`description` 等短目录，让 Agent 知道有哪些能力。
2. 核心流程：判断任务需要某个 Skill 后再加载完整 `SKILL.md`。
3. 细则/附件：再按任务需要读取参考文档、脚本、模板等资源。

## 关键点

`description` 更像路由条件，重点是“什么时候该用/不该用”，而不是泛泛介绍能力。