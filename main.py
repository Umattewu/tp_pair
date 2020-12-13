def afficher_message(message):
    tableau_noms = message.split(',')
    if len(message.strip()) == 0:
        return "Hello, my friend"
    elif message.isupper() == 1:
        return str("HELLO, ") + str(message) + str("!")
    elif len(tableau_noms) == 1:
        return str("Hello, ") + str(tableau_noms[0].title())
    else:
        nom = ""
        nom_en_majuscule = ""
        cpt_maj = 0
        cpt_min = 0
        guests = []
        tableau_entre_sans_doublons = sans_doublon(tableau_noms)

        for mot in tableau_entre_sans_doublons:
            mot = mot.strip()
            if mot[0] != '!':
                if mot.isupper() == 1:
                    nom_en_majuscule = str(". AND HELLO, ") + str(mot) + str(" !")
                    cpt_maj += 1
                else:
                    cpt_min += 1
                    if mot == tableau_entre_sans_doublons[-1] and len(nom) > 1:
                        nom = str(nom) + str(" and ") + str(mot.title())
                    elif mot[0] == '*':
                        guests.append(mot[1:].title())
                    else:
                        nom = str(nom) + str(", ") + str(mot.title())

        if len(guests) == 1:
            nom = str(nom) + str(" and our special guest ") + str(guests[0].title())
        if "yoda" in tableau_entre_sans_doublons:
            return message_yoda(cpt_min, cpt_maj, nom)
        if cpt_min > 5:
            return "Hello, world !"
        elif cpt_maj > 5:
            return "HELLO, WORLD !"
        return str("Hello") + str(nom) + str(nom_en_majuscule)

def sans_doublon(tableau_noms):
    tableau_sans_doublon = []
    for mot in tableau_noms:
        mot = mot.strip()
        if tableau_noms.count(mot) > 1:
            mot = str(mot) + str("(x") + str(tableau_noms.count(mot)) + str(")")
        if mot not in tableau_sans_doublon:
            tableau_sans_doublon.append(mot)
    return tableau_sans_doublon

def message_yoda(cpt_min, cpt_maj, nom):
    if cpt_min > 5:
        return "World, Hello !"
    elif cpt_maj > 5:
        return "WORLD, HELLO !"
    return str(nom[2:]) + str(", Hello")