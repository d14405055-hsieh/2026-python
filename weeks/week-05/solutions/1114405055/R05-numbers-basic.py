"""R05. 數字基礎：四捨五入、進制、格式化。"""

from __future__ import annotations

import math
from decimal import Decimal, localcontext


def rounding_examples() -> dict[str, int | float]:
    """示範銀行家捨入與負位數 round。"""
    a = 1627731
    return {
        "round_1": round(1.27, 1),
        "round_3": round(1.25361, 3),
        "round_half_0_5": round(0.5),
        "round_half_2_5": round(2.5),
        "round_hundreds": round(a, -2),
    }


def decimal_examples() -> dict[str, float | Decimal]:
    """示範 float 誤差、Decimal 精確度與 fsum。"""
    da, db = Decimal("4.2"), Decimal("2.1")
    with localcontext() as ctx:
        ctx.prec = 3
        div_val = Decimal("1.3") / Decimal("1.7")
    return {
        "float_sum": 4.2 + 2.1,
        "decimal_sum": da + db,
        "decimal_div": div_val,
        "fsum": math.fsum([1.23e18, 1, -1.23e18]),
    }


def format_examples(x: float = 1234.56789) -> dict[str, str]:
    """回傳常見數字格式化結果。"""
    return {
        "fixed_2": format(x, "0.2f"),
        "align_10_1": format(x, ">10.1f"),
        "comma": format(x, ","),
        "comma_fixed_2": format(x, "0,.2f"),
        "scientific": format(x, "e"),
    }


def base_examples(n: int = 1234) -> dict[str, int | str]:
    """示範二、八、十六進制轉換與反轉。"""
    return {
        "bin": bin(n),
        "oct": oct(n),
        "hex": hex(n),
        "format_b": format(n, "b"),
        "format_x": format(n, "x"),
        "from_hex": int("4d2", 16),
        "from_oct": int("2322", 8),
    }


if __name__ == "__main__":
    print(rounding_examples())
    print(decimal_examples())
    print(format_examples())
    print(base_examples())
