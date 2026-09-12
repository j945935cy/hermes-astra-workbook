# 第 15 章管理實作附頁

通用欄位直接使用共用四模板，不另複製一套：
- [任務授權](../../templates/management/task-authorization.md)
- [驗收簽收](../../templates/management/acceptance-handoff.md)
- [未決與變更](../../templates/management/issues-changes.md)
- [採用維運](../../templates/management/adoption-operations.md)

以下只附本例特有欄位。所有空白填「待確認」；作者示意不是簽核或模型紀錄。表單以編輯器另存到私人練習目錄；prepare 不會複製本頁。

## collaboration-record.md 章別附頁

路線（選一）：人工分工演練／真實 delegation 試作。人工按 A、B 各自工作單保存兩報告，最後自己整合；無工具也可完成，不冒稱委派通過。真實路線需兩次工作 ID、完成事件與來源／三報告讀回紀錄，仍待模型實測。

A 工作單：只讀 sessions.csv、contract.md；只寫 capacity.md；依 registered > capacity 列 ID、差額、原值，禁止改來源。B 工作單：同輸入；只寫 ownership.md；列 confirmed 且空 owner，說明 draft 排除。工作目錄填各自可達的絕對路徑。整合者獨占 final.md，核對來源後才合併。每份報告填輸入與契約版。

| 工作 ID | 輸入／契約版 | 報告位置 | 截止 | 完成／驗收 | 決策者 |
|---|---|---|---|---|---|
| 人工-A 或真實 ID | 待填 | 本輪 capacity.md | 待填 | 未開始 | 待填 |
| 人工-B 或真實 ID | 待填 | 本輪 ownership.md | 待填 | 未開始 | 待填 |

開工決策（先填上限）：單代理基準＝未知；可平行部分＝兩項檢查；呼叫上限＝待批准；重試上限＝待批准；人工審查時間上限＝待批准；準備／重複讀取／等待／整合／審查／重工實際時間＝分項未知；供應商實際用量／費用＝未知。沒有基準不說更省。上限未填只走不用模型的人工線；達上限停或退回單代理。

桌面故障演練：B 未完成→截止時人決定等或部分交付，空白不是零問題；A 遲到→版本核對後只由整合者納入新版本，不覆蓋已批准 final；來源不同版→停止混合，重交一致來源。接手須先查舊狀態，unknown 不表示取消；新輪不同目錄／ID，避免重複寫入。
