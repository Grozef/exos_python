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

if __name__ == "__main__":
    trier_contacts()
