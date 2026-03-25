import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR / "problem_10056_handwritten.py"


def run_program(input_data: str) -> str:
    result = subprocess.run(
        [sys.executable, str(TARGET)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test10056(unittest.TestCase):
    def test_common_case(self) -> None:
        input_data = "1\n3 0.5 2\n"
        expected = "0.2857"
        self.assertEqual(run_program(input_data), expected)

    def test_zero_probability(self) -> None:
        input_data = "1\n10 0.0 3\n"
        expected = "0.0000"
        self.assertEqual(run_program(input_data), expected)


if __name__ == "__main__":
    unittest.main()
