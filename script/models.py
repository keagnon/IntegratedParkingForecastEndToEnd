# models.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def model_data(file_path='/home/alimou/Desktop/memoire/script/velib_cleaned.csv'):
    # Charger les données nettoyées
    cleaned_data = pd.read_csv(file_path)

    # Vérifier si l'ensemble de données nettoyé n'est pas vide
    if cleaned_data.empty:
        print("L'ensemble de données nettoyé est vide. Impossible de procéder à l'encodage.")
        return

    # Encodage des variables catégorielles
    encoded_data = encode_categorical(cleaned_data)

    # Mise à l'échelle des données
    scaled_data = scale_data(encoded_data)

    # Entraînement du modèle et prédictions
    predictions, y_test = train_and_predict(scaled_data)

    # Calcul des scores
    calculate_scores(predictions, y_test)

def encode_categorical(data):
    # Encodage des variables catégorielles
    categorical_cols = data.select_dtypes(include='object').columns
    transformer = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(), categorical_cols)],
        remainder='passthrough'
    )
    encoded_data = transformer.fit_transform(data)
    
    # Récupérer les noms de colonnes après l'encodage
    if len(categorical_cols) > 0:
        encoded_columns = transformer.get_feature_names_out(input_features=categorical_cols)
        # Créer un DataFrame avec les colonnes encodées
        return pd.DataFrame(encoded_data, columns=list(encoded_columns) + list(data.columns[len(categorical_cols):]))
    else:
        # Si aucune colonne catégorielle, renvoyer le DataFrame tel quel
        return data

def scale_data(data):
    # Mise à l'échelle des variables numériques
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[numerical_cols])
    data[numerical_cols] = scaled_data
    return data

def train_and_predict(data):
    # Séparation des features et de la target
    X = data.drop('Nombre total vélos disponibles', axis=1)
    y = data['Nombre total vélos disponibles']

    # Division du jeu de données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Création du pipeline avec le modèle RandomForestRegressor
    model = Pipeline([
        ('preprocessor', ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), X.select_dtypes(include=['float64', 'int64']).columns),
                ('cat', OneHotEncoder(), X.select_dtypes(include='object').columns)
            ]
        )),
        ('regressor', RandomForestRegressor(random_state=42))
    ])

    # Entraînement du modèle
    model.fit(X_train, y_train)

    # Prédictions sur l'ensemble de test
    predictions = model.predict(X_test)

    return predictions, y_test

def calculate_scores(predictions, y_test):
    # Calcul des scores
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"\nMean Squared Error (MSE): {mse}")
    print(f"R-squared (R2): {r2}")

# Test de la fonction
if __name__ == "__main__":
    model_data()
