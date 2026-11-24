#!/usr/bin/env python3
"""LLM Wiki lint：檢查連結、frontmatter、來源引用、孤兒頁、閱讀深度、數字是否有出處。"""
import re, sys, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
GENERATED = {"lint-report"}

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    d = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                d[k.strip()] = v.strip()
    return d, text[m.end():] if m else text

pages = {p.relative_to(WIKI).with_suffix("").as_posix(): p for p in WIKI.rglob("*.md")}
raw_cards = {p.name: p for p in RAW.glob("*.md")}
errors, warns, infos = [], [], []

# 1 frontmatter
meta = {}
for stem, p in pages.items():
    d, body = fm(p.read_text(encoding="utf-8"))
    meta[stem] = (d, body)
    for k in ("title", "type"):
        if k not in d:
            errors.append(f"[frontmatter] {stem} 缺少 {k}")

# 2 links
links = {}
for stem, (d, body) in meta.items():
    ls = re.findall(r"\[\[([^\]]+)\]\]", body)
    links[stem] = ls
    for l in ls:
        if l not in pages and l not in GENERATED:
            errors.append(f"[連結] {stem} 的 [[{l}]] 找不到頁面")

# 3 factual bullets need a source link (concept pages)
for stem, (d, body) in meta.items():
    if not stem.startswith("concepts/"):
        continue
    for line in body.splitlines():
        s = line.strip()
        if re.match(r"^(-|\d+\.)\s", s) and "[[sources/" not in s and not s.startswith("- 標註") and not s.startswith("- 相關"):
            errors.append(f"[引用] {stem} 有句子沒有來源：{s[:30]}…")

# 4 sources: frontmatter stems exist
for stem, (d, body) in meta.items():
    if "sources" in d:
        for s in re.findall(r"[\w\-]+", d["sources"].strip("[]")):
            if f"sources/{s}" not in pages:
                errors.append(f"[來源] {stem} 的 sources 欄位 {s} 找不到來源頁")

# 5 orphan pages
index_links = set(links.get("index", []))
for stem in pages:
    if stem not in ("index",) and stem not in index_links and stem not in GENERATED:
        warns.append(f"[孤兒頁] {stem} 沒有被 index.md 連到")

# 6 read depth
weak = {}
for stem, (d, body) in meta.items():
    if stem.startswith("sources/") and d.get("read_depth", "") not in ("全文", "課程頁全文"):
        weak[stem] = d.get("read_depth", "未標示")
for s, depth in weak.items():
    users = [c for c, (d, b) in meta.items() if c.startswith("concepts/") and f"[[{s}]]" in b]
    warns.append(f"[閱讀深度] {s}（{depth}）被 {len(users)} 個概念頁引用：{', '.join(u.split('/')[1] for u in users)} → 待查全文")

# 7 raw cards required keys
for name, p in raw_cards.items():
    d, _ = fm(p.read_text(encoding="utf-8"))
    for k in ("url", "retrieved", "reliability", "read_depth"):
        if k not in d:
            errors.append(f"[來源卡] {name} 缺少 {k}")

# 8 numbers must appear in raw cards
raw_text = "\n".join(p.read_text(encoding="utf-8") for p in raw_cards.values())
for stem, (d, body) in meta.items():
    if stem in ("log", "index"):
        continue
    for n in set(re.findall(r"\d+(?:\.\d+)?%", body)):
        if n not in raw_text:
            errors.append(f"[數字] {stem} 的 {n} 在來源卡中找不到")

# 9 source count
topic_cards = [n for n, p in raw_cards.items() if "不計入" not in p.read_text(encoding="utf-8")]
infos.append(f"主題來源卡 {len(topic_cards)} 張（作業要求至少 5 篇）：{'達標' if len(topic_cards) >= 5 else '未達標'}")
infos.append(f"wiki 頁面 {len(pages)} 頁，連結 {sum(len(v) for v in links.values())} 條")

today = datetime.date(2026, 11, 24).isoformat()
lines = [f"---\ntitle: Lint 報告\ntype: report\n---\n# Lint 報告（{today}）\n"]
lines += [f"## 錯誤（{len(errors)}）"] + ([f"- {e}" for e in errors] or ["- 無"])
lines += [f"\n## 警告（{len(warns)}）"] + ([f"- {w}" for w in warns] or ["- 無"])
lines += ["\n## 資訊"] + [f"- {i}" for i in infos]
report = "\n".join(lines) + "\n"
(WIKI / "lint-report.md").write_text(report, encoding="utf-8")
print(report)
sys.exit(1 if errors else 0)
