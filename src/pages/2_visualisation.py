import streamlit as st
from data_visualization import plot_histogram, plot_histogrammes_double_x, plot_histogram_for_strings, plot_boxplot, plot_bar_chart, plot_scatterplot, plot_correlation_matrix, plot_heatmap, plot_map, plot_filtered_map
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

    st.header("Visualisation des données nettoyées")
    if 'data' not in st.session_state:
        st.session_state.data = None

    if st.session_state.data is not None:
        vis_type = st.selectbox("Choisissez un type de visualisation", ["Histogramme","Histogramme Double x", "Box Plot","Histogram for strings", "Diagramme en barres", "Nuage de points", "Matrice de corrélation", "Heatmap", "Map", "Map Filtrée"])
        if vis_type == "Histogramme":
            plot_histogram(st.session_state.data)
        elif vis_type == "Histogram for strings":
            plot_histogram_for_strings(st.session_state.data)
        elif vis_type == "Box Plot":
            plot_boxplot(st.session_state.data)
        elif vis_type == "Diagramme en barres":
            plot_bar_chart(st.session_state.data)
        elif vis_type == "Nuage de points":
            plot_scatterplot(st.session_state.data)
        elif vis_type == "Matrice de corrélation":
            plot_correlation_matrix(st.session_state.data)
        elif vis_type == "Heatmap":
            plot_heatmap(st.session_state.data)
        elif vis_type == "Map":
            plot_map(st.session_state.data)       
        elif vis_type == "Map Filtrée":
            plot_filtered_map(st.session_state.data)   
        elif vis_type == "Histogramme Double x":
            plot_histogrammes_double_x(st.session_state.data)       
    else:
        st.warning("Veuillez d'abord charger les données.")

if __name__ == "__main__":
    main()
