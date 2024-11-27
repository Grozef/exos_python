def ajouter_contact():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    email = input("Entrez l'adresse email : ")

    with open("contacts.txt", "a") as fichier:
        fichier.write(f"{nom}, {prenom}, {email}\n")

    print("Contact ajouté avec succès.")

if __name__ == "__main__":
    ajouter_contact()
