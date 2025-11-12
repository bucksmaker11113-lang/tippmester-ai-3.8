# MZ/X 4.5 Fusion³D Core - Feature Store modul
# Feladata: AI tanulási inputok előkészítése és tárolása

import pandas as pd
import os
from datetime import datetime

class FeatureStore:
    """Központi tároló a tisztított és előkészített tanulási adatokhoz."""

    def __init__(self, path="data/processed/features.csv"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(f"[FeatureStore] Inicializálva → {self.path}")

    def save_features(self, df: pd.DataFrame):
        """Tisztított feature-adatok mentése CSV-be."""
        if df.empty:
            print("[FeatureStore] Üres adathalmaz – nem menthető.")
            return False

        df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            df.to_csv(self.path, index=False, mode='a', header=not os.path.exists(self.path))
            print(f"[FeatureStore] {len(df)} sor hozzáadva a feature-store-hoz.")
            return True
        except Exception as e:
            print(f"[FeatureStore] Mentési hiba: {e}")
            return False

    def load_features(self, limit=1000):
        """Legutóbbi feature-adatok betöltése a tanuláshoz."""
        if not os.path.exists(self.path):
            print("[FeatureStore] Nincs korábbi feature fájl.")
            return pd.DataFrame()

        try:
            df = pd.read_csv(self.path)
            print(f"[FeatureStore] {len(df)} sor betöltve a feature-store-ból.")
            return df.tail(limit)
        except Exception as e:
            print(f"[FeatureStore] Betöltési hiba: {e}")
            return pd.DataFrame()
