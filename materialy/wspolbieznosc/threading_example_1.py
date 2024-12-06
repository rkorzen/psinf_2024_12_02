import threading
import time

def worker(name, delay):
    print(f"Wątek {name} rozpoczął działanie.")
    time.sleep(delay)
    print(f"Wątek {name} zakończył działanie.")

if __name__ == "__main__":
    t1 = time.time()
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(f"W{i+1}", 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Wszystkie wątki zakończyły działanie w {time.time() - t1:.2f} sekund.")
