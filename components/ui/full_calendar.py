import streamlit as st
from database import cursor
import pandas as pd

def kalender():

    st.subheader("Prüfkalender")

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    df = pd.DataFrame(daten, columns=["Fahrzeug","TÜV"])

    if len(df)==0:
        st.info("Keine Termine vorhanden")
        return

    st.dataframe(df)
