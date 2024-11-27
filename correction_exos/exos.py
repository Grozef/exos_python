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

# Exercices Sequence 3 - Correction Python

# -1-

# print("Calculette")
# resultat = float(input("Saisir un nombre : "))
# while True:
#     operation = str(input("Saisir une operation : + - * / ou 'stop' pour arreter "))
#     while operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != 'stop':
#         print("Saisie incorrecte")
#         operation = str(input("Saisir une operation : + - * / ou stop pour arreter "))
#     if operation == 'stop':
#         break
#     else:
#         n = float(input("Saisir un nombre : "))
#         if operation == '/':
#             while n == 0:
#                 print("0 non admis - Ressaisir : ")
#                 n = float(input("Saisir un nombre : "))
#             resultat = resultat / n
#         elif operation == '+':
#             resultat = resultat + n
#         elif operation == '-':
#             resultat = resultat - n
#         else:
#             resultat = resultat * n
#         print("Le resultat est :", resultat)


# -2-

# print("Tri - Bubble Sort")
 
# def tri_a_bulles(tableau):
#     l = len(tableau)
#     # Je lis tous les eléments du tableau
#     for i in range(l):
#         for j in range(0, l-i-1):
#             # On echange les elements si l'element lu est superieur au suivant
#             if tableau[j] > tableau[j+1] :
#                 tableau[j], tableau[j+1] = tableau[j+1], tableau[j]

# # Soit le tableau suivant
# tableau = [63, 23, 15, 69, 8, 5, 22, 33, 99, 97]

# l = len(tableau)
# print ("Le tableau initial est :")
# for i in range(l):

#     print (tableau[i])

# tri_a_bulles(tableau)

# print ("Le tableau apres le tri a bulles est devenu : ")
# for i in range(l):
#     print (tableau[i])


# -3-

# 1ere version

# # Factorielle simple
# def factorielle(v): 
#     if v < 0: 
#         print("La factorielle d'un nombre negatif n'existe pas")
#     elif v == 0: 
#         return 1
#     else: 
#         f = 1
#         while(v > 1): 
#             f *= v 
#             v -= 1
#         return f

# # Algorithme principal
# v = int(input("Saisir un entier : "))
# print("La factorielle de",v,"est", factorielle(v))

# 2eme version

# # Factorielle recursive
# def factorielle(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorielle(n-1)

# # Algorithme principal
# v = int(input("Saisir un entier : "))
# print("La factorielle de",v,"est", factorielle(v)) 

# -4-

# 1ere version

# nb = int(input("Saisir le nombre d'entiers a afficher : "))
# a = 0
# b = 1
# total = 0

# print("Les", nb, "premiers entiers de la suite de Fibonacci sont :")
# for n in range(nb):
#   print(total, end = " ")
#   a = b
#   b = total
#   total = a + b

# 2eme version

# nb = int(input("Saisir le nombre d'entiers a afficher : "))

# def fibonacci_recursive(n):
#    if n <= 1:
#        return n
#    else:
#        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)

# # Algorithme principal
# print("Les", nb, "premiers entiers de la suite de Fibonacci sont :")
# for i in range(nb):
#     print(fibonacci_recursive(i), end = " ")

# -5-

# Luhn CB

# def verif_carte(numero_carte):
#     # On transforme le numero de la carte saisie en un tableau d'entiers
#     tableau = [int(i) for i in str(numero_carte)]

#     # On parcourt le tableau de droite a gauche en partant de l'avant dernier chiffre
#     for i in range(len(tableau) - 2, -1, -2):
#         tableau[i] *= 2
#         if tableau[i] > 9:
#             tableau[i] -= 9

#     # len(tableau) - 2 : valeur de depart de la sequence
#     # len(tableau) donne la longueur du tableau
#     # len(tableau) - 2 enleve 2 a cette longueur
#     # donc on commence a l'indice correspondant a l'avant-dernier element du tableau
#     # 
#     # -1 : valeur de fin de la sequence
#     # la sequence se termine avant d'atteindre l'indice -1
#     # donc elle s'arrête juste avant le premier element du tableau
#     # 
#     # -2 : c'est le pas de la sequence, c'est-a-dire l'increment entre chaque 
#     # element de la sequence. En specifiant -2, on itere sur chaque deuxieme 
#     # indice en partant de l'avant-dernier jusqu'au premier.

#     # On calcule la somme des chiffres
#     total = sum(tableau)

#     # La carte est valide si la somme des chiffres est un multiple de 10
#     return total % 10 == 0

# # Exemple d'utilisation
# # carte_valide = verif_carte("4532015112830366")
# carte_saisie = int(input("Saisir votre numero de carte bancaire : "))
# carte_valide = verif_carte(carte_saisie)
# if carte_valide:
#     print("La carte bancaire est valide.")
# else:
#     print("La carte bancaire n'est pas valide.")

# Luhn ISBN

# def verif_isbn(isbn):
#     # On supprime les eventuels tirets
#     isbn = isbn.replace('-', '')

#     # On verifie si la longueur est correcte
#     if len(isbn) != 13:
#         return False

#     # On convertir le numero ISBN en un tableau d'entiers
#     tableau = [int(i) for i in isbn]

#     # On appliquer l'algorithme de Luhn en doublant chaque deuxieme chiffre
#     for i in range(0, len(tableau), 2):
#         tableau[i] *= 2

#     # On calcule la somme des chiffres
#     total = sum(tableau)

#     # On verifie si le total est un multiple de 10
#     return total % 10 == 0

# # Exemple
# #isbn = "978-3-16-148410-0"
# isbn = "978-2-416-01545-8"
# if verif_isbn(isbn):
#     print("Le numero ISBN est valide")
# else:
#     print("Le numero ISBN n'est pas valide")

# # La fonction verif_isbn prend en entree un numero ISBN-13 sous forme d'une
# # chaîne de caracteres. Elle supprime les tirets eventuels puis verifie si 
# # la longueur # du numero est correcte (13 chiffres). 
# # Ensuite, elle applique l'algorithme de Luhn, en doublant chaque deuxieme chiffre,
# # et verifie si le total est un multiple de 10. 
# # Si c'est le cas, la fonction retourne True, indiquant que le numero ISBN-13 
# # est valide selon l'algorithme de Luhn, sinon elle retourne False.

# -6-

# 1ere version

# def decalage(c,k):
#     # decale une lettre majuscule. Les autres caracteres ne sont pas modifies
#     car = ord(c.upper())
#     car += k
#     while car > 90:
#         car -= 26
#     while car < 65:
#         car += 26
#     return chr(car)

# def cesar(message,d,crypte):
#     # effectue le decalage d sur les caracteres de message
#     chiffre=''
#     for c in message:
#         if crypte:
#             chiffre += decalage(c,d)
#         else:
#             chiffre += decalage(c,-d)

#     return chiffre

# # Algorithme principal
# texte = str(input("Saisir un texte : "))
# decal = int(input("Saisir un decalage : "))
# # Je transforme le message
# print("Message : ")
# texte_code = cesar(texte,decal,True)
# print(texte_code)
# # Je reviens au message d'origine
# texte_decode = cesar(texte_code,decal,False)
# print("Message d'origine : ")
# print(texte_decode)

# 2eme version

# def chiffre_de_cesar(message, decalage):
#     resultat = ""

#     for lettre in message:
#         if lettre.isalpha():  # Verifier si la lettre est alphabetique
#             if lettre.isupper():
#                 resultat += chr((ord(lettre) + decalage - 65) % 26 + 65)
#             else:
#                 resultat += chr((ord(lettre) + decalage - 97) % 26 + 97)
#         else:
#             resultat += lettre

#     return resultat

# # Exemple d'utilisation
# message_original = "Bonjour, ceci est un exemple de chiffre de Cesar!"
# decalage = 3

# message_chiffre = chiffre_de_cesar(message_original, decalage)
# print("Message original:", message_original)
# print("Message chiffre:", message_chiffre)

# 3eme version

# #!/usr/bin/env python3 
# # coding: utf-8 
  
# # Fonction de chiffrement/dechiffrement 
# def cesar(msg="", clef=0): 
# 	alphabet="abcdefghijklmnopqrstuvwxyz" 
# 	chiffre="" 
  
# 	# On prend chaque lettre du mot (converti en minuscules) 
# 	for l in msg.lower(): 
# 		# On recherche la position de la lettre dans l'alphabet 
# 		pos=alphabet.find(l) 
  
# 		# Si la lettre est presente 
# 		if pos != -1: 
# 			# On recupere la lettre decalee dans l'alphabet (on boucle si depassement) 
# 			chiffre+=alphabet[(pos+clef) % len(alphabet)] 
# 		else: 
# 			# Sinon on prend la lettre originelle 
# 			chiffre+=l 
# 		# if 
# 	# for 
# 	return chiffre 
# # cesar() 
  
# message="Hello World !!!" 
# chiffre=cesar(message, 5) 
# dechiffre=cesar(chiffre, -5) 
# print(message, "=>", chiffre, "=>", dechiffre)

# -7-

# # fonction de recherche dichotomique appelee dans le corps principal de l'algorithme
# def recherche_dichotomique(e, tableau):
# 	milieu = 0
# 	debut = 0
# 	fin = len(tableau) - 1
	
# 	while debut <= fin:

# 		# on fait une division entiere pour ne pas avoir un milieu de tableau au format float
# 		milieu = (debut + fin) // 2

# 		# 1ere hypothese : x est superieur a l'element milieu du tableau
# 		# on se positionne dans la partie superieure du tableau par rapport a la variable milieu
# 		if tableau[milieu] < e:
# 			debut = milieu + 1

# 		# 2eme hypothese : x est inferieur a l'element milieu du tableau
# 		# on se positionne dans la partie inferieure du tableau par rapport à la variable milieu
# 		elif tableau[milieu] > e:
# 			fin = milieu - 1

# 		# x est dans le tableau a la position milieu
# 		else: 
# 			return milieu

# 	# x ne se trouve pas dans le tableau
# 	return -1

# # algorithme principal
# tableau = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print (tableau)
# e = int(input("Saisir un entier : "))

# retour = recherche_dichotomique(e, tableau)

# if retour != -1:
# 	print(e, "est present dans le tableau - Position ", retour + 1)
# else:
# 	print(e, "ne se trouve pas dans le tableau")