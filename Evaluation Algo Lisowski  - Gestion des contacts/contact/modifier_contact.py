def modifier_contact():
    nom = input("Entrez le nom du contact à modifier : ")
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        for i, contact in enumerate(contacts):
            if contact.startswith(nom):
                prenom = input("Entrez le nouveau prénom : ")
                email = input("Entrez la nouvelle adresse email : ")
                contacts[i] = f"{nom}, {prenom}, {email}\n"

                with open("contacts.txt", "w") as fichier:
                    fichier.writelines(contacts)

                print("Contact modifié avec succès.")
                return

        print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

if __name__ == "__main__":
    modifier_contact()
