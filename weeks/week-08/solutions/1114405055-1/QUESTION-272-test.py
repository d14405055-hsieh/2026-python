import subprocess
import sys
from pathlib import Path


def run_case(input_text: str) -> str:
    script = Path(__file__).with_name("QUESTION-272.py")
    completed = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout


def main() -> None:
    input_text = '"To be or not to be," quoth the bard, "that is the question."\n'
    expected = "``To be or not to be,'' quoth the bard, ``that is the question.''\n"

    actual = run_case(input_text)
    if actual != expected:
        print("TEST FAILED")
        print("Expected:")
        print(expected, end="")
        print("Actual:")
        print(actual, end="")
        raise SystemExit(1)

    print("TEST PASSED")
    print(actual, end="")


if __name__ == "__main__":
    main()