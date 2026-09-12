# Agent Book 分块阅读版

按原书目录拆分《深入理解 AI Agent》，保留完整原文、图片、代码、公式、表格、例子、小结、思考题和参考资料。

[从引言开始阅读](notes/introduction/README.md) · [学习入口](learning/README.md) · [个人笔记](personal/README.md)

## 全书目录

- [引言](notes/introduction/README.md)
- [第1章：AI Agent 入门](notes/chapter1/README.md)
- [第2章：上下文工程](notes/chapter2/README.md)
- [第3章：用户记忆和知识库](notes/chapter3/README.md)
- [第4章：工具](notes/chapter4/README.md)
- [第5章：Coding Agent 与通用 Agent](notes/chapter5/README.md)
- [第6章：交互：观察与动作空间的扩展](notes/chapter6/README.md)
- [第7章：Agent 的评估](notes/chapter7/README.md)
- [第8章：模型后训练](notes/chapter8/README.md)
- [第9章：Agent 的持续进化](notes/chapter9/README.md)
- [第10章：多 Agent 协作](notes/chapter10/README.md)
- [后记：回到 Agent = LLM + 上下文 + 工具](notes/afterword/README.md)
- [思考题参考答案](notes/reference-answers/README.md)

二级标题对应主题目录，三级标题对应独立知识块；更深层标题保留在块内。章节及主题首页的导读也是正文，请按“下一篇”顺序阅读。

## 手动同步原书

在 GitHub 的 **Actions → Sync complete reading blocks → Run workflow** 手动同步。不会定时更新，也不会因为修改笔记自动触发。

本地只需 Python 3.10 或更新版本，无第三方依赖：

```sh
python3 tools/restructure_all_chapters.py --sync
python3 tools/restructure_all_chapters.py --check
```

不带参数时使用仓库中的原文快照离线重建；`--sync --ref <上游提交SHA>` 可指定来源版本。生成前先在临时目录校验，失败不会替换现有阅读内容。生成文件如果被手工修改，会停止并指出冲突，请先将个人修改保存到个人区。

## 来源与个人内容

- [原书网站](https://bojieli.github.io/ai-agent-book/) · [原始项目](https://github.com/bojieli/ai-agent-book)
- [固定来源版本与同步记录](source/README.md) · [原文快照](source/book/) · [原项目许可证](source/LICENSE)
- 本仓库正文为原文拆分重排，不是摘要；调整仅限目录导航、链接、锚点、脚注补齐和 Markdown 排版适配。
- `notes/` 和 `source/` 为生成内容；心得与补充放在 `personal/`，不会被同步修改。
- [迁移前的旧笔记](personal/legacy/notes/)已完整保留，其中第2章包含原来的学习摘要。归档不属于新版阅读目录。
