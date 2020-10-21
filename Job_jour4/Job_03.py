#!/usr/bin/python
# -*- coding: utf-8 -*-

x =  int(input("Tapez un chiffre: "))
n = int(input("saisir la valeur la puissance: "))

def puissance2(x,n):
    
    if n == 0:
        return 1
    else:
        return x * puissance2(x,n - 1)

print(puissance2(x,n))