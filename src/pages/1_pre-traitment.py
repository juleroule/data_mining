import streamlit as st
from data_cleaning import handle_missing_values, normalize_data, encode_categorical_columns
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

    st.header("Pré-traitement et nettoyage des données")
    if 'data' not in st.session_state:
        st.session_state.data = None

    if st.session_state.data is not None:
        st.subheader("Gestion des valeurs manquantes")
        missing_methods = st.multiselect(
            "Sélectionnez les méthodes de gestion des valeurs manquantes",
            ["Supprimer les lignes", "Supprimer les colonnes", "Remplacer par la moyenne", "Remplacer par la médiane", "Remplacer par le mode", "Imputation KNN", "Remplacer par NaN"]
        )
        
        st.subheader("Normalisation des données")
        normalization_method = st.selectbox(
            "Sélectionnez la méthode de normalisation",
            ["Aucune", "Min-Max", "Z-score"]
        )
        
        st.subheader("Encodage des colonnes catégorielles")
        encode_categorical = st.checkbox("Encoder les colonnes catégorielles")

        if st.button("Appliquer le pré-traitement"):
            data = st.session_state.data
            if missing_methods:
                data = handle_missing_values(data, missing_methods)
            if normalization_method != "Aucune":
                data = normalize_data(data, normalization_method)
            if encode_categorical:
                data = encode_categorical_columns(data)
            
            if data is not None:
                st.session_state.data = data
                st.write("Données après pré-traitement :")
                st.dataframe(data.head())
            else:
                st.warning("Le pré-traitement des données a échoué. Veuillez vérifier votre dataset et réessayer.")
    else:
        st.warning("Veuillez d'abord charger les données.")

if __name__ == "__main__":
    main()
