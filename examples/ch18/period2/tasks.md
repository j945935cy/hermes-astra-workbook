# 第二期工作單（人工核定後才交模型）

工作目錄：由人填入已核對的第二期絕對路徑。先由人確認 approval-record.md 已核定 period2-v1，未核定就停止。
在任何輸出前檢查 output/actions.csv、output/report.md、output/README.md；任一存在（含目錄、符號連結）即停止，不覆寫、刪除或自行另名。再讀 task-spec.md、verify.py、approved-baseline.md 與 input 兩檔；缺來源或未知狀態即停止。
只建立三個指定 output 檔；只可修正這次從空目標開始建立的成果，重啟遇部分輸出仍停止。保留 G03 未定負責人，依 N05 批准 G04 日期，完整列入 G05。不得修改來源、契約、驗收器或人的批准紀錄。
完成後實際執行 python3 -B verify.py，回報三檔路徑、退出碼與待人工審核項；失敗按既定契約修輸出，不能改答案。不寄送、不排程、不保存技能、不連服務。
