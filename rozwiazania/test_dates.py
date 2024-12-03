import unittest
from datetime import datetime
from zoneinfo import ZoneInfo
from dates import convert_date_to_timezones, is_dst

class TestConvertDateToTimezones(unittest.TestCase):
    def test_convert_date_to_timezones(self):
        date = datetime(2024, 1, 1, 12, 0, 0, tzinfo=ZoneInfo("UTC"))
        timezones = ["Europe/Warsaw", "America/New_York", "Asia/Tokyo"]
        result = convert_date_to_timezones(date, timezones)
        expected = {
            "Europe/Warsaw": datetime(2024, 1, 1, 13, 0, 0, tzinfo=ZoneInfo("Europe/Warsaw")),
            "America/New_York": datetime(2024, 1, 1, 7, 0, 0, tzinfo=ZoneInfo("America/New_York")),
            "Asia/Tokyo": datetime(2024, 1, 1, 21, 0, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        }
        self.assertEqual(result, expected)


class TestIsDst(unittest.TestCase):
    def test_is_dst_for_winter_time(self):
        date = datetime(2024, 1, 1, 12, 0, 0, tzinfo=ZoneInfo("Europe/Warsaw"))
        self.assertFalse(is_dst(date, "Europe/Warsaw"))

    def test_is_dst_for_summer_time(self):
        date = datetime(2024, 6, 1, 12, 0, 0, tzinfo=ZoneInfo("Europe/Warsaw"))
        self.assertTrue(is_dst(date, "Europe/Warsaw"))

if __name__ == "__main__":
    unittest.main()

