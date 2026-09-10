# 第 4 章｜任務規格：目標、輸入、限制與驗收｜配套

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
python3 -B scripts/prepare.py 4 "$HOME/hermes-workbook-04" &&
cd "$HOME/hermes-workbook-04"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `support-notes.md`

閱讀 [任務範本](tasks.md)，先在自己的文字編輯器逐段完成草稿；如要委派模型，須先完成書中模型環境與人工授權，並在已確認的新目錄啟動 `hermes`。套件與模型流程不包含在自動測試中。

## 預期產物

support-draft.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

三區「已知答覆」「待查問題」「發布前審核」；S1 PDF 不寄紙本，S2 原因未知，S3 阿青測兩種手機且期限未知，S4 政策未核准，S5 待小林確認。

## 負向測試

把手機慢歸因網路、承諾七日退款、宣稱小林已核准，均不通過。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
