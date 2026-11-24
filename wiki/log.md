---
title: 操作紀錄（只增不減）
type: log
---
## [2026-11-24] setup | 建立 wiki 骨架與 CLAUDE.md
- 主題定為「AI Agents 是什麼？」，方法參考 Karpathy 的 LLM Wiki 模式。

## [2026-11-24] ingest | 01 Anthropic〈Building effective agents〉
- 讀全文；分級 A。建立 sources 頁與 6 個概念頁。

## [2026-11-24] ingest | 02 ReAct、03 Reflexion
- 讀摘要與部分內文；分級 A；標註待查全文。

## [2026-11-24] ingest | 04 Weng 綜述
- 搜尋結果大量是二手整理（部落格、社群貼文、第三方筆記），一手頁面只讀到片段。
- 只採用一手頁面片段，二手內容不當依據；閱讀深度標為「僅摘要」，所有引用處加註「待查全文」。

## [2026-11-24] workflow 修改 | 新增 ingest 前置品質關卡
- 原因：取得資料這一步最常拿到二手、雜訊多的結果。
- 做法：來源卡必須先標可信度（A/B）與閱讀深度，核心主張只能來自 A；規則寫入 CLAUDE.md 第 3、4 條。

## [2026-11-24] ingest | 05 Ng 課程頁、06 Karpathy 方法
- 05 只讀課程頁介紹；06 為方法來源，不計入 5 篇主題來源。

## [2026-11-24] 待使用者確認的重點
- 本次重點由 AI 先整理；請使用者閱讀 sources 與 concepts 頁，確認要強調的概念，再進入簡報生成。

## [2026-11-24] lint | 第一次 lint
- 結果：錯誤 0；警告 3（ReAct、Reflexion、Weng 三個來源只讀到摘要或部分內文，待查全文）。
- 處理：警告不影響進入簡報階段，但簡報中引用這三個來源的內容必須保持保守，並在簡報上標註。

## [2026-11-24] query | 規劃簡報大綱
- 先讀 index.md，再讀 synthesis/what-is-an-ai-agent 與各概念頁，決定 7 張投影片，每張標註 wiki 依據（data-src）。

## [2026-11-24] check | 第一次簡報檢查（tools/check_deck.py）
- 結果：7 張投影片都有 wiki 依據，簡報中的數字（91%、80%）都能在來源卡找到；通過，未觸發重新生成。
- 簡報中引用 Weng、ReAct、Reflexion 的地方，都已在頁面上標註「待查全文」。
