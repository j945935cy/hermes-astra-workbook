# 第 6 章｜記憶、專案規則與技能：分清楚該存在哪裡｜配套

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

本章提供規則與任務草稿。從 repo 根目錄將規則複製至尚不存在的新資料夾：

```bash
python3 -B scripts/prepare.py 6 "$HOME/hermes-rules-practice"
```

確認 READY 路徑後，先閱讀新目錄的 AGENTS.md，再讀 [任務範本](tasks.md)。既有目錄會被拒絕，不覆寫規則。

閱讀 [任務範本](tasks.md)，先在自己的文字編輯器逐段完成草稿；如要委派模型，須先完成書中模型環境與人工授權，並在已確認的新目錄啟動 `hermes`。套件與模型流程不包含在自動測試中。

## 預期產物

專案規則審閱紀錄、技能草稿（不保存到 Hermes）。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

偏好／專案共同規則／程序／當次參數分開，未知測試保留未驗證。

## 負向測試

把當次期限與人名永久保存，或沒有實跑就宣稱已驗證技能，均不通過。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
