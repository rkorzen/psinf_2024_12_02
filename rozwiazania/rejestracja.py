import csv
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path

# Ustalanie bazowego katalogu dla ścieżek plików
BASE_DIR = Path(__file__).parent

def is_dst(date: datetime, timezone: str = "Europe/Warsaw") -> bool:
    """
    Sprawdza, czy data przypada na czas letni (DST) w określonej strefie czasowej.

    :param date: Obiekt datetime (może zawierać FixedOffset).
    :param timezone: Nazwa strefy czasowej (np. 'Europe/Warsaw').
    :return: True, jeśli data przypada na czas letni, False w przeciwnym razie.
    """
    # Pobranie obiektu strefy czasowej na podstawie nazwy
    tz = ZoneInfo(timezone)

    # Konwersja daty do pełnoprawnej strefy czasowej
    # To ważne, ponieważ FixedOffset nie zawiera informacji o DST
    date_with_tz = date.astimezone(tz)

    # Sprawdzanie różnicy DST: jeśli różnica wynosi timedelta(0), nie jest to czas letni
    return date_with_tz.tzinfo.dst(date_with_tz) != timedelta(0)

def read_csv(file_path: str) -> dict:
    """
    Odczytuje dane z pliku CSV i organizuje je w strukturze danych.

    :param file_path: Ścieżka do pliku CSV.
    :return: Słownik z danymi pracowników. Klucz to ID, wartość to lista sesji pracy.
    """
    employees = {}  # Inicjalizacja słownika, który będzie przechowywać dane pracowników

    # Otwieranie pliku CSV w trybie odczytu
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Czytanie danych w formacie słownikowym
        for row in reader:
            employee_id = row['ID']  # Pobieranie ID pracownika z wiersza
            start_time = datetime.fromisoformat(row['start_time'])  # Konwersja daty rozpoczęcia na obiekt datetime
            end_time = datetime.fromisoformat(row['end_time'])  # Konwersja daty zakończenia na obiekt datetime

            # Dodawanie nowego pracownika do słownika, jeśli nie istnieje
            if employee_id not in employees:
                employees[employee_id] = []

            # Dodanie sesji pracy do listy pracownika
            employees[employee_id].append({
                "start": start_time,
                "end": end_time
            })
    
    return employees  # Zwracanie słownika z danymi

def get_duration(session: dict) -> tuple[datetime, datetime, timedelta]:
    """
    Oblicza czas trwania sesji pracy.

    :param session: Słownik zawierający dane sesji pracy (start, end).
    :return: Krotka z datą rozpoczęcia, zakończenia i czasem trwania sesji.
    """
    start = session["start"]
    end = session["end"]
    duration = end - start  # Obliczanie różnicy między start a end
    return start, end, duration

def partial_report(session: dict) -> None:
    """
    Wypisuje szczegóły jednej sesji pracy.

    :param session: Słownik z danymi sesji pracy.
    """
    start, end, duration = get_duration(session)
    is_summer_time = is_dst(start) or is_dst(end)  # Sprawdzenie, czy start lub end przypada na czas letni
    print(f"  - {start.strftime('%Y-%m-%d %H:%M:%S %Z')} -> {end.strftime('%Y-%m-%d %H:%M:%S %Z')} "
          f"(Czas trwania: {duration}, DST: {'Tak' if is_summer_time else 'Nie'})")

def generate_detailed_report(employee_id: str, data: dict) -> None:
    """
    Generuje szczegółowy raport dla wybranego pracownika.

    :param employee_id: ID pracownika.
    :param data: Słownik z danymi pracowników.
    """
    if employee_id not in data:
        print(f"Pracownik o ID {employee_id} nie istnieje.")
        return

    sessions = data[employee_id]  # Pobieranie sesji pracy pracownika
    print(f"Raport szczegółowy dla pracownika ID {employee_id}:")
    total_duration = timedelta()  # Zmienna do sumowania czasu pracy

    # Iterowanie po sesjach pracy i generowanie raportu dla każdej
    for session in sessions:
        partial_report(session)

    # Obliczanie całkowitego czasu pracy
    hours, remainder = divmod(total_duration.total_seconds(), 3600)
    minutes = remainder // 60
    print(f"Łączny czas pracy: {int(hours)} godzin i {int(minutes)} minut.\n")

def generate_summary_report(data: dict) -> None:
    """
    Generuje zbiorczy raport dla wszystkich pracowników.

    :param data: Słownik z danymi pracowników.
    """
    print("Zbiorczy raport dla wszystkich pracowników:")
    for employee_id, sessions in data.items():
        total_duration = timedelta()  # Zmienna na łączny czas pracy
        dst_duration = timedelta()  # Zmienna na czas pracy w DST

        # Iterowanie po sesjach pracy i sumowanie czasu
        for session in sessions:
            start, end, duration = get_duration(session)
            total_duration += duration
            if is_dst(start) or is_dst(end):  # Sprawdzanie, czy sesja przypada na DST
                dst_duration += duration

        non_dst_duration = total_duration - dst_duration  # Czas pracy poza DST
        total_hours, total_minutes = divmod(total_duration.total_seconds(), 3600)
        dst_hours, dst_minutes = divmod(dst_duration.total_seconds(), 3600)
        non_dst_hours, non_dst_minutes = divmod(non_dst_duration.total_seconds(), 3600)

        # Wypisanie podsumowania dla pracownika
        print(f"Pracownik ID {employee_id}:")
        print(f"  - Łączny czas pracy: {int(total_hours)} godzin i {int(total_minutes) // 60} minut.")
        print(f"  - Czas pracy w DST: {int(dst_hours)} godzin i {int(dst_minutes) // 60} minut.")
        print(f"  - Czas pracy poza DST: {int(non_dst_hours)} godzin i {int(non_dst_minutes) // 60} minut.\n")

# Odczytanie danych z pliku CSV
data = read_csv(BASE_DIR.parent / "materialy" / "dane" / "work_sessions.csv")

# Generowanie raportów
generate_detailed_report("001", data)
generate_summary_report(data)
