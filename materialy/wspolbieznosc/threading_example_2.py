
import threading
import requests
import time

def fetch_url(url):
    print(f"Rozpoczęto pobieranie: {url}")
    response = requests.get(url)
    print(f"Pobrano dane z: {url} ({len(response.content)} bajtów)")

if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.google.com"
    ]

    start_time = time.time()

    threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"Wszystkie żądania zakończone w {time.time() - start_time:.2f} sekund.")
