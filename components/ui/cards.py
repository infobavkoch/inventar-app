import streamlit as st

def warnkarte(titel, wert, farbe):

    farben = {
        "rot": "#d9534f",
        "gelb": "#f0ad4e",
        "gruen": "#5cb85c"
    }

    st.markdown(f"""
    <div style="
        background-color:{farben[farbe]};
        padding:20px;
        border-radius:10px;
        margin:10px;
        color:white;
        font-size:20px;">
        <b>{titel}</b><br>
        {wert}
    </div>
    """, unsafe_allow_html=True)
