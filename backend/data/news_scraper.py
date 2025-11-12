import requests
from bs4 import BeautifulSoup

class NewsScraper:
    """Egyszerű hírgyűjtő Cointelegraph és Coindesk oldalakról."""
    def __init__(self):
        self.sources = [
            "https://cointelegraph.com/",
            "https://www.coindesk.com/"
        ]

    def fetch_latest(self, limit=5):
        headlines = []
        for url in self.sources:
            try:
                r = requests.get(url, timeout=10)
                soup = BeautifulSoup(r.text, "lxml")
                for h in soup.find_all("h2")[:limit]:
                    text = h.get_text(strip=True)
                    if len(text) > 20:
                        headlines.append(text)
            except Exception as e:
                print(f"[NewsScraper] Hiba: {e}")
        return headlines
