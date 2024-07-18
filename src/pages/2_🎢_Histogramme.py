import streamlit as st
from data_visualization import plot_histogram, plot_histogram_for_strings, plot_histogrammes_double_x, plot_histogram_string
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
    local_css("../styles.css")

    # Ajout du logo dans la barre latérale
    current_dir = os.path.dirname(__file__)
    logo_path = os.path.join(current_dir, "../image.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_column_width=True)
    else:
        st.sidebar.error("Logo non trouvé.")

    st.header("Visualisation des histogrammes")
    if 'data' not in st.session_state:
        st.session_state.data = None

    if st.session_state.data is not None:
        histogram_type = st.selectbox("Choisissez le type d'histogramme à afficher", 
                                      ["Histogramme Simple", "Histogramme de valeurs numériques", "Histogramme pour les chaînes de caractères", "Histogramme Double X"])
        
        if histogram_type == "Histogramme Simple":
            plot_histogram(st.session_state.data)
        elif histogram_type == "Histogramme de valeurs numériques":
            plot_histogram_string(st.session_state.data)
        elif histogram_type == "Histogramme pour les chaînes de caractères":
            plot_histogram_for_strings(st.session_state.data)
        elif histogram_type == "Histogramme Double X":
            plot_histogrammes_double_x(st.session_state.data)
    else:
        st.warning("Veuillez d'abord charger les données.")

if __name__ == "__main__":
    main()
