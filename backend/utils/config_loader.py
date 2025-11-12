# MZ/X 4.5.1 Fusion³D Core - Config Loader modul
# Feladata: beállítások és környezeti változók egységes kezelése

import os
import json
from utils.logger import logger

class Config:
    """Központi konfigurációkezelő modul az MZ/X rendszerhez."""

    def __init__(self, path="config.json"):
        self.path = path
        self.data = self._load_config()
        logger.info(f"Beállítások betöltve: {list(self.data.keys())}")

    def _load_config(self):
        """Config betöltése JSON-ból vagy környezeti változókból."""
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Nem sikerült beolvasni a config.json-t: {e}")
                return self._default_config()
        else:
            logger.warn("config.json nem található – alapértelmezett beállításokkal indul a rendszer.")
            return self._default_config()

    def _default_config(self):
        """Alapértelmezett biztonságos beállítások (Railway fallback)."""
        return {
            "EMAIL_RECEIVER": os.getenv("EMAIL_RECEIVER", "bucksmaker11111@gmail.com"),
            "DATA_PATH": os.getenv("DATA_PATH", "data/"),
            "REPORT_PATH": os.getenv("REPORT_PATH", "data/reports/"),
            "CACHE_PATH": os.getenv("CACHE_PATH", "data/cache/"),
            "AI_REFRESH_MINUTES": int(os.getenv("AI_REFRESH_MINUTES", 5)),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "APP_MODE": os.getenv("APP_MODE", "production"),
            "VERSION": "4.5.1",
            # Új beállítások az AutoReport Buildhez:
            "AUTO_REPORT_ENABLED": os.getenv("AUTO_REPORT_ENABLED", "true").lower() == "true",
            "REPORT_HOUR": int(os.getenv("REPORT_HOUR", 22))
        }

    def get(self, key, default=None):
        """Biztonságos lekérdezés."""
        return self.data.get(key, default)

    def save(self):
        """Beállítások mentése config.json-ba."""
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            logger.success(f"Beállítások mentve: {self.path}")
        except Exception as e:
            logger.error(f"Nem sikerült menteni a config.json-t: {e}")


# === Globális config objektum az egész rendszerhez ===
config = Config()
