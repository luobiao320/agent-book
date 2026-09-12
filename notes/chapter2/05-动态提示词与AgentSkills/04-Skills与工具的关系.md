<!-- 自动生成；个人补充请写入 personal/。 -->

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Skills 在上下文中的位置](03-Skills%E5%9C%A8%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%E7%9A%84%E4%BD%8D%E7%BD%AE.md) · [下一篇：Agent 状态栏：通过元信息增强 Agent 轨迹管理](../06-Agent%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%9A%E9%80%9A%E8%BF%87%E5%85%83%E4%BF%A1%E6%81%AF%E5%A2%9E%E5%BC%BAAgent%E8%BD%A8%E8%BF%B9%E7%AE%A1%E7%90%86/README.md)

> 所属章节：[第2章：上下文工程](../README.md)
>
> 来源：[原文及行号](https://github.com/bojieli/ai-agent-book/blob/d1502f59c1a8c40b4d1c51c250238cd9dd836f1b/book/chapter2.md#L822-L848) · [在线原书](https://bojieli.github.io/ai-agent-book/book/chapter2/)

<!-- 原文开始 -->

<a id="skills-与工具的关系"></a>

### Skills 与工具的关系

从上下文管理的角度看，Skills 机制对 KV Cache 极为友好。如果把所有专用代码工具的定义都放在系统提示词中，数量膨胀会消耗大量的 token，而且会干扰模型的注意力；而在 Skill + 通用执行器的模式下，工具数量始终很少（如第五章所示仅需七个核心工具），Skill 的内容通过前述的渐进式披露机制按需加载，不会影响已缓存的前缀。两种形态的详细对比和选择框架见第四章，第九章则探讨 Agent 在持续进化中如何判断一项经验应写成知识、指令、程序还是模型参数。

> **实验 2-6 ★★：使用 Agent Skills 从论文生成演示文稿**
>
> **实验目标**：验证 Agent 通过动态加载专业领域 Skill 完成复杂任务的能力。
>
> 使用 Claude Code（或任意支持 SKILL.md 渐进式披露的等价 Agent 运行时，如 Kimi Code）+ Anthropic 官方 PPTX Skill，从一篇学术论文的 PDF 生成一份 10-15 页的演示文稿。Skill 的内容是实验对象，运行时可以替换——并非每位读者都有 Anthropic 凭证，只要运行时具备「元数据目录 + 按需加载」的 Skills 机制即可。Agent 的执行流程体现了渐进式加载的过程：
>
> 1. 在运行时提供的 Skill 元数据目录中看到 PPTX Skill 的描述（目录在完整正文加载前可见）
> 2. 识别出任务需要该 Skill
> 3. 调用 Skill（或读取 `SKILL.md`）加载完整指令，获得核心流程
> 4. 选择性加载 `html2pptx.md` 获取详细方法
> 5. 使用捆绑的工具脚本（如 `scripts/thumbnail.py`）生成预览，使用模板文件作为设计的起点
>
> **验收标准**：生成的 PowerPoint 覆盖论文的主要内容（标题页、问题背景、方法概述、关键结果、结论），至少包含 3 张从论文中提取的图表且与文字说明一致，格式正确且可在 PowerPoint 或兼容软件中正常打开。
>

> **实验 2-7 ★★：从个人范文创建“去 AI 味”写作 Skill**
>
> **实验目标**：用少量人工范文生成一份可加载、可检查的写作 Skill，并观察它能否在新文章中复现作者的主要表达偏好。
>
> **实验说明**：准备三到五篇原创文章，让支持 Agent Skills 的运行时生成初版 `SKILL.md`；选择一个新题目起草文章，作者手动修改后，比较 before/after 并把稳定规律写回 Skill。验收只要求 Skill 具备清晰的触发条件、三到五条带示例的原则、作用域和例外，不把一次主观判断当作普遍规则。
>
> **实验说明了什么**：Skill 的价值在于把个人经验外化为按需加载的指令。一个短小、可读、能通过真实任务检验的初版，比一开始罗列几十条规则更适合作为后续迭代的起点。


<!-- 原文结束 -->

---

[全书目录](../../../README.md) · [上级目录](README.md) · [上一篇：Skills 在上下文中的位置](03-Skills%E5%9C%A8%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%E7%9A%84%E4%BD%8D%E7%BD%AE.md) · [下一篇：Agent 状态栏：通过元信息增强 Agent 轨迹管理](../06-Agent%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%9A%E9%80%9A%E8%BF%87%E5%85%83%E4%BF%A1%E6%81%AF%E5%A2%9E%E5%BC%BAAgent%E8%BD%A8%E8%BF%B9%E7%AE%A1%E7%90%86/README.md)
