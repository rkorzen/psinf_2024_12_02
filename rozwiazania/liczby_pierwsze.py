def is_prime(n: int) -> bool:
    """
    Sprawdza czy podana liczba jest pierwsza.
    
    Args:
        n: Liczba całkowita do sprawdzenia
        
    Returns:
        bool: True jeśli liczba jest pierwsza, False w przeciwnym razie
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(25)
        False
        >>> is_prime(0)
        False
        >>> is_prime(1)
        False
        >>> is_prime(-5)
        False
    """
    if n < 2:
        return False
        
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
            
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
