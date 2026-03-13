import streamlit as st
from components.qr.scanner import scanner

st.title("QR Scanner")

scanner()
