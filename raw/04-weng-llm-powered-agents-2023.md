---
title: LLM Powered Autonomous Agents
author: Lilian Weng
url: https://lilianweng.github.io/posts/2023-06-23-agent/
type: 技術部落格（領域內公認的綜述文章）
published: 2023-06-23
retrieved: 2026-11-24
reliability: A
read_depth: 僅摘要
---
重點（自行改寫；本次只讀到搜尋摘要片段，待查全文）：
- LLM 是 agent 的「大腦」，搭配三個零件：Planning（規劃）、Memory（記憶）、Tool use（工具使用）。
- Planning 包含任務分解成子目標，以及自我批評與反思並修正。LLM+P 是把規劃外包給傳統規劃器（用 PDDL 描述問題）。
- Memory：短期記憶相當於情境內學習；長期記憶多靠外部向量資料庫與快速檢索（MIPS、近似最近鄰）。
- Tool use：呼叫外部 API 取得模型權重裡沒有的資訊，例如即時資訊、執行程式碼、私有資料。例子有 MRKL、Toolformer、TALM、HuggingGPT。
- AutoGPT、GPT-Engineer、BabyAGI 被當作概念驗證範例。
