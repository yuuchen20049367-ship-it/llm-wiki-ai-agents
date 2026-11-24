---
title: LLM Wiki（idea file）
author: Andrej Karpathy
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
type: 方法來源（不計入主題來源）
retrieved: 2026-11-24
reliability: A
read_depth: 部分內文
---
重點（自行改寫）：
- 不是每次提問都從原始文件重新檢索，而是讓 LLM 持續建立並維護一組互相連結的 markdown 頁面（wiki）。
- 三層：原始來源（只讀）、wiki（LLM 寫）、schema（規則）。三種操作：ingest、query、lint。
- index.md 是內容目錄，查詢時先讀；log.md 是只增不減的時間紀錄。
