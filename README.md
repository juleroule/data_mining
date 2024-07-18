# Projet Data Mining

Ce projet est une application web interactive développée avec Streamlit pour la visualisation, le nettoyage, l'analyse, et la prédiction des données.

## Fonctionnalités

- **Chargement des données** : Chargez des fichiers CSV et affichez un aperçu et un résumé statistique des données.
- **Pré-traitement et nettoyage des données** : Gérez les valeurs manquantes, normalisez les données, et transformez les colonnes catégorielles.
- **Visualisation des données** : Affichez des histogrammes, des box plots, des nuages de points, des diagrammes en barres, des matrices de corrélation, et des cartes géographiques.
- **Clustering** : Exécutez des algorithmes de clustering K-Means et DBSCAN.
- **Prédiction** : Utilisez des modèles de régression linéaire et de classification Random Forest pour effectuer des prédictions.

## Prérequis

Assurez-vous d'avoir Python 3.7 ou plus installé sur votre machine.

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/projet-data-mining.git
    cd projet-data-mining
    ```

2. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

1. Placez vos fichiers de données CSV dans le dossier du projet ou spécifiez le chemin correct lors du chargement des données dans l'application.

2. Lancez l'application Streamlit :
    ```sh
    streamlit run 🏠_Home.py
    ```

3. Utilisez l'interface web pour :
    - Charger et explorer vos données
    - Effectuer des opérations de pré-traitement et de nettoyage
    - Visualiser les données
    - Appliquer des algorithmes de clustering et de prédiction

## Structure du projet

- **🏠_Home.py** : Page d'accueil de l'application. Charge les données, affiche un aperçu et un résumé statistique.
- **1_✨_Traitement.py** : Pré-traitement et nettoyage des données.
- **2_🎢_Histogramme.py** : Visualisation des histogrammes.
- **3_🗺️_Map.py** : Visualisation des données géographiques sur une carte.
- **4_👓_Visualisation.py** : Visualisation des données nettoyées (box plots, diagrammes en barres, nuages de points, matrices de corrélation, heatmaps).
- **5_💯_Analyse.py** : Exécution des algorithmes de clustering et de prédiction.
- **clustering.py** : Algorithmes de clustering et visualisations associées.
- **data_cleaning.py** : Fonctions pour le nettoyage des données.
- **data_loading.py** : Fonctions pour le chargement des données.
- **data_visualization.py** : Fonctions de visualisation des données.
- **prediction.py** : Algorithmes de prédiction et évaluations associées.
- **styles.css** : Fichier CSS pour la personnalisation de l'interface Streamlit.


