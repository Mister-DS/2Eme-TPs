#fruits = ['pomme', 'banane', 'orange']
#fruits.append('kiwi')
#fruits.remove('orange')
#fruits[2] = 'ananas'
#print(len(fruits))
#fruits.sort()
#print(fruits)

# nouvelle_campagne = {
#     "responsable_de_campagne": "Jeanne D'arc",
#     "nom_de_campagne": "Campagne nous aimons les chiens",
#     "date_de_debut": "01/01/2024",
#     "influenceur_important": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
# }

# taux_de_conversion = {}
# taux_de_conversion = dict()
# taux_de_conversion['Facebook'] = 3.4
# taux_de_conversion['Twitter'] = 3.3
# taux_de_conversion['Instagram'] = 3.2

# infos_labradoodle = {
#     "poids": "13 à 16 kg",
#     "origine": "États-Unis",
# }
# infos_labradoodle["nom_scientifique"] = "Canis lupus familiaris"
# infos_labradoodle.pop("nom_scientifique")
# infos_labradoodle.get("poids")
# print(infos_labradoodle)

# fruits = { 
#     "pomme": "rouge",
#     "banane": "jaune",
#     "orange": "orange"
# }
# fruits["kiwi"] = "vert"
# couleur_banane = fruits["banane"]
# fruits["pomme"] = 'vert'
# fruits.pop('banane')
# print(fruits)

# copine = "Gwendoline"

# match copine:
#     case "Sarah":
#         print("c'est qui cette pute")
#     case "Michel":
#         print("chuis pas gay frr")
#     case "Gwendoline":
#         print("Ouais c'est bien elle la femme de ma vie")
#     case _:
#         print("T KI ?")

# nombre_a_gauche = 2
# nombre_a_droite = 8
# symbole = "+"
# resultat = 0
#     # Vérifie si les deux nombres sont valides avec la fonction
#     # isinstance (soit un integer, soit un float)
# if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
#         print("Erreur: les deux nombres doivent être des nombres entiers")
# else:
#         nombre_a_gauche = int(nombre_a_gauche)
#         nombre_a_droite = int(nombre_a_droite)

# match symbole:
#     case "-":
#         resultat = nombre_a_droite - nombre_a_gauche
#     case "*":
#         resultat = nombre_a_droite * nombre_a_gauche
#     case "/": 
#         if nombre_a_droite == 0:
#             print("Erreur : impossible de diviser par 0")
#         else:
#             resultat = nombre_a_gauche / nombre_a_droite
#     case "+":
#         resultat = nombre_a_droite + nombre_a_gauche
#     case _:
#         print("Le symbole ne fait partie d'aucune des propositions")
# print(f"Le resultat est : {resultat}")

# for x in range(100):
#     print(f"{x} bouteille de bières")

# for x in range(10):
#     if x == 8:
#         break
#     print(x)

# liste = [1, 2, 3, 4, 5]

# for x in liste:
#     if x == 3:
#         continue
#     print(x)

# liste = input("Saisissez une liste de nombres séparés par des virgules : ")

#     # Séparer l'ensemble des nombres et les insérer dans une liste
# liste = liste.split(",")
#     # Afficher la liste des nombres
# print("Liste des nombres :", liste)

#     # Calculer la somme des nombres
# somme = 0
# for nombre in liste:
#         somme += int(nombre)
# print("Somme des nombres :", somme)

#     # Effectuer la moyenne à l'aide de la somme des nombre
# moyenne = somme / len(liste)
# print("Moyenne des nombres :", moyenne)

#     # Trouver le nombre d'entier supérieur à la moyenne
# nombre_sup_moyenne = 0
# for nombre in liste:
#         if int(nombre) > moyenne:
#             nombre_sup_moyenne += 1
# print("Nombre de nombres supérieurs à la moyenne :", nombre_sup_moyenne)

#     # Trouver le nombre d'entier pair
# nombre_pairs = 0
# i = 0
# while i < len(liste):
#         if int(liste[i]) % 2 == 0:
#             nombre_pairs += 1
#         i += 1
# print("Nombre de nombres pairs :", nombre_pairs)

# def addition(a, b):
#     resultat = a + b
#     print(resultat)

# param1 = 3
# param2 = 7
# addition(param1, param2)  # Affiche 10

# def salaire_mensuel(salaire_annuel):
#     salaire_mensuel = salaire_annuel / 12 
#     print(f"le salaire mensuel est : {salaire_mensuel}")

# salaire_mensuel(44000)

# def salaire_hebdomadaire(salaire_mensuel):
#     salaire_hebdomadaire = salaire_mensuel / 4
#     print(f"le salaire  hebdomadaire est : {salaire_hebdomadaire}")


# salaire_hebdomadaire(42000)

# def salaire_horaire(salaire_hebdomadaire, heure_travaille):
#     salaire_horaire = salaire_hebdomadaire / heure_travaille
#     print(f"le salaire horaire est : {salaire_horaire}")

# salaire_horaire(500, 14)

# def calcul_salaire(salaire_annuel, heures_travaillee):
#     salaire_annuel = input(int("Veuillez entrer votre salaire annuel"))
#     heures_travaillee = input(int("Veuillez entrer le nombre d'heures travaille"))
#     calcul_salaire = salaire_annuel / heures_travaillee
#     print(f"le salaire horaire est : {calcul_salaire}")

# def print_welcome_message():
#     print("Bienvenue sur la mini-calculatrice !")
    
# def input_two_number():
#     num1 = float(input("Entrez le premier nombre : "))
#     num2 = float(input("Entrez le deuxième nombre : "))
#     return num1, num2

# def print_menu_and_get_choice():
#     print("=== MENU ===")
#     print("1. Addition")
#     print("2. Soustraction")
#     print("3. Multiplication")
#     print("4. Division")

#     user_choice = input("Entrez votre choix (1-4) : ")

#     while user_choice not in ["1", "2", "3", "4"]:

#         user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

#     return user_choice

# def sum(a, b):
#     return a + b

# def substraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("Erreur : division par zéro")

# def run_calculation(user_choice):
#     num1, num2 = input_two_number()
#     match user_choice:
#         case '1':
#             result = sum(num1, num2)
#         case '2':
#             result = substraction(num1, num2)
#         case '3':
#             result = multiplication(num1, num2)
#         case '4':
#             result = division(num1, num2)
#         case _:
#             print("Choix invalide.")
#     return result

# if __name__ == '__main__':
#     print_welcome_message()
#     user_choice = print_menu_and_get_choice()
#     result = run_calculation(user_choice)
#     print(result)


# wallet = 5000
# computer_price = 900

# if computer_price <= wallet and computer_price > 1000:
#     wallet -= computer_price
#     print(f'Vous avez bien acheté votre ordinateur et il vous reste {wallet}')
# else:
#     soustraction = computer_price - wallet
#     print(f"Il vous manque {soustraction} € pour acheter l'ordinateur !")

# online_players = ["Graven", "Anana", "Cleymax", "Bob"]
# # modifier un indice ==> graven ==> gravenMax
# online_players[0] = "gravenMax"
# # injecter une valeur 
# online_players.insert(2, "Pendragon")
# #actualiser les personne 2-4
# online_players[2:4] = ["Paul", "Jacques"]
# #si on désire ajouter qqn à la fin de liste / plusieurs 
# online_players.append("Gameurs123")
# online_players.extend(["OnlineGamer", "Richard"])
# #le joueur anana se déconnecte 
# if "Anana" in online_players:
#     online_players.remove("Anana")
# #pour clear la liste 
# # online_players.clear()

# print(online_players)



# Tuples 

"""

(!) Tuple est un container immuable et donc ne peut pas etre modifier !

Création de tuples :

- mon_tuple = () # vide
- mon_tuple = 17, # une seul valeur
- mon_tuple = (17,) # idem
- mon_tuple = (17, 18, 19) # plusieurs valeurs

Accès aux valeurs :

- mon_tuple[x] # valeur d'indice x


2 raisons d'utiliser des tuples : 

- affectation multiple de variable
- retour multiple de fonction 
"""


# 




