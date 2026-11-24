---
title: 反思（Reflection）
type: concept
sources: [ng-agentic-ai-course, reflexion-shinn-2023, anthropic-building-effective-agents]
---
- 反思模式是讓 AI 批評自己的成果並迭代改進，類似自動化的程式碼審查。[[sources/ng-agentic-ai-course]]
- 反思可以納入執行時的訊號與外部工具回饋，不只靠模型自評。[[sources/ng-agentic-ai-course]]
- Reflexion：用文字回饋取代更新權重；agent 對回饋口語反思並存進記憶，下次嘗試時參考。[[sources/reflexion-shinn-2023]]
- Reflexion 的回饋來源有三類：二元環境回饋、預設的失敗啟發式規則、LLM 自我評估。[[sources/reflexion-shinn-2023]]
- 成果：HumanEval pass@1 為 91%，高於當時 GPT-4 的 80%。[[sources/reflexion-shinn-2023]]
- 在 workflow 中對應 evaluator-optimizer：有明確評估標準且迭代有價值時效果好。[[sources/anthropic-building-effective-agents]]

相關：[[concepts/workflow-patterns]]、[[concepts/memory]]
