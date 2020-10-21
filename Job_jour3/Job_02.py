import string

fichier = open("data.txt",'r')
Data = fichier.read()
alpha = list(string.ascii_letters)
listeCar = []

for car in Data:
    if car not in alpha and car not in listeCar:

        listeCar.append(car)
        if car != " ":
            Data.replace(car,"")

print("liste des caracteres speciaux:\n",listeCar)
ListeMots = Data.split()
print("nombre de mots sans caracteres speciaux: ",len(ListeMots))


""" for mot in ListeMots:
    if mot == " ":
        ListeMots.remove(mot)
print(len(ListeMots))
 """









fichier.close()