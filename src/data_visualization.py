import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

def plot_histogram(data):
    st.subheader("Histogrammes")
    x_column = st.selectbox("Choisissez une colonne pour l'axe des X", data.columns, key='hist_x')
    y_column = st.selectbox("Choisissez une colonne pour l'axe des Y", [None] + data.columns.tolist(), key='hist_y')
    sum_option = st.checkbox("Faire la somme des valeurs pour les mêmes catégories", key='sum_option')

    if x_column:
        plt.figure(figsize=(10, 6))  # Taille de la figure définie à 10x6 pouces
        if sum_option and y_column:
            # Faire la somme des valeurs de y_column pour chaque catégorie de x_column
            summed_data = data.groupby(x_column)[y_column].sum().reset_index()
            sns.barplot(x=x_column, y=y_column, data=summed_data)
            plt.title(f'Somme de {y_column} pour chaque {x_column}')
        elif y_column and y_column != x_column:
            sns.histplot(data=data, x=x_column, hue=y_column, multiple="stack", kde=True)
            plt.title(f'Histogramme de {x_column} avec {y_column} comme variable de couleur')
        else:
            sns.histplot(data[x_column].dropna(), kde=True)
            plt.title(f'Histogramme de {x_column}')
        st.pyplot(plt)

def plot_boxplot(data):
    st.subheader("Box plots")
    column = st.selectbox("Choisissez une colonne pour afficher le box plot", data.columns, key='boxplot')
    if column:
        plt.figure(figsize=(10, 6))  # Taille de la figure définie à 10x6 pouces
        sns.boxplot(x=data[column].dropna())
        plt.title(f'Box plot de {column}')
        st.pyplot(plt)

def plot_bar_chart(data):
    st.subheader("Diagrammes en barres")
    x_column = st.selectbox("Choisissez la colonne pour l'axe des X", data.columns, key='barchart_x')
    y_column = st.selectbox("Choisissez la colonne pour l'axe des Y", data.columns, key='barchart_y')
    
    if x_column and y_column:
        plt.figure(figsize=(10, 6))  # Taille de la figure définie à 10x6 pouces
        sns.barplot(x=data[x_column].dropna(), y=data[y_column].dropna())
        plt.title(f'Diagramme en barres entre {x_column} et {y_column}')
        st.pyplot(plt)
    else:
        st.warning("Veuillez choisir les colonnes pour afficher le diagramme en barres.")

def plot_scatterplot(data):
    st.subheader("Nuages de points")
    x_column = st.selectbox("Choisissez la colonne pour l'axe des X", data.columns, key='scatter_x')
    y_column = st.selectbox("Choisissez la colonne pour l'axe des Y", data.columns, key='scatter_y')
    if x_column and y_column and data[x_column].dtype in ['int64', 'float64'] and data[y_column].dtype in ['int64', 'float64']:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data[x_column].dropna(), y=data[y_column].dropna())
        plt.title(f'Nuage de points entre {x_column} et {y_column}')
        st.pyplot(plt)
    else:
        st.warning("Veuillez choisir des colonnes numériques pour afficher le nuage de points.")

def plot_correlation_matrix(data):
    st.subheader("Matrice de corrélation")
    corr = data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Matrice de corrélation')
    st.pyplot(plt)

def plot_heatmap(data):
    st.subheader("Heatmap")
    columns = st.multiselect("Choisissez les colonnes pour afficher le heatmap", data.columns)
    if columns:
        plt.figure(figsize=(10, 6))
        sns.heatmap(data[columns].dropna().corr(), annot=True, cmap='coolwarm')
        plt.title(f'Heatmap des colonnes sélectionnées')
        st.pyplot(plt)
    else:
        st.warning("Veuillez choisir au moins une colonne pour afficher le heatmap.")
