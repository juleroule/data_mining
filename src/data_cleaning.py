import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import streamlit as st

def handle_missing_values(data):
    st.subheader("Gestion des valeurs manquantes")
    
    # Sélection de la méthode de gestion des valeurs manquantes
    methods = st.multiselect(
        "Sélectionnez les méthodes de gestion des valeurs manquantes",
        ["Supprimer les lignes", "Supprimer les colonnes", "Remplacer par la moyenne", "Remplacer par la médiane", "Remplacer par le mode", "Imputation KNN", "Remplacer par NaN"]
    )

    original_shape = data.shape

    for method in methods:
        if method == "Supprimer les lignes":
            data = data.dropna()
        elif method == "Supprimer les colonnes":
            data = data.dropna(axis=1)
        elif method in ["Remplacer par la moyenne", "Remplacer par la médiane", "Remplacer par le mode"]:
            strategy = "mean" if method == "Remplacer par la moyenne" else "median" if method == "Remplacer par la médiane" else "most_frequent"
            imputer = SimpleImputer(strategy=strategy)
            data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
        elif method == "Imputation KNN":
            imputer = KNNImputer()
            data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
        elif method == "Remplacer par NaN":
            data = data.apply(lambda x: x.where(pd.notnull(x), None))

    # Supprimer les colonnes avec plus de 90% de valeurs manquantes
    threshold = 0.9
    missing_ratio = data.isnull().mean()
    columns_to_drop = missing_ratio[missing_ratio > threshold].index
    if len(columns_to_drop) > 0:
        data = data.drop(columns=columns_to_drop)
        st.write(f"Colonnes supprimées avec plus de {threshold*100}% de valeurs manquantes : {', '.join(columns_to_drop)}")

    if data.shape[0] == 0 or data.shape[1] == 0:
        st.error("Toutes les lignes ou colonnes ont été supprimées. Veuillez sélectionner une autre méthode de gestion des valeurs manquantes.")
        return None

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
    
    if data.empty:
        st.error("Les données sont vides après normalisation. Veuillez vérifier votre dataset et réessayer.")
        return None

    st.write("Données après normalisation :")
    st.dataframe(data.head())
    return data

def encode_categorical_columns(data):
    st.subheader("Encodage des colonnes catégorielles")
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    
    if data.empty:
        st.error("Toutes les colonnes catégorielles ont été supprimées. Veuillez vérifier votre dataset et réessayer.")
        return None

    st.write("Données après encodage :")
    st.dataframe(data.head())
    return data
