# Hermes Agent × GPT-6 Astra 讀者實作素材

Happy eBook Authors｜Happy eBook

《讓 AI 真正替你工作》的公開實作配套，提供虛構素材、任務範本、驗收器與參考程式；不是 Hermes 或 OpenAI 官方專案。不含章節書稿。

## 目前狀態

已提供 01–18 章對照索引與可公開素材；ch06／ch12 教學用 AGENTS.md 已經作者明確授權補齊。第 3 章保留 first-task 路徑。素材與確定性測試已驗證，不代表所有模型及外部整合流程已測完。

Python 標準函式庫測試通過；第 3 章有真實子代理產檔與父代理回讀證據，第 14 章有主編真實本機瀏覽器表單事件證據，第 18 章第一期另有真實 Astra CLI 正常與兩項停止測試。這些不等於乾淨 Windows 安裝或所有模型流程已驗證。詳見 [兼容狀態](docs/compatibility.md)。

## 起始狀態與精確命令

本校閱版請使用 [review-v4 固定 ZIP](https://github.com/j945935cy/hermes-astra-workbook/archive/refs/tags/review-v4.zip) 並解壓；若標籤尚未存在，表示新版仍在驗收，不要改用舊版本冒充。Code → Download ZIP 取得的是持續變動的 main。以包含 examples、scripts 的根目錄為目前工作目錄。WSL2／Bash、Python 3.11 以上；不需要模型帳號即可做離線驗證，不裝全域套件。

```bash
python3 --version
python3 -B scripts/verify_assets.py
python3 -B -m unittest discover -s tests -v
```

預期資產檢查 PASS、16 項 unittest 通過；其中第 10 章另跑 30 個驗收器情境。這些命令不產生模型答案。各章 README 有自己的起始狀態、prepare.py 複製命令、產物與正負向測試；永遠在新副本練習，不在 starter 目錄改寫。

新增共用入口：[操作卡](docs/practice-setup.md)、[任務與授權](templates/management/task-authorization.md)、[驗收與交接](templates/management/acceptance-handoff.md)、[未決與變更](templates/management/issues-changes.md)、[採用與維運](templates/management/adoption-operations.md)。第 18 章另有 [第二期受控素材](examples/ch18/period2/README.md)。

補充測試（同樣不呼叫模型）：

```bash
python3 -B -m unittest discover -s examples/ch13 -p test_regressions.py -v
python3 -B -m unittest discover -s examples/ch18/period2 -p test_period2.py -v
```

分別預期 1 項回歸測試（內含四種錯誤實作）及 12 項第二期測試通過。

## 章節索引

| 章 | 素材／任務 | 狀態 |
|---|---|---|
| 01 | [從聊天到交付：AI 工作代理到底改變了什麼](templates/ch01-task.md) | 紙筆／環境卡範本；不造空章節目錄 |
| 02 | [安裝 Hermes，接上 GPT-6 Astra](templates/ch02-task.md) | 紙筆／環境卡範本；不造空章節目錄 |
| 03 | [第一個任務：把散亂筆記變成可查核的行動清單](examples/first-task/README.md) | 起始素材與人工驗收 |
| 04 | [任務規格：目標、輸入、限制與驗收](examples/ch04/README.md) | 起始素材與人工驗收 |
| 05 | [工具、權限與成本：哪些事能交出去](templates/ch05-task.md) | 紙筆／環境卡範本；不造空章節目錄 |
| 06 | [記憶、專案規則與技能：分清楚該存在哪裡](examples/ch06/README.md) | 起始規則、範本與驗收基準已提供 |
| 07 | [失敗與續作：辨識假完成、處理中斷與重試](examples/ch07/README.md) | 起始素材與人工驗收 |
| 08 | [有來源的研究簡報：從搜尋到證據表](examples/ch08/README.md) | 起始素材與人工驗收 |
| 09 | [文件轉行動：負責人、期限與待確認事項](examples/ch09/README.md) | 起始素材與人工驗收 |
| 10 | [批次資料整理：清理、去重與例外清單](examples/ch10/README.md) | 原樣程式與正負向測試 |
| 11 | [內容交付：把素材變成可審查的出版包](examples/ch11/README.md) | 起始素材與人工驗收 |
| 12 | [接手陌生專案：先理解，再修改](examples/ch12/README.md) | 起始規則、範本與驗收基準已提供 |
| 13 | [從需求到功能：讓測試定義完成](examples/ch13/README.md) | 原樣程式與正負向測試 |
| 14 | [瀏覽器驗證：操作成功不等於任務成功](examples/ch14/README.md) | 原樣 HTML；本機表單證據與平台界線分列 |
| 15 | [多代理協作：分工、合併與獨立驗收](examples/ch15/README.md) | 原樣程式與正負向測試 |
| 16 | [排程與通知：本機結果和訊息交付的差別](examples/ch16/README.md) | 主線草稿；連線／註冊不執行 |
| 17 | [MCP 與外部服務：從唯讀開始連接](examples/ch17/README.md) | 主線草稿；連線／註冊不執行 |
| 18 | [畢業專案：建立你的個人 AI 工作站](examples/ch18/README.md) | 原樣程式與正負向測試 |

## 預期產物與正負向測試

[入門指南](docs/getting-started.md) → [first-task](examples/first-task/README.md) → [一般任務規格](templates/task-spec.md)。概念章的使用方式見 [範本說明](templates/README.md)。研究／文件路線是 08–11；程式／測試路線是 12–15；16–17 採不改設定的草稿主線。

正向測試核對固定素材、可執行參考程式和原樣驗收器；負向測試在 TemporaryDirectory 製造錯欄位、錯日期、缺檔與來源變更。prepare.py 對已有目的地（含壞符號連結）停止，無刪除式 reset；重跑另選新目錄。原樣程式集中於 starter／reference；reference 是人工答案，不是模型日誌。

## 未驗證界線與安全

完整細目見 [版本與測試狀態](docs/compatibility.md) 與 [提取清單](extraction-manifest.json)。雜湊不是語義判斷，參考答案不是執行結果，Python guard 不是獨立模型負測。教學用 AGENTS.md 經作者明確授權建立；所有 profile、排程、MCP、通知與真實憑證維持未修改。

公開素材不含書稿、EPUB、封面原檔、個人文件或憑證。虛構任務裡的「不公開」是案例內的發布限制，不妨礙作者提供這些教學素材；不代表真實工作獲得發布授權。不要上傳 API key、token、私人日誌或未去識別資料。

## 提問與授權

使用 [Issues](https://github.com/j945935cy/hermes-astra-workbook/issues/new/choose) 提供章節、版本、去識別錯誤與重現步驟；亦見 [勘誤](ERRATA.md)、[FAQ](docs/faq.md)。

目前未授予額外開源授權；著作權由 Happy eBook Authors 保留。公開閱讀不等於授權任意重製或商用，後續授權範圍另行公告。
