import qrcode
import streamlit as st

def qr_code(text):

    img = qrcode.make(text)

    st.image(img, width=200)

