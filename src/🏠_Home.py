import streamlit as st
from data_loading import load_data, display_data_preview, display_data_summary
import os

def local_css(file_name):
    current_dir = os.path.dirname(__file__)
    css_path = os.path.join(current_dir, file_name)
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"Le fichier {file_name} est introuvable.")

def main():
    # Chargement du CSS local
    local_css("styles.css")

    # Ajout du logo dans la barre latérale
    current_dir = os.path.dirname(__file__)
    logo_path = os.path.join(current_dir, "image.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_column_width=True)
    else:
        st.sidebar.error("Logo non trouvé.")

    st.header("Projet Data Mining")
    if 'data' not in st.session_state:
        st.session_state.data = None
    
    data = load_data()
    if data is not None:
        st.session_state.data = data
        display_data_preview(data)
        display_data_summary(data)
    elif st.session_state.data is not None:
        display_data_preview(st.session_state.data)
        display_data_summary(st.session_state.data)

if __name__ == "__main__":
    main()
