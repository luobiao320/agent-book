#!/usr/bin/env python3
"""按原书 Markdown 标题层级重建 notes/chapterN 目录。
规则：## -> 文件夹，### -> 独立 Markdown 文件；跳过“本章小结”和“思考题”。
源：https://github.com/bojieli/ai-agent-book/tree/main/book
"""
import re
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"本章小结", "思考题"}


def safe_name(s: str) -> str:
    s = re.sub(r"[\\/:*?\"<>|]", "-", s)
    s = re.sub(r"\s+", "", s)
    return s.strip(".-")


def split_chapter(n: int):
    url = f"https://raw.githubusercontent.com/bojieli/ai-agent-book/main/book/chapter{n}.md"
    text = urlopen(url).read().decode("utf-8")
    lines = text.splitlines()
    title = next((x[2:].strip() for x in lines if x.startswith("# ")), f"Chapter {n}")
    out = ROOT / "notes" / f"chapter{n}"
    out.mkdir(parents=True, exist_ok=True)

    # 清理旧的自动拆分目录和根 README/SOURCE；保留 chapter2 现有人工整理结果。
    if n != 2:
        for p in list(out.iterdir()):
            if p.name in {"README.md", "SOURCE.md"}:
                p.unlink()
            elif p.is_dir():
                import shutil
                shutil.rmtree(p)

    sections = []
    current = None
    for idx, line in enumerate(lines):
        if line.startswith("## "):
            h = re.sub(r"\s*\{.*?\}\s*$", "", line[3:].strip())
            if h in SKIP:
                current = None
                continue
            current = {"title": h, "start": idx, "subs": []}
            sections.append(current)
        elif current and line.startswith("### "):
            h = re.sub(r"\s*\{.*?\}\s*$", "", line[4:].strip())
            current["subs"].append((h, idx))

    # 计算每个 H2/H3 边界并写文件（保留原始内容，确保每个小节自包含）。
    for si, sec in enumerate(sections):
        end = sections[si+1]["start"] if si+1 < len(sections) else len(lines)
        folder = out / f"{si+1:02d}-{safe_name(sec['title'])}"
        folder.mkdir(parents=True, exist_ok=True)
        subs = sec["subs"]
        if not subs:
            body = lines[sec["start"]:end]
            (folder / "README.md").write_text("\n".join(body).rstrip()+"\n", encoding="utf-8")
            continue
        readme = [f"# {sec['title']}", "", f"> 来源：{url}", "", "## 小节", ""]
        for sj, (st, pos) in enumerate(subs):
            fn = f"{sj+1:02d}-{safe_name(st)}.md"
            readme.append(f"{sj+1}. [{st}](./{fn})")
            sub_end = subs[sj+1][1] if sj+1 < len(subs) else end
            body = lines[pos:sub_end]
            (folder / fn).write_text("\n".join(body).rstrip()+"\n", encoding="utf-8")
        (folder / "README.md").write_text("\n".join(readme)+"\n", encoding="utf-8")

    root = [f"# 第 {n} 章：{title}", "", f"> 原始章节：https://bojieli.github.io/ai-agent-book/book/chapter{n}/", "", "## 目录", ""]
    for si, sec in enumerate(sections):
        folder = f"{si+1:02d}-{safe_name(sec['title'])}"
        root.append(f"{si+1}. [{sec['title']}](./{folder}/README.md)")
    (out / "README.md").write_text("\n".join(root)+"\n", encoding="utf-8")
    (out / "SOURCE.md").write_text(f"# 来源\n\n原始章节：https://bojieli.github.io/ai-agent-book/book/chapter{n}/\n\n拆分：`##` → 文件夹，`###` → 文件；跳过本章小结和思考题。\n", encoding="utf-8")


if __name__ == "__main__":
    for n in [1,3,4,5,6,7,8,9,10]:
        split_chapter(n)
