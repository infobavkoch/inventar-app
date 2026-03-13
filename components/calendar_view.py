import streamlit as st
from database import cursor

def kalender():

    st.header("Prüftermine")

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    for d in daten:

        if d[1]:

            st.write("🚑", d[0], "TÜV:", d[1])
