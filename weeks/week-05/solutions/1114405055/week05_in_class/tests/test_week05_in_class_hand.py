"""week05 in-class 手打版測試（含繁體中文註解）。"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


def load_module(name: str):
    """動態載入模組：因檔名有連字號，需用 importlib。"""
    path = BASE / name
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入 {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestInClassHand(unittest.TestCase):
    """針對手打版（-hand.py）做核心行為驗證。"""

    def test_r01_hand(self):
        m = load_module("R_01_iterator_basics-hand.py")
        out = m.iterator_easy([1, 2, 3])
        self.assertEqual(out["taken"], [1, 2, 3])

    def test_r02_hand(self):
        m = load_module("R_02_enumerate_zip-hand.py")
        out = m.enumerate_zip_easy(["A", "B"], [10, 20])
        self.assertEqual(out["numbered"][0], (1, "A"))
        self.assertEqual(out["paired"][1], ("B", 20))

    def test_u01_hand(self):
        m = load_module("U_01_generator_basics-hand.py")
        self.assertEqual(m.generator_easy(), [3, 2, 1])

    def test_u02_hand(self):
        m = load_module("U_02_itertools-hand.py")
        out = m.itertools_easy()
        self.assertEqual(out["slice"], [2, 3, 4, 5])
        self.assertIn(("a", "b"), out["pairs"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
