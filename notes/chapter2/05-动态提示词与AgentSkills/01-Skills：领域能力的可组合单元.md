<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：动态提示词与 Agent Skills](README.md) · [下一篇：如何编写一份可用的 Skill](02-%E5%A6%82%E4%BD%95%E7%BC%96%E5%86%99%E4%B8%80%E4%BB%BD%E5%8F%AF%E7%94%A8%E7%9A%84Skill.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L768-L785) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="skills领域能力的可组合单元"></a>

### Skills：领域能力的可组合单元

Agent Skills 的核心思想是将 Agent 的能力模块化为独立的、可按需加载的知识包[^ch2-3]。每个 Skill 本质上是一套包含专业领域指导的提示词集合，就像为新员工准备的某个专项任务的操作手册。与传统的将所有指令塞入单一系统提示词的做法不同，Skills 采用了渐进式披露（Progressive Disclosure）的设计哲学——先给 Agent 看一份目录摘要，需要时再加载完整内容，就像你不会把公司所有部门的操作手册都堆到新员工桌上，而是先给一份总目录，需要哪本再去取。

[^ch2-3]: Anthropic, ["Equipping Agents for the Real World with Agent Skills"](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), 2025；Claude Code Docs, ["How Claude Code uses prompt caching"](https://code.claude.com/docs/en/prompt-caching), “Invoking skills and commands”；Agent Skills, ["How to add skills support to your agent"](https://agentskills.io/client-implementation/adding-skills-support), “Where to place the catalog”.
[^ch2-codex-skills]: OpenAI, ["Build skills"](https://developers.openai.com/codex/skills/), “How ChatGPT and Codex use skills”；OpenAI Codex 公开仓库中的 Skills extension 实现。

**第一层（元数据）**：每个 Skill 必须包含一个 `SKILL.md` 文件，开头是 YAML frontmatter（即文件顶部用 `---` 分隔的元数据块，类似书籍的版权页），包含 `name` 和 `description` 两个字段。目录应在主体正文加载前对 Agent 可见，使它能够先判断当前任务是否需要某项能力，而不必为所有能力支付完整的上下文成本。不同运行时可以把目录放在不同的上下文层，目录的共同作用是提供可发现性，而不是承载完整的领域流程。

元数据中的 `description` 字段是路由决策的关键——它应当足够短（控制常驻的 token 量），但写法要像路由条件而非功能介绍。可以明确写出“何时使用”和“何时不使用”的边界，并给出几条典型**反例**，以减少宽泛匹配带来的误触发；这是路由提示的写作建议，不是额外的格式字段。描述太宽泛（如 “help with backend”）等于任何后端相关的工作都能触发，路由就会失准；真正有效的描述是路由条件——“何时该用我”比“我能做什么”重要得多。

**第二层（核心流程）**：当 Agent 判断某个任务需要特定的 Skill 时，运行时才加载完整的 `SKILL.md`。触发加载的方式有两种：用户显式输入斜杠命令（如 `/pptx`）时，由客户端在本地拦截并展开，模型不必先发起一次工具调用；模型读过元数据目录后自己判断需要某个 Skill 时，则调用专用的 Skill 工具，比前者多一次 ReAct 往返。两条路径的落点相同——Claude Code 都在调用位置把 Skill 正文作为 user message 加入会话，模型自主触发时返回的那条 tool result 只是一句“正在启动 Skill”的占位符，并不承载正文[^ch2-cc-skill-inject]。没有专用激活工具的运行时则用通用文件读取工具去读 `SKILL.md`，正文以 tool result 的形式进入上下文。以 PPTX Skill[^ch2-4] 为例，其中包含处理 PowerPoint 文件的核心流程：如何通过 markitdown（Microsoft 开源的文档转 Markdown 工具）提取文本，如何解压 PPTX 文件访问原始的 XML 结构，以及关键文件的路径约定。

[^ch2-4]: Anthropic, "PPTX Skill", 2025. https://github.com/anthropics/skills/
[^ch2-cc-skill-inject]: Claude Code Docs, ["How Claude Code uses prompt caching"](https://code.claude.com/docs/en/prompt-caching), “Invoking skills and commands”：“Skills and commands inject their instructions as user messages at the point of invocation.” 两种触发方式的分工见 Agent Skills, ["How to add skills support to your agent"](https://agentskills.io/client-implementation/adding-skills-support), “User-explicit activation”：斜杠命令由 Harness 拦截并注入，模型无需自己发起激活动作。

**第三层（细则）**：通过文件引用深入到更详细的子文档。主文件引用了 `html2pptx.md`（通过 HTML 模板创建 PowerPoint 的详细工作流）、`reference.md`（格式技术细节）等。Agent 会根据具体的需求选择性地深入阅读相关的子文档。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：动态提示词与 Agent Skills](README.md) · [下一篇：如何编写一份可用的 Skill](02-%E5%A6%82%E4%BD%95%E7%BC%96%E5%86%99%E4%B8%80%E4%BB%BD%E5%8F%AF%E7%94%A8%E7%9A%84Skill.md)
