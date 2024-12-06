from multiprocessing import Process, Queue
import time

def compute_sum(n, queue):
    queue.put(sum(range(n)))

if __name__ == "__main__":
    start_time = time.time()
    queue = Queue()
    processes = [Process(target=compute_sum, args=(10_000_000, queue)) for _ in range(4)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    results = [queue.get() for _ in range(4)]
    print(f"Results: {results}")
    end_time = time.time()
    print(f"Parallel processing time: {end_time - start_time:.2f} seconds")
