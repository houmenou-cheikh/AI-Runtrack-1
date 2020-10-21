from random import *

def noteArrondie(listeDeNotes):

    print("oldList: ",listeDeNotes)
    for i,note in enumerate(listeDeNotes):
        deuxChiffre = int(note[1])
        if deuxChiffre >= 3 and deuxChiffre < 5:         
            print("oldNote: " ,note)
            newNote=note.replace(str(deuxChiffre),'5') 
            print("newNote",newNote)
            listeDeNotes.pop(i)
            listeDeNotes.insert(i,newNote)

        UnChiffre = int(note[0])
        if deuxChiffre >= 8 and deuxChiffre <= 9:         
            print("oldNote: ", note)
            FirstChiffre= UnChiffre+1
            
            newNote=str(FirstChiffre)+'0'
            print("newNote: ",newNote)
            listeDeNotes.pop(i)
            listeDeNotes.insert(i,newNote)
    print("NewList: ", listeDeNotes)            
   


noteArrondie(["81",'88','89','83','82','84','86','87','85'])