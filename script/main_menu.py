# main_menu.py
import subprocess
from exploration import explore_data  # Importer la fonction explore_data
from preprocessing import preprocess_data  # netoyage
from models import model_data  # prediction



while True:
    print("1. Exploration des données")
    print("2. Prétraitement des données")
    print("3. Entraîner le modèle")
    print("4. Quitter")

    choice = input("Choisissez une option (1-4): ")

    if choice == '1':
        explore_data()  # Appeler la fonction explore_data
    elif choice == '2':
        preprocess_data()
    elif choice == '3':
        model_data()
    elif choice == '4':
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
