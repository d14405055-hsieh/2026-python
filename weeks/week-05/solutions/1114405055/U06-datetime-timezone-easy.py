"""U06 easy：UTC 優先速記版。"""

from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def timezone_easy() -> tuple[datetime, datetime]:
    """同一個本地時間，直接加減與 UTC 計算會不同。"""
    central = ZoneInfo("America/Chicago")
    utc = ZoneInfo("UTC")
    local = datetime(2013, 3, 10, 1, 45, tzinfo=central)
    wrong = local + timedelta(minutes=30)
    correct = (local.astimezone(utc) + timedelta(minutes=30)).astimezone(central)
    return wrong, correct


if __name__ == "__main__":
    print(timezone_easy())
