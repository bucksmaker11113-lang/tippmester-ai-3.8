# MZ/X 4.5 Fusion³D Core - MetaMind modul
# A mesterséges intelligencia "tudata" és döntési naplója

from datetime import datetime

class MetaMind:
    """Az MZ/X belső logikai és önellenőrző modulja."""
    
    def __init__(self):
        self.state = "semleges"
        self.last_update = None
        self.logs = []
        print("[MetaMind] Inicializálás sikeres – belső tudati modul aktív.")

    def analyze_state(self, bias_value, sentiment):
        """Elemzi a torzítás és hangulat kapcsolatát, meghatározza a rendszerállapotot."""
        if bias_value > 0 and sentiment == "positive":
            self.state = "emelkedő"
        elif bias_value < 0 and sentiment == "negative":
            self.state = "csökkenő"
        elif sentiment == "neutral":
            self.state = "semleges"
        else:
            self.state = "bizonytalan"

        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"Állapot: {self.state.upper()} | Bias: {bias_value:.3f} | Sentiment: {sentiment}"
        self.log_message(msg)
        print(f"[MetaMind] {msg}")
        return self.state

    def log_message(self, message: str):
        """Üzenetet ment a belső logba, később overlay / riport modulhoz."""
        entry = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "message": message
        }
        self.logs.append(entry)
        if len(self.logs) > 100:
            self.logs.pop(0)  # ne nőjön végtelenre

    def get_logs(self, limit=10):
        """Legutóbbi üzenetek lekérése."""
        return self.logs[-limit:]

    def trigger_retrain(self):
        """AI újratanítás manuális vagy automatikus indítása."""
        self.log_message("Újratanítási ciklus elindítva.")
        print("[MetaMind] Újratanítási ciklus aktiválva.")
        # ide jöhet később a tényleges retrain logic
