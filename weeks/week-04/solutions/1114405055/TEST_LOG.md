# TEST_LOG

## 執行環境
- Python 3.9.6
- 作業路徑：`weeks/week-04/solutions/1114405055/`

## 測試指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 第一次執行（失敗，待修正）

- 結果：11 tests，9 passed，2 errors
- 失敗原因：`question_10019.py` 使用 `int.bit_count()`，Python 3.9 不支援。
- 修正內容：改為 `bin(x).count("1")`。

## 第二次執行（修正後）

- 結果：11 tests，11 passed，0 failed，0 errors
- 測試摘要：
  - TestQuestion948: 3 passed
  - TestQuestion10008: 2 passed
  - TestQuestion10019: 2 passed
  - TestQuestion10035: 2 passed
  - TestQuestion10038: 2 passed

## 結論

week-04 五題正式版與 easy 版皆可正常運作，測試全數通過。
