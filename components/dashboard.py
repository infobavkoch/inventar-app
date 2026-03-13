import streamlit as st
from database import cursor
from datetime import datetime
from components.utils import pruef_status

def dashboard():

    st.header("Dashboard")

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    for d in daten:

        if d[1]:

            datum = datetime.fromisoformat(d[1]).date()

            status = pruef_status(datum)

            st.write(f"🚑 {d[0]} — TÜV {datum} {status}")
