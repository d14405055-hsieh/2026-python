"""U04 easy：數字精度速記版。"""

from __future__ import annotations

import math
from decimal import ROUND_HALF_UP, Decimal


def trad_round(x: float) -> Decimal:
    """傳統四捨五入：0.5 -> 1。"""
    return Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def precision_easy() -> dict[str, object]:
    """保留最重要觀念：round 行為、NaN、Decimal 精確。"""
    c = float("nan")
    return {
        "round_0_5": round(0.5),
        "trad_round_0_5": trad_round(0.5),
        "nan_eq_self": (c == c),
        "is_nan": math.isnan(c),
        "decimal_ok": (Decimal("0.1") + Decimal("0.2") == Decimal("0.3")),
    }


if __name__ == "__main__":
    print(precision_easy())
