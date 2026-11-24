---
title: 什麼時候該用 Agent
type: concept
sources: [anthropic-building-effective-agents, ng-agentic-ai-course]
---
- 先找最簡單的解法，必要時才增加複雜度，甚至可以完全不做 agentic 系統。[[sources/anthropic-building-effective-agents]]
- 很多應用只要最佳化單次 LLM 呼叫，加上檢索與範例就夠。[[sources/anthropic-building-effective-agents]]
- Agentic 系統常以延遲與成本換取更好的表現，要想清楚值不值得。[[sources/anthropic-building-effective-agents]]
- 適合的情境：任務需要對話與行動、有明確成功標準、能形成回饋迴圈、並有適當人類監督；例如客服與程式碼代理（程式可用自動測試驗證）。[[sources/anthropic-building-effective-agents]]
- 三原則：保持簡單、透明（顯示規劃步驟）、把工具文件與測試做好。[[sources/anthropic-building-effective-agents]]
- 框架能加速起步，但可能遮住底層的提示與回應、增加除錯難度；建議先直接用 API。[[sources/anthropic-building-effective-agents]]
- Ng 的課程把評估（evals）、錯誤分析與元件層級評估列為實務重點。[[sources/ng-agentic-ai-course]]

相關：[[concepts/agent-loop]]、[[concepts/agentic-systems]]
