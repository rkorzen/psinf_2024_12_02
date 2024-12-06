def buggy_function():
    a = 5
    b = 0
    breakpoint()
    c = a / b  # Błąd dzielenia przez zero
    print(c)

if __name__ == "__main__":
    import ipdb; ipdb.set_trace()  # Punkt zatrzymania
    buggy_function()
