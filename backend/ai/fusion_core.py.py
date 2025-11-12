# MZ/X 4.5 Fusion³D Core - Ensemble AI Motor
# Összehangolja a Monte Carlo, Hybrid Bias és Sentiment Core motorokat

import asyncio
from datetime import datetime
from ai.montecarlo import MonteCarlo
from ai.hybrid_bias import HybridBias
from ai.sentiment_core import SentimentCore
from meta.meta_mind import MetaMind

class FusionCore:
    """Többszintű AI-összegző és háttértanuló rendszer."""

    def __init__(self):
        self.mc = MonteCarlo()
        self.bias = HybridBias()
        self.sent = SentimentCore()
        self.meta = MetaMind()
        self.last_result = None
        print("[FusionCore] Inicializálás kész – AI modulok betöltve.")

    async def background_learning(self):
        """Aszinkron AI-tanulás ciklus (5 percenként fut)."""
        while True:
            try:
                self.learn_cycle()
            except Exception as e:
                print(f"[FusionCore] Hiba a tanulási ciklusban: {e}")
            await asyncio.sleep(300)

    def learn_cycle(self):
        """Egy tanulási ciklus végrehajtása."""
        print("[FusionCore] Tanulási ciklus indítása...")

        # 1️⃣ Egyesített szignálok lekérése
        mc_signal = self.mc.predict()
        bias_signal = self.bias.calculate()
        sent_signal = self.sent.analyze()

        # 2️⃣ Többségi szavazásos döntés
        final_signal = self.vote([mc_signal, bias_signal, sent_signal])

        # 3️⃣ MetaMind állapotfrissítés
        state = self.meta.analyze_state(bias_signal, sent_signal)
        self.last_result = {
            "signal": final_signal,
            "state": state,
            "time": datetime.now().strftime("%H:%M:%S")
        }

        # 4️⃣ Log kiírás (később küldhető overlay / voice modulnak)
        print(f"[FusionCore] Eredmény: {final_signal} | Állapot: {state} | Idő: {self.last_result['time']}")

        return self.last_result

    def vote(self, signals):
        """Többségi döntés a három AI között."""
        try:
            return max(set(signals), key=signals.count)
        except Exception:
            return "neutral"

    def get_last_result(self):
        """Utolsó AI-döntés lekérése (API / overlay számára)."""
        return self.last_result or {"signal": "n/a", "state": "unknown"}
