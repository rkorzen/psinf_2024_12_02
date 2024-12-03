
# run this script as module to see the effect
# python -m mypackage.subpackage.module3
# to see error, run this script directly
# python mypackage/subpackage/module3.py

from ..module2 import some_function

def main():
    some_function()

if __name__ == "__main__":
    main()
