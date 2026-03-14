import streamlit as st
from database import get_connection

st.title("Inventar")

name = st.text_input("Name")
kategorie = st.text_input("Kategorie")
image = st.file_uploader("Bild hochladen", type=["png","jpg","jpeg"])

if image is not None:

    with open(f"uploads/{image.name}", "wb") as f:
        f.write(image.getbuffer())

    st.success("Bild gespeichert")
if st.button("Speichern"):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO inventar(name,kategorie) VALUES (?,?)",
        (name, kategorie)
    )

    conn.commit()
    conn.close()

    st.success("Gespeichert")
