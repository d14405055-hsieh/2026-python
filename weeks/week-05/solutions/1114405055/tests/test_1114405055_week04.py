"""1114405055 Week04 測試檔。

測試目標：
1) 驗證 AI easy 版本可執行。
2) 驗證手打版（-hand）可執行且結果合理。
"""

from __future__ import annotations

import importlib.util
import math
import unittest
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfoNotFoundError

BASE_DIR = Path(__file__).resolve().parents[1]


def load_module(filename: str):
    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestEasyAndHand(unittest.TestCase):
    def test_r04_hand(self):
        m = load_module("R04-strings-bytes-hand.py")
        data = m.bytes_basics()
        self.assertEqual(data["slice"], b"Hello")
        self.assertEqual(data["first_int"], 72)

    def test_r05_hand(self):
        m = load_module("R05-numbers-basic-hand.py")
        data = m.numbers_basics()
        self.assertEqual(data["round_half_even_0_5"], 0)
        self.assertEqual(data["hex"], "4d2")

    def test_r06_hand(self):
        m = load_module("R06-numbers-special-hand.py")
        data = m.special_numbers()
        self.assertTrue(data["isinf"])
        self.assertTrue(data["isnan"])

    def test_r07_hand(self):
        m = load_module("R07-datetime-basics-hand.py")
        data = m.datetime_basics()
        self.assertEqual(data["previous_monday"], datetime(2012, 8, 27))

    def test_r08_hand(self):
        m = load_module("R08-datetime-calendar-hand.py")
        first, next_first = m.month_range(date(2012, 8, 1))
        self.assertEqual(first, date(2012, 8, 1))
        self.assertEqual((next_first - first).days, 31)

    def test_r09_hand(self):
        m = load_module("R09-datetime-timezone-hand.py")
        try:
            data = m.timezone_convert()
        except ZoneInfoNotFoundError as exc:
            self.skipTest(f"系統缺少時區資料: {exc}")
        self.assertIn("to_utc", data)
        self.assertIn("to_taipei", data)

    def test_u01_hand(self):
        m = load_module("U01-strings-split-gotchas-hand.py")
        data = m.split_gotchas("asdf fjdk; afed, fjek,asdf, foo")
        self.assertEqual(data["rebuilt"], "asdf fjdk;afed,fjek,asdf,foo")

    def test_u02_hand(self):
        m = load_module("U02-regex-advanced-hand.py")
        out = m.regex_advanced("Today is 11/27/2012.")
        self.assertIn("27 Nov 2012", out)

    def test_u03_hand(self):
        m = load_module("U03-strings-format-perf-hand.py")
        data = m.format_perf_easy(["a", "b", "c"])
        self.assertEqual(data["joined_len"], 3)
        self.assertEqual(data["bytes_first"], 72)

    def test_u04_hand(self):
        m = load_module("U04-numbers-precision-hand.py")
        data = m.precision_easy()
        self.assertEqual(str(data["trad_round_0_5"]), "1")
        self.assertFalse(data["nan_eq_self"])

    def test_u05_hand(self):
        m = load_module("U05-datetime-gotchas-hand.py")
        data = m.datetime_gotchas_easy()
        self.assertEqual(data["jan31_plus1"], datetime(2012, 2, 29))

    def test_u06_hand(self):
        m = load_module("U06-datetime-timezone-hand.py")
        try:
            wrong, correct = m.timezone_easy()
        except ZoneInfoNotFoundError as exc:
            self.skipTest(f"系統缺少時區資料: {exc}")
        self.assertNotEqual(wrong.utcoffset(), correct.utcoffset())

    def test_u07_hand(self):
        m = load_module("U07-random-advanced-hand.py")
        data = m.random_easy()
        self.assertTrue(data["same_seed_same_seq"])
        self.assertEqual(data["secure_hex_len"], 32)

    def test_sample_easy(self):
        # 抽測一個 easy 版本，確保 AI 版也可正常載入執行
        m = load_module("R04-strings-bytes-easy.py")
        self.assertEqual(m.bytes_basics()["slice"], b"Hello")


if __name__ == "__main__":
    unittest.main(verbosity=2)
