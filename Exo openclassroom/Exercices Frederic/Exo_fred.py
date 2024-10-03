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


