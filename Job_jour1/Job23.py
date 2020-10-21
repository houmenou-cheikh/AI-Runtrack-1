
def tracerUnRectangle(width, heigth):

    for elt in range(width):
        if elt == 0:
            print("|"+ heigth * "-" + "|")
        elif elt == width-1:
            print("|"+ heigth *"-" + "|")
        else:
            print("|"+heigth* ' '+"|")

width = int(input("Donnez la valeur de votre largeur: "))
heigth = int(input("Donnez la valeur de votre longueur: ")) 

tracerUnRectangle(width,heigth)


