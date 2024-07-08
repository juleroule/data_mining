import streamlit as st
from data_loading import load_data, display_data_preview, display_data_summary
from data_cleaning import handle_missing_values, normalize_data
from data_visualization import plot_histogram, plot_boxplot
from clustering import perform_clustering
from prediction import perform_prediction

def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choisissez une section", ["Chargement des données", "Pré-traitement", "Visualisation", "Analyse", "Évaluation"])
    
    data = None
    
    if options == "Chargement des données":
        st.header("Chargement des données")
        data = load_data()
        if data is not None:
            display_data_preview(data)
            display_data_summary(data)
    
    if options == "Pré-traitement" and data is not None:
        st.header("Pré-traitement et nettoyage des données")
        data = handle_missing_values(data)
        data = normalize_data(data)
    
    if options == "Visualisation" and data is not None:
        st.header("Visualisation des données nettoyées")
        plot_histogram(data)
        plot_boxplot(data)
    
    if options == "Analyse" and data is not None:
        st.header("Clustering ou Prédiction")
        analysis_type = st.selectbox("Choisissez le type d'analyse", ["Clustering", "Prédiction"])
        if analysis_type == "Clustering":
            perform_clustering(data)
        elif analysis_type == "Prédiction":
            perform_prediction(data)
    
    if options == "Évaluation" and data is not None:
        st.header("Évaluation des Modèles")
        # Include specific evaluation functionalities if necessary

if __name__ == "__main__":
    main()
