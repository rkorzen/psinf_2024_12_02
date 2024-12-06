import time

def square(x):
    return x * x

if __name__ == "__main__":
    start_time = time.time()
    results = [square(x) for x in range(100_000_000)]
    end_time = time.time()
    print(f"Sequential processing time: {end_time - start_time:.2f} seconds")
