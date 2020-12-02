def affiche_message(message):
    if split_name(message) == "oui":
        tab = message.split(',')
        res = []
        maj = ""
        for mot in tab:
            if mot.isupper() == 1:
                maj = str(". AND HELLO, ") + str(mot) + str(" !")
            else:
               res.append(mot.title())
        for i in range(len(tab)):
            result = ", ".join(res)
        resultat = " and ".join(result)
        return str("Hello, ") + str(resultat) + str(maj)
    else:
        if len(message.strip()) == 0:
            return "Hello, my friend"
        elif(message.isupper()==1):
            return (str("HELLO, ")+str(message)+str("!"))
        return(str("Hello")+str(", ")+str(message.title()))

def split_name(chaine):
    cont = 0
    for lettre in chaine:
        if lettre == ',':
            return "oui"
