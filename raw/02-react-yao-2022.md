---
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
author: Shunyu Yao 等
url: https://arxiv.org/abs/2210.03629
type: 論文（ICLR 2023）
published: 2022-10-06
retrieved: 2026-11-24
reliability: A
read_depth: 部分內文
---
重點（自行改寫）：
- 讓 LLM 以交錯方式產生「推理過程」與「行動」。推理幫助追蹤與修正計畫、處理例外；行動讓模型向外界（例如 Wikipedia API）取得資訊。
- 在問答（HotpotQA）與事實查核（Fever）上，能減少純思維鏈推理常見的幻覺與錯誤傳遞，且過程比較容易讓人看懂。
- 在 ALFWorld 與 WebShop 上，成功率分別比模仿學習與強化學習方法高出絕對 34% 與 10%，而且只用一兩個範例提示。
