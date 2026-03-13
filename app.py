import database
import streamlit as st
from auth import login
from components.dashboard import dashboard

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Inventarverwaltung", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# LOGIN
if not login():
    st.stop()

# SIDEBAR
st.sidebar.title("Inventar App")

seite = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Fahrzeuge",
	"Material",
	"QR Scanner",
        "Ortsverein",
        "Lerchenstraße"
    ]
)

if seite == "Dashboard":
    dashboard()

if seite == "Fahrzeuge":
    st.switch_page("pages/fahrzeuge.py")

if seite == "Ortsverein":
    st.switch_page("pages/ortsverein.py")

if seite == "Lerchenstraße":
    st.switch_page("pages/lerchenstrasse.py")

if seite == "Material":
    st.switch_page("pages/material.py")

if seite == "QR Scanner":
    st.switch_page("pages/scanner.py")
