from rich import print
from tabulate import tabulate
from typing import Callable

orders = [
    {"product": "Laptop", "type": "online", "category": "electronics", "amount": 1200},
    {"product": "Chair", "type": "store", "category": "furniture", "amount": 300},
    {"product": "Book", "type": "vip", "category": "books", "amount": 50},
    {"product": "Phone", "type": "online", "category": "electronics", "amount": 800},
    {"product": "Table", "type": "store", "category": "furniture", "amount": 500},
]


def tax_factory(rate):
    def calculate_tax(order):
        order["tax_amount"] = order["calculated_amount"] * rate
        order["tax_rate"] = rate
        return order
    return calculate_tax

tax_functions = {
    "electronics": tax_factory(0.15),
    "furniture": tax_factory(0.10),
    "books": tax_factory(0.05),
}


# logika przetwarzania zamówienia
# dla online - dorzucamy 10 zł - kosztu dostawy
# dla vip - 10% rabatu ale tylko dla zamówień powyżej 100zł
# dla store - 5% rabatu

def process_online_order(order: dict[str, str | int]) -> dict[str, str | int]:
    order["calculated_amount"] = order["amount"] + 10
    order["discount"] = 10
    return order

def process_vip_order(order):
    if order["amount"] > 100:
        order["calculated_amount"] = order["amount"] * 0.9
        order["discount"] =  -(order["amount"] - order["calculated_amount"])
    else:
        order["calculated_amount"] = order["amount"]
        order["discount"] = 0
    return order

def process_store_order(order):
    order["calculated_amount"] = order["amount"] * 0.95
    order["discount"] =  -(order["amount"] - order["calculated_amount"])
    return order

order_processors = {
    "online": process_online_order,
    "vip": process_vip_order,
    "store": process_store_order,
}


def process_order(order: dict, tax_calculator: Callable, order_processor: Callable) -> dict:
    
    # tutaj trzeba zaaplikowac logike zamowienia:
    order = order_processor(order)

    # logika obliczania podatku:
    order = tax_calculator(order)
    
    return order

def process_orders(orders):

    summary = {
        "total_value": 0,
        "total_tax": 0,
        "order_count_by_type": {
            "online": 0,
            "store": 0,
            "vip": 0,
        }
    }

    for order in orders:
        tax_calculator = tax_functions[order["category"]]
        order_processor = order_processors[order["type"]]

        processed_order = process_order(order, tax_calculator, order_processor)


        summary["total_value"] += processed_order["amount"]
        summary["total_tax"] += processed_order["tax_amount"]
        summary["order_count_by_type"][processed_order["type"]] += 1

    print("Podsumowanie zamówień:")
    print(summary)
    print(display_summary_table(orders))


def display_summary_table(orders):

    return tabulate(orders, headers="keys", tablefmt="grid")


process_orders(orders)