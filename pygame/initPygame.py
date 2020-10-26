# pyg0010_bases.py
# Référence : https://openclassrooms.com/courses/interface-graphique-pygame-pour-python/premieres-fenetres
# Premier essais avec Pygame en Python 3
# Gestion d'événements :
# https://openclassrooms.com/courses/interface-graphique-pygame-pour-python/gestion-des-evenements-1
'''
Liste des modules de Pygame :
    display
    mixer   # pour la gestion du son
    draw
    event
    image
    mouse
    time
'''

import pygame
from pygame.locals import *

# Initialisation des modules de Pygame
pygame.init()

# Création d'une fenêtre graphique de Pygame
##fenetre = pygame.display.set_mode((640, 480))

# Permet de rendre la fenêtre de taille ajustable.
fenetre = pygame.display.set_mode((640,480), RESIZABLE)

# Une image pour le fond de la fenêtre
fond = pygame.image.load("images/background_herbe.jpg").convert()
perso1 = pygame.image.load("images/perso_1.png").convert_alpha()

# Ne fonctionne pas !???
perso1.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent


# Affiche l'image dans la fenêtre
fenetre.blit(fond, (0, 0))

# Affiche le personnage au-dessus de l'herbe
fenetre.blit(perso1, (200, 200))

# Actualise la fenêtre
pygame.display.flip()

nPosX = 200 # Position en X de la personne
nPosY = 200 # Position en Y de la personne

pygame.key.set_repeat(400, 30)

# Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

# ================================================
# Boucle principale
while continuer:

    # Boucle sur tous les événements gérés par Pygame
    for event in pygame.event.get():        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # La fenêtre a été fermée ou La touche ESC a été pressée.
            continuer = 0 # Indique de sortir de la boucle.

        if event.type == KEYDOWN:  # KEYUP existe aussi
            if event.key == K_RIGHT: nPosX += 20
            if event.key == K_LEFT: nPosX -= 20
            if event.key == K_UP: nPosY -= 20
            if event.key == K_DOWN: nPosY += 20
            
            fenetre.blit(fond, (0, 0))
            fenetre.blit(perso1, (nPosX, nPosY))

            # Actualise la fenêtre
            pygame.display.flip()

pygame.display.quit() # ferme la fenêtre, c.f. https://www.pygame.org/docs/ref/display.html
pygame.quit() # quitte pygame, c.f. https://www.pygame.org/docs/ref/pygame.html
