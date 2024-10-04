# #faire apparaitre une fenetre 
# from tkinter import *
# fen = Tk()
# fen.config(bg='black')
# fen.mainloop()


#Devine le chiffre entre 1 et 1000
# import random

# chiffre_random = random.randint(1, 1000)
# print(chiffre_random)  # Affiche un nombre aléatoire entre 1 et 1000
# input_user = 0

# while input_user != chiffre_random:
#     input_user = int(input("Veuillez entrer un chiffre entre 1 et 1000 : "))
    
#     if input_user < chiffre_random:
#         print(f"Trop petit, entrer un chiffre plus grand que {input_user}.")
#     elif input_user > chiffre_random:
#         print(f"Trop grand, entre un chiffre plus petit que {input_user}.")

# print(f"Bravo, vous avez trouvé le chiffre {chiffre_random} !")

#Programme qui lit un fichier texte 

# from collections import Counter

# with open("Exo_pour_python.txt", 'r', encoding="utf-8") as fichier:
#     contenu = fichier.read()

#     # Comptage des mots, lettres et phrases
#     mots = contenu.split()
#     nbr_mots = len(mots)
#     nbr_lettres = sum(len(mot) for mot in mots)
#     nbr_phrase = contenu.count('.') + contenu.count('!') + contenu.count('?')

#     # Trouver le mot le plus fréquent
#     compte_mots = Counter(mots)
#     mot_present, freq_max = compte_mots.most_common(1)[0]

#     # Affichage des résultats
#     print(f"Dans le fichier, il y a {nbr_mots} mot(s), {nbr_lettres} lettre(s), et {nbr_phrase} phrase(s).")
#     print(f"Le mot le plus fréquent est : '{mot_present}' avec {freq_max} occurrences.")


#Exercice 3 

import csv

class Contact:
    def __init__(self, nom, prenom, adresse, num_telephone):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.num_telephone = num_telephone
    #permet de transformer la classe en liste pour le csv    
    def transo(self):
        return [self.nom, self.prenom, self.adresse, self.num_telephone]
    
#Teste de la liste 
contacts = {
        Contact('Dierickx', "Simon", "Rue gailly 22", "0499500333"),
        Contact("Dupont", "Richard", "Rue des combattants 66", "04689457852")
    }
    
#nom du fichier csv
filename = 'contact.csv'

#Ouvrir le fichier en mode écriture 
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    #Ecrire l'en-tête
    writer.writerow(['Nom', 'Prenom', 'Adresse', 'Numéro de téléphone'])
    
    #ecrire les infos de chasque contact
    for c in contacts:
        writer.writerow(c.transo())
        
print(f"Les données on été entrée dans le fichier {filename}")

#Fonction pour trier les contacts 

def tri_contact(contacts, critere='nom'):
    if critere == "nom":
        return sorted(contacts, key=lambda contact: contact.nom)
    elif critere == 'prenom':
        return sorted(contacts, key=lambda contact: contact.prenom)
    elif critere == "adresse":
        return sorted(contacts, key=lambda contact: contact.adresse)
    elif critere == "num_telephone":
        return  sorted(contacts, key=lambda contact: contact.num_telephone)
    else :
        return "Aucun critère n'est bon"
    
contact_tri = tri_contact(contacts, critere="prenom")

for i in  contact_tri:
    print('Les contacts ont été trié')



