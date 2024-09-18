# exercice 1

# positif = input("Entre un nombre positif : ")
# print(positif)
# rayon = int(positif) * int(positif)

# Exercice 2

# positifUn = input("Entre un nombre positif : ")
# positifDeux = input("Entre un deuxième nombre positif : ")
# perimetre = int(positifUn) * int(positifDeux)
# print(perimetre)

#Exercice 3

# lequel = input("Entre True / False : ")
# if lequel == 'True':
#     print('False')
# elif lequel == 'False':
#     print('True')

#Exercice 4

# chiffre1 = int(input("Veuiller entre un chiffre : "))
# chiffre2 = int(input("Veuiller entre un second chiffre : "))

# if chiffre1 == chiffre2:
#     print('True')
# elif chiffre1 != chiffre2:
#     print('False')

# Exercice 5

# chiffre1 = int(input("Entre un chiffre plus grand : "))
# chiffre2 = int(input("Entre un chiffre plus petit : "))

# print(chiffre1 > chiffre2)

# Exercice 6 
 
#6.1 

# chif1 = 1 
# chif2 = float(12.2)
# add = chif1 + chif2
# print(add)

# L'addition est possible et se passe sans soucis 

# chif1 = float(15.698)
# chif2 = 15
# add = chif1 + chif2
# print(add)

# L'addition se fait également sans soucis 

#6.2 

# str1 = 'Test'
# str2 = 'Test2'
# addition = str1 + str2
# print(addition)

#L'addition des deux string sont possible elles se suiveront sans espace (Test1Test2)

#6.3

# a = 2
# b = "Je m'appelle groute"
# add = a+b
# print(add)

#L'addition ne se fait pas car on ne peut addition une chaine de caractère et un entier

# ---------------- Structure de controle -------------------

# Exo 1

# age = int(input("Entre votre age : "))
# ageMinimum = 18
# if age >= ageMinimum:
#     print("Majeur")
# elif age < ageMinimum:
#     print("Mineur")

#Exo 2 

# pair = int(input("Veuillez entrer un chiffre : "))
# if pair % 2 == 0:
#     print("Pair")
# else :
#     print("Impair")

#Exo 3

# Initialisation de la somme des valeurs positives
# somme = 0

# while True:
#     # Demande à l'utilisateur d'entrer une valeur
#     valeur = float(input("Entrez une valeur positive (ou 0 pour afficher la somme, ou une valeur négative pour quitter) : "))
    
#     # Vérifie si la valeur est négative
#     if valeur < 0:
#         print("Erreur : Valeur négative détectée. Le programme s'arrête.")
#         break
    
#     # Vérifie si la valeur est zéro
#     elif valeur == 0:
#         print(f"La somme des nombres encodés est : {somme}")
#         break
    
#     # Sinon, la valeur est positive
#     else:
#         somme += valeur

#Exercice 4

# Demande à l'utilisateur d'entrer un nombre
# a = float(input('Entrer un chiffre : '))

# # Initialisation du compteur
# nbreFoisDivi2 = 0

# # Continue tant que 'a' est plus grand que 1
# while a > 1:
#     a /= 2          # Divise 'a' par 2
#     nbreFoisDivi2 += 1  # Incrémente le compteur

# # Affiche le nombre de fois que l'on a divisé par 2
# print(nbreFoisDivi2)

#Exercice 5

# n = int(input("Veuillez entrez un nombre entier : "))
# if n**2:
#     print(n**2)
# else:
#     print('le nombre ne peut pas être calculé')

# Exercice 6

# n = int(input("Veuillez entrer un nombre positif : "))
# for i in range(1, n+1):
#     print((str(i)+ " ")* i)


