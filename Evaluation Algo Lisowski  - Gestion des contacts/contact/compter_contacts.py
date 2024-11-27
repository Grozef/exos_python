def compter_contacts():
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = fichier.readlines()

        print(f"Il y a {len(contacts)} contacts dans le fichier.")
    except FileNotFoundError:
        print("Le fichier contacts.txt n'existe pas.")

if __name__ == "__main__":
    compter_contacts()
