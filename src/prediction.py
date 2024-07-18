import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report, confusion_matrix, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def perform_prediction(data):
    if data.empty:
        st.error("Les données sont vides. Veuillez charger un dataset valide.")
        return
    
    prediction_method = st.selectbox("Choisissez un algorithme de prédiction", ["Régression Linéaire", "Classification Random Forest"])
    target_column = st.selectbox("Choisissez la colonne cible (variable dépendante)", data.columns)
    
    if prediction_method == "Régression Linéaire":
        st.write("Régression Linéaire")
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        if y.dtype not in ['int64', 'float64']:
            st.error("La colonne cible doit être numérique pour la régression.")
            return

        X = X.select_dtypes(include=['int64', 'float64'])
        
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        data['Prédictions'] = predictions
        st.write("Prédictions calculées avec succès !")
        st.dataframe(data.head())
        plot_predictions(y, predictions, "Régression Linéaire")
        evaluate_regression(y, predictions)
    
    elif prediction_method == "Classification Random Forest":
        st.write("Classification Random Forest")
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        if y.dtype not in ['object', 'int64']:
            st.error("La colonne cible doit être catégorielle pour la classification.")
            return

        X = X.select_dtypes(include=['int64', 'float64'])
        
        model = RandomForestClassifier()
        model.fit(X, y)
        predictions = model.predict(X)
        data['Prédictions'] = predictions
        st.write("Prédictions calculées avec succès !")
        st.dataframe(data.head())
        plot_predictions(y, predictions, "Classification Random Forest")
        evaluate_classification(y, predictions)

def plot_predictions(y, predictions, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y, y=predictions)
    plt.xlabel("Valeurs Réelles")
    plt.ylabel("Prédictions")
    plt.title(title)
    st.pyplot(plt)

def evaluate_regression(y, predictions):
    st.subheader("Évaluation des Prédictions")
    mse = mean_squared_error(y, predictions)
    r2 = r2_score(y, predictions)
    st.write(f"Mean Squared Error: {mse}")
    st.write(f"R²: {r2}")
    plt.figure(figsize=(10, 6))
    sns.residplot(x=y, y=predictions)
    plt.xlabel("Valeurs Réelles")
    plt.ylabel("Résidus")
    plt.title("Graphique des Résidus")
    st.pyplot(plt)

def evaluate_classification(y, predictions):
    st.subheader("Évaluation des Prédictions")
    report = classification_report(y, predictions, output_dict=True)
    st.write(pd.DataFrame(report).transpose())
    cm = confusion_matrix(y, predictions)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Prédictions")
    plt.ylabel("Valeurs Réelles")
    plt.title("Matrice de Confusion")
    st.pyplot(plt)
