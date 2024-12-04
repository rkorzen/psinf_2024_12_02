import requests
from collections import namedtuple

Rate = namedtuple("Rate", ["currency", "code", "mid"])


def get_rates() -> list[Rate]:
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/")
    response.raise_for_status()
    return [Rate(**rate) for rate in response.json()[0]["rates"]]

def exchange(currency: str, amount: float) -> float:
    rates = get_rates()

    for rate in rates:
        if rate.code == currency:
            return amount * rate.mid

    raise ValueError(f"Currency {currency} not found")

if __name__ == "__main__":
    print(exchange("USD", 100))
