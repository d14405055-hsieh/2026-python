# Week 09 作業提交（1114405055）

本資料夾提供 5 題練習，每題皆包含：
- AI 教學版程式（含中文註解）
- 手打版程式
- 學生自行撰寫測試（`tests/test_task*.py`）
- 測試紀錄（含至少一次失敗與一次全通過）

## 檔案結構

- `ai_task10189.py` / `student_task10189.py` / `tests/test_task10189.py`
- `ai_task10190.py` / `student_task10190.py` / `tests/test_task10190.py`
- `ai_task10193.py` / `student_task10193.py` / `tests/test_task10193.py`
- `ai_task10221.py` / `student_task10221.py` / `tests/test_task10221.py`
- `ai_task10222.py` / `student_task10222.py` / `tests/test_task10222.py`

## 測試方式

在本目錄執行：

```bash
python -m unittest discover -s tests -v
```

## 文件索引

- 測試案例整理：`TEST_CASES.md`
- Red/Green/Refactor 紀錄與測試輸出：`TEST_LOG.md`
- AI 使用說明：`AI_USAGE.md`

## 提交流程

1. 確認測試全通過。
2. `git add` 此資料夾所有新增檔案。
3. `git commit -m "week-09: submit 5 tasks with tests and logs"`
4. `git push` 到個人分支。
5. 依課程 `GITHUB_WORKFLOW.md` 開 PR。
