
def add(a, b):
    return a + b


def div(a, b):
    if b == 0:
        return None
        # raise ValueError("Dzielenie przez zero")
    return a / b

print(dir())
print(__name__)

if __name__ == "__main__":
    assert add(1, 2) == 3, "lewa strona nie jest rowna prawej"

    try:
        div(1, 0)
    except ValueError as e:
        assert str(e) == "Dzielenie przez zero", "Nieprawidłowy komunikat"
    else:
        assert False, "Oczekiwano wyjątku ValueError"
