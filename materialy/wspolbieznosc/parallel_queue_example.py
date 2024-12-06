from multiprocessing import Process, Queue
import time

def process_message(msg, queue):
    queue.put(f"Processed {msg}")

if __name__ == "__main__":
    start_time = time.time()
    queue = Queue()

    n = 10
    processes = [Process(target=process_message, args=(f"Message {i}", queue)) for i in range(n)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    processed_messages = [queue.get() for _ in range(n)]
    print(f"Processed {len(processed_messages)} messages")
    end_time = time.time()
    print(f"Parallel processing time: {end_time - start_time:.2f} seconds")

