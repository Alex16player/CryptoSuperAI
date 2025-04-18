# 🚀 CryptoSuperAI - Vollständige Streamlit-WebApp
import streamlit as st
import pandas as pd
import os
import subprocess

# 🔧 Ordnerpfade definieren
base_path = "./CryptoTradingAI"
data_path = os.path.join(base_path, "data")
model_path = os.path.join(base_path, "models")
log_path = os.path.join(base_path, "trades")
report_path = os.path.join(base_path, "reports")
super_ai_path = os.path.join(base_path, "super_ai")

# 🌐 Streamlit App Setup
st.set_page_config(page_title="CryptoSuperAI Dashboard", layout="wide")
st.title("🚀 CryptoSuperAI - Zentrale KI-Trading WebApp")

# 📌 Tab-Navigation
TABS = ["📊 Dashboard", "📈 Trading", "🧠 Modelltraining", "📄 Reports"]
selected_tab = st.sidebar.radio("Navigation", TABS)

# =============== 📊 Dashboard ===============
if selected_tab == "📊 Dashboard":
    st.subheader("📥 Trade Log")
    trade_log = os.path.join(log_path, "trade_log.csv")
    if os.path.exists(trade_log):
        df_log = pd.read_csv(trade_log)
        st.dataframe(df_log.tail(20))
        st.metric("Anzahl Trades", len(df_log))
        if 'Gewinn' in df_log.columns:
            st.metric("Durchschnittlicher Gewinn", round(df_log['Gewinn'].mean(), 2))
    else:
        st.warning("Keine trade_log.csv gefunden.")

# =============== 📈 Trading ===============
elif selected_tab == "📈 Trading":
    st.subheader("⚙️ Strategien & Super-KI steuern")

    col1, col2 = st.columns(2)

    if col1.button("▶️ Super-KI starten"):
        with st.spinner("Super-KI läuft..."):
            subprocess.Popen(["python3", os.path.join(super_ai_path, "decision_engine.py")])
        st.success("Super-KI gestartet!")

    if col2.button("⏹️ Super-KI stoppen"):
        subprocess.run(["pkill", "-f", "decision_engine.py"])
        st.info("Super-KI gestoppt")

# =============== 🧠 Modelltraining ===============
elif selected_tab == "🧠 Modelltraining":
    st.subheader("📦 Trainiere ein Modell")

    model_options = [f for f in os.listdir(super_ai_path) if f.startswith("train_") and f.endswith(".ipynb")]
    model_file = st.selectbox("Wähle ein Trainings-Notebook:", model_options)

    if st.button("🚀 Training starten"):
        st.info(f"Starte Training: {model_file}")
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", os.path.join(super_ai_path, model_file)])
        st.success("Training abgeschlossen")

# =============== 📄 Reports ===============
elif selected_tab == "📄 Reports":
    st.subheader("📑 Reports anzeigen")

    html_reports = [f for f in os.listdir(report_path) if f.endswith(".html")]
    selected_report = st.selectbox("Wähle einen HTML-Report:", html_reports)

    if selected_report:
        with open(os.path.join(report_path, selected_report), "r", encoding="utf-8") as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=800, scrolling=True)

