"""R05 easy：數字基礎速記版。"""

from __future__ import annotations

import math
from decimal import Decimal


def numbers_basics() -> dict[str, object]:
    """把四捨五入、Decimal、格式化、進位轉換一次示範。"""
    n = 1234
    x = 1234.56789
    return {
        "round_half_even_0_5": round(0.5),
        "round_half_even_2_5": round(2.5),
        "decimal_exact": Decimal("4.2") + Decimal("2.1"),
        "fsum": math.fsum([1.23e18, 1, -1.23e18]),
        "fmt": format(x, "0,.2f"),
        "bin": format(n, "b"),
        "hex": format(n, "x"),
    }


if __name__ == "__main__":
    print(numbers_basics())
