import string
import numpy as np
import matplotlib.pyplot as plt

fichier = open("data.txt",'r')
Data = fichier.read()
alpha = list(string.ascii_letters)
DicoAlpha = {}

for car in Data:
    if car  in alpha :
        if car.lower() not in DicoAlpha:    
            DicoAlpha[car.lower()] = 1
        elif car.lower() in DicoAlpha:
            DicoAlpha[car.lower()] += 1


TotaLetters = sum(list(DicoAlpha.values()))
P_Dico = {}
for letter in DicoAlpha:
    P_Dico[letter] = DicoAlpha[letter] / TotaLetters * 100

#print(P_Dico)
x1 = sorted(list(P_Dico.keys()))
y2 = list(P_Dico.values())

plt.bar(x1,y2,width= 0.8)
plt.ylabel('Pourcentage de recurrence / car')
plt.xlabel('lettre ou car')
plt.suptitle('poucentage d"apparition de chaque lettre')

plt.show() 