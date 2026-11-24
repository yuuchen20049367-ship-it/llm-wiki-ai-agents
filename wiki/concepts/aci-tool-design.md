---
title: Agent 與電腦的介面（ACI）：工具設計
type: concept
sources: [anthropic-building-effective-agents]
---
- 工具的定義與說明，應和整體 prompt 一樣花心思設計。[[sources/anthropic-building-effective-agents]]
- 類比：人機介面（HCI）要花多少力氣，agent-computer interface（ACI）就該花同樣多。[[sources/anthropic-building-effective-agents]]
- 做法：站在模型的角度檢查工具好不好懂、參數名稱與說明要清楚、用大量範例輸入測試找出常犯錯誤、並設計得讓人（與模型）較難用錯（poka-yoke）。[[sources/anthropic-building-effective-agents]]
- 案例：Anthropic 做 SWE-bench 代理時，花在最佳化工具的時間比最佳化整體 prompt 更多；把工具改成一律要求絕對路徑後，模型就不再弄錯路徑。[[sources/anthropic-building-effective-agents]]

相關：[[concepts/tool-use]]
