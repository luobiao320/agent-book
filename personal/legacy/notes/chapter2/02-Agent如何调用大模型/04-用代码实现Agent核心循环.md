# 用代码实现 Agent 的核心循环

原文：https://bojieli.github.io/ai-agent-book/book/chapter2/#用代码实现-agent-的核心循环

## 最小骨架

核心实现可以简化为一个循环：每次调用模型后，把 `assistant` 消息追加到 `messages`；如果有 `tool_calls`，执行工具并追加 `tool` 消息，然后继续；没有工具调用就结束。

## 工程理解

Agent Harness 的核心职责之一，就是管理不断增长的 `messages`：保持角色、顺序、工具调用关联和必要历史的完整性。

生产代码还需要加入最大迭代次数、错误处理、权限控制、超时和中断机制，避免 Agent 在工具循环中无限运行。