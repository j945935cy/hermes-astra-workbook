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

## 人工交接與延伸驗收

基準須記來源版、Python 實際版本、檢查時點、命令／退出狀態、test_trim_name 範圍與未驗範圍，並逐字核對四檔未變；真實專案已有 Git 才記提交及差異，不為教材初始化。來源或環境變動重建相關基準。

接手選項只比較維持現況、回傳提示、丟例外，列展示入口可能影響、需補測試與待確認者（待指定）。本例未看到其他呼叫端，不宣稱全系統相容。

讀懂純函式及測試副作用可續盤點；遇不明安裝、憑證、資料庫寫入或不能理解的副作用即 STOP、不執行，交付已讀、未讀高風險區域及需技術接手事項。人定投入上限，到限交受阻報告。只新增 onboarding.md，不改四檔；第 13 章另案。

共用欄位：[任務授權](../../templates/management/task-authorization.md)、[驗收交接](../../templates/management/acceptance-handoff.md)、[問題變更](../../templates/management/issues-changes.md)、[採用維運](../../templates/management/adoption-operations.md)；[準備說明](../../docs/practice-setup.md)。以上是練習檢核，不是已取得的真實核准。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
