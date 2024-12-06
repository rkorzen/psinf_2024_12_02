from multiprocessing import Pool
import time

def is_prime(n):
    """Sprawdza, czy liczba jest pierwsza."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_chunk(chunk):
    """Liczy liczby pierwsze w danym kawałku zakresu."""
    start, end = chunk
    return sum(1 for i in range(start, end) if is_prime(i))

if __name__ == "__main__":
    start_time = time.time()

    # Definiujemy zakres i dzielimy go na kawałki
    RANGE = (2, 10_000_000)
    NUM_PROCESSES = 8
    chunk_size = (RANGE[1] - RANGE[0]) // NUM_PROCESSES
    chunks = [(RANGE[0] + i * chunk_size, RANGE[0] + (i + 1) * chunk_size) for i in range(NUM_PROCESSES)]

    # Tworzymy pulę procesów i przetwarzamy równolegle
    with Pool(NUM_PROCESSES) as pool:
        results = pool.map(count_primes_in_chunk, chunks)

    total_primes = sum(results)  # Sumujemy wyniki z wszystkich procesów
    end_time = time.time()

    print(f"Parallel: Found {total_primes} primes in {end_time - start_time:.2f} seconds")
