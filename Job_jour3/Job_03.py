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

ListeMots = Data.split()

tailleMot = int(input('Veuillez renseigner la taille de votre mot: '))

nbr_mot = 0
for mot in ListeMots:
    if len(mot) == tailleMot:
        nbr_mot += 1
print("il y'a ",nbr_mot, " de taille",tailleMot)