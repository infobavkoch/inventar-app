import streamlit as st
from database import cursor

def pruefkalender():

    st.subheader("Prüftermine")

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    termine = []

    for f in daten:

        if f[1]:
            termine.append({
                "Fahrzeug":f[0],
                "TÜV":f[1]
            })

    if len(termine)==0:
        st.info("Keine Prüftermine vorhanden")
        return

    st.table(termine)
