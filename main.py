import streamlit as st
import os
import sys

# 📌 Füge alle wichtigen Pfade manuell hinzu
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
sys.path.append(os.path.join(base_dir, "super_ai"))
sys.path.append(os.path.join(base_dir, "utils"))

# ✅ Debug-Ausgabe (zur Laufzeit sehen)
st.text("📁 Basisverzeichnis: " + base_dir)
st.text("📁 Inhalte im Projektverzeichnis:")
st.text(str(os.listdir(base_dir)))
st.text("📁 Inhalte im super_ai/:")
try:
    st.text(str(os.listdir(os.path.join(base_dir, "super_ai"))))
except Exception as e:
    st.error(f"❌ Fehler beim Zugriff auf super_ai/: {e}")

# ✅ Jetzt sollte dieser Import funktionieren
try:
    from super_ai.ensemble_model import load_ensemble_model
    st.success("✅ Import erfolgreich!")
except ModuleNotFoundError as e:
    st.error(f"❌ Importfehler: {e}")
    st.stop()

# Beispiel-App-Inhalt
st.title("CryptoSuperAI")
st.write("Hier kommt dein Hauptinhalt hin...")
