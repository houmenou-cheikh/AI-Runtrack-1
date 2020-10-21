# coding: utf-8
import re
MyFile = open("domains.xml","r")
contenu = MyFile.read()
compteur = 0

x1 = re.findall(">.*\..?\.?.{3}", contenu)
for elt in x1:
    if elt[-1] != "<":
        compteur += 1
        #print(elt[1:])
    else:
        #print(elt[1:-1])
        compteur += 1

x2 = re.findall("w{3}\..*\..{3}", contenu)
for elt in x2:
    compteur += 1

print(compteur)