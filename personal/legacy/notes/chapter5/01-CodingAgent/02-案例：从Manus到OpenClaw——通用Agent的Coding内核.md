### 案例：从 Manus 到 OpenClaw——通用 Agent 的 Coding 内核

以 Manus、OpenClaw 为代表的通用 Agent 产品，把 Deep Research（深度调研）、Computer Use（电脑操控）和 Coding（代码生成）三大能力融合在一个系统中。那么，为什么本章开头说 Coding Agent 是其中的核心，而不是另外两者？

因为几乎所有高效的内容生成最终都要落到代码上。PPT、Word 文档本质上是 OOXML（Office Open XML，微软推出的办公文档开放标准）格式的代码。PDF 报告可以通过 Markdown、HTML 或 LaTeX 生成，数据分析和可视化可以由 Python 脚本完成，甚至 GUI 操作中成功的浏览器操作序列也可以被固化为可复用的代码（详见第九章）。Deep Research 的搜索和信息综合可通过代码驱动的 Web 请求和解析实现。Computer Use 虽然通用性更强，但成本、延迟和稳定性远不如直接通过代码或 API 来完成相同操作。代码生成是效率最高、成本最低、可复用性最强的能力基座。


![图5-1 OpenClaw 架构中的 Coding Agent 核心](images/fig5-1.svg)


用一个具体的执行流来理解这个架构。假设用户要求 “Help me analyze last quarter's sales data and create a summary report”：

1. **读记忆**：Agent 读取 `MEMORY.md`，发现用户偏好 PDF 格式的报告，数据源是 Google Sheets
2. **调工具**：通过网络搜索模块获取 Google Sheets API 的使用方法，通过代码执行下载数据
3. **写代码**：用 Python 生成数据分析脚本（pandas 聚合、matplotlib 可视化）
4. **生成产物**：将分析结果写入 `report.pdf`，图表写入 `charts/` 目录
5. **更新记忆**：在 `MEMORY.md` 中记录 “User's sales data is in Google Sheets, ID: xxx”，下次无需再问

整个过程中，文件系统是信息流转的枢纽——记忆从文件读取，产物写入文件，经验也保存为文件。

**文件系统作为 Agent 的中枢**。在 OpenClaw 的设计中，文件系统远不止是数据存储——它是 Agent 记忆、知识和能力的中枢。Agent 的长期记忆存储在 `MEMORY.md`（高层级事实和用户偏好）和按日期归档的 Markdown 日志中。选择 Markdown 而非向量数据库的决定看似反直觉，实际上极其有效：用户可以直接打开文件阅读和修改 Agent 的记忆（如果 Agent 记错了某件事，直接删除那一行即可），Markdown 天然保留时间顺序，避免语义检索中的时间混淆，而且可通过 Git 进行版本控制和回滚。

更关键的是，Agent 拥有写文件的能力，这意味着它具备了修改自身外部产物的技术条件。当 Agent 首次执行某个任务并发现了之前不知道的关键信息（例如给某银行打电话时，发现对方要求提供开户行地址才能验证身份），它可以先把发现写入记录。记录何时足以成为可靠知识、指令或程序，仍需结合更多轨迹与结果验证；这是第九章将讨论的持续进化问题。

**适用边界：哪些 Agent 以 Coding 为核心架构**。“Coding Agent 是通用 Agent 的核心” 这一判断主要适用于**以开放任务为目标**的通用 Agent——深度调研、内容生成、数据处理这类任务边界不确定、产物形态多样的场景。在这些场景中，无法预先枚举所有需要的工具，代码生成作为元能力提供了动态扩展能力边界的最经济路径，因此它是架构的核心。而另一类 Agent——例如垂直领域的客服 Agent——任务空间相对封闭，核心架构围绕固定的业务流程、领域工具和对话策略构建，代码在其中更多是工具箱里的一件工具而非架构中枢。但即便在后者，coding 也是重要的基础能力：精确计算、数据处理、规则校验都离不开它。
