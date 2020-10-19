def orderBy():

    listeChiffres = []
    while len(listeChiffres) < 5:
        chiffre = int(input("veuillez saisir un chiffre Svp: "))
        listeChiffres.append(chiffre)
        listeChiffres.sort()
    else:
        for chiffre in listeChiffres:
            print(chiffre)

orderBy()