# demo_script.py
# Ten skrypt demonstruje działanie namespace packages.
# Nie musisz ręcznie ustawiać PYTHONPATH, ponieważ ścieżki zostaną dodane do sys.path w tym skrypcie.

import sys
import os

# Dodanie katalogów namespace_part1 i namespace_part2 do sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([
    os.path.join(current_dir, "namespace_part1"),
    os.path.join(current_dir, "namespace_part2"),
])

# Importy z namespace package
from mynamespace.module1 import func1
from mynamespace.module2 import func2

if __name__ == "__main__":
    func1()
    func2()
