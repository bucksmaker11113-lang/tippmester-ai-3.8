import numpy as np
import pandas as pd

class HybridBiasAnalyzer:
    """Trend, momentum és statisztikai torzítások vizsgálata"""
    def __init__(self):
        self.bias_window = 14

    def evaluate_bias(self, df: pd.DataFrame):
        if df is None or len(df) < self.bias_window:
            return "neutral"
        df["returns"] = df["close"].pct_change()
        mean_ret = df["returns"].mean()
        vol = df["returns"].std()
        if mean_ret > vol * 0.5:
            return "bullish_bias"
        elif mean_ret < -vol * 0.5:
            return "bearish_bias"
        return "neutral"

    def calculate_confidence(self, df: pd.DataFrame):
        if "returns" not in df:
            df["returns"] = df["close"].pct_change()
        ratio = np.abs(df["returns"].mean()) / (df["returns"].std() + 1e-6)
        return min(1.0, ratio)
