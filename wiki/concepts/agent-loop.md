---
title: Agent 的運作迴圈
type: concept
sources: [anthropic-building-effective-agents]
---
- Agent 從人類的指令或討論開始；任務明確後自行規劃與執行，必要時回頭問人。[[sources/anthropic-building-effective-agents]]
- 每一步都要從環境取得「真實回饋」（例如工具回傳結果、程式執行結果）來判斷進度。[[sources/anthropic-building-effective-agents]]
- 可在檢查點或遇到阻礙時暫停徵求人的意見；也常設停止條件，例如最大迭代次數，以維持控制。[[sources/anthropic-building-effective-agents]]
- 實作往往很單純：LLM 依環境回饋，在迴圈中使用工具。[[sources/anthropic-building-effective-agents]]
- 風險：成本較高，且錯誤可能累積；建議在沙盒中充分測試並加上護欄。[[sources/anthropic-building-effective-agents]]

相關：[[concepts/react]]、[[concepts/when-to-use-agents]]
