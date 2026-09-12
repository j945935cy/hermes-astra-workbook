# 第18章第二期：受控新資料

此目錄為獨立 period2-v1 教材，未更改第一期固定素材或公共驗收器。Python 3.11+、WSL2/Bash；全部檢查離線，不需帳號。不要在 repo 的 starter 產出。

## 先批准再生成
1. 從 workbook repo 根目錄執行下方準備命令。目的地須全新，父目錄存在且祖先無符號連結；不複製 reference/output。失敗或 STOP 時不 cd、不交模型。
2. 在新目錄用編輯器讀 input、approved-baseline.md、task-spec.md、verify.py；核對 G04 由 N05 批准與新增 G05。先不要開模型或看 reference/output。
3. 另存 approval-record.md：批准人、時間、period2-v1、來源與驗收器核對、准用範圍。未核定就停。公開批准表僅作者虛構情境，不替你簽核。
4. 執行空起點驗收，應非零且缺 output/actions.csv。此失敗只證明不會接受空成果，不是代理停止測試。
5. 才交 tasks.md 的第二期工作單。模型只寫三份 output，不准改驗收器、批准表或來源。生成後自己實跑驗收與語義審閱，另填結案卡。
6. 最後才用 reference/output 三檔比對。第二期報告必須說 N05 已批准；不能沿用第一期的 G04「期限待確認」。第一期仍依自己的契約驗收。

```bash
python3 -B examples/ch18/period2/prepare_period2.py "$HOME/hermes-graduation-period2"
```

只有 READY 指向正確目錄才執行：

```bash
cd "$HOME/hermes-graduation-period2"
```

在新期根目錄（不要用 -O）：

```bash
python3 -B verify.py
```

空輸出預期退出非零；完整正確三檔應退出 0，印出 `ACCEPTED: structured deliverables; human review still required`。所有目標存在（包括符號連結）時模型應停止：這項模型行為仍待實測，不拿腳本結果冒充。重做另選新名稱，不刪舊成果。

## 離線正負測（回 workbook repo 根目錄）

```bash
python3 -B -m unittest discover -s examples/ch18/period2 -p 'test_period2.py' -v
```

tests 只在 TemporaryDirectory 組合 starter 與作者 reference，測完整參考、空輸出、錯日期、漏 G05、錯來源映射、未知狀態、重複、改來源、缺文件。另測準備腳本新路徑、既有路徑、空白、缺父目錄與符號連結拒絕。測試結束清理暫存目錄，不動正式來源。

編輯端模型正常產出、獨立驗收及內容讀回已限定通過，見 [驗證摘要](../verification.md)；真人批准／接手試讀、第二期模型停止行為與實際成本仍待測；沒有節時或節費結論。驗收器保持完整固定來源與精確答案，未泛化成任意週報系統。原始碼可審核，不把固定參考說成陌生資料能力證明。
