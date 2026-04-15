import subprocess
import sys
from pathlib import Path


def run_case(input_text: str) -> str:
    script = Path(__file__).with_name("QUESTION-118.py")
    completed = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def main() -> None:
    input_text = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
"""
    expected = """1 1 E
3 3 N LOST
2 3 S"""

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