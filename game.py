import pygame
from pygame.locals import *

from classes import *

#CONFIGURATION

pygame.init()
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
icone = pygame.image.load(icone_fenetre)
pygame.display.set_icon(icone)

# JEU

background = pygame.image.load(sprite_background)

monNiveau = Niveau(niveau1)
monNiveau.generer()

monPersonnage = Personnage()

continuer = True

while continuer:

    fenetre.blit(background, (0,0))
    monNiveau.afficher(fenetre)

    monPersonnage.deplacer(monNiveau)
    monPersonnage.afficher(fenetre)

    if monPersonnage.position == "a":
        print("VOUS AVEZ GAGNER")
        continuer = False

    # RAFRAICHISSEMENT
    pygame.display.flip()