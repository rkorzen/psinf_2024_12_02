def add(a, b):
    """
    Dodaje dwie liczby.

    Przykład:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


def greet(name):
    """
    Wypisuje powitanie.

    Przykład:
    >>> greet("Rafał")
    Cześć, Rafał!
    """
    print(f"Cześć, {name}!")


def ask_name():
    """
    Pyta o imię i wita użytkownika.

    Przykład:
    >>> import builtins
    >>> builtins.input = lambda: "Rafał"
    >>> ask_name()
    Jak masz na imię?
    Cześć, Rafał!
    """
    print("Jak masz na imię?")
    name = input()
    print(f"Cześć, {name}!")



if __name__ == "__main__":
    import doctest
    doctest.testmod()
