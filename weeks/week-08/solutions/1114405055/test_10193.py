import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AI = ROOT / "10193_ai_simple.py"
MAN = ROOT / "10193_manual.py"


CASES = [
    ("1\n", "5"),
    ("2\n", "10"),
    ("3\n", "13"),
    ("10\n", "122"),
]


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
    print("[TEST] 10193 開始")
    for idx, (inp, expected) in enumerate(CASES, start=1):
        ai = run(AI, inp)
        mh = run(MAN, inp)
        assert ai == expected, f"AI case{idx} 錯誤: {ai} != {expected}"
        assert mh == expected, f"手打 case{idx} 錯誤: {mh} != {expected}"
        assert ai == mh
        print(f"[PASS] case{idx}")
    print("[DONE] 10193 測試通過")


if __name__ == "__main__":
    main()
