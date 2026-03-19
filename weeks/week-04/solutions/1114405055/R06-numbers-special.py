# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
a = float("inf")
b = float("-inf")
c = float("nan")
print("無窮大與 NaN:")
print(f"float('inf'): {a}, float('-inf'): {b}, float('nan'): {c}")  # inf -inf nan
print(f"math.isinf({a}): {math.isinf(a)}")  # True
print(f"math.isnan({c}): {math.isnan(c)}")  # True
print(f"{a} + 45: {a + 45}, 10 / {a}: {10 / a}")  # inf 0.0
print(f"{a} / {a}: {a / a}, {a} + {b}: {a + b}")  # nan nan（未定義）
print(f"{c} == {c}: {c == c}")  # False（NaN 不等於自己！）

# ── 3.8 分數運算 ──────────────────────────────────────
print(f"\n分數運算:")
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(f"Fraction(5, 4) + Fraction(7, 16): {p + q}")  # 27/16
print(f"numerator: {r.numerator}, denominator: {r.denominator}")  # 35 64
print(f"float({r}): {float(r)}")  # 0.546875
print(f"limit_denominator(8): {r.limit_denominator(8)}")  # 4/7
print(f"Fraction(*(3.75).as_integer_ratio()): {Fraction(*(3.75).as_integer_ratio())}")  # 15/4

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
print(f"\n隨機操作:")
print(f"random.choice({values}): {random.choice(values)}")  # 隨機一個
print(f"random.sample({values}, 3): {random.sample(values, 3)}")  # 3 個不重複樣本

values = [1, 2, 3, 4, 5, 6]
random.shuffle(values)
print(f"打亂後的 {values} ")  # 打亂後的序列

print(f"random.randint(0, 10): {random.randint(0, 10)}")  # 0~10 整數

# 固定種子以重現結果
print(f"\n固定種子重現:")
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(3)]
print(f"第一次 (seed=42): {seq1}")

random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(3)]
print(f"第二次 (seed=42): {seq2}")
print(f"相同: {seq1 == seq2}")  # True

print(f"random.random(): {random.random()}")  # 隨機浮點數
