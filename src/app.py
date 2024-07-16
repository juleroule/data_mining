import streamlit as st
from data_loading import load_data, display_data_preview, display_data_summary
from data_cleaning import handle_missing_values, normalize_data, encode_categorical_columns
from data_visualization import plot_histogram, plot_boxplot, plot_bar_chart, plot_scatterplot, plot_correlation_matrix, plot_heatmap
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
    # Chargement du CSS local
    local_css("styles.css")

    # Ajout du logo dans la barre latérale
    current_dir = os.path.dirname(__file__)
    logo_path = os.path.join(current_dir, "image.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_column_width=True)
    else:
        st.sidebar.error("Logo non trouvé.")

    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choisissez une section", ["Chargement des données", "Pré-traitement", "Visualisation", "Analyse"])

    if 'data' not in st.session_state:
        st.session_state.data = None

    if options == "Chargement des données":
        st.header("Chargement des données")
        data = load_data()
        if data is not None:
            st.session_state.data = data
            display_data_preview(data)
            display_data_summary(data)
        elif st.session_state.data is not None:
            display_data_preview(st.session_state.data)
            display_data_summary(st.session_state.data)

    if options == "Pré-traitement":
        st.header("Pré-traitement et nettoyage des données")
        if st.session_state.data is not None:
            data = handle_missing_values(st.session_state.data)
            if data is not None:
                data = encode_categorical_columns(data)
            if data is not None:
                data = normalize_data(data)
            if data is not None:
                st.session_state.data = data
            else:
                st.warning("Le pré-traitement des données a échoué. Veuillez vérifier votre dataset et réessayer.")
        else:
            st.warning("Veuillez d'abord charger les données.")

    if options == "Visualisation":
        st.header("Visualisation des données nettoyées")
        if st.session_state.data is not None:
            vis_type = st.selectbox("Choisissez un type de visualisation", ["Histogramme", "Box Plot", "Diagramme en barres", "Nuage de points", "Matrice de corrélation", "Heatmap"])
            if vis_type == "Histogramme":
                plot_histogram(st.session_state.data)
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
        else:
            st.warning("Veuillez d'abord charger les données.")

    if options == "Analyse":
        st.header("Clustering ou Prédiction")
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
