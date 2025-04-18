# 🚀 CryptoSuperAI - Vollständige Streamlit-WebApp
import streamlit as st 
import pandas as pd
import os

# 🔧 Ordnerpfade definieren
base_path = "./CryptoTradingAI"
data_path = os.path.join(base_path, "data")
model_path = os.path.join(base_path, "models")
log_path = os.path.join(base_path, "trades")
report_path = os.path.join(base_path, "reports")
super_ai_path = os.path.join(base_path, "super_ai")

# 📦 Entscheidungseinheit importieren (Super-KI)
try:
    import sys
    sys.path.append(super_ai_path)
    import decision_engine
except Exception as e:
    decision_engine = None

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
        if decision_engine is not None:
            decision_engine.run()
            st.success("Super-KI wurde intern gestartet!")
        else:
            st.error("Super-KI-Modul konnte nicht geladen werden.")

    if col2.button("⏹️ Super-KI stoppen"):
        st.info("Super-KI Stoppen muss manuell erfolgen (kein Subprozess möglich auf Streamlit.io)")

    st.markdown("---")
    st.subheader("📤 Manuelle Trade-Ausführung")

    trade_symbol = st.text_input("📈 Symbol (z. B. BTC/USDT)", "BTC/USDT")
    trade_action = st.selectbox("🛒 Aktion", ["BUY", "SELL"])
    trade_amount = st.number_input("💰 Menge", min_value=0.0, value=0.1, step=0.01)

    if st.button("💥 Trade ausführen"):
        if os.path.exists(log_path):
            import datetime
            import csv
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            trade_data = [timestamp, trade_symbol, trade_action, trade_amount]
            trade_log_file = os.path.join(log_path, "manual_trades.csv")
            with open(trade_log_file, "a", newline="") as f:
                writer = csv.writer(f)
                if os.stat(trade_log_file).st_size == 0:
                    writer.writerow(["Timestamp", "Symbol", "Aktion", "Menge"])
                writer.writerow(trade_data)
            st.success(f"✅ Trade ausgeführt: {trade_action} {trade_amount} {trade_symbol}")
        else:
            st.error("⚠️ Trade-Verzeichnis nicht gefunden.")

# =============== 🧠 Modelltraining ===============
elif selected_tab == "🧠 Modelltraining":
    st.subheader("📦 Trainiere ein Modell")

    if os.path.exists(super_ai_path):
        model_options = [f for f in os.listdir(super_ai_path) if f.startswith("train_") and f.endswith(".ipynb")]
        if model_options:
            selected_model = st.selectbox("Wähle ein Trainings-Notebook:", model_options)
            st.warning("⚠️ Training von Notebooks ist auf Streamlit.io nicht direkt möglich. Bitte lokal ausführen.")
        else:
            st.info("Keine Trainings-Notebooks gefunden.")
    else:
        st.warning("super_ai-Ordner nicht gefunden.")

# =============== 📄 Reports ===============
elif selected_tab == "📄 Reports":
    st.subheader("📑 Reports anzeigen")

    if os.path.exists(report_path):
        html_reports = [f for f in os.listdir(report_path) if f.endswith(".html")]
        if html_reports:
            selected_report = st.selectbox("Wähle einen HTML-Report:", html_reports)
            if selected_report:
                with open(os.path.join(report_path, selected_report), "r", encoding="utf-8") as f:
                    html_content = f.read()
                    st.components.v1.html(html_content, height=800, scrolling=True)
        else:
            st.info("Keine HTML-Reports gefunden.")
    else:
        st.warning("Reports-Ordner nicht gefunden.")
