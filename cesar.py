def chiffre_de_cesar(message, decalage, sens):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in message:
        if char.isalpha():
            index = alphabet.index(char.lower())
            if sens == 'avant':
                index = (index + decalage) % 26
            else:
                index = (index - decalage) % 26
            if char.isupper():
                result += alphabet[index].upper()
            else:
                result += alphabet[index]
        else:
            result += char
    return result

def dechiffrer_message(message, decalage):
    return chiffre_de_cesar(message, decalage, 'arrière')

def main():
    message = input("Entrez votre message, attention, pas d'accents, de ponctuation ou de caractères spéciaux ! : ")
    decalage = int(input("Entrez le décalage : "))
    sens = input("Entrez le sens (avant ou arrière (n'oubliez pas l'accent !)) : ")

    if sens == 'avant':
        message_chiffre = chiffre_de_cesar(message, decalage, sens)
        print(f"Message chiffré : {message_chiffre}")

        # Demander à l'utilisateur s'il veut déchiffrer le message
        dechiffrer = input("Voulez-vous déchiffrer le message ? (oui/non) : ")
        if dechiffrer.lower() == 'oui':
            message_original = dechiffrer_message(message_chiffre, decalage)
            print(f"Message original : {message_original}")
    elif sens == 'arrière':
        message_dechiffre = chiffre_de_cesar(message, decalage, sens)
        print(f"Message déchiffré : {message_dechiffre}")
    else:
        print("Sens invalide. Veuillez entrer 'avant' ou 'arrière'.")

if __name__ == "__main__":
    main()


# README : 
# lancer le terminal
# allez dans le dossier du script python
# ici : cd C:\Users\fLisowski\Desktop\python -> mettez le chemin vers votre dossier a l'emplacement que vous lui avez attibué
# tapez la commande suivante dans le terminal pour lancer le mini programme
# python cesar.py