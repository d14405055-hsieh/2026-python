"""UVA 948 - Counterfeit Dollar (generalized coin set).

讀取多組測資，根據秤重結果找出唯一可能的假幣編號。
若無法唯一判定，輸出 0。
"""

from __future__ import annotations

from dataclasses import dataclass
import sys
from typing import Iterable, List


@dataclass
class Weighing:
    left: List[int]
    right: List[int]
    result: str  # '<', '>', '='


def _check_mode(coin: int, is_heavier: bool, weighings: Iterable[Weighing]) -> bool:
    """檢查某硬幣在指定輕重模式下是否與所有秤重相容。"""
    for w in weighings:
        in_left = coin in w.left
        in_right = coin in w.right

        if w.result == "=":
            if in_left or in_right:
                return False
            continue

        # 非平衡時，假幣必須在秤盤上，且方向必須符合結果。
        if not in_left and not in_right:
            return False

        if w.result == "<":
            if is_heavier:
                if in_left:
                    return False
            else:
                if in_right:
                    return False
        elif w.result == ">":
            if is_heavier:
                if in_right:
                    return False
            else:
                if in_left:
                    return False
        else:
            return False

    return True


def identify_fake_coin(n: int, weighings: List[Weighing]) -> int:
    """回傳唯一可成立的假幣編號，否則回傳 0。"""
    candidates: List[int] = []

    for coin in range(1, n + 1):
        heavier_ok = _check_mode(coin, True, weighings)
        lighter_ok = _check_mode(coin, False, weighings)
        if heavier_ok or lighter_ok:
            candidates.append(coin)

    return candidates[0] if len(candidates) == 1 else 0


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    idx = 0
    t = int(tokens[idx])
    idx += 1

    outputs: List[str] = []
    for _ in range(t):
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        weighings: List[Weighing] = []
        for _ in range(k):
            p = int(tokens[idx])
            idx += 1
            left = list(map(int, tokens[idx : idx + p]))
            idx += p
            right = list(map(int, tokens[idx : idx + p]))
            idx += p
            result = tokens[idx]
            idx += 1
            weighings.append(Weighing(left, right, result))

        outputs.append(str(identify_fake_coin(n, weighings)))

    return "\n\n".join(outputs)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
