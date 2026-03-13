import streamlit as st

def titel(text):

    st.markdown(f"""
    <h1 style='color:#1b4b72'>
    {text}
    </h1>
    """, unsafe_allow_html=True)
