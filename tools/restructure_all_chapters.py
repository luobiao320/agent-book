#!/usr/bin/env python3
"""按原书 Markdown 标题层级重建 notes/chapterN 目录，并生成 notes/MERGED.md。
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


def chapter_sort_key(path: Path):
    m = re.fullmatch(r"chapter(\d+)", path.name)
    return int(m.group(1)) if m else 10**9


def merge_third_level_files():
    """合并 notes/chapterN/<三级主题目录> 下的 Markdown 到 notes/MERGED.md。

    chapter 根目录的 README.md / SOURCE.md 不参与；三级主题目录里的 README.md
    仍参与，因为部分主题没有拆成更细的小节，正文就保存在 README.md 中。
    """
    notes = ROOT / "notes"
    entries = []

    chapters = sorted(
        (p for p in notes.iterdir() if p.is_dir() and re.fullmatch(r"chapter\d+", p.name)),
        key=chapter_sort_key,
    )

    for chapter in chapters:
        topic_dirs = sorted((p for p in chapter.iterdir() if p.is_dir()), key=lambda p: p.name)
        for topic_dir in topic_dirs:
            for md in sorted(topic_dir.rglob("*.md"), key=lambda p: p.as_posix()):
                entries.append(md)

    out = notes / "MERGED.md"
    merged = [
        "# Notes 合并版",
        "",
        "> 自动合并 `notes/chapterN/<三级主题目录>/**/*.md`。",
        "> 每个文件按文件名分段，并保留原始相对路径用于区分同名文件。",
        "",
        "## 目录",
        "",
    ]

    for i, md in enumerate(entries, 1):
        rel = md.relative_to(notes).as_posix()
        merged.append(f"{i}. `{rel}`")

    for md in entries:
        rel = md.relative_to(notes).as_posix()
        merged.extend([
            "",
            "---",
            "",
            f"## {md.name}",
            "",
            f"> 原文件：`notes/{rel}`",
            "",
            md.read_text(encoding="utf-8").rstrip(),
            "",
        ])

    out.write_text("\n".join(merged).rstrip() + "\n", encoding="utf-8")
    print(f"Merged {len(entries)} Markdown files into {out.relative_to(ROOT)}")


if __name__ == "__main__":
    for n in [1,3,4,5,6,7,8,9,10]:
        split_chapter(n)
    merge_third_level_files()
