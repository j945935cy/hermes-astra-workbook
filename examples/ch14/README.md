# 第 14 章｜瀏覽器驗證：操作成功不等於任務成功｜配套

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
python3 -B scripts/prepare.py 14 "$HOME/hermes-workbook-14" &&
cd "$HOME/hermes-workbook-14"
```

預期 `READY:` 與精確目的地；只複製以下起始檔，不複製參考答案或本配套 README：

- `index.html`

在新練習目錄啟動：

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

同一瀏覽器開啟 http://127.0.0.1:8765/，依正負向清單填表；只用虛構姓名。結束在服務終端機按 Ctrl+C，重新載入確認不可達。連接埠衝突就停止，勿殺不明程序或改成 0.0.0.0。重做改用專用新瀏覽器設定檔；不清全部網站資料。自動 suite 用臨時 loopback 埠，不與 8765 上的既有服務競爭。

## 預期產物

本機表單與人工驗收紀錄，不是真實報名。生成前不預置這些成果。所有參考答案均為人工素材，不是模型快照。

## 正向測試

送出 練習小雨，重整仍存在；重複送出不增加；全空白顯示錯誤且名單不變。記下同一設定檔與完整 URL。

## 負向測試

另建副本移除 localStorage.setItem，重整保存驗收應失敗；勿直接寫 storage 冒充操作。HTTP 404／關閉後連線拒絕只是服務層負測。

變異只在新副本做；自動 suite 使用 TemporaryDirectory，結束自動清理；正式來源前後均由固定 SHA-256 清單核對。重做使用新一期目錄，不清空或覆寫舊成果。

## 未驗證界線

主編另提供真實本機 Browser Use 表單事件證據：首次儲存、同網址重載、重複、全空白輸入均通過，截圖已由主編目視檢查。此為 DOM click() 路線，不證明滑鼠座標可點性、鍵盤無障礙、Windows／WSL2 後端安裝全流程；儲存拒絕與損壞 JSON 未測。

素材雜湊與語法檢查不是語義驗收；人工逐項對照來源與授權。本套 Python suite 不做模型端到端；補充實測範圍以上述主編證據為限，不能推廣為所有代理都遵守停止條件或沒有外部副作用。第 14 章 HTTP 通過不代表瀏覽器保存／視覺已測；第 16／17 章不建立 profile、排程、gateway 或 MCP 連線。原生 Windows、乾淨 WSL 安裝、macOS 與其他 Linux 未驗證。

[任務範本](tasks.md)｜[全書索引](../../README.md)｜[版本與測試範圍](../../docs/compatibility.md)
