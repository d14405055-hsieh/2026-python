import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR / "problem_10055_handwritten.py"


def run_program(input_data: str) -> str:
    result = subprocess.run(
        [sys.executable, str(TARGET)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test10055(unittest.TestCase):
    def test_toggle_and_query(self) -> None:
        input_data = "5 5\n2 1 5\n1 3\n2 1 5\n1 5\n2 2 5\n"
        expected = "0\n1\n0"
        self.assertEqual(run_program(input_data), expected)

    def test_toggle_same_index_twice(self) -> None:
        input_data = "3 4\n1 2\n2 1 3\n1 2\n2 1 3\n"
        expected = "1\n0"
        self.assertEqual(run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
