# super_ai/vote_system.py

def vote_decision(df, model):
    """
    Gibt eine Dummy-Entscheidung basierend auf den letzten Datenzeilen zurück.
    Erwartet ein Modell mit predict-Methode.
    """
    try:
        # Simulierter Feature-Vektor (z. B. [EMA, RSI, MACD])
        X = [[df["ema_20"].iloc[-1], df["rsi"].iloc[-1], df["macd"].iloc[-1]]]
        prediction = model.predict(X)[0]
        return "buy" if prediction == 1 else "sell"
    except Exception as e:
        return f"error: {e}"
