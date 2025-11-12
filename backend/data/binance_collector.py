import ccxt
import pandas as pd
from datetime import datetime

class BinanceCollector:
    def __init__(self):
        self.exchange = ccxt.binance()

    def get_data(self, symbol="BTC/USDT", limit=200):
        try:
            ohlc = self.exchange.fetch_ohlcv(symbol, timeframe="1h", limit=limit)
            df = pd.DataFrame(ohlc, columns=["timestamp", "open", "high", "low", "close", "volume"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
            return df
        except Exception as e:
            print(f"[BinanceCollector] Hiba: {e}")
            return None
