### Skills：把工具发现变成“按需查阅”

近来更流行的一种思路来自 Skills 机制。第二章从上下文工程的角度介绍过 Skills 的**渐进式披露**（Progressive Disclosure）；这里换个角度，把它看作一种工具发现范式。它与上一节最大的不同，是不再需要那套 “嵌入索引 + 语义匹配” 的基础设施。

**渐进式披露。** 这是第一章命名的渐进式披露模式在工具侧的变体。像 MCP 这样的协议倾向于把工具的完整 schema 一次性摆在模型面前（要么全量注入、要么靠检索预筛先选出一批），Skills 则相反：Agent 启动时只看到一份薄薄的目录——每个 skill 的 `name` 与 `description`（合计数百 token）。当**当前上下文**真的需要某种能力时，模型才去读取对应的 sub-skill，并顺着其中的引用再往下一层，读取具体的脚本或子文档。

Skill 更接近人使用参考资料的方式。没有人会把一本工具书或整个维基百科从第一页读到最后一页，而是顺着索引和目录，根据当下需要逐个查阅词条。工具的详细定义不必全部常驻上下文，用到哪条查哪条。

专用工具要达到同样的渐进式披露，必须在工具之外另建一层——嵌入索引、检索元工具、`tool_search` 与 `tool_reference` 这类 API 原语，也就是上一节那套基础设施存在的理由。因此，Skills 是一种更现代、也更省心的工具发现思路。

前面把 MCP 与 Skill Hub 讲成两条并行的渠道，但它们并非互不相干：MCP 官方已经在推动 skill 经由 MCP 被发现和传递[^ch4-skills-over-mcp]。也就是说，同一个 skill 既可以躺在 Skill Hub 里等 `npx` 来装，也可以由一台 MCP 服务器供给。

[^ch4-skills-over-mcp]: Model Context Protocol, “Build an MCP server with Agent Skills” 与 “Skills over MCP Working Group”. https://modelcontextprotocol.io/docs/2026-07-28/develop/build-with-agent-skills；https://modelcontextprotocol.io/community/working-groups/skills-over-mcp

以上都是所有工具共通的问题：能力做成什么形态、怎么描述、参数如何传、用什么协议承载、规模上来之后怎么暴露。下面转入三类工具各自的设计重点，从感知工具开始。
