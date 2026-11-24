---
title: 五種 Workflow 模式
type: concept
sources: [anthropic-building-effective-agents]
---
1. **Prompt chaining**：把任務拆成固定步驟，每次 LLM 呼叫處理上一步的輸出，中間可加程式檢查（gate）確認沒跑偏。[[sources/anthropic-building-effective-agents]]
2. **Routing**：先分類輸入，再導向專門的後續處理。[[sources/anthropic-building-effective-agents]]
3. **Parallelization**：多個 LLM 同時處理，再由程式彙整；分成分段（sectioning）與投票（voting）兩種。[[sources/anthropic-building-effective-agents]]
4. **Orchestrator-workers**：中央 LLM 動態拆解任務、分派給工作者 LLM，再整合結果；子任務不是預先定好的。[[sources/anthropic-building-effective-agents]]
5. **Evaluator-optimizer**：一個 LLM 生成答案，另一個評估並回饋，形成迴圈；適合有明確評估標準、且迭代能帶來可衡量改善的情況。[[sources/anthropic-building-effective-agents]]

相關：[[concepts/reflection]]、[[concepts/agentic-systems]]
