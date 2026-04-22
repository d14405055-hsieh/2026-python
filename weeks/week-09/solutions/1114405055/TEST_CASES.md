# TEST_CASES

## Task 1: 10189 Minesweeper

- 測試檔：`tests/test_task10189.py`
- 重點案例：
  - 官方型態多組輸入（含空行輸出格式）
  - 最小邊界 `1x1` 只有地雷

## Task 2: 10190 Divide, But Not Quite Conquer!

- 測試檔：`tests/test_task10190.py`
- 重點案例：
  - 可完整整除到 1 的序列
  - 中途不可整除、`n < 2`、`m < 2`

## Task 3: 10193 All You Need Is Love

- 測試檔：`tests/test_task10193.py`
- 重點案例：
  - `gcd == 1` 與 `gcd > 1` 混合測試
  - 單一測資最小組合

## Task 4: 10221 Satellites

- 測試檔：`tests/test_task10221.py`
- 重點案例：
  - `180 deg` 幾何檢查（弧長與弦長）
  - `60 deg` 與 `3600 min` 等價輸入

## Task 5: 10222 Decode the Mad man

- 測試檔：`tests/test_task10222.py`
- 重點案例：
  - 句子解碼（含大小寫）
  - 空白與標點保留
