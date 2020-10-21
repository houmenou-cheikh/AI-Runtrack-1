def drawTriangle(heigth):

    for elt in range(heigth):
        if  elt < heigth-1: 
            print((heigth-elt)*" "+ "/"+ 2*elt*" " + '\\')
        else :
            print(" /"+(2*heigth-2)* '_'+"\\")


drawTriangle(10)