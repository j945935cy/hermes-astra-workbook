# 第 3 章｜第一個任務：把散亂筆記變成可查核的行動清單｜配套

Happy eBook Authors｜虛構教材素材；本頁不是章節書稿。

本次增補的 [N4 待確認交接與退回版](handoff-example.md) 是人工練習，不是批准或實測紀錄；新頁待本版整合發布固定提交。

## 起始狀態

Windows＋WSL2／Bash、Python 3.11 以上；[共用準備卡](../../docs/practice-setup.md)說明 READY／STOP 與路線選擇。從 repo 根目錄準備，在新練習目錄執行與驗收；來源缺失、輸出已存在或切換失敗就停，不覆寫。離線檢查不需要模型帳號；模型試跑另可能計費。

## 精確命令

從 repo 根目錄執行，這兩個命令不呼叫 Hermes、不改設定、不裝套件：

```bash
python3 -B scripts/verify_assets.py
python3 -B -m unittest discover -s tests -v
```

建立自己的全新副本（若同名已存在就停止；改新名稱並同步改 cd，不刪舊成果）：

```bash
python3 -B scripts/prepare.py 3 "$HOME/hermes-first-task" &&
cd "$HOME/hermes-first-task"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `examples/first-task/notes.md`

閱讀 [任務範本](tasks.md)，先在自己的文字編輯器逐段完成草稿；如要委派模型，須先完成書中模型環境與人工授權，並在已確認的新目錄啟動 `hermes`。套件與模型流程不包含在自動測試中。

## 預期產物

output/action-items.md。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

亦可對照 [人工驗收基準](expected.md)；它不是模型實跑輸出。

N1 三份摘要／小林／期限待確認；N2 阿青／2026-10-15；N3 提案未決議；N4 未指派且期限未知；N5 會議時間未知。

## 負向測試

將 N4 寫成阿青或套用 N2 日期即不通過；來源不存在應停止；已有 output/action-items.md 應停止且原檔雜湊不變。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

主編另提供真實 Hermes 子代理／GPT-6 Astra 首次產檔、父代理語義回讀與來源雜湊通過的去識別摘要。已有輸出／缺來源負向只驗 Python guard，未用獨立新模型重跑；完整 CLI 與乾淨安裝仍未驗證。

素材雜湊與語法檢查不能代替人工語義驗收。未實跑的模型、停止行為與外部整合不宣稱通過；完整平台限制見[版本與測試範圍](../../docs/compatibility.md)。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
