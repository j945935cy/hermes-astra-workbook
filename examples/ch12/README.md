# 第 12 章｜接手陌生專案：先理解，再修改｜配套

Happy eBook Authors｜虛構教材素材；本頁不是章節書稿。

## 起始狀態

Windows＋WSL2／Bash、Python 3.11 以上。先將終端機切到此 repo 根目錄（包含 examples 與 scripts）。不要在配套 starter 裡做產出；任務輸出起初不得存在。無須模型帳號即可跑下列離線檢查。模型工作另可能計費。

教學用 [AGENTS.md](AGENTS.md) 已經作者明確授權提供。使用前先閱讀；prepare.py 只複製至新練習目錄，不安裝全域規則。

## 精確命令

從 repo 根目錄執行，這兩個命令不呼叫 Hermes、不改設定、不裝套件：

```bash
python3 -B scripts/verify_assets.py
python3 -B -m unittest discover -s tests -v
```

建立自己的全新副本（若同名已存在就停止；改新名稱並同步改 cd，不刪舊成果）：

```bash
python3 -B scripts/prepare.py 12 "$HOME/hermes-workbook-12" &&
cd "$HOME/hermes-workbook-12"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `README.md`
- `app.py`
- `test_app.py`

在新練習目錄執行：

```bash
python3 -B app.py
python3 -B -m unittest -v
python3 -B -c 'from app import make_label; print(repr(make_label("", 0)))'
```

`starter/README.md` 是章內原樣的專案測試素材（不是配套完整指南）；另附 AGENTS.md，由 prepare.py 一併複製。確定性程式測試已跑；接手代理仍需自行實測。

## 預期產物

onboarding.md（另行補妥章內規則後）；本配套先執行程式基準。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

app.py 印出 林青｜2 位；unittest 實際執行 1 項；空姓名零席次觀察為 ｜0 位，不等於已決定需求。

## 負向測試

副本移除 strip 後單元測試應拒絕；零個測試不算通過；擅改程式超出接手報告授權。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
