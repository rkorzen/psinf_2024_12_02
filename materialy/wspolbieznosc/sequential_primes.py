import time

def is_prime(n):
    """Sprawdza, czy liczba jest pierwsza."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    """Liczy liczby pierwsze w danym zakresie."""
    return sum(1 for i in range(start, end) if is_prime(i))

if __name__ == "__main__":
    start_time = time.time()
    result = count_primes_in_range(2, 10_000_000)  # Zakres do sprawdzenia
    end_time = time.time()
    print(f"Sequential: Found {result} primes in {end_time - start_time:.2f} seconds")

