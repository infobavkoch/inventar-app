import streamlit as st

st.set_page_config(page_title="Inventarverwaltung",layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Inventar & Prüfungsverwaltung")

st.markdown("### Dashboard")

col1,col2,col3 = st.columns(3)

with col1:
    if st.button("🚑 Fahrzeuge"):
        st.switch_page("pages/fahrzeuge.py")

with col2:
    if st.button("🏠 Ortsverein"):
        st.switch_page("pages/ortsverein.py")

with col3:
    if st.button("🏢 Lerchenstraße"):
        st.switch_page("pages/lerchenstrasse.py")
