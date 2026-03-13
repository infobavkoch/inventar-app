import streamlit as st
from database import conn,cursor

st.title("Materialverwaltung")

fahrzeug = st.number_input("Fahrzeug ID")

name = st.text_input("Material")
nummer = st.text_input("Materialnummer")
pruefung = st.date_input("Prüftermin")

if st.button("Material speichern"):

    cursor.execute(
        "INSERT INTO meetb (fahrzeug_id,name,nummer,pruefung) VALUES (?,?,?,?)",
        (fahrzeug,name,nummer,pruefung)
    )

    conn.commit()

    st.success("Material gespeichert")
