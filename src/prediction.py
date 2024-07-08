import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def perform_prediction(data):
    prediction_method = st.selectbox("Choisissez un algorithme de prédiction", ["Régression Linéaire", "Classification Random Forest"])
    target_column = st.selectbox("Choisissez la colonne cible (variable dépendante)", data.columns)
    if prediction_method == "Régression Linéaire":
        X = data.drop(columns=[target_column])
        y = data[target_column]
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        data['Prédictions'] = predictions
        st.write("Prédictions calculées avec succès !")
        st.dataframe(data.head())
        plot_predictions(y, predictions, "Régression Linéaire")
        evaluate_regression(y, predictions)
    elif prediction_method == "Classification Random Forest":
        X = data.drop(columns=[target_column])
        y = data[target_column]
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
    st.write(f"Mean Squared Error: {mse}")

def evaluate_classification(y, predictions):
    st.subheader("Évaluation des Prédictions")
    report = classification_report(y, predictions, output_dict=True)
    st.write(pd.DataFrame(report).transpose())
