import subprocess
import sys
from pathlib import Path


def run_case(input_text: str) -> str:
    script = Path(__file__).with_name("QUESTION-100.py")
    completed = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def main() -> None:
    input_text = """1 10
100 200
201 210
900 1000
"""
    expected = """1 10 20
100 200 125
201 210 89
900 1000 174"""

    actual = run_case(input_text)
    if actual != expected:
        print("TEST FAILED")
        print("Expected:")
        print(expected)
        print("Actual:")
        print(actual)
        raise SystemExit(1)

    print("TEST PASSED")
    print(actual)


if __name__ == "__main__":
    main()