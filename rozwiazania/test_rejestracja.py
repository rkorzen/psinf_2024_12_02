import pytest
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os
import csv
from pathlib import Path
from rejestracja import is_dst, read_csv, get_duration, generate_detailed_report, generate_summary_report


# Fixture do tworzenia tymczasowego pliku CSV
@pytest.fixture
def temp_csv(tmp_path):
    file_path = tmp_path / "work_sessions.csv"
    data = [
        {"ID": "001", "start_time": "2024-06-15T08:30:00+02:00", "end_time": "2024-06-15T16:30:00+02:00"},
        {"ID": "001", "start_time": "2024-12-15T08:30:00+01:00", "end_time": "2024-12-15T16:30:00+01:00"},
        {"ID": "002", "start_time": "2024-07-01T09:00:00+02:00", "end_time": "2024-07-01T17:00:00+02:00"}
    ]

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "start_time", "end_time"])
        writer.writeheader()
        writer.writerows(data)

    return file_path


# Test funkcji is_dst
def test_is_dst():
    summer_date = datetime(2024, 6, 15, 12, 0, tzinfo=ZoneInfo("Europe/Warsaw"))
    winter_date = datetime(2024, 12, 15, 12, 0, tzinfo=ZoneInfo("Europe/Warsaw"))

    assert is_dst(summer_date) is True  # Czas letni
    assert is_dst(winter_date) is False  # Czas standardowy


# Test funkcji read_csv
def test_read_csv(temp_csv):
    data = read_csv(temp_csv)
    assert "001" in data
    assert "002" in data

    session = data["001"][0]
    assert session["start"] == datetime.fromisoformat("2024-06-15T08:30:00+02:00")
    assert session["end"] == datetime.fromisoformat("2024-06-15T16:30:00+02:00")


# Test funkcji get_duration
def test_get_duration():
    session = {
        "start": datetime(2024, 6, 15, 8, 30, tzinfo=ZoneInfo("Europe/Warsaw")),
        "end": datetime(2024, 6, 15, 16, 30, tzinfo=ZoneInfo("Europe/Warsaw"))
    }
    start, end, duration = get_duration(session)
    assert duration == timedelta(hours=8)
    assert start.hour == 8
    assert end.hour == 16


# Test funkcji generate_detailed_report
def test_generate_detailed_report(temp_csv, capsys):
    data = read_csv(temp_csv)
    generate_detailed_report("001", data)

    captured = capsys.readouterr()
    assert "2024-06-15 08:30:00 UTC+02:00" in captured.out  # Zmiana na format UTC+02:00
    assert "Czas trwania: 8:00:00" in captured.out
    assert "DST: Tak" in captured.out



# Test funkcji generate_summary_report
def test_generate_summary_report(temp_csv, capsys):
    data = read_csv(temp_csv)
    generate_summary_report(data)

    captured = capsys.readouterr()
    assert "Pracownik ID 001" in captured.out
    assert "Czas pracy w DST: 8 godzin" in captured.out
    assert "Czas pracy poza DST: 8 godzin" in captured.out
    assert "Pracownik ID 002" in captured.out
