from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def convert_date_to_timezones(date: datetime, timezones: list[str]) -> dict[str, datetime]:
    result: dict[str, datetime] = {}
    for timezone in timezones:
        result[timezone] = date.astimezone(ZoneInfo(timezone))
    return result


def is_dst(date: datetime, timezone: str) -> bool:
    tz = ZoneInfo(timezone)
    return date.astimezone(tz).dst() != timedelta(0)