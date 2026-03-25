import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR / "problem_10050_handwritten.py"


def run_program(input_data: str) -> str:
    result = subprocess.run(
        [sys.executable, str(TARGET)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test10050(unittest.TestCase):
    def test_sample(self) -> None:
        input_data = "1\n14\n3\n3\n4\n8\n"
        expected = "5"
        self.assertEqual(run_program(input_data), expected)

    def test_everyday_hartal_with_weekend(self) -> None:
        input_data = "1\n7\n2\n1\n2\n"
        expected = "5"
        self.assertEqual(run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
