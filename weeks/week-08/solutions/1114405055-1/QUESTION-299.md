# 題目 299

## 交付內容

- AI 簡單版： [QUESTION-299-easy.py](QUESTION-299-easy.py)
- 手打程式： [QUESTION-299.py](QUESTION-299.py)
- 測試程式： [QUESTION-299-test.py](QUESTION-299-test.py)
- 測試 LOG： [QUESTION-299-log.md](QUESTION-299-log.md)

## 解題摘要

這題是計算火車排列的 inversion 數。

- 直接枚舉所有 i < j 的組合。
- 前面的數字比後面大，就代表多一組交換。
- 因為長度很小，所以雙迴圈就夠用。
