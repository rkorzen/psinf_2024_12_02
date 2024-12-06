import asyncio

async def async_task(name, delay):
    print(f"Zadanie {name} rozpoczęte.")
    await asyncio.sleep(delay)
    print(f"Zadanie {name} zakończone po {delay} sekundach.")

async def main():
    tasks = [
        async_task("A", 2),
        async_task("B", 3),
        async_task("C", 1)
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    import time
    t1 = time.time()
    asyncio.run(main())
    print(f"Wszystkie zadania zakończone w {time.time() - t1:.2f} sekund.")
