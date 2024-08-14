import streamlit as st
from PIL import Image

# Funkce pro kontrolu kvality fotografie (např. kontrola rozlišení)
def check_image_quality(image):
    width, height = image.size
    if width < 800 or height < 600:
        return False
    return True

st.title("Kontrola kvality fotografií")

# Formulář pro nahrání fotografií
with st.form("upload_form"):
    uploaded_files = st.file_uploader("Nahrajte fotografie", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    submit_button = st.form_submit_button("Zkontrolovat kvalitu")

# Po kliknutí na tlačítko "Zkontrolovat kvalitu"
if submit_button:
    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Nahraná fotografie: {uploaded_file.name}", use_column_width=True)
            
            # Kontrola kvality fotografie
            if check_image_quality(image):
                st.success(f"Fotografie {uploaded_file.name} splňuje požadavky na kvalitu.")
            else:
                st.error(f"Fotografie {uploaded_file.name} má nedostatečné rozlišení.")
    else:
        st.warning("Nebyla nahrána žádná fotografie.")
