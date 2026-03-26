"""U05. 日期時間常見陷阱。"""

from __future__ import annotations

import calendar
import timeit
from datetime import datetime


def add_one_month(dt: datetime) -> datetime:
    """月份 +1，若目標月天數不足，將日期 clamp 到月底。"""
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month)
    return dt.replace(year=year, month=month, day=day)


def use_strptime(s: str) -> datetime:
    """標準做法：strptime。"""
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    """高效做法：手動 split 後轉 int。"""
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


def benchmark_parse(number: int = 100) -> tuple[float, float]:
    """比較 strptime 與手動解析的效能。"""
    dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]
    t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=number)
    t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=number)
    return t1, t2


if __name__ == "__main__":
    print(add_one_month(datetime(2012, 1, 31)))
    print(add_one_month(datetime(2012, 9, 23)))
    print(benchmark_parse())
