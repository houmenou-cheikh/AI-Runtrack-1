import string

fichier = open("data.txt",'r')
Data = fichier.read()
DataLow = Data.lower()
alpha = list(string.ascii_lowercase) 

for car in DataLow:
    if car not in alpha and car != " ":
            DataLow.replace(car,"")

ListeMots = DataLow.split()
dicoLs = {}
for l in alpha :
    dicoLs[l] = {l:0} 

print(dicoLs)

