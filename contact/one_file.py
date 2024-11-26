def ajouter_contact():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    email = input("Entrez l'adresse email : ")

    with open("contacts.txt", "a") as fichier:
        fichier.write(f"{nom}, {prenom}, {email}\n")

    print("Contact ajouté avec succès.")

def lire_contacts():
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        for contact in contacts:
            nom, prenom, email = contact.strip().split(", ")
            print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

def trier_contacts():
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        contacts.sort(key=lambda x: x.split(", ")[0])

        with open("contacts.txt", "w") as fichier:
            fichier.writelines(contacts)

        print("Contacts triés avec succès.")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

def compter_contacts():
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        print(f"Il y a {len(contacts)} contacts dans le fichier.")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

def rechercher_contact():
    nom = input("Entrez le nom à rechercher : ")
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        for contact in contacts:
            if contact.startswith(nom):
                nom, prenom, email = contact.strip().split(", ")
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
                return

        print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

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

def main():
    while True:
        print("\nMenu:")
        print("1. Ajouter un contact")
        print("2. Lire les contacts")
        print("3. Trier les contacts")
        print("4. Compter les contacts")
        print("5. Rechercher un contact")
        print("6. Modifier un contact")
        print("7. Supprimer un contact")
        print("8. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            lire_contacts()
        elif choix == "3":
            trier_contacts()
        elif choix == "4":
            compter_contacts()
        elif choix == "5":
            rechercher_contact()
        elif choix == "6":
            modifier_contact()
        elif choix == "7":
            supprimer_contact()
        elif choix == "8":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
