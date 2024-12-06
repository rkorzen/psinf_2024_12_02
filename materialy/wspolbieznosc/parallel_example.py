from multiprocessing import Pool
import time

def square(x):
    return x * x

if __name__ == "__main__":
    start_time = time.time()
    with Pool(4) as pool:  # Tworzymy pulę z 4 procesów
        results = pool.map(square, range(100_000_000), chunksize=10000)
    end_time = time.time()
    print(f"Parallel processing time: {end_time - start_time:.2f} seconds")

