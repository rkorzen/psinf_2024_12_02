import asyncio

async def async_task(name, delay):
    print(f"Watek {name} rozpoczł działanie")
    await asyncio.sleep(delay)  
    print(f"Watek {name} zakończył działanie")


async def main():

    tasks = [
        async_task("A", 2),
        async_task("B", 2),
        async_task("C", 2),
        
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time
    t1 = time.time()
    asyncio.run(main())
    print(f"Czas: {time.time() - t1}")
    
