# Week 03 Solution — 1114405055

> Python 版本：3.12+

---

## 本週目標達成

- 熟悉字串處理與格式轉換（UVA 272、UVA 490）
- 練習模擬題的狀態轉移（UVA 118）
- 練習基礎演算法與計數（UVA 100、UVA 299）

---

## 完成題目清單

| 題目 | 狀態 | 檔案 |
|------|------|------|
| UVA 100 | ✅ 完成 | `uva100_3n1.py` |
| UVA 118 | ✅ 完成 | `uva118_mutant_flatworld.py` |
| UVA 272 | ✅ 完成 | `uva272_tex_quotes.py` |
| UVA 299 | ✅ 完成 | `uva299_train_swapping.py` |
| UVA 490 | ✅ 完成 | `uva490_rotating_sentences.py` |

---

## 執行方式

```bash
# UVA 100
python uva100_3n1.py < input_100.txt

# UVA 118
python uva118_mutant_flatworld.py < input_118.txt

# UVA 272
python uva272_tex_quotes.py < input_272.txt

# UVA 299
python uva299_train_swapping.py < input_299.txt

# UVA 490
python uva490_rotating_sentences.py < input_490.txt
```

---

## 演算法摘要

- UVA 100：以 memoization 快取 cycle length，區間掃描取最大值。
- UVA 118：維護方向、位置與 scent 集合，模擬每個機器人的每步指令。
- UVA 272：逐字掃描，遇到 `"` 時在 `` 與 '' 間交替替換。
- UVA 299：計算 inversion 數量，等於最少相鄰交換次數。
- UVA 490：先右側補空白成矩形，再做 90 度順時針旋轉輸出。
