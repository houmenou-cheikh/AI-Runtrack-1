import xml.etree.ElementTree as ET
import re

MyFile = open("domains.xml","r")
contenu = MyFile.read()
x = re.findall("w{3}\..*\..{3}", contenu)

tree = ET.parse('domains.xml')
root = tree.getroot()

listeExtension = []
for elt in root.iter("column"):
    if "." in elt.text:
        listeExtension.append(elt.text)


print(len(listeExtension) + len(x))

