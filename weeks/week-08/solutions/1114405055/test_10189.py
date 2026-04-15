import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AI_FILE = ROOT / "10189_ai_simple.py"
MANUAL_FILE = ROOT / "10189_manual.py"


CASE_1_INPUT = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""

CASE_1_EXPECTED = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100"""


def run_script(script: Path, data: str) -> str:
    cp = subprocess.run(
        [sys.executable, str(script)],
        input=data,
        text=True,
        capture_output=True,
        check=True,
    )
    return cp.stdout.strip()


def main() -> None:
    print("[TEST] 開始測試 10189")

    ai_out = run_script(AI_FILE, CASE_1_INPUT)
    hand_out = run_script(MANUAL_FILE, CASE_1_INPUT)

    assert ai_out == CASE_1_EXPECTED, "AI 版本與預期輸出不一致"
    print("[PASS] AI 版本通過範例測資")

    assert hand_out == CASE_1_EXPECTED, "手打版本與預期輸出不一致"
    print("[PASS] 手打版本通過範例測資")

    assert ai_out == hand_out, "AI 版本與手打版本輸出不一致"
    print("[PASS] 兩版本輸出一致")

    print("[DONE] 全部測試通過")


if __name__ == "__main__":
    main()
