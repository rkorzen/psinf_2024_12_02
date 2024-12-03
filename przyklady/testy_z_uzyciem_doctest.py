def add(a, b):
    """
    Dodaje dwie liczby

    Przykład:
    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b


def div(a, b):
    """
    Dzieli dwie liczby
    
    Przykład:
    >>> div(1, 2)
    0.5
    >>> div(1, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return a / b


def reverse_string(s: str) -> str:
    """
    Odwraca string
    
    Przykład:
    >>> reverse_string("abc")
    'cba'

    >>> reverse_string("")
    ''
    """
    return s[::-1]


def get_sorted_keys(d: dict) -> list:
    """
    Zwraca posortowane klucze słownika

    Przykład:
    >>> get_sorted_keys({"a": 1, "b": 2, "c": 3})
    ['a', 'b', 'c']
    """
    return sorted(d.keys())


def return_gen():
    """
    Zwraca generator

    Przykład:
    >>> list(return_gen())
    [1, 2, 3]
    """
    yield from [1, 2, 3]


def hello():
    """
    Pyta o imię i wita

    Przykład:
    >>> import builtins
    >>> builtins.input = lambda: "Ala"
    >>> hello()
    Jak masz na imię?
    Hello Ala!
    """

    print("Jak masz na imię?")
    imie = input()
    print(f"Hello {imie}!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
