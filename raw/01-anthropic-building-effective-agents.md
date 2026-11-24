---
title: Building effective agents
author: Anthropic（Erik S., Barry Zhang）
url: https://www.anthropic.com/research/building-effective-agents
type: 官方技術文章
published: 2024-12-19
retrieved: 2026-11-24
reliability: A
read_depth: 全文
---
重點（自行改寫）：
- 把「讓 LLM 做事的系統」統稱 agentic systems，再分成 workflow（預先寫好的程式路徑）與 agent（LLM 自己動態決定流程與工具）。
- 建議先找最簡單的解法；很多應用只要「一次 LLM 呼叫 + 檢索 + 範例」就夠。
- 基本積木是 augmented LLM（LLM + 檢索、工具、記憶）。
- 五種 workflow：prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。
- Agent 本質是 LLM 依環境回饋在迴圈中使用工具；要有停止條件（例如最大迭代次數）；成本較高、錯誤可能累積。
- 三原則：簡單、透明（顯示規劃步驟）、把 agent-computer interface（ACI）的工具文件與測試做好。
- 他們做 SWE-bench 代理時，花在最佳化工具的時間比最佳化 prompt 還多。
- 頁面註記：文中許多工具生態在 2024 年 12 月之後已改變。
