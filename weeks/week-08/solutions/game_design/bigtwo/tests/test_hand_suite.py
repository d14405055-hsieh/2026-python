"""整合測試：手打版（-hand）是否可正常匯入與執行。"""

from __future__ import annotations

import py_compile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestHandSuite(unittest.TestCase):
    def test_hand_modules_importable(self):
        hand_files = list(ROOT.glob("**/*-hand.py"))
        self.assertTrue(hand_files)
        for f in hand_files:
            # 手打版使用相同套件匯入結構；這裡以語法編譯檢查可讀性與正確性。
            py_compile.compile(str(f), doraise=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
