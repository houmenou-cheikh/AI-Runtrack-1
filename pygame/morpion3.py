import time
import pygame
from pygame.locals import *
import sys
import random

###################  creer la fenetre du plateau  ######################
pygame.init()
fenetre = pygame.display.set_mode((648,604), RESIZABLE)
pygame.display.set_caption("***\__Jeu de Morpion__/***")
debut = pygame.image.load("home0.png").convert()
fenetre.blit(debut, (0,0))
pygame.display.flip()

####################  rajouter une option aide  ########################
 
def besoinAide():
  help = pygame.image.load("help.png").convert()
  fenetre.blit(help, (0,0))
  pygame.display.flip()
  
  while True:
    for event in pygame.event.get():                  				#demande d'aide avec bouton	
      if event.type==KEYDOWN:
        pageAccueil()
        
      if event.type==MOUSEBUTTONDOWN:								#demande d'aide avec la souris
        if event.button == 1:
          pageAccueil()
          
####################  definition de la page d accueil  #################

def pageAccueil():
  """la page d'accueil du jeu"""
	
  debut = pygame.image.load("home0.png").convert()
  fenetre.blit(debut, (0,0))
  pygame.display.flip()
  
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
        
      elif event.type == MOUSEBUTTONDOWN:					#si on clic sur le bouton de la souris
        if event.button == 1:								#si c'est le bouton gauche de la souris
          if 425 < event.pos[1]:							#si le curseur de la souris se trouve en desous de la position 488 de la fenetre
            besoinAide()									#ouvrir la page aide 
            
          elif 425 > event.pos[1]:							#commencer le jeu en appyant sur n'import quel bouton
            game()											#faire appel a la fonction jouerAuMorpion
        
################## les conditions existant pour gagner ################
def gagnant(b):
  if b[0]==b[1]==b[2] and b[0]!=0:							#alignements horizonteaux
    l=b[0]
    return l
  if b[3]==b[4]==b[5] and b[3]!=0:
    l=b[3]
    return l
  if b[6]==b[7]==b[8] and b[6]!=0:
    l=b[6]
    return l
  if b[0]==b[3]==b[6] and b[0]!=0:							#alignements verticaux
    l=b[0]
    return l
  if b[1]==b[4]==b[7] and b[1]!=0:
    l=b[1]
    return l
  if b[2]==b[5]==b[8] and b[2]!=0:
    l=b[2]
    return l
  if b[0]==b[4]==b[8] and b[4]!=0:							#aligement sur les diagonaux
    l=b[4]
    return l
  if b[2]==b[4]==b[6] and b[4]!=0:
    l=b[4]
    return l
  if b[0]!=0 and b[1]!=0 and b[2]!=0 and b[3]!=0 and b[4]!=0 and b[5]!=0 and b[6]!=0 and b[7]!=0 and b[8]!=0:
    return 3
  return 0


def Tjrs_gagnant(b):
  if (b[0]==b[1]== 1 or b[0]==b[1]== 2) and b[2]==0:							#alignements horizonteaux
    l= 3
    return l
  elif (b[2]==b[1]== 1 or b[2]==b[1]== 2) and b[0]==0:							#alignements horizonteaux
    l= 1
    return l
  elif (b[3]==b[4]== 1 or b[3]==b[4]== 2) and b[5]==0:
    l=6
    return l
  elif (b[5]==b[4]== 1 or b[5]==b[4]== 2) and b[3]==0:
    l=4
    return l
  elif (b[6]==b[7]== 1 or b[6]==b[7]== 2) and b[8]==0:
    l=9
    return l
  elif (b[8]==b[7]== 1 or b[8]==b[7]== 2) and b[6]==0:
    l=7
    return l
  elif (b[0]==b[3]== 1 or b[0]==b[3]== 2) and b[6]==0:							#alignements verticaux
    l=7
    return l
  elif (b[6]==b[3]== 1 or b[6]==b[3]== 2) and b[0]==0:							#alignements verticaux
    l=1
    return l
  elif (b[1]==b[4]== 1 or b[1]==b[4]== 2) and b[7]==0:
    l=8
    return l
  elif (b[7]==b[4]== 1 or b[7]==b[4]== 2) and b[1]==0:
    l=2
    return l
  elif (b[2]==b[5]== 1 or b[2]==b[5]== 2) and b[8]==0:
    l=9
    return l
  elif (b[8]==b[5]== 1 or b[8]==b[5]== 2) and b[2]==0:
    l=3
    return l
  elif (b[0]==b[4]== 1 or b[0]==b[4]== 2) and b[8]==0:							#aligement sur les diagonaux
    l=9
    return l
  elif (b[8]==b[4]== 1 or b[8]==b[4]== 2) and b[0]==0:							#aligement sur les diagonaux
    l=1
    return l
  elif (b[2]==b[4]== 1 or b[2]==b[4]== 2) and b[6]==0:
    l=7
    return l
  elif (b[6]==b[4]== 1 or b[6]==b[4]== 2) and b[2]==0:
    l=3
    return l
    
  elif (b[0]==b[2]== 1 or b[0]==b[2]== 2) and b[1]==0:
    l=2
    return l
  elif (b[3]==b[5]== 1 or b[3]==b[5]== 2) and b[4]==0:
    l=5
    return l
  elif (b[6]==b[8]== 1 or b[6]==b[8]== 2) and b[7]==0:
    l=8
    return l
  elif( b[6]==b[0]== 1 or b[6]==b[0]== 2) and b[3]==0:
    l=4
    return l
  elif( b[7]==b[1]== 1 or b[7]==b[1]== 2) and b[4]==0:
    l=5
    return l
  elif (b[8]==b[2]== 1 or b[8]==b[2]== 2) and b[5]==0:
    l=6
    return l
  elif (b[0]==b[8]== 1 or b[0]==b[8]== 2) and b[4]==0:
    l=5
    return l
  elif (b[6]==b[2]== 1 or b[6]==b[2]== 2) and b[4]==0:
    l=5
    return l

  return 100
#######################  joueur humain  ##############################
def J1_joue(localCase):
    croix = pygame.image.load("croix.png").convert()
    fenetre.blit(croix, localCase)
    pygame.display.flip()
 
#########################  joueur AI  ################################

def AI_joue(localCase):
    croix = pygame.image.load("Rond.png").convert()
    fenetre.blit(croix, localCase)
    pygame.display.flip()
    
#######################  game function  ##############################
  
def game():
     fond = pygame.image.load("plateauDuJeu.png").convert()
     fenetre.blit(fond, (0,0))
     tcroix = pygame.image.load("tcroix.png").convert()
     fenetre.blit(tcroix, (595,540))
     pygame.display.flip()
     
     background=[0,0,0,0,0,0,0,0,0]
     caseVide = {1:(40,360),2:(236,360),3:(435,360),4:(40,183),5:(236,183),6:(435,183),7:(40,15),8:(236,15),9:(435,15)}
     caseForcing = {1:(40,360),2:(236,360),3:(435,360),4:(40,183),5:(236,183),6:(435,183),7:(40,15),8:(236,15),9:(435,15)}
     J1 = 1
     case = 0
     
     while True:
      g=gagnant(background)
      if g==1:
          gcroix = pygame.image.load("gcroix.png").convert()
          fenetre.blit(gcroix, (200,542))
          pygame.display.flip()
          time.sleep(1)
          menu = pygame.image.load("menu.png").convert()
          fenetre.blit(menu, (190,200))
          pygame.display.flip()

          while True:
            for event in pygame.event.get():
              if event.type==KEYDOWN:
                if event.key == K_KP0:
                  pageAccueil()										#revenir a la page d'accueil
                  
                if event.key == K_KP1:								#recommencer le Jeu
                  game()
                  
              if event.type == QUIT:
                  pygame.quit()

      if g==2:
          grond = pygame.image.load("grond.png").convert()
          fenetre.blit(grond, (200,542))
          pygame.display.flip()
          time.sleep(1)
          menu = pygame.image.load("menu.png").convert()
          fenetre.blit(menu, (190,200))
          pygame.display.flip()
          
          while True:
            for event in pygame.event.get():
              if event.type==KEYDOWN:
                if event.key == K_KP0:
                  pageAccueil()
                if event.key == K_KP1:
                  game()
                  
              if event.type == QUIT:
                  pygame.quit()
      	 
      for event in pygame.event.get():                  				#demande d'aide avec bouton	
         if event.type == QUIT:
           pygame.quit()
           sys.exit()
            
         if J1 == 1 and event.type==KEYDOWN:
           tcroix = pygame.image.load("tcroix.png").convert()
           fenetre.blit(tcroix, (580,542))
           pygame.display.flip()  
           if event.key == K_KP1:
             case = 1
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
           
           if event.key == K_KP2:
             case = 2
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
             
           if event.key == K_KP3:
             case = 3
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
           
           if event.key == K_KP4:
             case = 4
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
             
           if event.key == K_KP5:
             case = 5
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
             
           if event.key == K_KP6:
             case = 6
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
             
           if event.key == K_KP7:
             case = 7
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
             
           if event.key == K_KP8:
             case = 8
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
             
           if event.key == K_KP9:
             case = 9
             try:
               J1_joue(caseVide[case])
               del caseVide[case]
               background[case-1] = 1
               J1 = 2
             except:
               pass
  ###########################  IA Game  #############################           
         elif J1 == 2 :

           if list(caseVide.keys()) != []:
             trond = pygame.image.load("trond.png").convert()				#joueur Numero 2
             fenetre.blit(trond, (580,542))
             pygame.display.flip()
             time.sleep(0.5)
             choice_IA = Tjrs_gagnant(background)
             
             if choice_IA != 100 and choice_IA in list(caseVide.keys()):
               AI_joue(caseVide[choice_IA])
               del caseVide[choice_IA]
               background[choice_IA -1] = 2
               J1 = 1

             elif choice_IA != 100:
               AI_joue(caseForcing[choice_IA])
               background[choice_IA -1] = 2
               J1 = 1 
             else:
               if background[4] == 0:
                 AI_joue(caseVide[5])
                 del caseVide[5]
                 background[4] = 2
                 J1 = 1	
               else:		
                 AI_choice = random.choice(list(caseVide.keys()))
                 AI_joue(caseVide[AI_choice])
                 del caseVide[AI_choice]
                 background[AI_choice -1] = 2
                 J1 = 1

             
           elif list(caseVide.keys()) == []:   
             egalite = pygame.image.load("egalite.png").convert()
             fenetre.blit(egalite, (230,542))
             blanc = pygame.image.load("blanc.png").convert()
             fenetre.blit(blanc, (580,542))
             pygame.display.flip()
             time.sleep(1)
             menu = pygame.image.load("menu.png").convert()
             fenetre.blit(menu, (190,200))
             pygame.display.flip()
          
             while True:
               for event in pygame.event.get():
                 if event.type==KEYDOWN:
                   if event.key == K_KP0:
                     pageAccueil()
                  
                   if event.key == K_KP1:
                     game()

                 if event.type == QUIT:
                   pygame.quit() 
			 

#########################  quitter le jeu  ###########################
for event in pygame.event.get():
       if event.type == QUIT:
          pygame.quit()
          sys.exit()
 

# GO Play 
pageAccueil()
