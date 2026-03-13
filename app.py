import streamlit as st
from components.dashboard import dashboard
from components.calendar_view import kalender

# optionales Login
try:
    from auth import login
except:
    def login():
        return True

st.set_page_config(
    page_title="Inventarverwaltung",
    layout="wide"
)

# CSS laden
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Login prüfen
if not login():
    st.stop()

st.sidebar.title("Inventar App")

seite = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Fahrzeuge",
        "Ortsverein",
        "Lerchenstraße",
        "Kalender"
    ]
)

if seite == "Dashboard":
    dashboard()

elif seite == "Fahrzeuge":
    st.switch_page("pages/fahrzeuge.py")

elif seite == "Ortsverein":
    st.switch_page("pages/ortsverein.py")

elif seite == "Lerchenstraße":
    st.switch_page("pages/lerchenstrasse.py")

elif seite == "Kalender":
    kalender()
