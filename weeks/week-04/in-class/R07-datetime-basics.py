"""R07. 日期時間基本運算。"""

from __future__ import annotations

from datetime import datetime, timedelta

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def timedelta_examples() -> dict[str, object]:
    """示範 timedelta 加減與總時數計算。"""
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    dt = datetime(2012, 9, 23)
    d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
    return {
        "days": c.days,
        "hours": c.total_seconds() / 3600,
        "plus_10_days": dt + timedelta(days=10),
        "d2_minus_d1_days": (d2 - d1).days,
        "leap_diff": (datetime(2012, 3, 1) - datetime(2012, 2, 28)).days,
        "normal_diff": (datetime(2013, 3, 1) - datetime(2013, 2, 28)).days,
    }


def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    """取得 start 之前最近一次的指定星期。"""
    if start is None:
        start = datetime.today()
    day_num = start.weekday()
    target = WEEKDAYS.index(dayname)
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


if __name__ == "__main__":
    print(timedelta_examples())
    base = datetime(2012, 8, 28)
    print(get_previous_byday("Monday", base))
    print(get_previous_byday("Friday", base))
