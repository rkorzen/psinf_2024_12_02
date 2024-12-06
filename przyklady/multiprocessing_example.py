from multiprocessing import Pool
import math
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n

def count_primes_in_chunks(chunk):
    start, end = chunk
    return [n for n in range(start, end) if is_prime(n)]

if __name__ == "__main__":
    # Duży zakres danych
    total_range = 1_000_000
    chunk_size = 50_000
    ranges = [(i, i + chunk_size) for i in range(1, total_range, chunk_size)]

    # Sekwencyjne wykonanie
    start_time = time.time()
    sequential_results = []
    for chunk in ranges:
        sequential_results.append(count_primes_in_chunks(chunk))
    sequential_all_primes = [prime for sublist in sequential_results for prime in sublist]
    sequential_time = time.time() - start_time
    print(f"SEKWENCYJNE - Wszystkie liczby pierwsze: {len(sequential_all_primes)}")
    print(f"Czas sekwencyjny: {sequential_time:.2f} s")

    # Wykonanie z użyciem multiprocessing
    start_time = time.time()
    with Pool(processes=4) as pool:
        parallel_results = pool.map(count_primes_in_chunks, ranges)
    parallel_all_primes = [prime for sublist in parallel_results for prime in sublist]
    parallel_time = time.time() - start_time
    print(f"RÓWNOLEGŁE - Wszystkie liczby pierwsze: {len(parallel_all_primes)}")
    print(f"Czas równoległy: {parallel_time:.2f} s")

    # Porównanie czasów
    print(f"\nRóżnica czasu: {sequential_time - parallel_time:.2f} s")
