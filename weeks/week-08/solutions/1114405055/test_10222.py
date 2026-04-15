import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AI = ROOT / "10222_ai_simple.py"
MAN = ROOT / "10222_manual.py"


def run(script: Path, data: str) -> str:
    cp = subprocess.run(
        [sys.executable, str(script)],
        input=data,
        text=True,
        capture_output=True,
        check=True,
    )
    return cp.stdout


def main() -> None:
    print("[TEST] 10222 開始")

    case1_in = "r\n"
    case1_out = "e\n"

    a1 = run(AI, case1_in)
    m1 = run(MAN, case1_in)
    assert a1 == case1_out
    assert m1 == case1_out
    assert a1 == m1
    print("[PASS] case1")

    case2_in = "t y\n"
    case2_out = "r t\n"
    a2 = run(AI, case2_in)
    m2 = run(MAN, case2_in)
    assert a2 == case2_out
    assert m2 == case2_out
    print("[PASS] case2")

    print("[DONE] 10222 測試通過")


if __name__ == "__main__":
    main()
