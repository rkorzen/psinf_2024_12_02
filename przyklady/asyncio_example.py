import asyncio
import time
async def worker(name, duration):
    print(f"{name} started")
    await asyncio.sleep(duration)
    print(f"{name} finished")

async def main():
    tasks = [worker(f"Task-{i}", 2) for i in range(5)]
    await asyncio.gather(*tasks)

t = time.time()
asyncio.run(main())
print(f"Time taken: {time.time() - t} seconds")
