---
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
author: Noah Shinn 等
url: https://arxiv.org/abs/2303.11366
type: 論文（NeurIPS 2023）
published: 2023-03-20
retrieved: 2026-11-24
reliability: A
read_depth: 部分內文
---
重點（自行改寫）：
- 不更新模型權重，而是用「文字形式的回饋」強化 agent：agent 對任務回饋做口語反思，並把反思文字存進情節記憶，下一次嘗試時參考。
- 回饋來源有三類：二元的環境回饋、預先定義的失敗啟發式規則、LLM 自我評估。
- 在 HumanEval 程式題上 pass@1 達 91%，高於當時 GPT-4 的 80%；在 AlfWorld 決策任務上，12 次迭代學習後比強基線高出絕對 22%。
