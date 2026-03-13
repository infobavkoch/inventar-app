import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

def scanner():

    st.subheader("QR-Code Scanner")

    data = qrcode_scanner()

    if data:
        st.success("Code erkannt:")
        st.write(data)
