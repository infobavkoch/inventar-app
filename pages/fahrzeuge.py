import streamlit as st
from database import conn,cursor

st.title("Fahrzeugverwaltung")

suche = st.text_input("Fahrzeug suchen")

tab1,tab2 = st.tabs(["Neues Fahrzeug","Fahrzeugliste"])

with tab1:

    name = st.text_input("Bezeichnung")
    kenn = st.text_input("Kennzeichen")
    funk = st.text_input("Funkrufname")
    tuev = st.date_input("Nächster TÜV")

    if st.button("Speichern"):

        cursor.execute(
        "INSERT INTO fahrzeuge (bezeichnung,kennzeichen,funkrufname,tuev) VALUES (?,?,?,?)",
        (name,kenn,funk,tuev)
        )

        conn.commit()

        st.success("Fahrzeug gespeichert")

with tab2:

    cursor.execute("SELECT * FROM fahrzeuge")

    daten = cursor.fetchall()

    for f in daten:

        if suche.lower() in f[1].lower():

            st.subheader(f[1])

            st.write("Kennzeichen:",f[2])
            st.write("Funkrufname:",f[3])
            st.write("TÜV:",f[4])

            if st.button("Details",key=f[0]):

                st.session_state["fahrzeug"]=f[0]

                st.switch_page("pages/fahrzeug_details.py")

            st.divider()
