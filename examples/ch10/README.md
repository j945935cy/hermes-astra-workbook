# 第 10 章｜批次資料整理：清理、去重與例外清單｜配套

Happy eBook Authors｜虛構教材素材；本頁不是章節書稿。

## 起始狀態

Windows＋WSL2／Bash、Python 3.11 以上。先將終端機切到此 repo 根目錄（包含 examples 與 scripts）。不要在配套 starter 裡做產出；任務輸出起初不得存在。無須模型帳號即可跑下列離線檢查。模型工作另可能計費。

## 精確命令

從 repo 根目錄執行，這兩個命令不呼叫 Hermes、不改設定、不裝套件：

```bash
python3 -B scripts/verify_assets.py
python3 -B -m unittest discover -s tests -v
```

建立自己的全新副本（若同名已存在就停止；改新名稱並同步改 cd，不刪舊成果）：

```bash
python3 -B scripts/prepare.py 10 "$HOME/hermes-workbook-10" &&
cd "$HOME/hermes-workbook-10"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `registrations.csv`
- `verify.py`
- `test_verify.py`
- `rules.md`

在新練習目錄執行 `python3 -B test_verify.py`：預期 30 個 OK（2 個正向、28 個故意錯誤）；這些是人工驗收器測資，不是清理器產物。正式產物完成後執行 `python3 -B verify.py`；空起點預期 FileNotFoundError。R9 副本使用 `python3 -B verify.py --r9`。本章沒有清理器參考實作，配套不代造一份偏離章文的演算法。

## 預期產物

preview.md、經確認才建立的 clean_registrations.py、clean.csv、duplicates.csv、exceptions.csv、summary.md，以及人工作業交接 operations.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

八列分流 clean=R1/R3/R7，duplicates=R2→R1，exceptions=R4/R5/R6/R8；完整欄位、原值及理由須相符。

## 負向測試

R9 擴充使用副本與 --r9：有效組 R1/R2/R9 全衝突；缺 summary、錯欄位、修剪 raw_email 都拒絕。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 人工交接與延伸驗收

完整原碼在 [verify.py](starter/verify.py)、[test_verify.py](starter/test_verify.py)；不需抄寫即可依上方命令跑正負測。故意錯誤的 exit=1 被測試程式判為 OK 是預期拒絕，不要改成通過。

另由人建立 operations.md，記本次用途、clean 可用範圍／核准狀態與例外接手：R4 缺信箱、R5 席次格式、R6/R8 範圍未決。角色待指定、未答保持未答；exceptions 不代表取消參加資格，是否先交部分名單由資料擁有人決定。固定 summary 與 schema 不加管理欄。

只更正 R5 是經資料擁有人確認的新來源批次，規則可仍 v1；核准自然語言轉換表才另編規則 v2。兩案保留舊來源／輸出與核准依據，記影響紀錄及全批重驗結果。現有驗收器只驗固定八列與 R9，不支援任意新來源／新版規則；延伸另訂檢查，不刪舊檢查。

共用欄位：[任務授權](../../templates/management/task-authorization.md)、[驗收交接](../../templates/management/acceptance-handoff.md)、[問題變更](../../templates/management/issues-changes.md)、[採用維運](../../templates/management/adoption-operations.md)；[準備說明](../../docs/practice-setup.md)。以上是練習檢核，不是已取得的真實核准。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
