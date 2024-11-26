import re

def lire_fichier(fichier):
    try:
        with open(fichier, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def ecrire_fichier(fichier, contacts):
    with open(fichier, "w") as f:
        f.writelines(contacts)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Fonctionnalités principales
def ajouter_contact():
    nom = input("Entrez le nom : ").strip()
    prenom = input("Entrez le prénom : ").strip()
    email = input("Entrez l'adresse email : ").strip()

    while not is_valid_email(email):
        print("Adresse email invalide. Veuillez réessayer.")
        email = input("Entrez l'adresse email : ").strip()

    contacts = lire_fichier("contacts.txt")
    for contact in contacts:
        if contact.startswith(nom + ", "):
            print("Ce contact existe déjà.")
            return

    with open("contacts.txt", "a") as fichier:
        fichier.write(f"{nom}, {prenom}, {email}\n")

    print("Contact ajouté avec succès.")

def lire_contacts():
    contacts = lire_fichier("contacts.txt")
    if not contacts:
        print("Aucun contact à afficher.")
        return

    print(f"\n{'Nom':<15} {'Prénom':<15} {'Email'}")
    print("-" * 40)
    for contact in contacts:
        nom, prenom, email = contact.strip().split(", ")
        print(f"{nom:<15} {prenom:<15} {email}")

def trier_contacts():
    contacts = lire_fichier("contacts.txt")
    if not contacts:
        print("Aucun contact à trier.")
        return

    critere = input("Trier par nom, prénom ou email : ").lower()
    index = {"nom": 0, "prenom": 1, "email": 2}.get(critere, 0)
    contacts.sort(key=lambda x: x.split(", ")[index])

    ecrire_fichier("contacts.txt", contacts)
    print("Contacts triés avec succès.")

def compter_contacts():
    contacts = lire_fichier("contacts.txt")
    print(f"Il y a {len(contacts)} contacts dans le fichier.")

def rechercher_contact():
    nom = input("Entrez le nom à rechercher : ").strip().lower()
    contacts = lire_fichier("contacts.txt")

    for contact in contacts:
        if contact.lower().startswith(nom):
            nom, prenom, email = contact.strip().split(", ")
            print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
            return

    print("Aucun contact trouvé avec ce nom.")

def modifier_contact():
    nom = input("Entrez le nom du contact à modifier : ").strip()
    contacts = lire_fichier("contacts.txt")

    for i, contact in enumerate(contacts):
        if contact.lower().startswith(nom.lower()):
            prenom = input("Entrez le nouveau prénom : ").strip()
            email = input("Entrez la nouvelle adresse email : ").strip()

            while not is_valid_email(email):
                print("Adresse email invalide. Veuillez réessayer.")
                email = input("Entrez la nouvelle adresse email : ").strip()

            contacts[i] = f"{nom}, {prenom}, {email}\n"
            ecrire_fichier("contacts.txt", contacts)
            print("Contact modifié avec succès.")
            return

    print("Aucun contact trouvé avec ce nom.")

def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer : ").strip()
    contacts = lire_fichier("contacts.txt")

    confirm = input(f"Êtes-vous sûr de vouloir supprimer {nom} ? (oui/non) : ").strip().lower()
    if confirm != "oui":
        print("Suppression annulée.")
        return

    with open("contacts.txt", "w") as fichier:
        for contact in contacts:
            if not contact.lower().startswith(nom.lower()):
                fichier.write(contact)

    print("Contact supprimé avec succès.")

# Menu principal
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

        choix = input("Entrez votre choix : ").strip()

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
