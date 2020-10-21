saisi = input("veuillez saisir votre texte: ")

MyFile = open("output.txt","a")
MyFile.write(saisi)
