from multiprocessing import Pool
import time

def is_prime(n):
    if n < 2: return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def count_primes_in_range(chunk):
    start, end = chunk
    return sum([1 for i in range(start, end) if is_prime(i)])


if __name__ == "__main__":
    start_time = time.time()
    
    RANGE = (2, 10000)
    NUM_PROCESSES = 8
    
    chunk_size = (RANGE[1] - RANGE[0]) // NUM_PROCESSES
    
    chunks = [(RANGE[0] + i * chunk_size, RANGE[0] + (i+1) * chunk_size) for i in range(NUM_PROCESSES)]
    chunks

    with Pool(NUM_PROCESSES) as pool:
        results = pool.map(count_primes_in_range, chunks)

    total_primes = sum(results)
    end_time = time.time()
    print(f"Parallel: Found {results} primes in {end_time - start_time:.2f} s")
    
