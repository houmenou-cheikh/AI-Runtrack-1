import string

def newWord():
    
    oldWord = input("Veuillez saisir un nouveau mot: ")
    alphabet = list(string.ascii_lowercase)
    dicoAlphabet = {}
    InvDicoAphabet = {}
    for postion, letter in enumerate(alphabet):
        dicoAlphabet[letter] = postion
        InvDicoAphabet[postion] = letter

    listeNewWord = []
    listeOfoldWord = oldWord.split(" ")
    for lettre in oldWord:
        if len(listeOfoldWord)> 1 or lettre not in alphabet:
            oldWord = input("**Ce mot contient un caractere incorrecte,Veuillez saisir un seul mot**: ")

        else:
            listeNewWord.append(dicoAlphabet[lettre])
        
    NewWord = ''           
    listeOrdonnee = sorted(listeNewWord)
    for pos in listeOrdonnee:
        NewWord = NewWord + InvDicoAphabet[pos]

    print(NewWord)


newWord()