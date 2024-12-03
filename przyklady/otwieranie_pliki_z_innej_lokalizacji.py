import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
p = BASE_DIR / "dane" / "work_sessions.csv"

# with open(p, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
    
#     for row in reader:
#         print(row)


with p.open() as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        print(row)
