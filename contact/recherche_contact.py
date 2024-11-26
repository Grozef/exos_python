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

if __name__ == "__main__":
    rechercher_contact()
