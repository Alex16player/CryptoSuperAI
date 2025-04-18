import streamlit as st
import os
import sys

# 📌 Add parent directory to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'super_ai')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

# 📦 Try to import your custom modules
try:
    from super_ai.ensemble_model import load_ensemble_model
    from super_ai.vote_system import vote_decision
    from utils.indicators import calculate_indicators
    from utils.preprocessing import load_price_data
except ModuleNotFoundError as e:
    st.error(f"❌ Importfehler: {e}")
    st.stop()

# 🧠 Load model once
@st.cache_resource
def get_model():
    try:
        return load_ensemble_model("models/super_ai_model.pkl")
    except Exception as e:
        st.error(f"❌ Fehler beim Laden des Modells: {e}")
        return None

# 🧾 Hauptseite
st.set_page_config(page_title="CryptoSuperAI", layout="wide")
st.title("🧠 CryptoSuperAI – KI-gestütztes Krypto-Trading")

# 📈 Eingabe: Ticker & Zeitrahmen
ticker = st.text_input("💱 Kryptowährung", "BTC")
timeframe = st.selectbox("⏰ Zeitrahmen", ["1m", "5m", "15m", "1h", "4h", "1d"])

# 🚀 Daten laden & verarbeiten
if st.button("📊 Daten analysieren & Vorhersage starten"):
    with st.spinner("Daten werden geladen..."):
        try:
            df = load_price_data(ticker, timeframe)
            df = calculate_indicators(df)
            model = get_model()
            if model:
                prediction = vote_decision(df, model)
                st.success(f"📢 Super-KI Empfehlung: **{prediction.upper()}**")
                st.line_chart(df["close"])
        except Exception as e:
            st.error(f"❌ Fehler während der Analyse: {e}")
