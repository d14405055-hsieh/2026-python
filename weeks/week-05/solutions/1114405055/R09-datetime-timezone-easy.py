"""R09 easy：時區轉換速記版。"""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo


def timezone_convert() -> dict[str, datetime]:
    """Chicago -> Taipei 的轉換，並示範 UTC 儲存。"""
    central = ZoneInfo("America/Chicago")
    taipei = ZoneInfo("Asia/Taipei")
    utc = ZoneInfo("UTC")
    local = datetime(2012, 12, 21, 9, 30, tzinfo=central)
    return {
        "local": local,
        "to_taipei": local.astimezone(taipei),
        "to_utc": local.astimezone(utc),
    }


if __name__ == "__main__":
    print(timezone_convert())
