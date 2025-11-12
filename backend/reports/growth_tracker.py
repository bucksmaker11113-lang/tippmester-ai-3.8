# MZ/X 4.5 Fusion³D Core - Growth Tracker modul
# Feladata: az AI rendszer teljesítményének, ROI-jának és találati arányának követése

import os
import json
from datetime import datetime

class GrowthTracker:
    """Napi / heti szintű AI fejlődési trendeket követő modul."""

    def __init__(self, path="data/reports/growth_log.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(f"[GrowthTracker] Inicializálva → {self.path}")

    def log_result(self, roi: float, confidence: float, bias_value: float):
        """Egy új tanulási eredmény hozzáadása a loghoz."""
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "roi": round(roi, 3),
            "confidence": round(confidence, 3),
            "bias": round(bias_value, 3)
        }

        data = self._load_data()
        data.append(entry)
        self._save_data(data)

        print(f"[GrowthTracker] Új eredmény mentve → ROI: {roi:.2f}, Confidence: {confidence:.2f}")

    def get_summary(self, last_n=20):
        """Összegző statisztika az utolsó N rekord alapján."""
        data = self._load_data()[-last_n:]
        if not data:
            return {"avg_roi": 0, "avg_conf": 0, "avg_bias": 0}

        avg_roi = sum(d["roi"] for d in data) / len(data)
        avg_conf = sum(d["confidence"] for d in data) / len(data)
        avg_bias = sum(d["bias"] for d in data) / len(data)

        return {
            "avg_roi": round(avg_roi, 3),
            "avg_conf": round(avg_conf, 3),
            "avg_bias": round(avg_bias, 3),
            "entries": len(data)
        }

    def _load_data(self):
        """Segédfüggvény: log betöltése JSON-ból."""
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _save_data(self, data):
        """Segédfüggvény: log mentése JSON-ba."""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
