import subprocess
import sys
from pathlib import Path


def run_case(input_text: str) -> str:
    script = Path(__file__).with_name("QUESTION-490.py")
    completed = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout


def main() -> None:
    input_text = """ABC
DE
F
"""
    expected = """FDA
 EB
  C"""

    actual = run_case(input_text)
    if actual != expected:
        print("TEST FAILED")
        print("Expected:")
        print(expected)
        print("Actual:")
        print(actual)
        raise SystemExit(1)

    print("TEST PASSED")
    print(actual, end="")


if __name__ == "__main__":
    main()