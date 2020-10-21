import string

def newWord():
    
    oldWord = input("Veuillez saisir un nouveau mot: ")
    halfWord = round(len(oldWord) / 2) 
    socle = oldWord[0:halfWord] 
 
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
            print("**Ce mot contient un caractere incorrecte,Veuillez saisir un seul mot**: ")
            return 1
		
     
    for let in oldWord[halfWord: ]:
         listeNewWord.append(dicoAlphabet[let])
        
    NewWord = ''           
    listeOrdonnee = sorted(listeNewWord)
    for pos in listeOrdonnee:
        NewWord = NewWord + InvDicoAphabet[pos]
    
    NewWord = socle + NewWord
    print('le nouveau mot est:  ',NewWord)


newWord()
