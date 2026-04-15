import subprocess
import sys
from pathlib import Path


def run_case(input_text: str) -> str:
    script = Path(__file__).with_name("QUESTION-299.py")
    completed = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def main() -> None:
    input_text = """3
3
3 1 2
4
4 3 2 1
5
1 3 5 2 4
"""
    expected = """Optimal train swapping takes 2 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 3 swaps."""

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