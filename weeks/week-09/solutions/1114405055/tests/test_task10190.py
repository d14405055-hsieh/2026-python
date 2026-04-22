import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from student_task10190 import solve


class TestTask10190(unittest.TestCase):
    def test_valid_and_invalid(self) -> None:
        data = "81 3\n31 2\n64 4\n1 5\n"
        expected = "81 27 9 3 1\nBoring!\n64 16 4 1\nBoring!"
        self.assertEqual(solve(data), expected)

    def test_non_divisible_midway(self) -> None:
        data = "72 8\n"
        expected = "Boring!"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
