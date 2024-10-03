import subprocess  # Importation du module subprocess pour exécuter des commandes système.
import tkinter as tk  # Importation de tkinter pour créer des interfaces graphiques.
from tkinter import ttk  # Importation du module ttk pour utiliser des widgets stylisés.

# Fonction pour scanner les réseaux WiFi
def scanner_reseaux_wifi():
    try:
        # Exécution de la commande 'netsh wlan show interfaces' pour obtenir les informations WiFi.
        # L'argument text=True permet de récupérer la sortie en tant que chaîne de caractères.
        # L'encodage "cp850" est utilisé pour éviter les erreurs de décodage sous Windows.
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], text=True, encoding="cp850")
        return result  # Retourne la sortie du scan des réseaux.
    except Exception as e:
        # En cas d'erreur, retourne un message avec la description de l'erreur.
        return f"Erreur lors du scan : {e}"

# Fonction pour afficher les réseaux scannés dans la zone de texte
def afficher_reseau():
    result = scanner_reseaux_wifi()  # Appelle la fonction pour scanner les réseaux.
    texte_affichage.delete(1.0, tk.END)  # Efface le contenu actuel de la zone de texte (de la première ligne à la fin).
    texte_affichage.insert(tk.END, result)  # Insère le résultat du scan dans la zone de texte.

# Création de la fenêtre principale
fenetre = tk.Tk()  # Initialisation de la fenêtre tkinter.
fenetre.title("Scan réseau WiFi")  # Définition du titre de la fenêtre.
fenetre.geometry("800x600")  # Définition de la taille de la fenêtre.

# Création d'un label (étiquette) pour le titre
titre = ttk.Label(fenetre, text="Liste des réseaux", font=("Helvetica", 16, "bold"))  # Création d'une étiquette avec un texte et une police stylée.
titre.pack(pady=10)  # Placement du label dans la fenêtre avec un espacement vertical (padding) de 10 pixels.

# Création d'un bouton pour lancer le scan des réseaux
btn_scanner = ttk.Button(fenetre, text="Scanner", command=afficher_reseau)  # Création d'un bouton qui appelle la fonction afficher_reseau lorsqu'il est cliqué.
btn_scanner.pack(pady=10)  # Placement du bouton avec un espacement vertical de 10 pixels.

# Création d'une zone de texte pour afficher les résultats du scan
texte_affichage = tk.Text(fenetre, wrap=tk.WORD, width=70, height=15)  # Création d'une zone de
