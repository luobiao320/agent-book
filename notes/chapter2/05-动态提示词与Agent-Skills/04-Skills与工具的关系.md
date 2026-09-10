# Skills 与工具的关系

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#skills-与工具的关系

## 区分

- Tool：提供动作能力，解决“能调用什么”。
- Skill：提供任务方法，解决“应该如何完成某类工作”。

Skill 可以指导 Agent 组合多个通用工具，也可以附带脚本、模板和领域规范。

当能力数量很大时，“少量通用执行器 + 按需 Skill”通常比把所有专用工具 schema 永久塞进前缀更节省上下文。