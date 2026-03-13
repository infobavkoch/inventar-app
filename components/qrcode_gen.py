import qrcode
import streamlit as st

def create_qr(text):

    qr = qrcode.make(text)

    st.image(qr)
