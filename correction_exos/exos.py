## sequence 1

# Saisie des variables
v1 = int(input("Saisissez la première variable (v1) : "))
v2 = int(input("Saisissez la deuxième variable (v2) : "))

# Affichage des valeurs avant inversion
print("Avant inversion:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Inversion des valeurs
v1, v2 = v2, v1

# Affichage des valeurs après inversion
print("Après inversion:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Saisie du montant HT et du taux de TVA
montant_HT = float(input("Saisissez le montant HT : "))
taux_TVA = float(input("Saisissez le taux de TVA (en %) : "))

# Calcul de la TVA
TVA = montant_HT * (taux_TVA / 100)

# Calcul du montant TTC
montant_TTC = montant_HT + TVA

# Affichage des résultats
print(f"Montant HT : {montant_HT} €")
print(f"Montant de la TVA : {TVA} €")
print(f"Montant TTC : {montant_TTC} €")

# Saisie de la note
note = float(input("Saisissez la note sur 20 : "))

# Conversion de la note en lettre
if note <= 5:
    lettre = "E"
elif note <= 8:
    lettre = "D"
elif note <= 11:
    lettre = "C"
elif note <= 14:
    lettre = "B"
else:
    lettre = "A"

# Affichage du résultat
print(f"La note {note} correspond à la lettre {lettre}")

# Saisie de la quantité de produits et du prix unitaire
quantite = float(input("Saisissez la quantité de produits : "))
prix_unitaire = float(input("Saisissez le prix unitaire HT : "))

# Calcul du montant total HT
montant_HT = quantite * prix_unitaire

# Application de la remise
if montant_HT < 200:
    remise = 2.5
elif montant_HT < 400:
    remise = 5
elif montant_HT < 700:
    remise = 7.5
else:
    remise = 10

# Montant après remise
montant_remise = montant_HT * (1 - remise / 100)

# Calcul de la TVA
TVA = montant_remise * 0.20

# Calcul du montant TTC
montant_TTC = montant_remise + TVA

# Affichage des résultats
print(f"Montant HT : {montant_HT} €")
print(f"Remise : {remise}%")
print(f"Montant après remise : {montant_remise} €")
print(f"Montant de la TVA : {TVA} €")
print(f"Montant TTC : {montant_TTC} €")

# Saisie de la consommation en minutes
minutes = float(input("Saisissez votre consommation habituelle en minutes : "))

# Calcul du coût pour chaque offre
offre_1 = 10 + 0.05 * minutes
offre_2 = 20 + 0.02 * minutes

# Affichage de l'offre la plus avantageuse
if offre_1 < offre_2:
    print(f"L'offre la plus avantageuse est l'offre 1 : {offre_1} €")
else:
    print(f"L'offre la plus avantageuse est l'offre 2 : {offre_2} €")

# Saisie du nombre de photocopies
photocopies = int(input("Saisissez le nombre de photocopies : "))

# Calcul du coût en fonction du nombre de photocopies
if photocopies <= 10:
    facture = photocopies * 0.1
elif photocopies <= 20:
    facture = 10 * 0.1 + (photocopies - 10) * 0.08
elif photocopies <= 50:
    facture = 10 * 0.1 + 10 * 0.08 + (photocopies - 20) * 0.06
else:
    facture = 10 * 0.1 + 10 * 0.08 + 30 * 0.06 + (photocopies - 50) * 0.03

# Affichage du montant de la facture
print(f"Le montant de la facture est : {facture} €")

# Saisie du prix unitaire
prix = float(input("Saisissez le prix unitaire du produit : "))

# Calcul du nouveau prix en fonction du pourcentage d'augmentation
if prix < 20:
    nouveau_prix = prix * 1.10
elif prix < 50:
    nouveau_prix = prix * 1.075
elif prix < 100:
    nouveau_prix = prix * 1.05
else:
    nouveau_prix = prix * 1.025

# Affichage du nouveau prix
print(f"Le nouveau prix unitaire est : {nouveau_prix} €")

# Saisie de la quantité de produits
quantite = int(input("Saisissez la quantité de produits : "))

# Choix du mode de livraison
livraison = input("Choisissez le mode de livraison (rapide ou normal) : ").lower()

# Calcul du délai de livraison
if quantite < 50:
    délai = 2 if livraison == "rapide" else 4
elif quantite < 100:
    délai = 3 if livraison == "rapide" else 5
else:
    délai = 5 if livraison == "rapide" else 7

# Affichage du délai
print(f"Le délai de livraison est : {délai} jours")

# Saisie des deux dates
jour1 = int(input("Saisissez le jour de la première date : "))
mois1 = int(input("Saisissez le mois de la première date : "))
annee1 = int(input("Saisissez l'année de la première date : "))

jour2 = int(input("Saisissez le jour de la deuxième date : "))
mois2 = int(input("Saisissez le mois de la deuxième date : "))
annee2 = int(input("Saisissez l'année de la deuxième date : "))

# Comparaison des dates
date1 = (annee1, mois1, jour1)
date2 = (annee2, mois2, jour2)

if date1 > date2:
    print("La première date est la plus récente.")
else:
    print("La deuxième date est la plus récente.")

# Exercices Sequence 1 - Correction Python

# -1-

# print ("Inversion du contenu de deux variables")
# v1 = input("Saisir une premiere variable : ")
# print ("v1 vaut :", v1)
# v2 = input("Saisir une deuxieme variable : ")
# print ("v2 vaut :", v2)
# v3 = v1
# v1 = v2
# v2 = v3
# print ("Apres inversion :")
# print ("v1 vaut :", v1)
# print ("v2 vaut :", v2)

# -2-

# print ("Calcul TVA et TTC")
# ht = float(input("Saisir un montant HT : "))
# print ("ht vaut :", ht)
# taux = float(input("Saisir un taux de TVA : "))
# print ("taux vaut :", taux)
# tva = ht * (taux / 100)
# print ("Le montant de la TVA vaut : ", round(tva,2)) 
# ttc = ht + tva
# print ("Le montant TTC vaut : ", round(ttc,2))

# -3-

# print ("La note devient une lettre")
# note = float(input("Saisir la note : "))
# print ("La note saisie est : ", note)
# if note <=  5:
# 	print ("La lettre est : E")
# elif note <= 8:
# 	print ("La lettre est : D")
# elif note <= 11:
# 	print ("La lettre est : C")
# elif note <= 14:
# 	print ("La lettre est : B")
# else: print ("La lettre est : A")

# -4-

# print ("Calcul HT et Remises")
# qte = float(input("Saisir une quantite: "))
# print ("La quantite vaut :", qte)
# pu = float(input("Saisir un prix unitaire : "))
# print ("Le taux vaut :", pu)
# print ("Le prix unitaire vaut :", pu)
# ht = qte * pu
# print ("Le montant HT vaut : ", ht) 
# if ht < 200:
#     print ("Remise 2.5 %")
#     ht = ht * 0.975
# elif ht < 400:
#     print ("Remise 5 %")
#     ht = ht * 0.95
# elif ht < 700:
#     print ("Remise 7.5 %")
#     ht = ht * 0.925
# else: 
#     print ("Remise 10 %")
#     ht = ht * 0.9
# print ("Le montant HT apres remise vaut : ", round(ht,2))
# print ("Le montant de TVA vaut : ", round(ht * 0.2,2))
# print ("Le montant TTC vaut : ", round(ht * 1.2,2))


# -5-

# print ("Offres Telephoniques")
# conso = int(input("Saisir votre consommation en heures : "))
# print ("La consommation vaut :", conso)
# if (10 + conso*0.5) < (20 + conso * 0.2):
# 	print ("Il faut choisir l offre 1")
# elif (10 + conso*0.5) > (20 + conso * 0.2):
# 	print ("Il faut choisir l offre 2")
# else: print ("Les deux offres sont equivalentes")

# -6-

# print ("Calcul du prix des photocopies")
# nb = int(input("Saisir votre nombre de photocopies : "))
# print ("Le nombre de photocopies vaut : ", nb)
# if nb <=  10:
# 	prix = nb * 0.1
# elif nb <= 20:
# 	prix = (10 * 0.1) + (nb - 10) * 0.08
# elif nb <= 50:
# 	prix = (10 * 0.1) + (10 * 0.08) + (nb - 20) * 0.06
# else: prix = (10 * 0.1) + (10 * 0.08) + (30 * 0.06) + (nb - 50) * 0.03
# print ("Le prix est : ", round(prix,2))

# -7-

# print ("Algorithme Augmentation des tarifs")
# pu = float(input("Saisir un prix unitaire: "))
# if pu < 20:
#     pu = pu * 1.1
# elif pu < 50:
#     pu = pu * 1.075
# elif pu < 100:
#     pu = pu * 1.05
# else:
#     pu = pu * 1.025
# print ("Le nouveau prix est : ", pu)

# -8-

# print ("Algorithme Delais de livraison")
# qte = int(input("Saisir une quantite : "))
# mode = str(input("Saisir un mode de livraison : rapide ou normal --> "))
# if mode == "rapide":
#     if qte < 50:
#         delai = 2
#     elif qte < 100:
#         delai = 3
#     else:
#         delai = 5
# else:
#     if qte < 50:
#         delai = 4
#     elif qte < 100:
#         delai = 5
#     else:
#         delai = 7
# print ("Le delai de livraison est de", delai, "jours")

# -9-

# print("Algorithme Comparer deux dates")
# j1 = int(input("Saisir le jour de la premiere date : "))
# m1 = int(input("Saisir le mois de la premiere date : "))
# a1 = int(input("Saisir l'annee de la premiere date : "))
# j2 = int(input("Saisir le jour de la deuxieme date : "))
# m2 = int(input("Saisir le mois de la deuxieme date : "))
# a2 = int(input("Saisir l'annee de la deuxieme date : "))

# if a1 < a2:
#     print("La date 1 est la plus ancienne")
# elif a1 > a2:
#     print("La date 2 est la plus ancienne")
# else:
#     if m1 < m2:
#         print("La date 1 est la plus ancienne")
#     elif m1 > m2:
#         print("La date 2 est la plus ancienne")
#     else:
#         if j1 < j2:
#             print("La date 1 est la plus ancienne")
#         elif j1 > j2:
#             print("La date 2 est la plus ancienne")
#         else:
#             print("Les 2 dates sont identiques")
          
          
## sequence deux

# Tableau déjà rempli de 5 entiers
tableau = [1, 2, 3, 4, 5]

# Afficher le contenu du tableau du dernier au premier
for i in range(len(tableau) - 1, -1, -1):
    print(tableau[i])

# Initialiser un tableau vide pour stocker 10 entiers
tableau = []

# Saisir 10 entiers et les ranger dans le tableau
for i in range(10):
    entier = int(input(f"Entrez l'entier {i + 1}: "))
    tableau.append(entier)

# Afficher le tableau pour vérification
print("Tableau rempli:", tableau)

# Constituer une table de multiplication de 9 par 9
table_multiplication = []

for i in range(1, 10):
    ligne = []
    for j in range(1, 10):
        ligne.append(i * j)
    table_multiplication.append(ligne)

# Afficher la table de multiplication
for ligne in table_multiplication:
    print(ligne)

# Tableau de 10 entiers
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inverser les valeurs contenues dans le tableau
for i in range(len(tableau) // 2):
    tableau[i], tableau[len(tableau) - 1 - i] = tableau[len(tableau) - 1 - i], tableau[i]

# Afficher le tableau inversé
print("Tableau inversé:", tableau)

##  Correction sequence deux
# - 1 -

# print ("Affichage du contenu d'un tableau de 5 entiers du dernier au premier element")
# tableau = [17, 22, 9, 23, 63]
# print ("Affichage dans l'ordre")
# for i in range(0, 5, 1):
#     print(tableau[i])
# print ("Affichage dans l'ordre inverse")
# for i in range(4, -1, -1):
#     print(tableau[i])

# - 2 -

# print("Remplir un tableau de 10 entiers")
# tableau=[]
# for i in range(10):
#     tableau.append(int(input("Saisir un entier : ")))
#     print(tableau[i])
# print(tableau)

# - 3 -

# print ("Affichage de la table de multiplication de 9 par 9")
# for i in range(1,10):
#     for j in range(1,10):
#         print(i * j)
#         if j == 9:
#            print("\n")

# - 4 -

# # Inverser le contenu d'un tableau : version 1, passer par une variable intermeediaire
# tableau = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
# for i in range(0, 5):
#   v = tableau[i]
#   tableau[i] = tableau[10 - i - 1]
#   tableau[10 - i - 1] = v

# print(tableau)# Inverser le contenu d'un tableau : version 2
# tableau = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
# longueur = len(tableau) - 1
# tableau_inverse = []
# while (longueur >= 0):
#   tableau_inverse.append(tableau[longueur])
#   longueur = longueur - 1
# print(tableau_inverse)

# # Inverser le contenu d'un tableau : version 3
# tableau = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
# longueur = len(tableau) - 1
# tableau_inverse = []
# tableau_inverse = tableau[::-1]
# print(tableau_inverse)

# # Inverser le contenu d'un tableau : version 4
# tableau = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
# longueur = len(tableau) - 1
# tableau_inverse = []
# tableau_inverse = list(reversed(tableau))
# print(tableau_inverse)

# # Inverser le contenu d'un tableau : version 5
# tableau = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
# longueur = len(tableau) - 1
# tableau_inverse = []
# tableau_inverse = [num for num in reversed(tableau)]
# print(tableau_inverse)



## sequence trois  
            
def calculette():
    resultat = float(input("Entrez un nombre: "))
    while True:
        operateur = input("Entrez l'opérateur (+, -, *, /) ou 'q' pour quitter: ")
        if operateur == 'q':
            break
        if operateur in ['+', '-', '*', '/']:
            nombre = float(input("Entrez un autre nombre: "))
            if operateur == '+':
                resultat += nombre
            elif operateur == '-':
                resultat -= nombre
            elif operateur == '*':
                resultat *= nombre
            elif operateur == '/':
                if nombre != 0:
                    resultat /= nombre
                else:
                    print("Erreur: division par zéro.")
                    continue
            print("Résultat: ", resultat)
        else:
            print("Opérateur invalide.")

def tri_a_bulles():
    tableau = [64, 34, 25, 12, 22, 11, 90, 45, 77, 54]
    n = len(tableau)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
    print("Tableau trié: ", tableau)

tri_a_bulles()

def factorielle_boucle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

def factorielle_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorielle_recursive(n - 1)
def fibonacci_boucle(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def luhn(num):
    num = [int(i) for i in str(num)]
    check_sum = 0
    for i in range(len(num)-1, -1, -1):
        if (len(num) - i) % 2 == 0:
            double = num[i] * 2
            if double > 9:
                check_sum += double - 9
            else:
                check_sum += double
        else:
            check_sum += num[i]
    return check_sum % 10 == 0

def verifier_numero(num):
    if luhn(num):
        print("Numéro valide")
    else:
        print("Numéro invalide")

# Exemple : verifier_numero(8763)

def chiffre_de_cesar(message, decalage, sens):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in message:
        if char.isalpha():
            index = alphabet.index(char.lower())
            if sens == 'avant':
                index = (index + decalage) % 26
            else:
                index = (index - decalage) % 26
            if char.isupper():
                result += alphabet[index].upper()
            else:
                result += alphabet[index]
        else:
            result += char
    return result

message = input("Entrez votre message : ")
decalage = int(input("Entrez le décalage : "))
sens = input("Entrez le sens (avant ou arrière) : ")
print(chiffre_de_cesar(message, decalage, sens))

def recherche_dichotomique(tab, target):
    gauche, droite = 0, len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tab[milieu] == target:
            return milieu
        elif tab[milieu] < target:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1

def tester_recherche():
    tab = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    target = int(input("Entrez un nombre à rechercher: "))
    resultat = recherche_dichotomique(tab, target)
    if resultat != -1:
        print(f"L'élément est trouvé à l'index {resultat}.")
    else:
        print("L'élément n'est pas dans le tableau.")

tester_recherche()

