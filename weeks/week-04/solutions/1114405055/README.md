# Week 04 作業 - 1114405055

本次完成 week-04 指定 5 題：
- QUESTION-948
- QUESTION-10008
- QUESTION-10019
- QUESTION-10035
- QUESTION-10038

每題皆提供兩個版本：
- 正式版：`question_xxxxx.py`
- 簡單好記版：`question_xxxxx_easy.py`

## 檔案結構

```text
weeks/week-04/solutions/1114405055/
├── question_948.py
├── question_948_easy.py
├── question_10008.py
├── question_10008_easy.py
├── question_10019.py
├── question_10019_easy.py
├── question_10035.py
├── question_10035_easy.py
├── question_10038.py
├── question_10038_easy.py
├── tests/
│   └── test_week04.py
├── TEST_CASES.md
├── TEST_LOG.md
└── AI_USAGE.md
```

## 執行方式

在 `weeks/week-04/solutions/1114405055/` 下：

```bash
python question_10035.py < input.txt
python question_10035_easy.py < input.txt
```

其他題目同理，將檔名換成對應題號即可。

## 測試方式

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 補充說明

- `QUESTION-10019.md` 題目敘述文字與題號有落差，本提交以 week-04 指定題號 `10019`（Funny Encryption Method）實作。
- 測試檔同時驗證正式版與 easy 版輸出一致。
