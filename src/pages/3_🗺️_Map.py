import streamlit as st
import pandas as pd
from data_visualization import plot_filtered_map, plot_map
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

    st.title("Visualisation des données géographiques")

    if 'data' in st.session_state and st.session_state.data is not None:
        data = st.session_state.data

        plot_map(data)
        plot_filtered_map(data)

    else:
        st.warning("Veuillez charger les données avant de visualiser la carte.")

if __name__ == "__main__":
    main()


