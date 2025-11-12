# MZ/X 4.5 Fusion³D Core - Logger modul
# Feladata: egységes logolási és naplózási rendszer biztosítása az egész alkalmazás számára

import os
from datetime import datetime
import threading

class Logger:
    """Színes, időbélyeges logolás fájlba és konzolra egyaránt."""

    def __init__(self, logfile="data/logs/mzx_core.log"):
        self.logfile = logfile
        os.makedirs(os.path.dirname(logfile), exist_ok=True)
        self.lock = threading.Lock()
        print(f"[Logger] Inicializálva → {self.logfile}")

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message: str, level: str = "INFO"):
        """Log bejegyzés rögzítése."""
        entry = f"[{self._timestamp()}] [{level}] {message}"
        color = {
            "INFO": "\033[94m",    # kék
            "WARN": "\033[93m",    # sárga
            "ERROR": "\033[91m",   # piros
            "SUCCESS": "\033[92m", # zöld
        }.get(level, "\033[0m")

        # Konzolra színesen
        print(f"{color}{entry}\033[0m")

        # Fájlba is mentés
        with self.lock:
            with open(self.logfile, "a", encoding="utf-8") as f:
                f.write(entry + "\n")

    # === Kényelmi rövidítések ===
    def info(self, msg): self.log(msg, "INFO")
    def success(self, msg): self.log(msg, "SUCCESS")
    def warn(self, msg): self.log(msg, "WARN")
    def error(self, msg): self.log(msg, "ERROR")


# === Globális logger példány (importálható) ===
logger = Logger()
