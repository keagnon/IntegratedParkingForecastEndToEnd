# preprocessing.py
import pandas as pd

def preprocess_data(file_path='/home/alimou/Desktop/memoire/script/velib-disponibilite-en-temps-reel.csv',
                    output_file='/home/alimou/Desktop/memoire/script/velib_cleaned.csv'):
    # Charger les données
    data = pd.read_csv(file_path, nrows=500, sep=';', header=0)

    # Remplacer les valeurs manquantes par la médiane des colonnes numériques
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

    # Afficher les données propres
    print("\nDonnées propres après nettoyage:")
    print(data.head())

    # Sauvegarder les données propres dans un nouveau fichier CSV
    data.to_csv(output_file, index=False)
    print(f"\nLes données propres ont été sauvegardées dans {output_file}.")

# Test de la fonction
if __name__ == "__main__":
    preprocess_data()
