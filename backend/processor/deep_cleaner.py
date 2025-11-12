# MZ/X 4.5 Fusion³D Core - Deep Data Cleaner modul
# Feladata: adattisztítás, zajszűrés és anomália detektálás az AI tanuláshoz

import pandas as pd
from sklearn.ensemble import IsolationForest
from datetime import datetime

class DeepCleaner:
    """Automatikus adattisztító az AI-tanulási folyamatokhoz."""

    def __init__(self, contamination=0.01):
        self.contamination = contamination
        self.last_run = None
        print(f"[DeepCleaner] Modul inicializálva (kontamináció: {contamination*100:.1f}%).")

    def clean_dataframe(self, df: pd.DataFrame):
        """Eltávolítja az anomáliás sorokat numerikus oszlopok alapján."""
        if df.empty:
            print("[DeepCleaner] Üres DataFrame – nincs mit tisztítani.")
            return df

        try:
            num_df = df.select_dtypes(include=["number"])
            clf = IsolationForest(contamination=self.contamination, random_state=42)
            preds = clf.fit_predict(num_df)

            clean_df = df[preds == 1].copy()
            self.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            removed = len(df) - len(clean_df)
            print(f"[DeepCleaner] Tisztítás kész ({removed} sor eltávolítva). Idő: {self.last_run}")

            return clean_df

        except Exception as e:
            print(f"[DeepCleaner] Hiba a tisztítás során: {e}")
            return df
