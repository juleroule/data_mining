import streamlit as st
from clustering import perform_clustering
from prediction import perform_prediction
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

    st.header("Clustering ou Prédiction")
    if 'data' not in st.session_state:
        st.session_state.data = None

    if st.session_state.data is not None:
        analysis_type = st.selectbox("Choisissez le type d'analyse", ["Clustering", "Prédiction"])
        if analysis_type == "Clustering":
            perform_clustering(st.session_state.data)
        elif analysis_type == "Prédiction":
            perform_prediction(st.session_state.data)
    else:
        st.warning("Veuillez d'abord charger les données.")

if __name__ == "__main__":
    main()
