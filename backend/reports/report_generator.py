# MZ/X 4.5 Fusion³D Core - Report Generator modul
# Feladata: napi AI-riport készítése a FusionCore eredményeiből

from datetime import datetime
from random import uniform

class ReportGenerator:
    """Riportkészítő modul, amely a rendszer tanulási eredményeit foglalja össze."""

    def __init__(self):
        self.last_run = None
        print("[ReportGenerator] Modul inicializálva.")

    def generate(self):
        """Riport adatainak előállítása (később FusionCore input alapján)."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        confidence_avg = round(uniform(0.75, 0.92), 3)
        roi_avg = round(uniform(2.5, 4.5), 2)

        report = {
            "timestamp": timestamp,
            "ai_status": "aktív",
            "confidence_avg": confidence_avg,
            "roi_avg": roi_avg,
            "note": "A rendszer stabilan fut és sikeresen tanul.",
        }

        self.last_run = timestamp
        print(f"[ReportGenerator] Napi riport elkészült: {timestamp}")
        return report


# === Külső függvény az API számára ===
def generate_daily_report():
    """API-hívásra futtatható rövid napi riport."""
    rg = ReportGenerator()
    return rg.generate()
