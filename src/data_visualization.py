import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_histogram(data):
    st.subheader("Histogrammes")
    column = st.selectbox("Choisissez une colonne pour afficher l'histogramme", data.columns)
    if column:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Histogramme de {column}')
        st.pyplot(plt)

def plot_boxplot(data):
    st.subheader("Box plots")
    column = st.selectbox("Choisissez une colonne pour afficher le box plot", data.columns, key='boxplot')
    if column:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data[column])
        plt.title(f'Box plot de {column}')
        st.pyplot(plt)
