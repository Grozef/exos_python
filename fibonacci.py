# 4 Exercice récursivité : la suite de Fibonacci
# Leonardo Fibonacci est un mathématicien italien du XIIIe siècle, célèbre pour avoir introduit en
# Europe le système de numération indo-arabe, incluant le chiffre zéro. Il a joué un rôle majeur dans
# le développement des mathématiques occidentales.
# Également célèbre pour la suite de nombres qui porte son nom, appelée la "suite de Fibonacci".
# Cette suite est définie en commençant par les nombres 0 et 1, et chaque nombre suivant est la
# somme des deux nombres précédents. Ainsi, la suite commence par : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
# et ainsi de suite.
# Cette suite apparaît dans de nombreux phénomènes naturels et a de nombreuses applications en
# mathématiques, en sciences et en informatique.
# Exercice à réaliser
# Faire saisir un entier.
# Calculer la valeur de la suite de Fibonacci au rang de cet entier avec deux méthodes différentes :
#  en utilisant une boucle
#  en utilisant la récursivité

# def fibonacci_boucle(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1

#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

# def fibonacci_recursif(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

# n = int(input("Entrez un entier pour calculer la valeur de la suite de Fibonacci: "))

# resultat_boucle = fibonacci_boucle(n)
# print(f"La valeur de la suite de Fibonacci au rang {n} (boucle) est: {resultat_boucle}")

# resultat_recursif = fibonacci_recursif(n)
# print(f"La valeur de la suite de Fibonacci au rang {n} (récursivité) est: {resultat_recursif}")

def fibonacci_boucle(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursif(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_recursif(n - 1, memo) + fibonacci_recursif(n - 2, memo)
        return memo[n]

n = int(input("Entrez un entier pour calculer la valeur de la suite de Fibonacci: "))

resultat_boucle = fibonacci_boucle(n)
print(f"La valeur de la suite de Fibonacci au rang {n} (boucle) est: {resultat_boucle}")

resultat_recursif = fibonacci_recursif(n)
print(f"La valeur de la suite de Fibonacci au rang {n} (récursivité) est: {resultat_recursif}")

# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attibué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python fibonacci.py
