# 讀者入門

## 先備條件

能下載與解壓縮檔案，並知道輸入資料與輸出資料的差別。第一個練習不要求 Python 或 Git。

本書規劃以 Windows＋WSL2 為主要命令列實驗環境；其他平台差異將於實測後補充。第一個練習素材本身是純文字，並不代表所有平台都已測試。

## 安裝與模型

依 [Hermes 官方安裝文件](https://hermes-agent.nousresearch.com/docs/getting-started/installation) 安裝，依 [模型設定文件](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models) 連接你有權使用的模型。

本教材以 GPT-6 Astra 為目標；能否使用取決於供應商、帳號資格與實際設定，不保證所有訂閱都能使用，也不保證免費。先確認供應商顯示的計費或用量限制。不要把憑證貼到 Issues。

## 第一個成果

開啟 `examples/first-task/README.md`，只允許讀取虛構素材並新增 `output/action-items.md`。結果需以來源逐項人工驗收，不能只問模型「你完成了嗎」。
