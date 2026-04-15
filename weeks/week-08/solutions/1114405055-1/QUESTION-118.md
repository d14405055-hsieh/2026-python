# 題目 118

## 交付內容

- AI 簡單版： [QUESTION-118-easy.py](QUESTION-118-easy.py)
- 手打程式： [QUESTION-118.py](QUESTION-118.py)
- 測試程式： [QUESTION-118-test.py](QUESTION-118-test.py)
- 測試 LOG： [QUESTION-118-log.md](QUESTION-118-log.md)

## 解題摘要

這題是機器人模擬與 scent 判斷。

- 用方向表處理轉向與前進。
- 每次前進時檢查是否越界。
- 掉出邊界的座標會留下 scent，之後遇到同一格就跳過會掉落的指令。
