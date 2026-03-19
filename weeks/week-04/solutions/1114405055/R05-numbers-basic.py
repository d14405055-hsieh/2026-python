# R05. 數字基礎：四捨五入、進制、格式化（3.1-3.4）
# 主題：round / Decimal / math.fsum / format / bin/oct/hex

import math
from decimal import Decimal, localcontext


def demo_rounding():
    """3.1 四捨五入規則。"""
    print("=== 3.1 四捨五入 ===")
    print("round(1.27, 1) ->", round(1.27, 1))
    print("round(1.25361, 3) ->", round(1.25361, 3))

    # Python 使用銀行家捨入：.5 會捨入到最近偶數。
    print("round(0.5) ->", round(0.5))
    print("round(1.5) ->", round(1.5))
    print("round(2.5) ->", round(2.5))

    value = 1627731
    # ndigits 為負時，表示對十位/百位/千位進行四捨五入。
    print("round(1627731, -2) ->", round(value, -2))


def demo_decimal_and_fsum():
    """3.2 浮點誤差與高精度解法。"""
    print("\n=== 3.2 精確浮點數 ===")
    print("4.2 + 2.1 ->", 4.2 + 2.1)

    da, db = Decimal("4.2"), Decimal("2.1")
    print("Decimal('4.2') + Decimal('2.1') ->", da + db)

    # localcontext 可暫時調整 Decimal 精度，不影響全域設定。
    with localcontext() as ctx:
        ctx.prec = 3
        print("Decimal('1.3') / Decimal('1.7') with prec=3 ->", Decimal("1.3") / Decimal("1.7"))

    # fsum 對「大數 + 小數 + 負大數」等情境更穩定。
    nums = [1.23e18, 1, -1.23e18]
    print("normal sum with + ->", nums[0] + nums[1] + nums[2])
    print("math.fsum(nums) ->", math.fsum(nums))


def demo_number_formatting():
    """3.3 常見數字格式化。"""
    x = 1234.56789
    print("\n=== 3.3 數字格式化 ===")
    print("format(x, '0.2f') ->", format(x, "0.2f"))
    print("format(x, '>10.1f') ->", format(x, ">10.1f"))
    print("format(x, ',') ->", format(x, ","))
    print("format(x, '0,.2f') ->", format(x, "0,.2f"))
    print("format(x, 'e') ->", format(x, "e"))


def demo_base_conversion():
    """3.4 二進位/八進位/十六進位互轉。"""
    n = 1234
    print("\n=== 3.4 進制轉換 ===")
    print("bin(n) ->", bin(n))
    print("oct(n) ->", oct(n))
    print("hex(n) ->", hex(n))
    print("format(n, 'b') ->", format(n, "b"))
    print("format(n, 'x') ->", format(n, "x"))
    print("int('4d2', 16) ->", int("4d2", 16))
    print("int('2322', 8) ->", int("2322", 8))


if __name__ == "__main__":
    demo_rounding()
    demo_decimal_and_fsum()
    demo_number_formatting()
    demo_base_conversion()
