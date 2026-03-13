import streamlit as st
from database import cursor
from datetime import datetime
from components.utils import pruef_status


def dashboard():

    st.header("Dashboard")

    cursor.execute("SELECT bezeichnung, tuev FROM fahrzeuge")
    daten = cursor.fetchall()

    warnungen = []

    for d in daten:

        if d[1]:

            datum = datetime.fromisoformat(str(d[1])).date()
            status = pruef_status(datum)

            if "🔴" in status or "🟡" in status:
                warnungen.append((d[0], datum, status))

    if warnungen:

        st.subheader("⚠ Prüfungen bald fällig")

        for w in warnungen:
            st.write(f"🚑 {w[0]} — TÜV {w[1]} {w[2]}")

    else:

        st.success("Alle Prüfungen aktuell")
