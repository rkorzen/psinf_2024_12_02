import os

module_1_content = """
# run this script as module to see the effect
# python -m mypackage.module1
# to see error, run this script directly
# python module1.py
# or
# python mypackage/module1.py
from .module2 import some_function

def main():
    some_function()

if __name__ == "__main__":
    main()
"""

module_2_content = """
# This script contains function that will be imported
# in module1.py and subpackage/module3.py


def some_function():
    print("Hello from module2!")

if __name__ == "__main__":
    some_function()
"""

module_3_content = """
# run this script as module to see the effect
# python -m mypackage.subpackage.module3
# to see error, run this script directly
# python mypackage/subpackage/module3.py

from ..module2 import some_function

def main():
    some_function()

if __name__ == "__main__":
    main()
"""


def create_example_structure():
    structure = {
        "relative_imports_example": {
            "__init__.py": "",
            "module1.py": module_1_content,
            "module2.py": module_2_content,
            "subpackage": {
                "__init__.py": "",
                "module3.py": module_3_content,
            }
        }
    }

    def create_files(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(path, content)
            else:
                with open(path, "w") as file:
                    file.write(content)

    create_files(".", structure)

create_example_structure()
