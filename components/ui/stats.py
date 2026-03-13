import plotly.express as px
import streamlit as st
from database import cursor
import pandas as pd

def statistik():

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    df = pd.DataFrame(daten, columns=["Fahrzeug","TÜV"])

    if len(df)==0:
        return

    chart = px.histogram(df, x="TÜV")

    st.plotly_chart(chart)
