from __future__ import annotations

import math
import sys


def solve(data: str) -> str:
    rows = [s.strip() for s in data.splitlines() if s.strip()]
    if not rows:
        return ""

    case_count = int(rows[0])
    ans: list[str] = []

    for case_no in range(1, case_count + 1):
        s1 = rows[2 * case_no - 1]
        s2 = rows[2 * case_no]
        n1 = int(s1, 2)
        n2 = int(s2, 2)

        if math.gcd(n1, n2) > 1:
            ans.append(f"Pair #{case_no}: All you need is love!")
        else:
            ans.append(f"Pair #{case_no}: Love is not all you need!")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
