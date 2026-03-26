"""R08 easy：日期範圍與字串轉日期速記版。"""

from __future__ import annotations

from calendar import monthrange
from datetime import date, datetime, timedelta


def month_range(start: date) -> tuple[date, date]:
    """回傳該月起日與下月起日（右開區間）。"""
    _, days = monthrange(start.year, start.month)
    return start, start + timedelta(days=days)


def parse_ymd(text: str) -> datetime:
    """手動 split 解析 YYYY-MM-DD。"""
    y, m, d = text.split("-")
    return datetime(int(y), int(m), int(d))


def calendar_basics() -> dict[str, object]:
    """整理兩個核心題型：月範圍 + 日期解析。"""
    first, next_first = month_range(date(2012, 8, 1))
    return {
        "first": first,
        "last": next_first - timedelta(days=1),
        "parsed": parse_ymd("2012-09-20"),
    }


if __name__ == "__main__":
    print(calendar_basics())
