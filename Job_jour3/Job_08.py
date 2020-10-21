import string
import numpy as np
import matplotlib.pyplot as plt


fichier = open("data.txt",'r')
Data = fichier.read()
listeTaille = {}

ListeMots = Data.replace("*","").split()
for mot in ListeMots:
    if len(mot) not in listeTaille:
        listeTaille[len(mot)] = 1
    else:
        listeTaille[len(mot)] += 1

#print(listeTaille)
x1 = list(listeTaille.keys())
y2 = list(listeTaille.values())

plt.bar(x1,y2,width=0.7)
plt.ylabel('Pourcentage de recurrence / car')
plt.xlabel('lettre ou car')
plt.suptitle('poucentage d"apparition de chaque lettre')

plt.show() 
