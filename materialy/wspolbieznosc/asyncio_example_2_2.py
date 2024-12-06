async def fetch_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Pobrano dane z {url} ({len(content)} znaków)")
        return content

async def main():
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.google.com"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        # Przechowywanie wyników
        for url, content in zip(urls, results):
            print(f"Zawartość z {url}: {content[:100]}...")  # Wyświetl pierwsze 100 znaków

if __name__ == "__main__":
    import time
    t1 = time.time()
    asyncio.run(main())
    print(f"Wszystkie zadania zakończone w {time.time() - t1:.2f} sekund.")
