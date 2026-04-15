import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AI = ROOT / "10221_ai_simple.py"
MAN = ROOT / "10221_manual.py"


CASE_INPUT = """500 30 deg
700 60 min
200 45 deg
"""

CASE_EXPECT = """3633.775503 3592.408346
124.616509 124.614927
5215.043805 5082.035982"""


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
    print("[TEST] 10221 開始")
    ai = run(AI, CASE_INPUT)
    mh = run(MAN, CASE_INPUT)
    assert ai == CASE_EXPECT, "AI 版本輸出不符範例"
    assert mh == CASE_EXPECT, "手打版本輸出不符範例"
    assert ai == mh
    print("[PASS] 範例測資")
    print("[DONE] 10221 測試通過")


if __name__ == "__main__":
    main()
