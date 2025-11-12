# MZ/X 4.5.1 Fusion³D Core - AutoReporter modul
# Feladata: napi automatikus riport generálása és e-mailes küldése

import threading
import schedule
import time
from reports.report_mailer import send_daily_report
from utils.logger import logger
from utils.config_loader import config

class AutoReporter:
    """Háttérfolyamat napi automatikus riportküldéshez."""

    def __init__(self):
        self.enabled = config.get("AUTO_REPORT_ENABLED", True)
        self.report_hour = config.get("REPORT_HOUR", 22)
        if self.enabled:
            logger.info(f"AutoReport ütemezve {self.report_hour}:00 órára.")
            self._start_scheduler()
        else:
            logger.warn("AutoReport funkció kikapcsolva (config alapján).")

    def _start_scheduler(self):
        schedule.every().day.at(f"{self.report_hour:02d}:00").do(self._run_report)
        t = threading.Thread(target=self._loop, daemon=True)
        t.start()

    def _loop(self):
        while True:
            schedule.run_pending()
            time.sleep(60)

    def _run_report(self):
        logger.info("Automatikus riport generálása...")
        try:
            result = send_daily_report()
            logger.success(f"Riport automatikusan elküldve: {result['receiver']}")
        except Exception as e:
            logger.error(f"AutoReport hiba: {e}")
