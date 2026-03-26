"""Week 04 in-class unit tests.

重點：這些檔名包含連字號，不能直接用 import，
所以透過 importlib 依檔案路徑動態載入。
"""

from __future__ import annotations

import importlib.util
import math
import unittest
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def load_module(filename: str):
    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestWeek04Regular(unittest.TestCase):
    def test_r04(self):
        m = load_module("R04-strings-bytes.py")
        self.assertEqual(m.slice_head(b"Hello World"), b"Hello")
        self.assertEqual(m.first_items(), ("H", 72))

    def test_r05(self):
        m = load_module("R05-numbers-basic.py")
        self.assertEqual(m.rounding_examples()["round_half_0_5"], 0)
        self.assertEqual(m.base_examples()["from_hex"], 1234)

    def test_r06(self):
        m = load_module("R06-numbers-special.py")
        data = m.inf_nan_examples()
        self.assertTrue(data["isinf"])
        self.assertTrue(data["isnan"])
        self.assertFalse(data["nan_equal_self"])

    def test_r07(self):
        m = load_module("R07-datetime-basics.py")
        base = datetime(2012, 8, 28)
        self.assertEqual(m.get_previous_byday("Monday", base), datetime(2012, 8, 27))

    def test_r08(self):
        m = load_module("R08-datetime-calendar.py")
        first, end = m.get_month_range(date(2012, 8, 1))
        self.assertEqual(first, date(2012, 8, 1))
        self.assertEqual((end - first).days, 31)
        self.assertEqual(m.parse_ymd("2012-09-20"), datetime(2012, 9, 20))

    def test_r09(self):
        m = load_module("R09-datetime-timezone.py")
        zones = m.find_taipei_zones()
        self.assertIn("Asia/Taipei", zones)

    def test_u01(self):
        m = load_module("U01-strings-split-gotchas.py")
        _, _, rebuilt = m.split_with_delimiters("asdf fjdk; afed, fjek,asdf, foo")
        self.assertEqual(rebuilt, "asdf fjdk;afed,fjek,asdf,foo")

    def test_u02(self):
        m = load_module("U02-regex-advanced.py")
        out = m.rewrite_dates("Today is 11/27/2012.")
        self.assertIn("27 Nov 2012", out)
        self.assertEqual(
            m.replace_keep_case("PYTHON python Python"),
            "SNAKE snake Snake",
        )

    def test_u03(self):
        m = load_module("U03-strings-format-perf.py")
        self.assertEqual(m.safe_format("{name} has {n} messages.", {"name": "Guido"}), "Guido has {n} messages.")
        self.assertEqual(m.bytes_index_diff(), ("H", 72))

    def test_u04(self):
        m = load_module("U04-numbers-precision.py")
        self.assertEqual(str(m.trad_round(2.5)), "3")
        nan_eq, is_nan, clean = m.nan_demo([1.0, float("nan"), 3.0])
        self.assertFalse(nan_eq)
        self.assertTrue(is_nan)
        self.assertEqual(clean, [1.0, 3.0])

    def test_u05(self):
        m = load_module("U05-datetime-gotchas.py")
        self.assertEqual(m.add_one_month(datetime(2012, 1, 31)), datetime(2012, 2, 29))
        self.assertEqual(m.use_strptime("2012-09-20"), m.use_manual("2012-09-20"))

    def test_u06(self):
        m = load_module("U06-datetime-timezone.py")
        wrong, correct = m.dst_boundary_demo()
        self.assertNotEqual(wrong.utcoffset(), correct.utcoffset())

    def test_u07(self):
        m = load_module("U07-random-advanced.py")
        seq1, seq2, same = m.reproducible_sequences()
        self.assertTrue(same)
        self.assertEqual(seq1, seq2)
        secure = m.secure_random_samples()
        self.assertEqual(secure["token_hex_len"], 32)
        self.assertEqual(secure["token_bytes_len"], 16)


class TestWeek04Easy(unittest.TestCase):
    def test_easy_files(self):
        easy_files = [
            "R04-strings-bytes-easy.py",
            "R05-numbers-basic-easy.py",
            "R06-numbers-special-easy.py",
            "R07-datetime-basics-easy.py",
            "R08-datetime-calendar-easy.py",
            "R09-datetime-timezone-easy.py",
            "U01-strings-split-gotchas-easy.py",
            "U02-regex-advanced-easy.py",
            "U03-strings-format-perf-easy.py",
            "U04-numbers-precision-easy.py",
            "U05-datetime-gotchas-easy.py",
            "U06-datetime-timezone-easy.py",
            "U07-random-advanced-easy.py",
        ]
        for filename in easy_files:
            mod = load_module(filename)
            callables = [name for name, value in vars(mod).items() if callable(value) and not name.startswith("__")]
            self.assertTrue(callables, f"{filename} 沒有可呼叫函式")


if __name__ == "__main__":
    unittest.main(verbosity=2)
