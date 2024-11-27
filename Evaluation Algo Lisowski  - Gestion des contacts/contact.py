# import Regex
import re

# Fonctions pour lire et écrire dans le fichier
# Gestion des erreurs 

def lire_fichier(fichier):
    """
    Lit le contenu d'un fichier et retourne les lignes sous forme de liste.
    Si le fichier n'existe pas ou une erreur survient, retourne une liste vide.
    """
    try:
        with open(fichier, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Fichier non trouvé : {fichier}. Retour d'une liste vide.")
        return []
    except IOError as e:
        print(f"Erreur de lecture du fichier {fichier} : {e}")
        return []

def ecrire_fichier(fichier, contacts):
    """
    Écrit une liste de contacts dans le fichier en remplaçant son contenu.
    Gère les erreurs d'écriture.
    """
    try:
        with open(fichier, "w") as f:
            f.writelines(contacts)
    except IOError as e:
        print(f"Erreur d'écriture dans le fichier {fichier} : {e}")

def is_valid_email(email):
    """
    Vérifie si une adresse email est valide à l'aide d'une expression régulière. Merci Regex.
    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Fonction pour ajouter un nouveau contact
def ajouter_contact():
    """
    Ajoute un contact dans le fichier après vérification des doublons et validation de l'email.
    Gère les erreurs liées à l'entrée utilisateur.
    """
    try:
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
    except Exception as e:
        print(f"Erreur lors de l'ajout du contact : {e}")

# Fonction pour lire et afficher tous les contacts
def lire_contacts():
    """
    Affiche tous les contacts présents dans le fichier de manière formatée.
    Gère les erreurs de lecture.
    """
    try:
        contacts = lire_fichier("contacts.txt")
        if not contacts:
            print("Aucun contact à afficher.")
            return
        
        for contact in contacts:
            nom, prenom, email = contact.strip().split(", ")
            print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
    except Exception as e:
        print(f"Erreur lors de l'affichage des contacts : {e}")

# Fonction pour trier les contacts
def trier_contacts():
    """
    Trie les contacts alphabetiquement, par nom, prénom ou email selon le choix de l'utilisateur.
    Gère les erreurs de tri et d'écriture.
    """
    try:
        contacts = lire_fichier("contacts.txt")
        if not contacts:
            print("Aucun contact à trier.")
            return

        critere = input("Trier alphabetiquement par nom, prénom ou email : ").lower()
        index = {"nom": 0, "prenom": 1, "email": 2}.get(critere, 0)
        contacts.sort(key=lambda x: x.split(", ")[index])

        ecrire_fichier("contacts.txt", contacts)
        print("Contacts triés avec succès.")
    except Exception as e:
        print(f"Erreur lors du tri des contacts : {e}")

# Fonction pour compter le nombre de contacts
def compter_contacts():
    """
    Compte et affiche le nombre de contacts présents dans le fichier.
    """
    try:
        contacts = lire_fichier("contacts.txt")
        print(f"Il y a {len(contacts)} contacts dans le fichier.")
    except Exception as e:
        print(f"Erreur lors du comptage des contacts : {e}")

# Fonction pour rechercher un contact par nom
def rechercher_contact():
    """
    Recherche un contact par nom de manière insensible à la casse.
    Gère les erreurs de format ou de lecture.
    """
    try:
        nom = input("Entrez le nom à rechercher : ").strip().lower()
        contacts = lire_fichier("contacts.txt")

        if not contacts:
            print("Le fichier de contacts est vide.")
            return

        for contact in contacts:
            if contact.lower().startswith(nom):
                nom, prenom, email = contact.strip().split(", ")
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
                return

        print("Aucun contact trouvé avec ce nom.")
    except ValueError as e:
        print(f"Erreur lors de la lecture des contacts : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

# Fonction pour modifier un contact
def modifier_contact():
    """
    Permet de modifier les informations d'un contact existant.
    Gère les erreurs d'entrée utilisateur et d'écriture.
    """
    try:
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
    except Exception as e:
        print(f"Erreur lors de la modification du contact : {e}")

# Fonction pour supprimer un contact
def supprimer_contact():
    """
    Supprime un contact du fichier après confirmation.
    Gère les erreurs de suppression.
    """
    try:
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
    except Exception as e:
        print(f"Erreur lors de la suppression du contact : {e}")

# Menu principal
def main():
    while True:
        try:
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
        except Exception as e:
            print(f"Une erreur inattendue est survenue : {e}")

# Exécution du programme principal
if __name__ == "__main__":
    main()

# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attribué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python contact.py
