"""U04. 數字精度的陷阱與選擇。"""

from __future__ import annotations

import math
import timeit
from decimal import ROUND_HALF_UP, Decimal


def trad_round(x: float, n: int = 0) -> Decimal:
    """傳統四捨五入：使用 Decimal + ROUND_HALF_UP。"""
    d = Decimal(str(x))
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


def rounding_demo() -> dict[str, int | Decimal]:
    """比較銀行家捨入與傳統四捨五入。"""
    return {
        "round_0_5": round(0.5),
        "round_2_5": round(2.5),
        "round_3_5": round(3.5),
        "trad_0_5": trad_round(0.5),
        "trad_2_5": trad_round(2.5),
    }


def nan_demo(data: list[float]) -> tuple[bool, bool, list[float]]:
    """示範 NaN 比較陷阱與過濾。"""
    c = float("nan")
    clean = [x for x in data if not math.isnan(x)]
    return c == c, math.isnan(c), clean


def float_vs_decimal() -> dict[str, object]:
    """比較 float 與 Decimal 在精度與效能上的差異。"""
    t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
    t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
    return {
        "float_sum": 0.1 + 0.2,
        "float_eq": (0.1 + 0.2 == 0.3),
        "decimal_sum": Decimal("0.1") + Decimal("0.2"),
        "decimal_eq": (Decimal("0.1") + Decimal("0.2") == Decimal("0.3")),
        "float_time": t1,
        "decimal_time": t2,
    }


if __name__ == "__main__":
    print(rounding_demo())
    print(nan_demo([1.0, float("nan"), 3.0, float("nan"), 5.0]))
    print(float_vs_decimal())
