import csv
from datetime import datetime, timedelta
from dates import is_dst
from collections import defaultdict
from pathlib import Path

TimeSession = dict[str, datetime]
EmployeesDict = dict[str, list[TimeSession]]

def read_csv(file_path) -> EmployeesDict:
    result: EmployeesDict = defaultdict(list)

    with open(file_path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            employee_id = row["ID"]
            start_time = datetime.fromisoformat(row["start_time"])
            end_time = datetime.fromisoformat(row["end_time"])

            result[employee_id].append({
                "start": start_time,
                "end": end_time
            })
    return result

def get_duration(session: TimeSession) -> tuple[datetime, datetime, timedelta]:
    start = session["start"]
    end = session["end"]
    duration = end - start
    return start, end, duration

def fmt_date(date: datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M:%S %Z")

def generate_detailed_report(employee_id: str, data: EmployeesDict):
    """
    Raport szczegółowy dla pracownika ID 001:
    - 2024-06-15 08:30:00 CEST -> 2024-06-15 16:30:00 CEST (Czas trwania: 8:00:00, DST: Tak)
    - 2024-12-15 08:30:00 CET -> 2024-12-15 16:30:00 CET (Czas trwania: 8:00:00, DST: Nie)
    Łączny czas pracy: 16 godzin i 0 minut.
    
    """

    print(f"Raport szczegółowy dla pracownika ID {employee_id}:")

    sessions = data[employee_id]

    for session in sessions:
        start, end, duration = get_duration(session)
        is_summer_time = is_dst(start) or is_dst(end)
        print(f"{fmt_date(start)} -> {fmt_date(end)} (Czas trwania: {duration}, DST: {'Tak' if is_summer_time else 'Nie'})")

def generate_summary_report(data: EmployeesDict):
    for employee_id, sessions in data.items():
        

        total_duration = timedelta()
        dst_duration = timedelta()

        for session in sessions:
            start, end, duration = get_duration(session)
            total_duration += duration
            if is_dst(start) or is_dst(end):
                dst_duration += duration

        non_dst_duration = total_duration - dst_duration
        
        total_hours, total_minutes = divmod(total_duration.seconds, 3600)
        total_minutes = total_minutes // 60

        dst_hours, dst_minutes = divmod(dst_duration.seconds, 3600)
        dst_minutes = dst_minutes // 60

        non_dst_hours, non_dst_minutes = divmod(non_dst_duration.seconds, 3600)
        non_dst_minutes = non_dst_minutes // 60


        print(f"Pracownik ID {employee_id}")
        print(f"  - Łączny czas pracy: {total_hours} godzin i {total_minutes} minut.")
        print(f"  - Czas pracy w DST: {dst_hours} godzin i {dst_minutes} minut.")
        print(f"  - Czas pracy poza DST: {non_dst_hours} godzin i {non_dst_minutes} minut.")


if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent.parent
    data_file = BASE_DIR / "dane" / "work_sessions.csv"
    data = read_csv(data_file)
    generate_detailed_report("001", data)
    generate_summary_report(data)