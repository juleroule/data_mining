import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

# Fonction utilitaire pour obtenir les colonnes numériques
def get_numerical_columns(data):
    return [col for col in data.columns if data[col].dtype in ['int64', 'float64']]

def plot_histogram(data):
    st.subheader("Histogrammes")
    numerical_columns = get_numerical_columns(data)
    
    # Sélection de la première colonne pour l'axe des X
    x_column = st.selectbox("Choisissez une colonne pour l'axe des X", numerical_columns, key='hist_x')
    
    # Option pour afficher un deuxième histogramme
    add_second_hist = st.checkbox("Ajouter un deuxième histogramme", key='second_hist')
    if add_second_hist:
        second_x_column = st.selectbox("Choisissez une colonne pour le deuxième histogramme", numerical_columns, key='second_hist_x')

    if x_column:
        plt.figure(figsize=(20, 6))  # Taille de la figure définie à 20x6 pouces
        plt.subplot(1, 2, 1)  # Premier histogramme
        sns.histplot(data[x_column].dropna(), kde=True)
        plt.title(f'Histogramme de {x_column}')
        
        if add_second_hist and second_x_column:
            plt.subplot(1, 2, 2)  # Deuxième histogramme
            sns.histplot(data[second_x_column].dropna(), kde=True)
            plt.title(f'Histogramme de {second_x_column}')
        
        st.pyplot(plt, use_container_width=True)
        
def get_string_columns(data):
    return [col for col in data.columns if pd.api.types.is_string_dtype(data[col])]

def plot_histogram_for_strings(data):
    st.subheader("Histogrammes pour les valeurs de type string")
    string_columns = get_string_columns(data)
    
    if not string_columns:
        st.error("Aucune colonne de type string disponible dans le dataset.")
        return
    
    # Sélection de la première colonne pour l'axe des X
    x_column = st.selectbox("Choisissez une colonne pour l'axe des X", string_columns, key='hist_x')
    
    # Option pour afficher un deuxième histogramme
    add_second_hist = st.checkbox("Ajouter un deuxième histogramme", key='second_hist')
    if add_second_hist:
        second_x_column = st.selectbox("Choisissez une colonne pour le deuxième histogramme", string_columns, key='second_hist_x')

    if x_column:
        plt.figure(figsize=(20, 6))  # Taille de la figure définie à 20x6 pouces
        plt.subplot(1, 2, 1)  # Premier histogramme
        value_counts = data[x_column].value_counts()
        plt.bar(value_counts.index, value_counts.values, edgecolor='black')
        plt.title(f'Histogramme de {x_column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        
        if add_second_hist and second_x_column:
            plt.subplot(1, 2, 2)  # Deuxième histogramme
            value_counts = data[second_x_column].value_counts()
            plt.bar(value_counts.index, value_counts.values, edgecolor='black')
            plt.title(f'Histogramme de {second_x_column}')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.xticks(rotation=45)
        
        st.pyplot(plt, use_container_width=True)

def plot_boxplot(data):
    st.subheader("Box plots")
    numerical_columns = get_numerical_columns(data)
    column = st.selectbox("Choisissez une colonne pour afficher le box plot", numerical_columns, key='boxplot')
    if column:
        plt.figure(figsize=(10, 6))  # Taille de la figure définie à 10x6 pouces
        sns.boxplot(x=data[column].dropna())
        plt.title(f'Box plot de {column}')
        st.pyplot(plt)

def plot_bar_chart(data):
    st.subheader("Diagrammes en barres")
    numerical_columns = get_numerical_columns(data)
    x_column = st.selectbox("Choisissez la colonne pour l'axe des X", numerical_columns, key='barchart_x')
    y_column = st.selectbox("Choisissez la colonne pour l'axe des Y", numerical_columns, key='barchart_y')
    
    if x_column and y_column:
        plt.figure(figsize=(10, 6))  # Taille de la figure définie à 10x6 pouces
        sns.barplot(x=data[x_column].dropna(), y=data[y_column].dropna())
        plt.title(f'Diagramme en barres entre {x_column} et {y_column}')
        st.pyplot(plt)
    else:
        st.warning("Veuillez choisir les colonnes pour afficher le diagramme en barres.")

def plot_scatterplot(data):
    st.subheader("Nuages de points")
    numerical_columns = get_numerical_columns(data)
    x_column = st.selectbox("Choisissez la colonne pour l'axe des X", numerical_columns, key='scatter_x')
    y_column = st.selectbox("Choisissez la colonne pour l'axe des Y", numerical_columns, key='scatter_y')
    if x_column and y_column:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data[x_column].dropna(), y=data[y_column].dropna())
        plt.title(f'Nuage de points entre {x_column} et {y_column}')
        st.pyplot(plt)
    else:
        st.warning("Veuillez choisir des colonnes numériques pour afficher le nuage de points.")

def plot_correlation_matrix(data):
    st.subheader("Matrice de corrélation")
    numerical_columns = get_numerical_columns(data)
    corr = data[numerical_columns].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Matrice de corrélation')
    st.pyplot(plt)

def plot_heatmap(data):
    st.subheader("Heatmap")
    numerical_columns = get_numerical_columns(data)
    columns = st.multiselect("Choisissez les colonnes pour afficher le heatmap", numerical_columns)
    if columns:
        plt.figure(figsize=(10, 6))
        sns.heatmap(data[columns].dropna().corr(), annot=True, cmap='coolwarm')
        plt.title(f'Heatmap des colonnes sélectionnées')
        st.pyplot(plt)
    else:
        st.warning("Veuillez choisir au moins une colonne pour afficher le heatmap.")
