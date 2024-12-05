import asyncio
import aiohttp

urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.google.com"
    ]

async def fetch_url(session, url):
    print(f"Rozpoczęto pobieranie: {url}")
    
    async with session.get(url) as response:
        content = await response.text()
        print(f"pobrano dane z {url} ({len(content)} b)")
        return content
    
    
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time
    t1 = time.time()
    asyncio.run(main())
    print(f"Czas {time.time()-t1}")
