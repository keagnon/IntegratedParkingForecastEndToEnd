# exploration.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Preprocessing import *

#In[]
def apercu_donnees(df, n=5):
    """Affiche les premières lignes du jeu de données."""
    return df.head(n)

def statistiques_descriptives(df):
    """Calcule les statistiques descriptives pour les colonnes numériques."""
    return df.describe()
#In[]
def distribution_valeurs(df, colonne):
    """Affiche la distribution des valeurs pour une colonne donnée."""
    plt.figure(figsize=(8, 6))
    sns.histplot(df[colonne], kde=True)
    plt.title(f'Distribution de {colonne}')
    plt.xlabel(colonne)
    plt.ylabel('Fréquence')
    plt.show()


def plot_correlation_with_target(data, target_variable):
    """
    Crée une heatmap de corrélation entre la variable cible et les autres variables numériques.

    Args:
    data (DataFrame): DataFrame contenant les données.
    target_variable (str): Nom de la variable cible.

    Returns:
    None
    """
    # Sélection de la colonne correspondant à la variable cible
    target_column = data[target_variable]

    # Sélection des variables numériques autres que la variable cible
    df_numerical = data.select_dtypes(include='number').drop(columns=[target_variable])

    # Calcul de la corrélation entre la variable cible et les autres variables numériques
    correlation_with_target = df_numerical.corrwith(target_column)

    # Création de la barplot
    plt.figure(figsize=(25, 15))  # Augmentation de la taille de la figure
    correlation_with_target.plot(kind='bar', color='skyblue')
    plt.title(f'Corrélation avec la variable {target_variable}')
    plt.xlabel('Variables')
    plt.ylabel('Corrélation')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajustement automatique de la mise en page
    plt.show()




def analyse_frequence(df, colonne):
    """Compte la fréquence des différentes catégories dans une colonne catégorielle."""
    plt.figure(figsize=(8, 6))
    sns.countplot(x=colonne, data=df)
    plt.title(f'Fréquence de {colonne}')
    plt.xlabel(colonne)
    plt.ylabel('Fréquence')
    plt.xticks(rotation=45)
    plt.show()

def visualisation_geographique(df):
    """Visualise les emplacements des stationnements sur une carte."""
    plt.scatter(df['X longitude parc WGS84'], df['Y latitude parc WGS84'], alpha=0.5)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Répartition géographique des stationnements')
    plt.show()

# Utilisation des fonctions
apercu_donnees(df)
statistiques_descriptives(df)
distribution_valeurs(df, 'Nbre total places')
# Appel de la fonction pour afficher la corrélation avec la variable 'Nbre total places'
plot_correlation_with_target(df, 'Nbre total places')
analyse_frequence(df, 'Type usagers')
visualisation_geographique(df)


# %%
