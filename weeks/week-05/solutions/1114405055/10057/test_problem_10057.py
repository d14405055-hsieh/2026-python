import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR / "problem_10057_handwritten.py"


def run_program(input_data: str) -> str:
    result = subprocess.run(
        [sys.executable, str(TARGET)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test10057(unittest.TestCase):
    def test_odd_count(self) -> None:
        input_data = "5\n1 2 3 4 5\n"
        expected = "3 1 1"
        self.assertEqual(run_program(input_data), expected)

    def test_even_count(self) -> None:
        input_data = "4\n1 2 3 4\n"
        expected = "2 2 2"
        self.assertEqual(run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
