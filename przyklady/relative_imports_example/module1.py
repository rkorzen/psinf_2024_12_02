
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
