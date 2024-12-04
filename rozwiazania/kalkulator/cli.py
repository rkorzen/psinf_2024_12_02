import sys
from core import exchange

if len(sys.argv) != 3:
    print("Usage: cli.py <currency> <amount>")
    sys.exit(1)

currency, amount = sys.argv[1], float(sys.argv[2])
print(f"{amount} {currency} is {exchange(currency, amount):.2f} PLN")
