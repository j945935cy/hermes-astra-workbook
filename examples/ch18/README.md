# 第 18 章｜畢業專案：建立你的個人 AI 工作站｜配套

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
python3 -B scripts/prepare.py 18 "$HOME/hermes-workbook-18" &&
cd "$HOME/hermes-workbook-18"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `input/tasks.csv`
- `input/notes.md`
- `task-spec.md`
- `verify.py`

在新練習目錄執行 `python3 -B verify.py`，空起點預期非零（缺產物）。讀者經批准生成後再執行，預期 ACCEPTED 並提醒 human review still required。`reference/output/` 是人工參考 CSV 與配套手寫文件，不是模型執行證據；自動測試只在臨時副本將它們組合驗證。不用 `-O`。

## 預期產物

output/actions.csv、output/report.md、output/README.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

CSV 僅 G02/G03/G04，G03 owner、G04 due 待確認；報告三個必要標題並保留未批准建議。

## 負向測試

副本擅填 G04 日期、漏 G03、重複 G02、未知狀態、錯來源對應均拒絕；已有任一目標含符號連結應停止，屬待模型實測。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
