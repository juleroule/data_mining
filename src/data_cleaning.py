import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import streamlit as st

def handle_missing_values(data):
    st.subheader("Gestion des valeurs manquantes")

    # Remplacer les chaînes vides par NaN
    data = data.replace("", pd.NA)

    # Formulaire pour suppression de lignes et colonnes
    st.markdown("### Suppression de lignes et colonnes")
    drop_rows = st.checkbox("Supprimer les lignes entièrement vides")
    drop_columns = st.checkbox("Supprimer les colonnes avec plus de 90% de valeurs manquantes")
    encode_categoricals = st.checkbox("Transformer les colonnes catégorielles en valeurs chiffrées")

    if st.button("Appliquer suppression de lignes et colonnes"):
        original_data = data.copy()
        initial_rows = data.index
        initial_columns = data.columns

        if drop_rows:
            data = data.dropna(how='all')
            removed_rows = set(initial_rows) - set(data.index)
            if removed_rows:
                st.write(f"Lignes supprimées (entièrement vides) : {', '.join(map(str, removed_rows))}")

        if drop_columns:
            threshold = 0.1 * data.shape[0]
            data = data.dropna(axis=1, thresh=threshold)
            removed_columns = set(initial_columns) - set(data.columns)
            if removed_columns:
                st.write(f"Colonnes supprimées avec plus de 90% de valeurs manquantes : {', '.join(removed_columns)}")

        if encode_categoricals:
            data = encode_categorical_columns(data)
            if data is None:
                st.error("Erreur lors de l'encodage des colonnes catégorielles.")
                return None

        if not drop_rows and not drop_columns and not encode_categoricals:
            st.write("Aucune suppression de lignes ou colonnes ni transformation des colonnes n'a été sélectionnée.")

        if data.shape[0] == 0 or data.shape[1] == 0:
            st.error("Toutes les lignes ou colonnes ont été supprimées. Veuillez sélectionner une autre méthode de gestion des valeurs manquantes.")
            return None

        st.write("Données après suppression de lignes et colonnes :")
        st.dataframe(data.head())

    # Formulaire pour remplacement des valeurs manquantes
    st.markdown("### Remplacement des valeurs manquantes")
    method = st.radio(
        "Sélectionnez une méthode de remplacement des valeurs manquantes",
        ["Aucune", "Remplacer par la moyenne", "Remplacer par la médiane", "Remplacer par le mode", "Imputation KNN", "Remplacer par NaN"]
    )

    if st.button("Appliquer remplacement des valeurs manquantes"):
        if method != "Aucune":
            original_data = data.copy()
            numeric_columns = [col for col in data.columns if data[col].dtype in ['int64', 'float64']]

            if method in ["Remplacer par la moyenne", "Remplacer par la médiane", "Remplacer par le mode"]:
                strategy = "mean" if method == "Remplacer par la moyenne" else "median" if method == "Remplacer par la médiane" else "most_frequent"
                imputer = SimpleImputer(strategy=strategy)
                data[numeric_columns] = imputer.fit_transform(data[numeric_columns])
            elif method == "Imputation KNN":
                imputer = KNNImputer()
                data[numeric_columns] = imputer.fit_transform(data[numeric_columns])
            elif method == "Remplacer par NaN":
                data = data.apply(lambda x: x.where(pd.notnull(x), None))

            # Supprimer les colonnes avec plus de 90% de valeurs manquantes après imputation
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
        else:
            st.write("Aucune méthode de remplacement des valeurs manquantes n'a été sélectionnée.")
    
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