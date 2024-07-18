import streamlit as st
from data_cleaning import handle_missing_values, normalize_data
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
    local_css("../styles.css")

    current_dir = os.path.dirname(__file__)
    logo_path = os.path.join(current_dir, "../image.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_column_width=True)
    else:
        st.sidebar.error("Logo non trouvé.")

    st.header("Pré-traitement et nettoyage des données")
    if 'data' not in st.session_state:
        st.session_state.data = None

    if st.session_state.data is not None:
        st.write("Données originales :")
        st.dataframe(st.session_state.data.head())

        data = handle_missing_values(st.session_state.data)
        if data is not None:
            data = normalize_data(data)
        if data is not None:
            st.session_state.data = data
            st.write("Données après pré-traitement :")
            st.dataframe(st.session_state.data.head())
        else:
            st.warning("Le pré-traitement des données a échoué. Veuillez vérifier votre dataset et réessayer.")
    else:
        st.warning("Veuillez d'abord charger les données.")

if __name__ == "__main__":
    main()