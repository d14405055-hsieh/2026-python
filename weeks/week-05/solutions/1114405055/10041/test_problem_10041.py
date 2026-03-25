import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR / "problem_10041_handwritten.py"


def run_program(input_data: str) -> str:
    result = subprocess.run(
        [sys.executable, str(TARGET)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test10041(unittest.TestCase):
    def test_basic_cases(self) -> None:
        input_data = "2\n2 2 4\n3 2 4 6\n"
        expected = "2\n4"
        self.assertEqual(run_program(input_data), expected)

    def test_unbalanced_addresses(self) -> None:
        input_data = "1\n5 1 2 3 4 100\n"
        expected = "101"
        self.assertEqual(run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
