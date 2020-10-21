import string
import numpy as np
import matplotlib.pyplot as plt


fichier = open("data.txt",'r')
Data = fichier.read()
alpha = list(string.ascii_letters)
listeLettres = {}

ListeMots = Data.replace("*","").split()
for mot in ListeMots:
    if (mot[0]).lower() not in listeLettres and mot[0] in alpha :
        listeLettres[(mot[0]).lower()] = 1
    elif mot[0] in alpha:
        listeLettres[(mot[0]).lower()] += 1

#print(listeLettres)
Tot_Occ = sum(list(listeLettres.values()))
P_listeLettres = {}
for letter in listeLettres:
    P_listeLettres[letter] = listeLettres[letter] / Tot_Occ * 100
print(P_listeLettres)

x1 = list(P_listeLettres.keys())
y2 = list(P_listeLettres.values())

plt.bar(x1,y2,width=0.8)
plt.ylabel('Pourcentage de recurrence / car')
plt.xlabel('lettre ou car')
plt.suptitle('poucentage d"apparition de chaque lettre')

plt.show() 
