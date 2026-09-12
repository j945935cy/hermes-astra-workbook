# 第13章確定性驗證

既有 WSL、Python 3.14.4；沒有呼叫模型。全部在暫存目錄操作，原 starter／acceptance.py 保持不變。

- starter 原版：python3 -B -m unittest -v 退出 1，明確 900 != 810；不是匯入錯誤。
- reference/fee.py 加 reference/test_fee.py：相同單元測試命令，4 tests OK、退出 0。
- 相同參考函式的 python3 -B acceptance.py：退出 0，ACCEPTED: fee contract。
- 章別 suite：1 test，包含參考版及 >3、==3、全量折扣、接受 True 四種變異；各變異同時被開發測試及獨立驗收拒絕。

從 workbook repo 根目錄重跑：

```bash
python3 -B -m unittest discover -s examples/ch13 -p 'test_regressions.py' -v
```

補測可立即通過，不稱每例都是測試先行。作者程式測試不等於讀者模型修正流程成功；讀者需另填批准人、真實工具紀錄、人工檢查與准用範圍。正式帳務未驗證。
