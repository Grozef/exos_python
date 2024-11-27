def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer : ")
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        with open("contacts.txt", "w") as fichier:
            for contact in contacts:
                if not contact.startswith(nom):
                    fichier.write(contact)

        print("Contact supprimé avec succès.")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

if __name__ == "__main__":
    supprimer_contact()
