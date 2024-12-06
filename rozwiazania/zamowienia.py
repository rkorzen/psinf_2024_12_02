from rich import print

# Funkcje przetwarzające zamówienia
def process_online_order(order):
    order["amount"] += 10  # Opłata za przesyłkę
    return order

def process_store_order(order):
    order["amount"] *= 0.95  # 5% rabatu
    return order

def process_vip_order(order):
    """
    10% rabatu, o ile wartość zamówienia to 100 PLN lub więcej.
    """
    if order["amount"] >= 100:
        order["amount"] *= 0.90  # 10% rabatu
    return order

# Słownik typów zamówień
order_processors = {
    "online": process_online_order,
    "store": process_store_order,
    "vip": process_vip_order,
}

# Fabryka funkcji dla podatków
def tax_factory(rate):
    def calculate_tax(amount):
        return amount * rate / 100, rate
    return calculate_tax

# Słownik reguł podatkowych
tax_rules = {
    "electronics": tax_factory(15),
    "books": tax_factory(5),
    "furniture": tax_factory(10),
}

# Funkcja do przetwarzania jednego zamówienia
def process_order(order, order_processor, tax_calculator):
    # Przetwarzanie zamówienia
    order = order_processor(order)
    # Obliczanie podatku

    tax_amount, tax_rate = tax_calculator(order["amount"])

    order["tax_rate"] = tax_rate
    order["tax_amount"] = tax_amount
    
    return order

# Funkcja główna
def process_orders(orders):
    summary = {"total_value": 0, "total_tax": 0,"order_count_by_type": {}}

    for order in orders:
        # Wybierz odpowiednią logikę przetwarzania
        order_processor = order_processors[order["type"]]
        tax_calculator = tax_rules[order["category"]]

        # Przetwórz zamówienie
        processed_order = process_order(order, order_processor, tax_calculator)

        # Aktualizuj podsumowanie
        summary["total_value"] += processed_order["amount"]
        summary["total_tax"] += processed_order["tax_amount"]
        summary["order_count_by_type"].setdefault(order["type"], 0)
        summary["order_count_by_type"][order["type"]] += 1

    return summary

# Przetwarzanie zamówień
orders = [
    {"product": "Laptop", "type": "online", "category": "electronics", "amount": 1200},
    {"product": "Chair", "type": "store", "category": "furniture", "amount": 300},
    {"product": "Book", "type": "vip", "category": "books", "amount": 50},
    {"product": "Phone", "type": "online", "category": "electronics", "amount": 800},
    {"product": "Table", "type": "store", "category": "furniture", "amount": 500},
]

summary = process_orders(orders)
print("Podsumowanie zamówień:", summary)