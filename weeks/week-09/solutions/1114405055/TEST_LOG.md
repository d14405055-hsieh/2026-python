# TEST_LOG

## 執行環境

- Python 3.12
- 指令：`python -m unittest discover -s tests -v`

## Red（失敗紀錄）

第一次整體測試（節錄）：

```text
FAILED (failures=2)
FAIL: test_geometry_values (test_task10221.TestTask10221.test_geometry_values)
AssertionError: 20231.856689118267 != 20231.856 within 3 places

FAIL: test_decode_sentence (test_task10222.TestTask10222.test_decode_sentence)
AssertionError: 'HeLLo WorLd\n' != 'Hello World\n'
```

第二次整體測試（節錄）：

```text
FAILED (failures=1)
FAIL: test_keep_spaces_and_symbols (test_task10222.TestTask10222.test_keep_spaces_and_symbols)
AssertionError: 'I Am FINE TODAY.\n' != 'I AM FINE TODAY.\n'
```

## Green（全通過紀錄）

第三次整體測試：

```text
Ran 10 tests in 0.002s
OK
```

## Refactor（重構紀錄）

### Task 1（10189）
- Red：先寫多組輸入格式測試。
- Green：完成鄰格計數邏輯，測試通過。
- Refactor：整理變數命名（`idx`、`field_index`）與輸出組裝。

### Task 2（10190）
- Red：加入不可整除中途失敗案例。
- Green：補上 `n < 2` / `m < 2` 與中途檢查。
- Refactor：抽出 `sequence_or_boring` 函式。

### Task 3（10193）
- Red：先寫 `gcd == 1` 與 `gcd > 1` 混合測試。
- Green：完成二進位轉整數與 `math.gcd` 判斷。
- Refactor：簡化輸入處理與 case 編號計算。

### Task 4（10221）
- Red：幾何值精度測試先失敗。
- Green：確認公式與角度轉換正確。
- Refactor：統一輸出到小數點後 6 位，測試採 `assertAlmostEqual`。

### Task 5（10222）
- Red：大小寫映射與期望值不一致。
- Green：修正映射邏輯（僅字母做大寫映射）與測試期望。
- Refactor：以對照表集中處理字元轉換。
