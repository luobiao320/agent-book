#!/usr/bin/env python3
"""从固定版本原文生成完整阅读块；仅使用 Python 标准库。

--sync 手动获取上游最新版本；默认使用 source/ 中的原文离线重建。
--check 只检查当前内容及重建一致性；首次迁移需 --migrate-legacy。
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import hashlib
import html
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
import tempfile
import time
import unicodedata
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "bojieli/ai-agent-book"
DOCUMENTS = ["introduction", *[f"chapter{n}" for n in range(1, 11)], "afterword", "reference-answers"]
MANIFEST = "source/manifest.json"
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
ATTRIBUTE = re.compile(r"[ \t]*\{(?:\s*#[\w.:-]+|\s*\.[\w-]+|\s*[\w-]+=[^{}]*)+\s*\}")
INLINE_CODE = re.compile(r"(`+)(?!`)(.*?)(?<!`)\1(?!`)", re.DOTALL)
LINK = re.compile(r"(?P<prefix>!?\[(?:\\.|[^\]\n]|\[[^\]\n]*\])*\]\()(?P<url><[^>\n]+>|(?:\\.|[^()\s]|\([^()\n]*\))+)")
DEFINITION = re.compile(r"^(?:> ?)* {0,3}\[([^\]]+)\]:[ \t]*(.*)$")
HTML_LINK = re.compile(r'''\b(src|href)=(['"])(.*?)\2''')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def fetch(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={"User-Agent": "agent-book-reader"}), timeout=45) as response:
                return response.read()
        except OSError:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def download_snapshot(destination, ref):
    api = f"https://api.github.com/repos/{REPOSITORY}"
    commit = json.loads(fetch(f"{api}/commits/{quote(ref, safe='')}"))["sha"]
    tree = json.loads(fetch(f"{api}/git/trees/{commit}?recursive=1"))
    if tree.get("truncated"):
        raise ValueError("上游目录被截断，停止同步")
    wanted = {f"book/{name}.md" for name in DOCUMENTS} | {"LICENSE", "NOTICE"}
    entries = [item for item in tree["tree"] if item["type"] == "blob" and
               (item["path"] in wanted or item["path"].startswith("book/images/"))]

    def download(item):
        data = fetch(f"https://raw.githubusercontent.com/{REPOSITORY}/{commit}/{quote(item['path'])}")
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob != item["sha"]:
            raise ValueError(f"下载内容不完整：{item['path']}")
        target = destination / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(download, entries))
    metadata = {"repository": REPOSITORY, "commit": commit,
                "files": {item["path"]: item["sha"] for item in entries},
                "paths": [item["path"] for item in tree["tree"]]}
    (destination / "upstream.json").write_bytes(json_bytes(metadata))
    return metadata


def checked_path(root, name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"非法文件路径：{name}")
    target = root / name
    if any((root.joinpath(*path.parts[:i])).is_symlink() for i in range(1, len(path.parts) + 1)):
        raise ValueError(f"不操作符号链接：{name}")
    return target


def load_snapshot(directory):
    metadata = json.loads((directory / "upstream.json").read_text())
    if metadata["repository"] != REPOSITORY or not re.fullmatch(r"[0-9a-f]{40}", metadata["commit"]):
        raise ValueError("来源元数据无效")
    required = {f"book/{name}.md" for name in DOCUMENTS} | {"LICENSE"}
    if not required <= metadata["files"].keys():
        raise ValueError("原文快照缺少章节或许可证")
    files = {}
    for name, expected in metadata["files"].items():
        data = checked_path(directory, name).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if actual != expected:
            raise ValueError(f"原文快照被修改或损坏：{name}")
        files[name] = data
    return metadata, files


def prose_lines(lines):
    """仅识别正文语法，围栏代码（含引用块内代码）、缩进代码和注释不参与拆分。"""
    fence = None
    comment = False
    result = []
    for line in lines:
        plain = re.sub(r"^(?: {0,3}> ?)+", "", line)
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", plain)
        if fence:
            result.append(False)
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            result.append(False)
            continue
        if comment or "<!--" in plain:
            comment = "-->" not in plain
            result.append(False)
            continue
        result.append(not plain.startswith(("    ", "\t")))
    if fence:
        raise ValueError("发现未闭合代码围栏，无法安全拆分")
    return result


def outside_code(text, transform):
    chunks = []
    start = 0
    for match in INLINE_CODE.finditer(text):
        chunks.extend([transform(text[start:match.start()]), match[0]])
        start = match.end()
    chunks.append(transform(text[start:]))
    return "".join(chunks)


def title_text(text):
    text = ATTRIBUTE.sub("", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return html.unescape(re.sub(r"<[^>]+>|[`*_]", "", text)).strip()


def slug(text):
    text = title_text(text).lower()
    return "".join(c for c in text if c in " -_" or unicodedata.category(c)[0] in "LNM").replace(" ", "-")


def safe_name(text):
    return re.sub(r"\s+", "", re.sub(r'[\\/:*?"<>|]', "-", title_text(text))).strip(".-") or "未命名"


def relative(source, target, anchor=""):
    path = posixpath.relpath(target, posixpath.dirname(source) or ".")
    return quote(path, safe="/-._~") + ("#" + quote(anchor, safe="-._~") if anchor else "")


def label(text):
    return title_text(text).replace("[", r"\[").replace("]", r"\]")


@dataclass
class Page:
    source: str
    path: str
    title: str
    start: int
    end: int
    parent: str


class Book:
    def __init__(self, metadata, files):
        self.metadata, self.files = metadata, files
        self.pages, self.headings, self.lines, self.masks = [], {}, {}, {}
        self.anchors, self.definitions = {}, {}
        self.warnings, self.remote_paths = set(), set()
        self.links, self.coverage = [], []
        self.outputs = {}
        for name in DOCUMENTS:
            self.split(f"book/{name}.md")

    def split(self, source):
        lines = self.files[source].decode("utf-8").splitlines(keepends=True)
        mask = prose_lines(lines)
        self.lines[source], self.masks[source] = lines, mask
        headings, counts = [], {}
        for i, line in enumerate(lines):
            match = HEADING.match(line.rstrip("\r\n")) if mask[i] else None
            if not match:
                continue
            base = slug(match[2])
            number = counts.get(base, 0)
            counts[base] = number + 1
            anchor = base + (f"-{number}" if number else "")
            explicit = re.search(r"\{#([\w.:-]+)", match[2])
            headings.append((i, len(match[1]), match[2], anchor, explicit[1] if explicit else None))
        if not headings or headings[0][1] != 1:
            raise ValueError(f"缺少章标题：{source}")
        self.headings[source] = headings
        root = f"notes/{Path(source).stem}"
        root_page = root + "/README.md"
        cuts = [(0, root_page, title_text(headings[0][2]), "README.md")]
        folder, section_count, subsection_count = root, 0, 0
        for i, level, title, _, _ in headings[1:]:
            if level == 2:
                section_count += 1
                subsection_count = 0
                folder = f"{root}/{section_count:02d}-{safe_name(title)}"
                cuts.append((i, folder + "/README.md", title_text(title), root_page))
            elif level == 3:
                subsection_count += 1
                path = f"{folder}/{subsection_count:02d}-{safe_name(title)}.md"
                cuts.append((i, path, title_text(title), folder + "/README.md"))
        pages = [Page(source, path, title, start, cuts[n+1][0] if n+1 < len(cuts) else len(lines), parent)
                 for n, (start, path, title, parent) in enumerate(cuts)]
        if "".join("".join(lines[p.start:p.end]) for p in pages) != self.files[source].decode("utf-8"):
            raise ValueError(f"原文切分存在遗漏或重复：{source}")
        for i, _, _, anchor, explicit in headings:
            page = next(p for p in pages if p.start <= i < p.end)
            self.anchors[source, anchor] = page.path
            if explicit:
                self.anchors[source, explicit] = page.path
        definitions = {}
        for i, line in enumerate(lines):
            match = DEFINITION.match(line.rstrip()) if mask[i] else None
            if match:
                end = i + 1
                while end < len(lines):
                    if lines[end].startswith(("    ", "\t")):
                        end += 1
                    elif not lines[end].strip() and end + 1 < len(lines) and lines[end+1].startswith(("    ", "\t")):
                        end += 1
                    else:
                        break
                definitions[match[1].casefold()] = "".join(lines[i:end])
        self.definitions[source] = definitions
        self.pages.extend(pages)

    def resolve(self, url, page, image=False):
        angle = url.startswith("<") and url.endswith(">")
        value = html.unescape(url[1:-1] if angle else url)
        value = re.sub(r"\\([() ])", r"\1", value)
        parts = urlsplit(value)
        source = page.source
        if parts.scheme or parts.netloc:
            prefix = "/ai-agent-book/book/"
            if parts.netloc == "bojieli.github.io" and parts.path.startswith(prefix):
                name = parts.path[len(prefix):].strip("/")
                source = "book/" + (name if name.endswith(".md") else name + ".md")
            else:
                return url
        elif parts.path:
            source = posixpath.normpath(posixpath.join(posixpath.dirname(page.source), unquote(parts.path)))
        fragment = unquote(parts.fragment)
        if source in self.lines:
            target = f"notes/{Path(source).stem}/README.md"
            if fragment:
                target = self.anchors.get((source, fragment))
                if not target:
                    self.warnings.add(f"原文锚点不存在：{page.source} → {value}")
                    return f"https://github.com/{REPOSITORY}/blob/{self.metadata['commit']}/{quote(source)}#{quote(fragment)}"
            self.links.append((page.path, target, fragment))
            result = relative(page.path, target, fragment)
        elif source in self.files:
            target = "source/" + source
            self.links.append((page.path, target, fragment))
            result = relative(page.path, target, fragment)
        else:
            normalized = source.rstrip("/")
            if normalized not in self.metadata["paths"]:
                self.warnings.add(f"上游目标不存在：{page.source} → {value}")
                if image:
                    raise ValueError(f"原图缺失，停止更新并保留现有内容：{page.source} → {value}")
            self.remote_paths.add(normalized)
            kind = "blob" if PurePosixPath(normalized).suffix else "tree"
            result = f"https://github.com/{REPOSITORY}/{kind}/{self.metadata['commit']}/{quote(normalized)}"
            if fragment:
                result += "#" + quote(fragment)
        return "<" + result + ">" if angle else result

    def rewrite(self, text, page):
        def replace_visible(line, pattern, replacement):
            protected = [(m.start(), m.end()) for m in INLINE_CODE.finditer(line)]
            return pattern.sub(lambda m: m[0] if any(start <= m.start() < end for start, end in protected)
                               else replacement(m), line)

        result = []
        lines = text.splitlines(keepends=True)
        for line, active in zip(lines, prose_lines(lines)):
            if not active:
                result.append(line)
                continue
            definition = DEFINITION.match(line.rstrip())
            if definition and not definition[1].startswith("^"):
                line = re.sub(r"(\]:[ \t]*)(<[^>]+>|\S+)", lambda m: m[1] + self.resolve(m[2], page), line, count=1)
            # 链接标签可含行内代码；保护代码里的伪链接，但仍改写真链接的目标。
            line = replace_visible(line, LINK, lambda m: m["prefix"] + self.resolve(m["url"], page, m["prefix"].startswith("!")))
            line = replace_visible(line, HTML_LINK, lambda m: f'{m[1]}={m[2]}{self.resolve(m[3], page, m[1] == "src")}{m[2]}')
            # 显式标题 ID 已转为锚点，仅移除非代码区域的排版属性。
            result.append(outside_code(line, lambda part: ATTRIBUTE.sub("", part)))
        return "".join(result)

    def document_title(self, source):
        title = title_text(self.headings[source][0][2])
        chapter = re.fullmatch(r"book/chapter(\d+)\.md", source)
        return f"第{chapter[1]}章：{title}" if chapter else title

    def navigation(self, page, index):
        links = [f"[全书目录]({relative(page.path, 'README.md')})",
                 f"[上级目录]({relative(page.path, page.parent)})"]
        if index:
            prev = self.pages[index-1]
            links.append(f"[上一篇：{label(prev.title)}]({relative(page.path, prev.path)})")
        if index+1 < len(self.pages):
            nxt = self.pages[index+1]
            links.append(f"[下一篇：{label(nxt.title)}]({relative(page.path, nxt.path)})")
        return " · ".join(links)

    def render(self):
        for index, page in enumerate(self.pages):
            source_lines = self.lines[page.source]
            raw = "".join(source_lines[page.start:page.end])
            anchors = {i: [a for a in [anchor, explicit] if a]
                       for i, _, _, anchor, explicit in self.headings[page.source]}
            body = []
            for i in range(page.start, page.end):
                if i in anchors:
                    body.append("\n" + "\n".join(f'<a id="{html.escape(a, quote=True)}"></a>' for a in dict.fromkeys(anchors[i])) + "\n\n")
                body.append(source_lines[i])
            content = self.rewrite("".join(body), page)
            # 缺少的定义复制到当前页，原定义仍保留在原位置。
            appendix, included = [], set()
            visible = "\n".join(l for l, active in zip(raw.splitlines(), prose_lines(raw.splitlines())) if active)
            while True:
                added = False
                for key, definition in self.definitions[page.source].items():
                    pattern = r"\[" + re.escape(key) + r"\](?!:)"
                    if key not in included and re.search(pattern, visible, re.I):
                        included.add(key)
                        if not re.search(r"^(?:> ?)* {0,3}\[" + re.escape(key) + r"\]:", raw, re.M | re.I):
                            normalized = re.sub(r"^> ?", "", definition, flags=re.M)
                            appendix.append(self.rewrite(normalized, page))
                            visible += "\n" + normalized
                            added = True
                if not added:
                    break
            for key in re.findall(r"\[\^([^\]]+)\](?!:)", visible):
                if "^" + key.casefold() not in self.definitions[page.source]:
                    self.warnings.add(f"原文脚注缺少定义：{page.source} → {key}")
            navigation = self.navigation(page, index)
            chapter_link = relative(page.path, f"notes/{Path(page.source).stem}/README.md")
            source_url = f"https://github.com/{REPOSITORY}/blob/{self.metadata['commit']}/{page.source}#L{page.start+1}-L{page.end}"
            header = f"<!-- 自动生成；个人补充请写入 personal/。 -->\n\n{navigation}\n\n> 所属章节：[{label(self.document_title(page.source))}]({chapter_link})\n>\n> 来源：[原文及行号]({source_url}) · [在线原书](https://bojieli.github.io/ai-agent-book/book/{Path(page.source).stem}/)\n\n"
            children = [child for child in self.pages if child.parent == page.path and child.path != page.path]
            footer = ""
            if children:
                footer += "\n## 阅读目录\n\n" + "\n".join(f"- [{label(child.title)}]({relative(page.path, child.path)})" for child in children) + "\n"
            if appendix:
                footer += "\n<!-- 补齐本页引用的原文定义 -->\n\n" + "\n".join(appendix)
            footer += "\n---\n\n" + navigation + "\n"
            self.outputs[page.path] = (header + "<!-- 原文开始 -->\n" + content + "\n<!-- 原文结束 -->\n" + footer).encode()
            self.coverage.append({"source": page.source, "output": page.path,
                                  "start_line": page.start+1, "end_line": page.end, "source_sha256": digest(raw.encode())})
        self.indexes()
        for source, target, anchor in self.links:
            if target.startswith("notes/") and target not in self.outputs:
                raise ValueError(f"内部链接目标缺失：{source} → {target}")
            if anchor and target.startswith("notes/") and f'id="{html.escape(anchor, quote=True)}"' not in self.outputs[target].decode():
                raise ValueError(f"内部锚点缺失：{source} → {target}#{anchor}")
        for path, data in self.files.items():
            self.outputs["source/" + path] = data
        metadata = dict(self.metadata, paths=sorted(self.remote_paths))
        self.outputs["source/upstream.json"] = json_bytes(metadata)
        report = ["# 同步记录", "", f"上游：{REPOSITORY}", f"", f"固定版本：`{metadata['commit']}`", "",
                  f"完整原文：{len(DOCUMENTS)} 篇；阅读页面：{len(self.pages)}；图片资源：{sum(p.startswith('book/images/') for p in self.files)}。", "",
                  "已核对全部原文切片连续覆盖、源文件内容校验和、本地图片及内部链接。", "", "## 上游内容问题", ""]
        report += sorted(self.warnings) if self.warnings else ["本次未发现缺失的上游目标或脚注定义。"]
        self.outputs["source/README.md"] = ("\n".join(report) + "\n").encode()
        return self.outputs

    def indexes(self):
        roots = [p for p in self.pages if p.parent == "README.md"]
        toc = "\n".join(f"- [{label(self.document_title(p.source))}]({quote(p.path, safe='/')})" for p in roots)
        self.outputs["README.md"] = f"""# Agent Book 分块阅读版

按原书目录拆分《深入理解 AI Agent》，保留完整原文、图片、代码、公式、表格、例子、小结、思考题和参考资料。

[从引言开始阅读](notes/introduction/README.md) · [学习入口](learning/README.md) · [个人笔记](personal/README.md)

## 全书目录

{toc}

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

- [原书网站](https://bojieli.github.io/ai-agent-book/) · [原始项目](https://github.com/{REPOSITORY})
- [固定来源版本与同步记录](source/README.md) · [原文快照](source/book/) · [原项目许可证](source/LICENSE)
- 本仓库正文为原文拆分重排，不是摘要；调整仅限目录导航、链接、锚点、脚注补齐和 Markdown 排版适配。
- `notes/` 和 `source/` 为生成内容；心得与补充放在 `personal/`，不会被同步修改。
- [迁移前的旧笔记](personal/legacy/notes/)已完整保留，其中第2章包含原来的学习摘要。归档不属于新版阅读目录。
""".encode()
        self.outputs["learning/README.md"] = """# 学习入口

[打开完整阅读目录](../README.md) · [从引言开始](../notes/introduction/README.md)

每页提供来源、返回目录、上一篇和下一篇。先阅读章前导读及主题说明，再进入知识块；原文图片、代码、脚注、小结和思考题均保留。

[个人笔记](../personal/README.md)用于保存自己的解释、疑问和阅读位置。

[原学习进度](progress.md)按原样保留，其中章节编号及统计沿用旧版，不代表本次生成内容的阅读状态；本次改造没有替你标记已学习或重置进度。
""".encode()


def inventory(root, prefix):
    directory = root / prefix
    if not directory.exists():
        return {}
    return {str(p.relative_to(root)): checked_path(root, str(p.relative_to(root))).read_bytes()
            for p in directory.rglob("*") if p.is_file() or p.is_symlink()}


def verify_managed(root, manifest):
    for name, expected in manifest["files"].items():
        path = checked_path(root, name)
        if not path.is_file() or digest(path.read_bytes()) != expected:
            raise ValueError(f"生成文件有手工修改或缺失，请先保存个人内容：{name}")
    for prefix in ("notes", "source"):
        for name in inventory(root, prefix):
            if name != MANIFEST and name not in manifest["files"]:
                raise ValueError(f"生成区存在未知文件，请移到 personal/：{name}")


def check_reading_links(root, outputs, archive, old_files):
    """检查实际生成的 Markdown，包括导航；不把代码示例当作链接。"""
    available = set(outputs) | set(archive)
    for name, data in outputs.items():
        if not (name.startswith("notes/") or name in {"README.md", "learning/README.md"}):
            continue
        lines = data.decode().splitlines(keepends=True)
        for line, active in zip(lines, prose_lines(lines)):
            if not active:
                continue
            protected = [(m.start(), m.end()) for m in INLINE_CODE.finditer(line)]
            for match in LINK.finditer(line):
                if any(start <= match.start() < end for start, end in protected):
                    continue
                url = urlsplit(match["url"].strip("<>"))
                if url.scheme or url.netloc:
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(url.path)))
                exists = target in available or any(p.startswith(target.rstrip("/") + "/") for p in available)
                if not exists and target not in old_files:
                    exists = checked_path(root, target).exists()
                if not exists:
                    raise ValueError(f"生成链接缺失：{name} → {target}")
                if url.fragment and target in outputs and target.endswith(".md"):
                    anchor = html.escape(unquote(url.fragment), quote=True)
                    if f'id="{anchor}"' not in outputs[target].decode():
                        raise ValueError(f"生成锚点缺失：{name} → {target}#{anchor}")


def install(root, outputs, old_files, archive):
    """先完整预检，再逐文件原子替换；写入异常时恢复已操作文件。"""
    changes = dict(outputs, **archive)
    for name, data in changes.items():
        path = checked_path(root, name)
        if path.exists() and name not in old_files and path.read_bytes() != data:
            raise ValueError(f"拒绝覆盖未登记文件：{name}")
    names = set(old_files) | set(changes)
    before = {name: checked_path(root, name).read_bytes() if (root / name).is_file() else None for name in names}
    with tempfile.TemporaryDirectory(prefix="agent-book-install-") as temp:
        stage = Path(temp)
        for name, data in changes.items():
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        touched = []
        try:
            for name in sorted(names):
                target = root / name
                data = changes.get(name)
                if data == before[name]:
                    continue
                touched.append(name)
                if data is None:
                    target.unlink()
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    # 临时文件位于目标目录，确保替换不跨文件系统。
                    with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as handle:
                        handle.write((stage / name).read_bytes())
                        temporary = Path(handle.name)
                    try:
                        os.replace(temporary, target)
                    finally:
                        temporary.unlink(missing_ok=True)
        except BaseException:
            for name in reversed(touched):
                target = root / name
                if before[name] is None:
                    target.unlink(missing_ok=True)
                else:
                    target.write_bytes(before[name])
            raise
    for prefix in ("notes", "source"):
        for path in sorted((root / prefix).rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if path.is_dir() and not any(path.iterdir()):
                path.rmdir()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", action="store_true", help="手动下载同一上游版本的完整正文和图片")
    parser.add_argument("--ref", default="main", help="同步的上游分支、标签或提交")
    parser.add_argument("--source-dir", type=Path, help="使用已下载且带 upstream.json 的快照")
    parser.add_argument("--check", action="store_true", help="只检查，不写入仓库")
    parser.add_argument("--migrate-legacy", action="store_true", help="首次运行时完整归档旧笔记")
    args = parser.parse_args()
    if args.check and (args.sync or args.migrate_legacy or args.source_dir):
        parser.error("--check 仅检查当前已保存的版本")
    if args.sync and args.source_dir:
        parser.error("--sync 与 --source-dir 不能同时使用")
    manifest_path = ROOT / MANIFEST
    old = json.loads(manifest_path.read_text()) if manifest_path.exists() else None
    archive = {}
    if old:
        if args.migrate_legacy:
            raise ValueError("已经迁移过，不重复归档")
        verify_managed(ROOT, old)
        old_files = set(old["files"]) | {MANIFEST}
    else:
        if not args.migrate_legacy:
            raise ValueError("首次生成需使用 --migrate-legacy，先保存旧笔记")
        if (ROOT / "personal/legacy").exists():
            raise ValueError("旧笔记归档已存在，停止以避免覆盖")
        legacy = {**inventory(ROOT, "notes"), **inventory(ROOT, "learning")}
        legacy["README.md"] = (ROOT / "README.md").read_bytes()
        archive = {"personal/legacy/" + name: data for name, data in legacy.items()}
        archive["personal/README.md"] = ("# 个人笔记\n\n这里保存个人心得、疑问和阅读位置，不受原书同步影响。\n\n"
                                          "[迁移前笔记](legacy/notes/) · [原第2章摘要](legacy/notes/chapter2/README.md) · [旧学习记录](legacy/learning/progress.md)\n\n"
                                          "旧笔记按字节完整归档，历史断链与章节名称也原样保留；完整阅读请使用[新版目录](../README.md)。\n").encode()
        old_files = set(inventory(ROOT, "notes")) | {"README.md", "learning/README.md"}
    with tempfile.TemporaryDirectory(prefix="agent-book-source-") as temp:
        directory = args.source_dir or ROOT / "source"
        if args.sync:
            directory = Path(temp)
            download_snapshot(directory, args.ref)
        metadata, files = load_snapshot(directory)
        book = Book(metadata, files)
        outputs = book.render()
        manifest = {"version": 1, "upstream_commit": metadata["commit"],
                    "files": {name: digest(data) for name, data in sorted(outputs.items())}, "coverage": book.coverage}
        outputs[MANIFEST] = json_bytes(manifest)
        check_reading_links(ROOT, outputs, archive, old_files)
        if args.check:
            differences = [name for name, data in outputs.items() if not (ROOT / name).is_file() or (ROOT / name).read_bytes() != data]
            if differences or set(old["files"]) != set(outputs) - {MANIFEST}:
                raise ValueError("当前文件与完整重建结果不一致：" + ", ".join(differences[:5]))
        else:
            # 下载可能耗时，落盘前再次检查，避免覆盖同步期间的新编辑。
            if old:
                if json.loads(manifest_path.read_text()) != old:
                    raise ValueError("同步期间来源清单发生变化，请重新运行")
                verify_managed(ROOT, old)
            elif any((ROOT / name).read_bytes() != legacy[name] for name in old_files):
                raise ValueError("迁移期间旧笔记发生变化，请重新运行以完整归档")
            install(ROOT, outputs, old_files, archive)
        print(f"{'检查通过' if args.check else '生成完成'}：{len(DOCUMENTS)} 篇原文，{len(book.pages)} 个阅读页面，"
              f"{sum(name.startswith('book/images/') for name in files)} 个图片资源；来源 {metadata['commit']}")
        for warning in sorted(book.warnings):
            print("上游提示：" + warning)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        print(f"停止：{error}", file=sys.stderr)
        sys.exit(1)
