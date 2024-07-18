from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def perform_clustering(data):
    if data.empty:
        st.error("Les données sont vides. Veuillez charger un dataset valide.")
        return

    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    if len(numerical_columns) == 0:
        st.error("Le dataset ne contient aucune colonne numérique pour le clustering.")
        return

    selected_columns = st.multiselect("Choisissez les colonnes pour le clustering", numerical_columns)
    if len(selected_columns) < 2:
        st.warning("Veuillez sélectionner au moins deux colonnes pour effectuer le clustering.")
        return
    
    data_selected = data[selected_columns]
    
    clustering_method = st.selectbox("Choisissez un algorithme de clustering", ["K-Means", "DBSCAN"])
    if clustering_method == "K-Means":
        n_clusters = st.slider("Nombre de clusters", 2, 10, 3)
        model = KMeans(n_clusters=n_clusters)
        clusters = model.fit_predict(data_selected)
        data['Cluster'] = clusters
        st.write("Clusters calculés avec succès !")
        st.dataframe(data.head())
        plot_clusters(data, selected_columns, "K-Means Clustering")
        plot_clusters_3d(data, selected_columns, "K-Means Clustering 3D")
        display_cluster_stats(data, clusters, model.cluster_centers_)
        evaluate_clustering(data_selected, clusters)
    elif clustering_method == "DBSCAN":
        eps = st.slider("Valeur de eps", 0.1, 10.0, 0.5)
        min_samples = st.slider("Nombre minimum d'échantillons", 1, 10, 5)
        model = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = model.fit_predict(data_selected)
        data['Cluster'] = clusters
        st.write("Clusters calculés avec succès !")
        st.dataframe(data.head())
        plot_clusters(data, selected_columns, "DBSCAN Clustering")
        plot_clusters_3d(data, selected_columns, "DBSCAN Clustering 3D")
        display_cluster_stats(data, clusters)
        evaluate_clustering(data_selected, clusters)

def plot_clusters(data, selected_columns, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[selected_columns[0]], y=data[selected_columns[1]], hue='Cluster', palette='viridis', data=data)
    plt.title(title)
    st.pyplot(plt)

def plot_clusters_3d(data, selected_columns, title):
    if len(selected_columns) < 3:
        st.warning("La visualisation en 3D nécessite au moins trois dimensions numériques.")
        return
    
    fig = px.scatter_3d(
        data, 
        x=selected_columns[0], 
        y=selected_columns[1], 
        z=selected_columns[2], 
        color='Cluster', 
        title=title
    )
    st.plotly_chart(fig)

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
