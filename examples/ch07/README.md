# 第 7 章｜失敗與續作：辨識假完成、處理中斷與重試｜配套

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
python3 -B scripts/prepare.py 7 "$HOME/hermes-workbook-07" &&
cd "$HOME/hermes-workbook-07"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `sources.md`

閱讀 [任務範本](tasks.md)，先在自己的文字編輯器逐段完成草稿；如要委派模型，須先完成書中模型環境與人工授權，並在已確認的新目錄啟動 `hermes`。套件與模型流程不包含在自動測試中。

## 預期產物

actions-v1.md、handoff.md、actions-v2.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

v1 僅 S1、S2；v2 為完整 S1–S4 快照且各一次，S2 依賴 S1，S3 未知，S4 提議。

## 負向測試

只有四列但缺來源／重複來源不通過；v2 已存在則停止所有寫入，不擅自 v3。交接誤報完成要依檔案指出。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 人工交接與延伸驗收

交接須分來源／產物版本、自查與人工驗收（確認者、範圍、時間）、S3 業務資訊應答角色、v2 修補授權人；未知保持待指定。

S5 延伸由人明確指定 sources-s5.md → actions-s5.md，保留原來源、v1、v2；新檔存在即 STOP。先列新增 S5 的差異，批准交接更新後才產出完整 S1–S5 快照；S5 仍是待討論，不新增採購承諾。舊驗收不涵蓋新來源。

重試前人定最小步驟、人工時間與次數上限；模型用量不可見標未知，不當自動限額。同錯誤再現停止，handoff 保留缺口及人工下一步；逾時僅查狀態，不盲目再寫。

共用欄位：[任務授權](../../templates/management/task-authorization.md)、[驗收交接](../../templates/management/acceptance-handoff.md)、[問題變更](../../templates/management/issues-changes.md)、[採用維運](../../templates/management/adoption-operations.md)；[準備說明](../../docs/practice-setup.md)。以上是練習檢核，不是已取得的真實核准。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
