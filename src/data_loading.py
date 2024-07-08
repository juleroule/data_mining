import pandas as pd
import streamlit as st

def load_data():
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    if uploaded_file is not None:
        header = st.checkbox("Le fichier contient-il une en-tête ?", value=True)
        separator = st.selectbox("Sélectionnez le type de séparation", [",", ";", "\t", "|"], index=0)
        try:
            if header:
                data = pd.read_csv(uploaded_file, sep=separator)
            else:
                data = pd.read_csv(uploaded_file, sep=separator, header=None)
            st.success("Données chargées avec succès !")
            return data
        except Exception as e:
            st.error(f"Erreur lors du chargement des données : {e}")
    return None

def display_data_preview(data):
    st.header("Aperçu des données")
    st.subheader("Premières lignes")
    st.dataframe(data.head())
    st.subheader("Dernières lignes")
    st.dataframe(data.tail())

def display_data_summary(data):
    st.header("Résumé statistique")
    st.write("Nombre de lignes et de colonnes : ", data.shape)
    st.write("Noms des colonnes : ", data.columns.tolist())
    st.write("Nombre de valeurs manquantes par colonne :")
    st.write(data.isnull().sum())
    st.subheader("Résumé statistique des données")
    st.write(data.describe())
