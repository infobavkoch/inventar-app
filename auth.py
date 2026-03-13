import streamlit_authenticator as stauth

names = ["Admin"]
usernames = ["admin"]

passwords = ["admin123"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
names,
usernames,
hashed_passwords,
"inventar_app",
"abcdef",
cookie_expiry_days=1
)

def login():

    name, authentication_status, username = authenticator.login("Login","main")

    if authentication_status:
        return True

    elif authentication_status == False:
        import streamlit as st
        st.error("Login falsch")

    elif authentication_status == None:
        import streamlit as st
        st.warning("Bitte einloggen")

    return False
