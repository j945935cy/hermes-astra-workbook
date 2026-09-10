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

preview.md、經確認才建立的 clean_registrations.py、clean.csv、duplicates.csv、exceptions.csv、summary.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

八列分流 clean=R1/R3/R7，duplicates=R2→R1，exceptions=R4/R5/R6/R8；完整欄位、原值及理由須相符。

## 負向測試

R9 擴充使用副本與 --r9：有效組 R1/R2/R9 全衝突；缺 summary、錯欄位、修剪 raw_email 都拒絕。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
