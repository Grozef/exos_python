def tri_a_bulles():

    tableau = []
    n = int(input("Choisissez le nombre d'éléments qui vont composer le tableauà trier: "))

    for i in range(n):
        element = int(input(f"Entrez l'élément {i+1}: "))
        tableau.append(element)

    for i in range(n):
        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]

    print("Tableau trié: ", tableau)

# Appel auto
if __name__ == "__main__":
    tri_a_bulles()
    
# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attibué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python tri_a_bulles.py
