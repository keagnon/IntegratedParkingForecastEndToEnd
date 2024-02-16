# exploration.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(file_path='/home/alimou/Desktop/memoire/script/velib-disponibilite-en-temps-reel.csv'):
    # Charger les données
    data = pd.read_csv(file_path , nrows=500, sep=';', header=0)

    # Informations générales sur le dataframe
    print("Informations générales sur le dataframe:")
    print(data.info())

    # Afficher les premières lignes du dataframe
    print("\nLes premières lignes du dataframe:")
    print(data.head())

    # Statistiques descriptives pour les colonnes numériques
    print("\nStatistiques descriptives pour les colonnes numériques:")
    print(data.describe())

    # Afficher les colonnes par type
    display_columns_by_type(data)

    # Explorer les données visuellement
    explore_visualizations(data)

def display_columns_by_type(data):
    print("\nAfficher les colonnes par type:")
    print(data.dtypes)

def explore_visualizations(data):
    print("\nExplorer les données visuellement:")

    # Afficher les histogrammes des variables numériques
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution de {col}')
        plt.show()

    # Afficher les graphiques de dispersion pour les relations entre variables
    sns.pairplot(data[numerical_cols])
    plt.show()

    # Afficher les diagrammes à barres pour les variables catégorielles
    categorical_cols = data.select_dtypes(include='object').columns
    for col in categorical_cols:
        plt.figure(figsize=(10, 5))
        sns.countplot(data[col])
        plt.title(f'Diagramme à barres de {col}')
        plt.show()

    # Afficher les boîtes à moustaches pour les valeurs aberrantes
    for col in numerical_cols:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=data[col])
        plt.title(f'Boîte à moustaches de {col}')
        plt.show()

    # Afficher les informations sur les valeurs manquantes
    print("\nInformations sur les valeurs manquantes:")
    print(data.isnull().sum())
