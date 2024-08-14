import streamlit as st
from PIL import Image

# Funkce pro kontrolu kvality fotografie (např. kontrola rozlišení)
def check_image_quality(image):
    width, height = image.size
    if width < 800 or height < 600:  # Příklad požadavku na minimální rozlišení
        return False
    return True

# Funkce pro zobrazení formuláře s kontrolou kvality
def photo_upload_form():
    st.title("Nahrávání referenčních fotek")
    uploaded_files = st.file_uploader("Nahrajte fotografie", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        st.write("Kontrola kvality fotografií:")
        images_to_replace = []

        for i, uploaded_file in enumerate(uploaded_files):
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Fotografie {i+1}: {uploaded_file.name}", use_column_width=True)

            if not check_image_quality(image):
                st.error(f"Fotografie {i+1} ({uploaded_file.name}) nesplňuje požadavky na kvalitu.")
                images_to_replace.append((i, uploaded_file))

        if images_to_replace:
            st.write("Některé fotografie nesplňují požadavky. Můžete je nahradit novými nebo je smazat.")

            for i, (index, uploaded_file) in enumerate(images_to_replace):
                replacement_file = st.file_uploader(f"Nahrajte novou verzi pro fotografii {index+1} ({uploaded_file.name})", type=["jpg", "jpeg", "png"], key=f"replace_{index}")
                if replacement_file:
                    uploaded_files[index] = replacement_file
                remove_photo = st.checkbox(f"Smazat fotografii {index+1} ({uploaded_file.name})", key=f"remove_{index}")
                if remove_photo:
                    uploaded_files[index] = None

            # Filtruje nahrané soubory, aby se odstranily smazané fotografie
            uploaded_files = [file for file in uploaded_files if file is not None]

        if st.button("Odeslat fotografie"):
            if uploaded_files:
                st.success("Fotografie byly úspěšně nahrány.")
                # Zde bys mohl přidat kód pro uložení fotografií nebo jejich další zpracování
            else:
                st.warning("Nebyla nahrána žádná fotografie.")

# Zobrazení formuláře
photo_upload_form()
