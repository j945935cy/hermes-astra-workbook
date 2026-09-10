規則版本：registrations-v1；以下規則連同後附固定輸出格式共同生效。
一、原檔唯讀；保留 row_id 與每列原始欄位。
二、name 與 email 只移除前後空白。
三、本次虛構案例經規格同意，email 全部轉小寫作比較鍵；
    不宣稱這適用所有真實郵件系統。
四、email 必填，本練習只檢查非空白，不驗證真實可投遞性。
五、seats 必須是 ASCII 十進位整數字串，轉換後介於 1 至 3。
六、先逐列檢查有效性，無效列直接進 exceptions，不參與分組。
七、對所有有效列按標準化 email 分組；若組內 name 或 seats 不同，
    整組進 exceptions，理由為「同信箱資料衝突」，不挑最新或先來者。
八、只有沒有衝突的有效組才去重：name、email、seats 全相同，
    保留來源中先出現者，其餘進 duplicates。衝突優先於完全重複分流。
九、每個原始 row_id 只進入 clean、duplicates、exceptions 其中一組。
十、產出 clean.csv、duplicates.csv、exceptions.csv 與 summary.md；
    每筆排除紀錄要有理由，重複列另有 retained_row_id。

### 固定輸出格式：規則版本 registrations-v1

以下欄位名稱與順序就是三份 CSV 的完整 schema（資料結構），不可省略、重複或另加欄位。每組按來源列順序輸出；空組仍須寫表頭。

- clean.csv：`row_id,name,email,seats,raw_name,raw_email,raw_seats`
- duplicates.csv：`row_id,name,email,seats,raw_name,raw_email,raw_seats,retained_row_id,reason`
- exceptions.csv：`row_id,name,email,seats,raw_name,raw_email,raw_seats,reason`

三組都保存原始 row_id。`raw_name/raw_email/raw_seats` 是來源解析後尚未修剪或轉型的原字串，連前後空白也保留。`name` 修剪前後空白；`email` 修剪後轉小寫。有效席次的 `seats` 是無前導零的十進位字串；席次無效時 `seats` 保留原字串，不猜「兩位」。席次原字串不先修剪，只接受 `[0-9]+`。本案例沒有多重無效原因；擴充資料遇到多重原因時先報缺信箱，再報席次格式，最後報範圍。

`reason` 採固定中文值：R2「完全重複」；R4「缺少信箱」；R5「席次非 ASCII 整數」；R6「席次低於 1」；R8「席次高於 3」。衝突列一律「同信箱資料衝突」。這讓驗收器能拒絕任意但非空白的理由；真實專案若要補詳情，須另訂新版 schema，不在這次偷偷加欄。

summary.md 採下列完整固定模板，數量與列號必須來自實際產物。除了 UTF-8 BOM、LF／CRLF 與最後一個換行差異外，固定驗收器不接受改寫或額外內容，以免錯誤聲明藏在自由文字裡。這是小教材的嚴格契約，不是所有摘要都必須長這樣。

```markdown
# 報名清理摘要
- 來源：registrations.csv
- 規則版本：registrations-v1
- 輸入列數：8
- clean：3
- duplicates：1
- exceptions：4
- 未處理例外：R4、R5、R6、R8；待人工確認，未自動修正
- 原檔：未覆寫；固定全文比對通過
```
