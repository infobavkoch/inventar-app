import streamlit as st
from database import cursor
from datetime import datetime, date
from components.utils import pruef_status


def dashboard():

    st.header("Dashboard")

    cursor.execute("SELECT bezeichnung, tuev FROM fahrzeuge")
    daten = cursor.fetchall()

    if len(daten) == 0:
        st.info("Noch keine Fahrzeuge angelegt.")
        return

    for fahrzeug in daten:

        name = fahrzeug[0]
        tuev = fahrzeug[1]

        if tuev:

            try:
                datum = datetime.fromisoformat(tuev).date()
            except:
                continue

            status = pruef_status(datum)

            st.write(f"🚑 **{name}**")
            st.write(f"TÜV: {datum}  {status}")
            st.divider()
