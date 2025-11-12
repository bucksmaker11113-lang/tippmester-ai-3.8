import re
import requests

class SentimentCore:
    """Hírekből, tweetekből és kulcsszavakból egyszerű hangulatelemző."""
    def __init__(self):
        self.positive_words = ["profit", "growth", "bull", "surge", "gain"]
        self.negative_words = ["loss", "drop", "bear", "crash", "fear"]

    def analyze_text(self, text):
        text = text.lower()
        score = 0
        for w in self.positive_words:
            score += len(re.findall(rf"\\b{w}\\b", text))
        for w in self.negative_words:
            score -= len(re.findall(rf"\\b{w}\\b", text))
        return "positive" if score > 0 else "negative" if score < 0 else "neutral"

    def fetch_sentiment(self, symbol="BTCUSDT"):
        try:
            r = requests.get("https://cryptopanic.com/api/v1/posts/?kind=news", timeout=10)
            if r.status_code == 200:
                data = r.json()
                titles = [p["title"] for p in data.get("results", [])[:10]]
                combined = " ".join(titles)
                return self.analyze_text(combined)
        except Exception:
            pass
        return "neutral"
