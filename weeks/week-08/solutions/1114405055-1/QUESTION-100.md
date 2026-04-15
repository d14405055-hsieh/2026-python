# 題目 100

## 交付內容

- AI 簡單版： [QUESTION-100-easy.py](QUESTION-100-easy.py)
- 手打程式： [QUESTION-100.py](QUESTION-100.py)
- 測試程式： [QUESTION-100-test.py](QUESTION-100-test.py)
- 測試 LOG： [QUESTION-100-log.md](QUESTION-100-log.md)

## 解題摘要

這題是 Collatz 序列區間最大 cycle length。

- 用快取記錄每個數字的 cycle length。
- 對每組輸入先取區間左右界，再掃描找最大值。
- 測試資料與執行記錄放在對應的 test 與 log 檔。
