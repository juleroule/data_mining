from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def perform_clustering(data):
    if data.empty:
        st.error("Les données sont vides. Veuillez charger un dataset valide.")
        return
    
    # Vérifier si les colonnes sont numériques
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    if len(numerical_columns) == 0:
        st.error("Le dataset ne contient aucune colonne numérique pour le clustering.")
        return

    clustering_method = st.selectbox("Choisissez un algorithme de clustering", ["K-Means", "DBSCAN"])
    if clustering_method == "K-Means":
        n_clusters = st.slider("Nombre de clusters", 2, 10, 3)
        model = KMeans(n_clusters=n_clusters)
        clusters = model.fit_predict(data[numerical_columns])
        data['Cluster'] = clusters
        st.write("Clusters calculés avec succès !")
        st.dataframe(data.head())
        plot_clusters(data, model, "K-Means Clustering")
        display_cluster_stats(data, clusters, model.cluster_centers_)
        evaluate_clustering(data[numerical_columns], clusters)
    elif clustering_method == "DBSCAN":
        eps = st.slider("Valeur de eps", 0.1, 10.0, 0.5)
        min_samples = st.slider("Nombre minimum d'échantillons", 1, 10, 5)
        model = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = model.fit_predict(data[numerical_columns])
        data['Cluster'] = clusters
        st.write("Clusters calculés avec succès !")
        st.dataframe(data.head())
        plot_clusters(data, model, "DBSCAN Clustering")
        display_cluster_stats(data, clusters)
        evaluate_clustering(data[numerical_columns], clusters)

def plot_clusters(data, model, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data.iloc[:, 0], y=data.iloc[:, 1], hue='Cluster', palette='viridis', data=data)
    plt.title(title)
    st.pyplot(plt)

def display_cluster_stats(data, clusters, centers=None):
    st.subheader("Statistiques des clusters")
    st.write("Nombre de points de données par cluster :")
    st.write(data['Cluster'].value_counts())
    if centers is not None:
        st.write("Centres des clusters :")
        st.write(centers)
    else:
        st.write("Nombre de clusters : ", len(set(clusters)) - (1 if -1 in clusters else 0))
        st.write("Nombre de points de données considérés comme bruit (étiquette -1) : ", list(clusters).count(-1))

def evaluate_clustering(data, clusters):
    st.subheader("Évaluation des Clusters")
    score = silhouette_score(data, clusters)
    st.write(f"Score de silhouette : {score}")
