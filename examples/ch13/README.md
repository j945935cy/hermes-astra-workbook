# 第 13 章｜從需求到功能：讓測試定義完成｜配套

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
python3 -B scripts/prepare.py 13 "$HOME/hermes-workbook-13" &&
cd "$HOME/hermes-workbook-13"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `fee.py`
- `test_fee.py`
- `acceptance.py`

在新練習目錄先執行 `python3 -B -m unittest -v`，預期非零且 900 != 810；這是刻意紅燈。經授權修改 fee.py 後，執行 `python3 -B -m unittest -v` 與 `python3 -B acceptance.py`，兩者均須退出 0。不用 `-O`（會略過 assert）。自動 suite 在臨時副本完成原樣參考版替換與變異檢查，不替讀者覆寫正式檔。

## 章別交付紀錄

使用 [管理實作附頁](management-lab.md) 填寫本次批准、驗收與限制；共用四模板由該頁連結，不由 prepare 預填。未測欄不能抄作者結果。完整必要回歸參考另見 `reference/test_fee.py`；原 starter 的刻意紅燈不變。

## 預期產物

修改後 fee.py 與實際測試紀錄；reference/fee.py 僅供對照。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

starter 原版測試因 900 != 810 失敗；參考版單元測試通過，acceptance.py 印出 ACCEPTED: fee contract。

## 負向測試

門檻 >3、僅 ==3、所有數量折扣、接受 True 的錯誤副本均被拒絕。不要修改 test_fee.py 或 acceptance.py 預期值。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。無模型端到端測試，不能宣稱代理有遵守停止條件、真實寫檔或外部無副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
