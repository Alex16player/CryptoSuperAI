# super_ai/ensemble_model.py

class DummyModel:
    def predict(self, X):
        return [1]  # Dummy: gibt immer "buy" zurück

def load_ensemble_model(path=None):
    return DummyModel()
