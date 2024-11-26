# 5 Algorithme de Luhn
# Hans Peter Luhn est un informaticien et ingénieur germano-américain qui a développé cet
# algorithme lors de son passage chez IBM dans les années 1950.
# L'algorithme de Luhn est utilisé pour vérifier divers numéros d'identification, par exemple les
# numéros des cartes de crédits, les codes-barres (exemple ISBN) ou encore les numéros de
# sécurité sociale. Voici comment il fonctionne :
# On démarre avec le dernier chiffre (à droite) et on se déplace vers la gauche, en doublant la valeur
# de tous les chiffres de rang pair : le dernier (c'est-à-dire la clef) est traité en 1er, il n'est pas doublé,
# l'avant-dernier (2e

# ) sera doublé. Si le double d'un chiffre dépasse 9, on le remplace par la somme

# de ses chiffres.
# Ainsi, sur les positions paires, les chiffres (0;1;2;3;4;5;6;7;8;9) deviennent (0;2;4;6;8;1;3;5;7;9)
# Par exemple, 1 111 devient 2 121, tandis que 8 763 devient 7 733 (car 2×6=12, et 1+2=3 ; 2×8=16, et
# 1+6=7) ;
# On additionne ensemble tous les chiffres du nombre ainsi obtenu. Par exemple, 1111 devient 2121
# dont la somme donne 6 (2+1+2+1) ; tandis que 8763 devient 7733 et 7+7+3+3 donne alors 20 ;
# Si le total est un multiple de 10 (le chiffre des unités est un zéro), alors le nombre est valide, en
# accord avec la formule de Luhn. Sinon il est invalide. Ainsi, 1 111 n'est pas valide (comme montré
# ci-dessus, il aboutit à 6), tandis que 8 763 est valide (comme montré ci-dessus, il aboutit à 20).

# Page 3 sur 4
# Pour déterminer le chiffre de contrôle ajouté à la fin du numéro, calculer la somme comme décrit
# ci-dessus, deux cas de figure se présentent alors :
#  Si la somme est un multiple de 10, le chiffre de contrôle final est égal à 0 ;
#  Si la somme n'est pas un multiple de 10, modifier le dernier chiffre pour obtenir un multiple de
# 10, soit 10 - (somme % 10) où somme % 10 désigne le reste de la division entière de la somme
# calculée par 10 (ce qui revient à ne garder que le chiffre des unités).
# (Source Wikipedia)
# Exercice à réaliser
# L’exercice à réaliser consiste à demander la saisie d’un numéro de carte bancaire (16 positions
# sans espaces) et ensuite vérifier si le numéro saisi est valide ou non.
def luhn_check(card_number):
    # Convertir le numéro de carte en une liste de chiffres
    digits = [int(digit) for digit in card_number]
    print(f"Chiffres initiaux: {digits}")

    # Doubler les chiffres de rang pair (en partant de la droite)
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = (digits[i] // 10) + (digits[i] % 10)
        print(f"Après doublage et ajustement: {digits}")

    # Additionner tous les chiffres
    total_sum = sum(digits)
    print(f"Somme totale: {total_sum}")

    # Vérifier si le total est un multiple de 10
    return total_sum % 10 == 0

# Demander à l'utilisateur de saisir un numéro de carte bancaire
card_number = input("Entrez un numéro de carte bancaire (16 chiffres sans espaces): ")

# Vérifier la longueur du numéro de carte
if len(card_number) == 16 and card_number.isdigit():
    if luhn_check(card_number):
        print("Le numéro de carte est valide.")
    else:
        print("Le numéro de carte est invalide.")
else:
    if len(card_number) < 16:
        print(f"Le numéro de carte doit contenir exactement 16 chiffres sans espaces. Vous avez saisi {len(card_number)} chiffres. Il manque {16 - len(card_number)} chiffres.")
    else:
        print(f"Le numéro de carte doit contenir exactement 16 chiffres sans espaces. Vous avez saisi {len(card_number)} chiffres. Il y a {len(card_number) - 16} chiffres en trop.")



# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attibué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python luhn.py