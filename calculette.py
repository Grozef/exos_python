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
        
def calculette():
    print("Bienvenue dans la calculatrice !")
    print("Vous pouvez effectuer des opérations arithmétiques de base.")
    print("Entrez un premier nombre puis la touche entrée, ensuite choisissez un opérateur (+, -, *, /) et la touche entrée, enfin un autre nombre et la touche entrée. Vous pouvez rebondir sur le résultat pour continuer les opérations. La division par 0 n'est pas possible. ")
    print("Pour quitter, entrez 'q' à la place de l'opérateur.")

    try:
        resultat = float(input("Entrez un nombre: "))
    except ValueError:
        print("Erreur: veuillez entrer un nombre valide.")
        return

    print("Résultat initial: ", resultat)

    while True:
        operateur = input("Entrez l'opérateur (+, -, *, /) ou 'q' pour quitter: ")
        if operateur == 'q':
            print("Calcul terminé.")
            break
        if operateur in ['+', '-', '*', '/']:
            try:
                nombre = float(input("Entrez un autre nombre: "))
            except ValueError:
                print("Erreur: veuillez entrer un nombre valide.")
                continue

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
                    print("Erreur: division par zéro petit malin, cela n'est pas possible ici, merci de recommencer.")
                    continue
            print("Résultat: ", resultat)
        else:
            print("Opérateur invalide.")

# Appel auto
if __name__ == "__main__":
    calculette()


# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attibué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python calculette.py
