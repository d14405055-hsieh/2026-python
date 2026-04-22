import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from student_task10222 import solve


class TestTask10222(unittest.TestCase):
    def test_decode_sentence(self) -> None:
        data = "Jr;;p Ept;f\n"
        expected = "Hello World\n"
        self.assertEqual(solve(data), expected)

    def test_keep_spaces_and_symbols(self) -> None:
        data = "O S, GOMR YPFSU/\n"
        expected = "I Am FINE TODAY.\n"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
