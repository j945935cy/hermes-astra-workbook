# 第 13 章管理實作附頁

通用欄位直接使用共用四模板，不另複製一套：
- [任務授權](../../templates/management/task-authorization.md)
- [驗收簽收](../../templates/management/acceptance-handoff.md)
- [未決與變更](../../templates/management/issues-changes.md)
- [採用維運](../../templates/management/adoption-operations.md)

以下只附本例特有欄位。所有空白填「待確認」；作者示意不是簽核或模型紀錄。表單以編輯器另存到私人練習目錄；prepare 不會複製本頁。

## fee-v1 章別需求與交付附頁

需求示意：F01 regular 三張 810／兩張 600；F02 student 三張 540、四張 720／兩張 400；F03 非正整數（含 True）與未知票種 ValueError。主辦人角色批准，姓名／時間未填就不宣稱真實簽核。混票、退款、稅額不納入。

| 交付欄位 | 作者參考 | 讀者空白紀錄 |
|---|---|---|
| 需求版本／批准人與時間 | fee-v1 虛構示意，無真實簽核 | 待填 |
| 變更檔 | fee.py；新增回歸 test_fee.py | 待填 |
| 原紅燈 | 原測試 900 != 810 | 待填原因及證據 |
| 補測 | reference/test_fee.py 保留原方法，加學生門檻、前一張、非法值；補測可立即綠燈 | 待填名稱對應行為 |
| 開發驗收 | python3 -B -m unittest -v，實測見 verification.md | 待填命令、退出碼、證據 |
| 獨立驗收 | python3 -B acceptance.py，實測見 verification.md | 待填命令、退出碼、證據 |
| 人工判斷／下一步 | 教材參考；不准正式帳務上線 | 待填人名、時間、准／退回、限制 |

只在補測階段允許新增 test_fee.py 方法；步驟二只改 fee.py。既有預期值與 acceptance.py 不改。學生兩張折扣另建 fee-v2 並先用共用變更卡批准，保留 fee-v1。完整四項回歸參考 `reference/test_fee.py` 不由 prepare 預置。
