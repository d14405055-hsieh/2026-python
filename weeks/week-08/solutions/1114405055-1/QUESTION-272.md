# 題目 272

## 交付內容

- AI 簡單版： [QUESTION-272-easy.py](QUESTION-272-easy.py)
- 手打程式： [QUESTION-272.py](QUESTION-272.py)
- 測試程式： [QUESTION-272-test.py](QUESTION-272-test.py)
- 測試 LOG： [QUESTION-272-log.md](QUESTION-272-log.md)

## 解題摘要

這題是將普通雙引號依序替換成 TeX 引號。

- 逐字掃描輸入文字。
- 用布林旗標切換下一個引號要輸出左引號或右引號。
- 其他字元維持原樣。
