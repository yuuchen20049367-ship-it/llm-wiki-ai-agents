---
title: 綜整：AI Agent 是什麼？（新手版）
type: synthesis
sources: [anthropic-building-effective-agents, weng-llm-powered-agents-2023, ng-agentic-ai-course, react-yao-2022, reflexion-shinn-2023]
---
## 一句話
AI Agent 是讓 LLM 依環境回饋，在迴圈中自己決定下一步、使用工具來完成任務的系統。[[concepts/agent-loop]]

## 由簡單到複雜的四個階段
1. 單次 LLM 呼叫（加上檢索與範例），許多應用其實就夠了。[[concepts/when-to-use-agents]]
2. 增強型 LLM：加上檢索、工具、記憶。[[concepts/augmented-llm]]
3. Workflow：流程由程式事先寫好。[[concepts/agentic-systems]]、[[concepts/workflow-patterns]]
4. Agent：流程由 LLM 自己動態決定。[[concepts/agentic-systems]]

## Agent 的三個零件
規劃、記憶、工具。[[concepts/planning]]、[[concepts/memory]]、[[concepts/tool-use]]（此框架來自 Weng 的綜述，該來源待查全文）

## 四個常見設計模式
反思、工具使用、規劃、多代理。[[concepts/reflection]]、[[concepts/tool-use]]、[[concepts/planning]]、[[concepts/multi-agent]]

## 兩個代表性研究
- ReAct：邊推理邊行動。[[concepts/react]]
- Reflexion：用文字反思學習。[[concepts/reflection]]

## 使用上的提醒
簡單優先、注意成本與錯誤累積、把工具介面設計好。[[concepts/when-to-use-agents]]、[[concepts/aci-tool-design]]

## 比喻（本 wiki 作者補充，非來源內容）
Workflow 像照食譜一步一步做菜；Agent 像自己決定要買什麼、怎麼煮、嚐過味道再調整的廚師。
