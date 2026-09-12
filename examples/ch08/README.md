# 第 8 章｜有來源的研究簡報：從搜尋到證據表｜配套

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
python3 -B scripts/prepare.py 8 "$HOME/hermes-workbook-08" &&
cd "$HOME/hermes-workbook-08"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `brief.md`
- `sources.md`

閱讀 [任務範本](tasks.md)，先在自己的文字編輯器逐段完成草稿；如要委派模型，須先完成書中模型環境與人工授權，並在已確認的新目錄啟動 `hermes`。套件與模型流程不包含在自動測試中。

## 預期產物

questions.md、evidence.md、decision.md；web-check.md 是分開的網路選做。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

F1 容量 40、CSV；F2 僅建立者可匯出；F4 35 人且可事前匯出；F3 匯出付費價格未知。每段短引須逐字存在。

## 負向測試

虛构 F5、聲稱協作者可下載、把資料刪除期限補成已知，均不通過。副本人數改 50 後不能沿用原推薦。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 人工交接與延伸驗收

decision.md 分暫定選案、假資料演練與真實資料試辦。政策及使用授權未知時，只能用假資料檢查流程或先詢問，不能送出真實報名個資；政策確認角色待指定，答案不預設合格。

F4 匯出安排須由建立者確認交付時點，協作者回覆可讀且符合報到用途；建立者無法交付或人數改變即暫停重評。50 人延伸保留舊建議，另記新來源版本與「容量結論失效，角色限制仍有效」。

questions.md 以正文支持必答題、或列阻擋與可接手詢問角色為交付門檻；人定搜尋上限到限便交暫定／受阻版，不以來源篇數代替品質。

共用欄位：[任務授權](../../templates/management/task-authorization.md)、[驗收交接](../../templates/management/acceptance-handoff.md)、[問題變更](../../templates/management/issues-changes.md)、[採用維運](../../templates/management/adoption-operations.md)；[準備說明](../../docs/practice-setup.md)。以上是練習檢核，不是已取得的真實核准。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
