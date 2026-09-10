# 人工參考交付說明（非執行紀錄）

## 起始狀態
此檔只供比對，不是已生成的模型成果。先準備新一期資料夾。
本期來源快照：input/tasks.csv、input/notes.md。先讀 report.md，再核對 actions.csv。

## 精確命令與預期產物
在本期根目錄執行 `python3 -B verify.py`，預期 ACCEPTED 訊息；不會新增文件。

## 正負向測試
人工參考 CSV 應接受；副本擅填 G04 日期應拒絕。用配套根目錄 `python3 -B -m unittest discover -s tests -v` 重現。

## 重跑與停止
另建未使用的新一期資料夾，保存本期 input 快照、task-spec.md、verify.py；output 從空目錄開始。任一目標已存在（含目錄、符號連結）就停止，不覆寫、不刪除、不自行另名；中斷後也不接管部分舊成果。只可在本次確認全空而開始的執行內修正新輸出。

## 未驗證界線
機械驗收不替代語義與停止行為檢查；模型、排程、通知、MCP 未驗證。
