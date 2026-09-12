# 第 11 章｜內容交付：把素材變成可審查的出版包｜配套

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
python3 -B scripts/prepare.py 11 "$HOME/hermes-workbook-11" &&
cd "$HOME/hermes-workbook-11"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `source.md`
- `editorial.md`

閱讀 [任務範本](tasks.md)，先在自己的文字編輯器逐段完成草稿；如要委派模型，須先完成書中模型環境與人工授權，並在已確認的新目錄啟動 `hermes`。套件與模型流程不包含在自動測試中。

## 預期產物

facts.md、draft-v1.md、review.md、draft-v2.md、changes.md、manifest.md、README.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

C1–C8 有依據，日期時區名額正確；正文與內部待補分區；仍未核准公開；manifest 僅列存在文件。

## 負向測試

免費、剩餘 12 席、假見證、假圖片、把草稿當發布版，均不通過；逐個開啟 manifest 路徑。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 人工交接與延伸驗收

先備只需理解第 10 章指定驗收短節，不需完整 Python。manifest 將檢查進度、範圍、使用／公開權限分開：draft-v2.md 可已核對事實但仍不可公開（C8），README 同步限制。

review 問題編號追到 changes、v2 修文與複核；已修待複核不等於結案。簽收綁版本、確認者、時間、依據，收件／內容審查／發布授權分欄，未回覆不自簽；舊版簽收不自動涵蓋新版。

小稿單人審可合成分區審查單，仍找得到來源、最新版、未決及權限；多人或多資產採完整包。風格輪次與投入時間先由人定，到限交待決版，阻擋發布項不因到限放行。

共用欄位：[任務授權](../../templates/management/task-authorization.md)、[驗收交接](../../templates/management/acceptance-handoff.md)、[問題變更](../../templates/management/issues-changes.md)、[採用維運](../../templates/management/adoption-operations.md)；[準備說明](../../docs/practice-setup.md)。以上是練習檢核，不是已取得的真實核准。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
