import streamlit as st

def scanner():

    st.header("QR Scanner")

    code = st.text_input("QR Code scannen")

    if code:

        st.success(f"Gescannter Code: {code}")
