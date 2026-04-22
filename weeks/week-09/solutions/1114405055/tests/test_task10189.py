import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from student_task10189 import solve


class TestTask10189(unittest.TestCase):
    def test_sample_case(self) -> None:
        data = (
            "4 4\n"
            "*...\n"
            "....\n"
            ".*..\n"
            "....\n"
            "3 5\n"
            "**...\n"
            ".....\n"
            ".*...\n"
            "0 0\n"
        )
        expected = (
            "Field #1:\n"
            "*100\n"
            "2210\n"
            "1*10\n"
            "1110\n\n"
            "Field #2:\n"
            "**100\n"
            "33200\n"
            "1*100"
        )
        self.assertEqual(solve(data), expected)

    def test_single_mine(self) -> None:
        data = "1 1\n*\n0 0\n"
        expected = "Field #1:\n*"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
