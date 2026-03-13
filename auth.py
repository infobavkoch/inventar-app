import streamlit as st

def login():

    if "login" not in st.session_state:
        st.session_state.login = False

    if st.session_state.login:
        return True

    st.title("Login")

    user = st.text_input("Benutzer")
    pw = st.text_input("Passwort", type="password")

    if st.button("Login"):

        if user == "admin" and pw == "1234":
            st.session_state.login = True
            st.rerun()

        else:
            st.error("Login falsch")

    return False
