# MZ/X 4.5 Fusion³D Core - Bias Mapper modul
# Feladata: torzítási értékek elemzése és klaszterezése az AI tanulási adataiból

import numpy as np
from sklearn.cluster import KMeans
from datetime import datetime

class BiasMapper:
    """Nemlineáris torzítás-elemző és vizualizációs előkészítő modul."""

    def __init__(self):
        self.model = None
        self.labels = None
        self.last_update = None
        print("[BiasMapper] Modul inicializálva – KMeans elemzésre kész.")

    def map_clusters(self, bias_values, n_clusters=3):
        """KMeans klaszterezés az AI által gyűjtött bias értékekre."""
        if not bias_values or len(bias_values) < n_clusters:
            print("[BiasMapper] Nincs elég adat klaszterezéshez.")
            return None

        X = np.array(bias_values).reshape(-1, 1)
        kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
        kmeans.fit(X)

        self.model = kmeans
        self.labels = kmeans.labels_
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        clusters = {}
        for i in range(n_clusters):
            cluster_points = X[self.labels == i].flatten().tolist()
            clusters[i] = {
                "átlag": round(np.mean(cluster_points), 4),
                "darab": len(cluster_points)
            }

        print(f"[BiasMapper] {n_clusters} klaszter létrehozva | Utolsó frissítés: {self.last_update}")
        return clusters

    def predict_cluster(self, new_bias):
        """Meghatározza, melyik klaszterbe tartozik egy új torzítási érték."""
        if self.model is None:
            print("[BiasMapper] Nincs betöltött modell.")
            return None
        label = int(self.model.predict([[new_bias]])[0])
        print(f"[BiasMapper] Bias érték {new_bias:.4f} → klaszter #{label}")
        return label
