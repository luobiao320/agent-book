# Skills 在上下文中的位置

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#skills-在上下文中的位置

## 核心结论

不同 Harness 的消息角色实现并不完全相同，但共同原则是：少量 Skill 目录先可发现，完整 Skill 正文在选中后再注入。

第一次加载 Skill 会产生新的 token 成本；之后如果轨迹保持追加式，前缀可以继续复用。Skills 的收益不是“零成本”，而是避免启动时一次性加载所有领域说明。