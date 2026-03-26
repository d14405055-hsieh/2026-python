"""R07 easy：日期時間基本運算速記版。"""

from __future__ import annotations

from datetime import datetime, timedelta

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def previous_weekday(dayname: str, start: datetime) -> datetime:
    """回傳 start 之前最近一次的指定星期。"""
    offset = (7 + start.weekday() - WEEKDAYS.index(dayname)) % 7 or 7
    return start - timedelta(days=offset)


def datetime_basics() -> dict[str, object]:
    """timedelta 與 weekday 計算重點。"""
    base = datetime(2012, 8, 28)
    span = timedelta(days=2, hours=6) + timedelta(hours=4.5)
    return {
        "hours": span.total_seconds() / 3600,
        "next_10_days": datetime(2012, 9, 23) + timedelta(days=10),
        "previous_monday": previous_weekday("Monday", base),
    }


if __name__ == "__main__":
    print(datetime_basics())
