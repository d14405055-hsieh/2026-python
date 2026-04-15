import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AI = ROOT / "10190_ai_simple.py"
MAN = ROOT / "10190_manual.py"


def run(script: Path, data: str) -> str:
    cp = subprocess.run(
        [sys.executable, str(script)],
        input=data,
        text=True,
        capture_output=True,
        check=True,
    )
    return cp.stdout.strip()


def main() -> None:
    print("[TEST] 10190 開始")

    case1_in = """2 4 3 10
0 1 1
3 1 -1
"""
    case1_out = "65.00"

    ai1 = run(AI, case1_in)
    m1 = run(MAN, case1_in)
    assert ai1 == case1_out, f"AI case1 錯誤: {ai1}"
    assert m1 == case1_out, f"手打 case1 錯誤: {m1}"
    assert ai1 == m1
    print("[PASS] case1")

    case2_in = """1 5 10 2
0 5 0
"""
    case2_out = "0.00"
    ai2 = run(AI, case2_in)
    m2 = run(MAN, case2_in)
    assert ai2 == case2_out
    assert m2 == case2_out
    print("[PASS] case2")

    print("[DONE] 10190 測試通過")


if __name__ == "__main__":
    main()
