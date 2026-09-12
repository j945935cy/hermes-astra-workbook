# 任務範本（貼入對話，不是 Shell）

依順序逐段執行；涉及修改既有產物的步驟須先審閱並確認。

## 任務 1

讀 registrations.csv 與 rules.md。
先建立 preview.md，逐列列出預計分類與理由，不寫正式三份 CSV。
計算交給 Python 的 csv 模組與集合處理，不靠聊天文字心算。
指出規則是否有歧義；若沒有，等待我確認後才建立整理腳本。

## 預覽確認後的清理程式任務

使用標準函式庫新增 clean_registrations.py；相對腳本讀取素材。同名輸出存在（含符號連結）就停止，不覆寫。只有人工確認 preview.md 後才執行，最後回讀三份 CSV 與 summary.md。這是配套整理的工作單，章內未提供清理程式參考實作。

## 人工作業交接

另建 operations.md：本次用途、clean 可用範圍／尚待核准、R4/R5/R6/R8 的待詢問角色及回覆狀態；未知角色待指定。部分名單能否先交由資料擁有人決定，exceptions 不等於取消資格。不改固定 summary.md 或 CSV schema。
