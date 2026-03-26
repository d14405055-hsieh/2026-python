"""R06 easy：特殊數值速記版。"""

from __future__ import annotations

import math
import random
from fractions import Fraction


def special_numbers(seed: int = 42) -> dict[str, object]:
    """inf / nan / Fraction / random 的最小可記憶版本。"""
    rng = random.Random(seed)
    a = float("inf")
    c = float("nan")
    f = Fraction(5, 4) * Fraction(7, 16)
    return {
        "isinf": math.isinf(a),
        "isnan": math.isnan(c),
        "nan_eq_self": (c == c),
        "fraction": f,
        "fraction_float": float(f),
        "rand": rng.randint(0, 10),
    }


if __name__ == "__main__":
    print(special_numbers())
