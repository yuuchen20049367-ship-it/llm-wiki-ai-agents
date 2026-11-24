#!/usr/bin/env python3
"""簡報檢查節點：每張投影片都要有 wiki 依據；簡報裡的數字必須在 wiki / 來源卡找得到。"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
deck = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
wiki_text = "\n".join(p.read_text(encoding="utf-8") for p in list((ROOT/"wiki").rglob("*.md")) + list((ROOT/"raw").glob("*.md")))
problems = []
slides = re.findall(r'<section class="slide"([^>]*)>(.*?)</section>', deck, re.S)
print(f"投影片數：{len(slides)}")
for n, (attrs, body) in enumerate(slides, 1):
    m = re.search(r'data-src="([^"]*)"', attrs)
    if not m:
        problems.append(f"第 {n} 張沒有 data-src（沒有 wiki 依據）"); continue
    for stem in m.group(1).split(","):
        if not (ROOT/"wiki"/f"{stem}.md").exists():
            problems.append(f"第 {n} 張引用的 wiki 頁不存在：{stem}")
    text = re.sub(r"<[^>]+>", " ", body)
    for num in set(re.findall(r"\d+(?:\.\d+)?%", text)):
        if num not in wiki_text:
            problems.append(f"第 {n} 張的數字 {num} 在 wiki 找不到出處")
    print(f"第 {n} 張：依據 {m.group(1)} ✓")
print("結果：", "通過" if not problems else "有問題")
for p in problems: print(" -", p)
sys.exit(1 if problems else 0)
