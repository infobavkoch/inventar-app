image = st.file_uploader("Bild hochladen")

if image:
    with open(f"uploads/{image.name}", "wb") as f:
        f.write(image.getbuffer())
