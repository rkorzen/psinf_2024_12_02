import time

def process_message(msg):
    return f"Processed {msg}"

if __name__ == "__main__":
    start_time = time.time()
    messages = [process_message(f"Message {i}") for i in range(10_000)]
    print(f"Processed {len(messages)} messages")
    end_time = time.time()
    print(f"Sequential processing time: {end_time - start_time:.2f} seconds")
