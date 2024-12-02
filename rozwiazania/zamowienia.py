

orders = [
    {"product": "Laptop", "type": "online", "category": "electronics", "amount": 1200},
    {"product": "Chair", "type": "store", "category": "furniture", "amount": 300},
    {"product": "Book", "type": "vip", "category": "books", "amount": 50},
    {"product": "Phone", "type": "online", "category": "electronics", "amount": 800},
    {"product": "Table", "type": "store", "category": "furniture", "amount": 500},
]


def tax_factory(rate):
    def calculate_tax(amount):
        return amount * rate
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


def process_order(order, tax_calculator):
    
    # tutaj trzeba zaaplikowac logike zamowienia:

    
    # logika obliczania podatku:
    order["tax_amount"] = tax_calculator(order["amount"])
    
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
        
        processed_order = process_order(order, tax_calculator)
    

        summary["total_value"] += processed_order["amount"]
        summary["total_tax"] += processed_order["tax_amount"]
        summary["order_count_by_type"][processed_order["type"]] += 1

    print("Podsumowanie zamówień:")
    print(summary)

process_orders(orders)