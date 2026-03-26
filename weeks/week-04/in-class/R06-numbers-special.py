"""R06. 特殊數值：無窮大、NaN、分數、隨機。"""

from __future__ import annotations

import math
import random
from fractions import Fraction


def inf_nan_examples() -> dict[str, object]:
	"""示範 inf 與 nan 的常見運算結果。"""
	a = float("inf")
	b = float("-inf")
	c = float("nan")
	return {
		"isinf": math.isinf(a),
		"isnan": math.isnan(c),
		"inf_add": a + 45,
		"div_inf": 10 / a,
		"inf_div_inf_is_nan": math.isnan(a / a),
		"inf_plus_ninf_is_nan": math.isnan(a + b),
		"nan_equal_self": c == c,
	}


def fraction_examples() -> dict[str, object]:
	"""示範 Fraction 的加乘、近似與轉換。"""
	p = Fraction(5, 4)
	q = Fraction(7, 16)
	r = p * q
	return {
		"sum": p + q,
		"mul_num_den": (r.numerator, r.denominator),
		"float": float(r),
		"limit_8": r.limit_denominator(8),
		"from_ratio": Fraction(*(3.75).as_integer_ratio()),
	}


def random_examples(seed: int = 42) -> dict[str, object]:
	"""使用固定種子產生可重現隨機結果。"""
	rng = random.Random(seed)
	values = [1, 2, 3, 4, 5, 6]
	picked = rng.choice(values)
	sampled = rng.sample(values, 3)
	shuffled = values[:]
	rng.shuffle(shuffled)
	randint_value = rng.randint(0, 10)
	random_value = rng.random()
	return {
		"choice": picked,
		"sample": sampled,
		"shuffled": shuffled,
		"randint": randint_value,
		"random": random_value,
	}


if __name__ == "__main__":
	print(inf_nan_examples())
	print(fraction_examples())
	print(random_examples())
