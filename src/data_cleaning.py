import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import streamlit as st

def handle_missing_values(data):
    st.subheader("Gestion des valeurs manquantes")
    missing_value_method = st.selectbox(
        "Sélectionnez la méthode de gestion des valeurs manquantes",
        ["Supprimer les lignes", "Supprimer les colonnes", "Remplacer par la moyenne", "Remplacer par la médiane", "Remplacer par le mode", "Imputation KNN"]
    )
    if missing_value_method == "Supprimer les lignes":
        data = data.dropna()
    elif missing_value_method == "Supprimer les colonnes":
        data = data.dropna(axis=1)
    elif missing_value_method == "Remplacer par la moyenne":
        imputer = SimpleImputer(strategy="mean")
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    elif missing_value_method == "Remplacer par la médiane":
        imputer = SimpleImputer(strategy="median")
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    elif missing_value_method == "Remplacer par le mode":
        imputer = SimpleImputer(strategy="most_frequent")
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    elif missing_value_method == "Imputation KNN":
        imputer = KNNImputer()
        data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    st.write("Données après traitement des valeurs manquantes :")
    st.dataframe(data.head())
    return data

def normalize_data(data):
    st.subheader("Normalisation des données")
    normalization_method = st.selectbox(
        "Sélectionnez la méthode de normalisation",
        ["Aucune", "Min-Max", "Z-score"]
    )
    if normalization_method == "Min-Max":
        scaler = MinMaxScaler()
        data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    elif normalization_method == "Z-score":
        scaler = StandardScaler()
        data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    st.write("Données après normalisation :")
    st.dataframe(data.head())
    return data
