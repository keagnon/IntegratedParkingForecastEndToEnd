#!/usr/bin/env python
# coding: utf-8

# # Imputation
# 
# 

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# """ Lecture du fichier CSV """
path_fichier = r'C:\Users\User\Desktop\projet rncp\stationnement-en-ouvrage.csv'
df = pd.read_csv(path_fichier, sep=';')


# """ Suppression colonnes jugées peu pertinentes pour la suite des analyses   """
def drop_columns(df, columns_to_drop):
    """
    Supprime les colonnes spécifiées d'un DataFrame.
    
    Args:
    - df : DataFrame : Le DataFrame à modifier.
    - columns_to_drop : list : Liste des noms des colonnes à supprimer.
    
    Returns:
    - df : DataFrame : Le DataFrame avec les colonnes supprimées.
    """
    return df.drop(columns_to_drop, axis=1)

# """ Liste des colonnes à supprimer """
columns_to_drop = ["Nom parc", "Identifiant", "Adresse principale", "URL ressource services", "Numéro SIRET",
                   "Arrondissement", "Code zones résidentielles", "Type ouvrage", "Gratuit",
                   "Date application tarif abonnement", "Date application tarif horaire"]

# """ Appel de la fonction pour supprimer les colonnes """
drop_columns(df, columns_to_drop)

# """ Affichage du DataFrame résultant """
pd.set_option('display.max_columns', None)



def check_missing_values(df):
    """
    Vérifie et affiche le nombre de valeurs manquantes par colonne dans un DataFrame.

    Args:
    data (DataFrame): DataFrame contenant les données à vérifier.
    """
    # Calcul des valeurs manquantes par colonne
    missing_values = df.isna().sum()

    # Affichage
    print("Nombre de valeurs manquantes par colonne :")
    print(missing_values)
    
check_missing_values(df)


def fillna_with_mean(df, columns):
    """
    Remplace les valeurs manquantes dans les colonnes spécifiées par la moyenne de chaque colonne.

    Args:
    - df : DataFrame : Le DataFrame à modifier.
    - columns : list : Liste des noms des colonnes à traiter.

    Returns:
    - df : DataFrame : Le DataFrame avec les valeurs manquantes remplacées par la moyenne.
    """
    for column in columns:
        df[column] = df[column].fillna(df[column].mean())
    return df

# Liste des colonnes à traiter
columns_to_fill = ['Tarif_1h', 'Tarif_2h', 'Tarif_3h', 'Tarif_4h', 'Tarif_7h', 'Tarif_8h', 'Tarif_9h', 'Tarif_10h',
                   'Tarif_11h', 'Tarif_12h', 'Tarif_24h', 'Tarif_15mn', 'Tarif_30mn', 'Tarif_1h30',
                   'Tarif abonnement PMR mensuel', 'Tarif abonnement PMR timestriel', 'Tarif abonnement PMR annuel',
                   'Tarif abonnement VéhElect mensuel', 'Tarif abonnement VéhElect trimestriel',
                   'Tarif abonnement VéhElect annuel', 'Abonnement résident', 'Tarif abonnement moto trimestriel',
                   'Tarif abonnement moto annuel', 'Tarif abonnement moto mensuel', 'Tarif moto 1ere heure',
                   'Tarif petit rouleur annuel mini', 'Tarif petit rouleur annuel maxi', 'Tarif horaire préférentiel Moto Pass 2RM',
                   "Tarif de l'abonnement au Pass 2RM mensuel", "Tarif de l'abonnement au Pass 2RM trimestriel",
                   "Tarif de l'abonnement au Pass 2RM annuel", 'Tarif résident mensuel', 'Tarif abonnement parc relais annuel',
                   'Tarif abonnement place attribuée annuel', 'Tarif_30mn Moto', 'Tarif_24h Moto', 'Tarif_15mn Moto',
                   'Tarif moto petit rouleur annuel mini', 'Tarif moto petit rouleur annuel maxi', 'Tarif résident annuel',
                   'Tarif abonnement vélo mensuel']

# """Appel de la fonction pour remplacer les valeurs manquantes par la moyenne"""
fillna_with_mean(df, columns_to_fill)

def impute_missing_values(df):
    """
    Impute les valeurs manquantes dans les colonnes spécifiées d'un DataFrame.

    Args:
    data (DataFrame): DataFrame contenant les données à imputer.

    Returns:
    DataFrame: DataFrame avec les valeurs manquantes imputées.
    """
    # Liste des colonnes nécessitant une imputation
    columns_to_impute = [
        'Tarif_1h', 'Tarif_2h', 'Tarif_3h', 'Tarif_4h', 'Tarif_7h', 'Tarif_8h', 'Tarif_9h', 'Tarif_10h', 'Tarif_11h', 'Tarif_12h',
        'Tarif_24h', 'Tarif_15mn', 'Tarif_30mn', 'Tarif_1h30', 'Tarif abonnement PMR mensuel', 'Tarif abonnement PMR timestriel',
        'Tarif abonnement PMR annuel', 'Tarif abonnement VéhElect mensuel', 'Tarif abonnement VéhElect trimestriel', 'Tarif abonnement VéhElect annuel',
        'Abonnement résident', 'Tarif abonnement moto trimestriel', 'Tarif abonnement moto annuel', 'Tarif abonnement moto mensuel',
        'Tarif moto 1ere heure', 'Tarif petit rouleur annuel mini', 'Tarif petit rouleur annuel maxi',
        'Tarif horaire préférentiel Moto Pass 2RM', "Tarif de l'abonnement au Pass 2RM mensuel", "Tarif de l'abonnement au Pass 2RM trimestriel",
        "Tarif de l'abonnement au Pass 2RM annuel", 'Tarif résident mensuel', 'Tarif abonnement parc relais annuel', 'Tarif abonnement place attribuée annuel',
        'Tarif_30mn Moto', 'Tarif_24h Moto', 'Tarif_15mn Moto', 'Tarif moto petit rouleur annuel mini', 'Tarif moto petit rouleur annuel maxi',
        'Tarif résident annuel', 'Tarif abonnement vélo mensuel'
    ]

    # Création de l'objet imputer
    imputer = SimpleImputer(strategy='mean')

    # Imputation des valeurs manquantes dans les colonnes spécifiées
    df[columns_to_impute] = imputer.fit_transform(df[columns_to_impute])

    return df

impute_missing_values(df)


# # Encodage 
# Encodage binaire des valeurs catégorielles
def replace_yes_no_with_binary(data, columns):
    """
    Remplace les valeurs "OUI" par 1 et "NON" par 0 pour les colonnes spécifiées dans un DataFrame.

    Args:
    data (DataFrame): DataFrame contenant les colonnes à traiter.
    columns (list): Liste des noms des colonnes à traiter.

    Returns:
    DataFrame: DataFrame avec les valeurs remplacées.
    """
    for column in columns:
        data[column] = data[column].replace({'OUI': 1, 'NON': 0})
    return data

# Liste des colonnes à traiter
colonnes_a_traiter = ['Tarif moto petit rouleur', 'Parc amodié', 'Parc relais','Parc affilié au dispositif Pass 2RM','Tarif VL résident','Ascenseur surface','Tarif VL petit rouleur','Tarif moto résident']

# Appel de la fonction pour remplacer les valeurs dans le DataFrame
replace_yes_no_with_binary(df, colonnes_a_traiter)





# Utiliser la fonction get_dummies() de Pandas pour appliquer le One-Hot Encoding
def encode_columns(data, columns):
    """
    Encode les colonnes spécifiées en utilisant la méthode one-hot encoding.

    Args:
    data (DataFrame): DataFrame contenant les colonnes à encoder.
    columns (list): Liste des noms des colonnes à encoder.

    Returns:
    DataFrame: DataFrame avec les colonnes encodées.
    """
    encoded_data = pd.get_dummies(data, columns=columns)
    return encoded_data

# Colonnes à encoder
colonnes_a_encoder = ['Type usagers', 'Délégataire', 'Horaire ouverture non abonnés', 'Tarif PMR']

# Appel de la fonction pour encoder les colonnes spécifiées
encode_columns(df, colonnes_a_encoder)


# # Choix de l'encodage One hot : 
# #Le One-Hot Encoding permet de conserver toutes les informations contenues dans une variable catégorielle sans introduire de relation d'ordre artificielle entre les catégories.
# #Le One-Hot Encoding transforme les variables catégorielles en vecteurs binaires, ce qui les rend compatibles avec les algorithmes ML .
# #Le One-Hot Encoding facilite l'interprétation des modèles en rendant les variables catégorielles explicites dans les résultats, ce qui permet de comprendre facilement l'impact de chaque catégorie sur les prédictions du modèle.

# # Mise à l'echelle

# permet de mettre toutes les caractéristiques numériques sur la même échelle, ce qui est important pour certains algorithmes d'apprentissage automatique qui sont sensibles à l'échelle des caractéristiques


def normalize_numeric_columns(df, numeric_columns):
    """
    Normalise les colonnes numériques spécifiées en utilisant StandardScaler.

    Args:
    data (DataFrame): DataFrame contenant les colonnes numériques à normaliser.
    numeric_columns (list): Liste des noms des colonnes numériques à normaliser.

    Returns:
    DataFrame: DataFrame avec les colonnes numériques normalisées.
    """
    # Instanciation de l'objet StandardScaler
    scaler = StandardScaler()

    # Normalisation des données numériques
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df

# Colonnes numériques à normaliser
colonnes_numeriques_a_normaliser = [
    'Nbre total places', 'Nbre place parc relais', 'Nbre place PMR', 'Nbre place voit elec', 'Nbre place vélo', 
    'Nbre place velo-2rm elec', 'Nbre place autopartage', 'Nbre place 2rm', 'Nbre place covoiturage', 'Hauteur max', 
    'Tarif_1h', 'Tarif_2h', 'Tarif_3h', 'Tarif_4h', 'Tarif_24h', 'Tarif_15mn', 'Tarif_30mn', 'Tarif_1h30', 'Tarif_7h', 
    'Tarif_8h', 'Tarif_9h', 'Tarif_10h', 'Tarif_11h', 'Tarif_12h', 'Tarif abonnement PMR mensuel', 
    'Tarif abonnement PMR timestriel', 'Tarif abonnement PMR annuel', 'Tarif abonnement VéhElect mensuel', 
    'Tarif abonnement VéhElect trimestriel', 'Tarif abonnement VéhElect annuel', 'Tarif moto 1ere heure', 
    'Tarif abonnement moto mensuel', 'Tarif abonnement moto trimestriel', 'Tarif abonnement moto annuel', 
    'Tarif abonnement vélo mensuel', 'Tarif_15mn Moto', 'Tarif_30mn Moto', 'Tarif_24h Moto', 'Tarif moto petit rouleur', 
    'Tarif moto petit rouleur annuel mini', 'Tarif moto petit rouleur annuel maxi', 'Tarif moto résident', 
    'Tarif moto résident annuel', 'Tarif abonnement place attribuée annuel', 'Tarif abonnement parc relais annuel', 
    'Tarif résident mensuel', 'Tarif horaire préférentiel Moto Pass 2RM', "Tarif de l'abonnement au Pass 2RM mensuel", 
    "Tarif de l'abonnement au Pass 2RM trimestriel", "Tarif de l'abonnement au Pass 2RM annuel"
]

# Appel de la fonction pour normaliser les colonnes numériques spécifiées
normalize_numeric_columns(df, colonnes_numeriques_a_normaliser)



