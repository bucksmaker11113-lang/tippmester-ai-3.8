# MZ/X 4.5 Fusion³D Core - Report Mailer modul
# Feladata: napi riport e-mailben történő kiküldése automatikusan vagy manuálisan

import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from reports.report_generator import generate_daily_report

# Címzett (módosítható, de be van állítva alapértelmezésként)
DEFAULT_RECEIVER = "bucksmaker11111@gmail.com"

class ReportMailer:
    """Riport e-mailes értesítő rendszer."""

    def __init__(self, sender="mzxfusion@system.ai", smtp_server="localhost"):
        self.sender = sender
        self.smtp_server = smtp_server
        print("[ReportMailer] Inicializálva – alapértelmezett e-mail beállítások betöltve.")

    def create_message(self, report: dict):
        """Riport adataiból e-mail szöveg létrehozása."""
        body = (
            f"📊 MZ/X 4.5 Fusion³D Core – Napi AI Riport\n\n"
            f"Dátum: {report['timestamp']}\n"
            f"Rendszer állapota: {report['ai_status']}\n"
            f"Átlagos biztonsági szint: {report['confidence_avg']}\n"
            f"Átlagos ROI: {report['roi_avg']} %\n"
            f"Megjegyzés: {report['note']}\n\n"
            f"Automatikus üzenet – MZ/X 4.5 rendszer"
        )

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = f"MZ/X napi AI-riport – {report['timestamp']}"
        msg["From"] = self.sender
        msg["To"] = DEFAULT_RECEIVER
        return msg

    def send_mail(self, report: dict):
        """E-mail küldése az alapértelmezett címre."""
        try:
            msg = self.create_message(report)

            # ⚙️ Alap SMTP küldés (Railway kompatibilis mock serverrel)
            with smtplib.SMTP(self.smtp_server) as server:
                server.send_message(msg)
                print(f"[ReportMailer] Riport elküldve → {DEFAULT_RECEIVER}")

            return True

        except Exception as e:
            print(f"[ReportMailer] Hiba az e-mail küldés során: {e}")
            return False


# === Külső függvény – egyszerű hívás API-ból ===
def send_daily_report():
    """Teljes napi riport generálása és kiküldése."""
    report = generate_daily_report()
    mailer = ReportMailer()
    mailer.send_mail(report)
    return {
        "status": "sent",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "receiver": DEFAULT_RECEIVER
    }
