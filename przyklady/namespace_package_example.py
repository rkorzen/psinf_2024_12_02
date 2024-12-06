import os

# Zawartość modułów
module1_content = """\
# module1.py
# Funkcja dostępna w namespace package ś
def func1():
    print("Function 1 from part 1")
"""

module2_content = """\
# module2.py
# Funkcja dostępna w namespace package mynamespace
def func2():
    print("Function 2 from part 2")
"""

demo_script_content = """\
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
"""

# Struktura katalogów
structure = {
    "namespace_package_example": {
        "namespace_part1": {
            "mynamespace": {
                "__init__.py": None,  # Brak __init__.py, aby utworzyć namespace package
                "module1.py": module1_content
            }
        },
        "namespace_part2": {
            "mynamespace": {
                "__init__.py": None,  # Brak __init__.py, aby utworzyć namespace package
                "module2.py": module2_content
            }
        },
        "demo_script.py": demo_script_content
    }
}

def create_files(base_path, structure):
    """
    Funkcja tworzy pliki i katalogi na podstawie zadanego słownika struktury.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_files(path, content)
        else:
            if content is not None:  # Tworzymy tylko pliki z treścią
                with open(path, "w") as file:
                    file.write(content)

def create_namespace_package_structure():
    """
    Tworzy strukturę dla demonstracji namespace packages w katalogu namespace_package_example.
    """
    base_path = "namespace_package_example"
    create_files(base_path, structure["namespace_package_example"])

# Uruchomienie skryptu
create_namespace_package_structure()
