import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from student_task10193 import solve


class TestTask10193(unittest.TestCase):
    def test_mixed_pairs(self) -> None:
        data = "3\n110\n101\n1010\n1011\n100\n10000\n"
        expected = (
            "Pair #1: Love is not all you need!\n"
            "Pair #2: Love is not all you need!\n"
            "Pair #3: All you need is love!"
        )
        self.assertEqual(solve(data), expected)

    def test_all_need_love(self) -> None:
        data = "1\n10\n100\n"
        expected = "Pair #1: All you need is love!"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
