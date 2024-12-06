import time

def compute_sum(n):
    return sum(range(n))

if __name__ == "__main__":
    start_time = time.time()
    results = [compute_sum(10_000_000) for _ in range(4)]
    print(f"Results: {results}")
    end_time = time.time()
    print(f"Sequential processing time: {end_time - start_time:.2f} seconds")

