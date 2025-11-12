import numpy as np

class MonteCarloEngine:
    def __init__(self, iterations=5000):
        self.iterations = iterations

    def generate_signal(self, df):
        if df is None or len(df) < 10:
            return "neutral"
        returns = df["close"].pct_change().dropna()
        outcomes = []
        for _ in range(self.iterations):
            sim = np.random.choice(returns, len(returns), replace=True)
            outcomes.append(np.mean(sim))
        mean_outcome = np.mean(outcomes)
        if mean_outcome > 0.002:
            return "long"
        elif mean_outcome < -0.002:
            return "short"
        return "neutral"
