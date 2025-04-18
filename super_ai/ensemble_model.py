# super_ai/ensemble_model.py

import joblib

# Dummy-Loader für Modell (kann später durch echtes Modell ersetzt werden)
def load_ensemble_model(path=None):
    # Du kannst später hier ein echtes Modell mit joblib.load(path) laden
    class DummyModel:
        def predict(self, X):
            return [1]  # 1 = BUY, 0 = SELL
    return DummyModel()
