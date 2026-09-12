# 第 4 章｜任務規格：目標、輸入、限制與驗收｜配套

Happy eBook Authors｜虛構教材素材；本頁不是章節書稿。

本次增補的 [內容批准範圍、追加需求與部分交付](review-exercises.md) 是人工練習，不是批准或實測紀錄；新頁待本版整合發布固定提交。

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
python3 -B scripts/prepare.py 4 "$HOME/hermes-support-lab" &&
cd "$HOME/hermes-support-lab"
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

素材雜湊與語法檢查不能代替人工語義驗收。未實跑的模型、停止行為與外部整合不宣稱通過；完整平台限制見[版本與測試範圍](../../docs/compatibility.md)。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
