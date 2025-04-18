
# 🚀 Streamlit WebApp für CryptoTradingAI
import streamlit as st
import pandas as pd
import os

# Basisverzeichnisse
data_path = "./data"
log_path = "./trades"
model_path = "./models"

# Titel
st.set_page_config(page_title="CryptoSuperAI Dashboard", layout="wide")
st.title("🚀 CryptoSuperAI Trading Dashboard")

# 📥 Trade Log laden
log_file = os.path.join(log_path, "trade_log.csv")
if os.path.exists(log_file):
    df_log = pd.read_csv(log_file)
    st.subheader("📈 Letzte Trades")
    st.dataframe(df_log.tail(20))
else:
    st.warning("Keine trade_log.csv gefunden.")

# 📊 KPI-Übersicht
if 'df_log' in locals():
    col1, col2, col3 = st.columns(3)
    col1.metric("Anzahl Trades", len(df_log))
    if 'Gewinn' in df_log.columns:
        col2.metric("Durchschn. Gewinn", f"{df_log['Gewinn'].mean():.2f}")
    if 'Rendite %' in df_log.columns:
        col3.metric("Rendite %", f"{df_log['Rendite %'].sum():.2f}%")

# 📦 Modelle anzeigen
if os.path.exists(model_path):
    model_files = os.listdir(model_path)
    st.subheader("🧠 Verfügbare Modelle")
    st.write(model_files)
else:
    st.warning("Kein Modelle-Ordner gefunden.")

# 📁 Daten durchsuchen
if os.path.exists(data_path):
    st.subheader("📂 Daten")
    files = os.listdir(data_path)
    selected_file = st.selectbox("Wähle eine CSV-Datei:", [f for f in files if f.endswith('.csv')])
    if selected_file:
        df = pd.read_csv(os.path.join(data_path, selected_file))
        st.write(df.head())
else:
    st.warning("Datenordner nicht gefunden.")
