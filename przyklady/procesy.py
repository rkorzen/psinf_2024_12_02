import multiprocessing
import time

def worker(name, duration):
    """
    Funkcja reprezentująca pracę wykonywaną przez każdy proces.
    """
    print(f"{name} started")
    time.sleep(duration)
    print(f"{name} finished")

def run_multiprocessing():
    """
    Główna funkcja uruchamiająca procesy.
    """
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(f"Process-{i}", 2))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")

# Konieczne dla poprawnego działania w Jupyter Notebooku
if __name__ == "__main__":
    t = time.time()
    run_multiprocessing()
    print(f"Time taken: {time.time() - t} seconds")
