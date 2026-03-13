import streamlit as st
import hashlib
from database import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():

    conn = get_connection()
    c = conn.cursor()

    st.title("🔐 Inventar Login")

    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")

    if st.button("Login"):

        hashed = hash_password(password)

        c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
        )

        user = c.fetchone()

        if user:
            st.session_state["user"] = username
            st.session_state["role"] = user[3]
            st.rerun()
        else:
            st.error("Login fehlgeschlagen")
