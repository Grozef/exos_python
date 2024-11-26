import re

# Fonctions pour lire et écrire dans le fichier
def lire_fichier(fichier):

    """
    Lit le contenu d'un fichier et retourne les lignes sous forme de liste.
    Si le fichier n'existe pas, retourne une liste vide.
    """

    try:
        with open(fichier, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def ecrire_fichier(fichier, contacts):

    """
    Écrit une liste de contacts dans le fichier en remplaçant son contenu.
    """
    with open(fichier, "w") as f:
        f.writelines(contacts)

def is_valid_email(email):
    """
    Vérifie si une adresse email est valide à l'aide d'une expression régulière.
    """

    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Fonction pour ajouter un nouveau contact
def ajouter_contact():
    """
    Ajoute un contact dans le fichier après vérification des doublons et validation de l'email.
    """

    nom = input("Entrez le nom : ").strip()
    prenom = input("Entrez le prénom : ").strip()
    email = input("Entrez l'adresse email : ").strip()

    # Vérifie la validité de l'email
    while not is_valid_email(email):
        print("Adresse email invalide. Veuillez réessayer.")
        email = input("Entrez l'adresse email : ").strip()

    # Vérifie si le contact existe déjà
    contacts = lire_fichier("contacts.txt")
    for contact in contacts:
        if contact.startswith(nom + ", "):
            print("Ce contact existe déjà.")
            return

    # Ajoute le contact dans le fichier
    with open("contacts.txt", "a") as fichier:
        fichier.write(f"{nom}, {prenom}, {email}\n")

    print("Contact ajouté avec succès.")

# Fonction pour lire et afficher tous les contacts
def lire_contacts():

    """
    Affiche tous les contacts présents dans le fichier de manière formatée.
    """

    contacts = lire_fichier("contacts.txt")
    if not contacts:
        print("Aucun contact à afficher.")
        return

    print(f"\n{'Nom':<15} {'Prénom':<15} {'Email'}")
    print("-" * 40)
    for contact in contacts:
        nom, prenom, email = contact.strip().split(", ")
        print(f"{nom:<15} {prenom:<15} {email}")

# Fonction pour trier les contacts
def trier_contacts():

    """
    Trie les contacts par nom, prénom ou email selon le choix de l'utilisateur.
    """

    contacts = lire_fichier("contacts.txt")
    if not contacts:
        print("Aucun contact à trier.")
        return

    # Demande à l'utilisateur le critère de tri
    critere = input("Trier par nom, prénom ou email : ").lower()
    index = {"nom": 0, "prenom": 1, "email": 2}.get(critere, 0)
    contacts.sort(key=lambda x: x.split(", ")[index])

    ecrire_fichier("contacts.txt", contacts)
    print("Contacts triés avec succès.")

# Fonction pour compter le nombre de contacts
def compter_contacts():
    """
    Compte et affiche le nombre de contacts présents dans le fichier.
    """

    contacts = lire_fichier("contacts.txt")
    print(f"Il y a {len(contacts)} contacts dans le fichier.")

# Fonction pour rechercher un contact par nom
def rechercher_contact():

    """
    Recherche un contact par nom de manière insensible à la casse.
    """

    nom = input("Entrez le nom à rechercher : ").strip().lower()
    contacts = lire_fichier("contacts.txt")

    for contact in contacts:
        if contact.lower().startswith(nom):
            nom, prenom, email = contact.strip().split(", ")
            print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
            return

    print("Aucun contact trouvé avec ce nom.")

# Fonction pour modifier un contact
def modifier_contact():
    """
    Permet de modifier les informations d'un contact existant.
    """

    nom = input("Entrez le nom du contact à modifier : ").strip()
    contacts = lire_fichier("contacts.txt")

    for i, contact in enumerate(contacts):
        if contact.lower().startswith(nom.lower()):
            prenom = input("Entrez le nouveau prénom : ").strip()
            email = input("Entrez la nouvelle adresse email : ").strip()

            # Vérifie la validité de l'email
            while not is_valid_email(email):
                print("Adresse email invalide. Veuillez réessayer.")
                email = input("Entrez la nouvelle adresse email : ").strip()

            # Met à jour les informations du contact
            contacts[i] = f"{nom}, {prenom}, {email}\n"
            ecrire_fichier("contacts.txt", contacts)
            print("Contact modifié avec succès.")
            return

    print("Aucun contact trouvé avec ce nom.")

# Fonction pour supprimer un contact
def supprimer_contact():
    """
    Supprime un contact du fichier après confirmation.
    """

    nom = input("Entrez le nom du contact à supprimer : ").strip()
    contacts = lire_fichier("contacts.txt")

    # Demande confirmation à l'utilisateur
    confirm = input(f"Êtes-vous sûr de vouloir supprimer {nom} ? (oui/non) : ").strip().lower()
    if confirm != "oui":
        print("Suppression annulée.")
        return

    # Supprime le contact s'il existe
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

        # Appelle la fonction correspondante en fonction du choix
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

# Exécution du programme principal
if __name__ == "__main__":
    main()



# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attibué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python calculette.py
