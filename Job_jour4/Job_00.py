#!/usr/bin/python
# -*- coding: utf-8 -*-

N = int(input("Tapez un chiffre positif: "))

def factorielleDe(N):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    if N < 0:
        return "Veuillez entrer un nombre positif svt! "


    elif N < 1:
        return 1
    else:
        return N * factorielleDe(N - 1)

print(factorielleDe(N))