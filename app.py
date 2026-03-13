import streamlit as st
from database import init_db, get_connection
from auth import login
from datetime import datetime

init_db()

if "user" not in st.session_state:
    login()
    st.stop()

conn = get_connection()
c = conn.cursor()

st.sidebar.title("Inventar System")

menu = st.sidebar.selectbox(
"Navigation",
[
"Dashboard",
"Fahrzeuge"
]
)

if st.sidebar.button("Logout"):
    del st.session_state["user"]
    st.rerun()

# ------------------
# Dashboard
# ------------------

if menu == "Dashboard":

    st.title("Dashboard")

    col1,col2 = st.columns(2)

    c.execute("SELECT COUNT(*) FROM fahrzeuge")
    col1.metric("Fahrzeuge", c.fetchone()[0])

    c.execute("SELECT COUNT(*) FROM tuev")
    col2.metric("TÜV Einträge", c.fetchone()[0])

# ------------------
# Fahrzeuge
# ------------------

if menu == "Fahrzeuge":

    tab1,tab2 = st.tabs(["Fahrzeug anlegen","Fahrzeugliste"])

    with tab1:

        name = st.text_input("Bezeichnung")
        kenn = st.text_input("Kennzeichen")
        funk = st.text_input("Funkrufname")

        if st.button("Speichern"):

            c.execute(
            "INSERT INTO fahrzeuge (bezeichnung,kennzeichen,funkrufname) VALUES (?,?,?)",
            (name,kenn,funk)
            )

            conn.commit()

            st.success("Fahrzeug gespeichert")

    with tab2:

        c.execute("SELECT id,bezeichnung FROM fahrzeuge")
        fahrzeuge = c.fetchall()

        if fahrzeuge:

            fahrzeug_dict = {f[1]:f[0] for f in fahrzeuge}

            selected = st.selectbox(
            "Fahrzeug auswählen",
            fahrzeug_dict.keys()
            )

            fahrzeug_id = fahrzeug_dict[selected]

            termin = st.date_input("Nächster TÜV")

            if st.button("TÜV speichern"):

                c.execute(
                "INSERT INTO tuev (fahrzeug_id,termin) VALUES (?,?)",
                (fahrzeug_id,str(termin))
                )

                conn.commit()

            c.execute(
            "SELECT termin FROM tuev WHERE fahrzeug_id=?",
            (fahrzeug_id,)
            )

            rows = c.fetchall()

            for r in rows:

                d = datetime.strptime(r[0], "%Y-%m-%d")
                diff = (d - datetime.today()).days

                if diff < 0:
                    status="🔴 abgelaufen"
                elif diff < 90:
                    status="🟡 bald"
                else:
                    status="🟢 ok"

                st.write(r[0], status)
