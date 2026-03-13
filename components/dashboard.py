from components.ui.full_calendar import kalender
import streamlit as st
from database import cursor
from datetime import datetime
from components.utils import pruef_status
from components.ui.cards import warnkarte
from components.ui.calendar import pruefkalender


def dashboard():

    st.title("Dashboard")

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    rot=0
    gelb=0
    gruen=0

    for d in daten:

        if d[1]:

            datum = datetime.fromisoformat(d[1]).date()

            status = pruef_status(datum)

            if "🔴" in status:
                rot+=1

            elif "🟡" in status:
                gelb+=1

            else:
                gruen+=1

    col1,col2,col3 = st.columns(3)

    with col1:
        warnkarte("Überfällige Prüfungen",rot,"rot")

    with col2:
        warnkarte("Bald fällig",gelb,"gelb")

    with col3:
        warnkarte("Alles OK",gruen,"gruen")

    st.divider()

    pruefkalender()
st.divider()
kalender()
