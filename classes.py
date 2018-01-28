import pygame
from pygame.locals import *

from constantes import *
from fonctions import *

class Niveau:
    """"Classe du niveau"""

    def __init__(self, fichier):
        """Constructeur"""

        # VARIABLES
        self.fichier = fichier
        self.structure = []

        # SPRITES 
        self.mur = pygame.image.load(sprite_mur).convert()
        self.depart = pygame.image.load(sprite_depart).convert()
        self.arrivee = pygame.image.load(sprite_arrivee).convert_alpha()

    def generer(self):
        """Génère la structure du niveau en fonction du fichier donné"""

        ma_structure = listeDouble(15,15)

        with open(self.fichier, "r") as fichier:
            nb_l = 0
            for ligne in fichier:
                nb_c = 0
                for col in ligne:
                    if col != "\n":
                        ma_structure[nb_c][nb_l] = col
                    nb_c += 1
                nb_l += 1
            self.structure = ma_structure

    def afficher(self, fenetre):
        """Affiche le niveau avec les sprites correcpondants"""

        nb_l = 0

        for ligne in self.structure:

            nb_c = 0
            for col in ligne:

                coord_x = nb_l*taille_sprite
                coord_y = nb_c*taille_sprite

                if col == "d":
                    fenetre.blit(self.depart, (coord_x, coord_y))
                elif col == "a":
                    fenetre.blit(self.arrivee, (coord_x, coord_y))
                elif col == "m":
                    fenetre.blit(self.mur, (coord_x, coord_y))

                nb_c+=1

            nb_l+=1

class Personnage:
    """Classe du personnage jouable"""

    def __init__(self):
        """Constructeur du personnage"""

        # VARIABLES
        self.x = 0
        self.y = 0
        self.position = "d"

        # SPRITES
        self.haut = pygame.image.load(dk_haut)
        self.bas = pygame.image.load(dk_bas)
        self.droite = pygame.image.load(dk_droite)
        self.gauche = pygame.image.load(dk_gauche)
        self.now = self.bas



    def __check(self, niveau):
        """Renvoie les mouvements possibles"""

        can_move = {"haut":False, "bas":False, "droite":False, "gauche":False}

        # HAUT
        if self.y > 0:
            if niveau.structure[self.x][self.y-1] != "m" :
                can_move["haut"] = True

        # BAS
        if self.y < 14:
            if niveau.structure[self.x][self.y+1] != "m":
                can_move["bas"] = True

        # DROITE
        if self.x < 14:
            if niveau.structure[self.x+1][self.y] != "m":
                can_move["droite"] = True

        # GAUCHE
        if self.x > 0:
            if niveau.structure[self.x-1][self.y] != "m":
                can_move["gauche"] = True

        return can_move
    
    def deplacer(self, niveau):
        """Méthode pour déplacer le personnage sur la map"""

        can_move = self.__check(niveau)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP and can_move["haut"]:
                    self.position = niveau.structure[self.x][self.y-1]
                    self.y += -1
                    self.now = self.haut
                elif event.key == K_DOWN and can_move["bas"]:
                    self.position = niveau.structure[self.x][self.y+1]              
                    self.y += 1
                    self.now = self.bas
                elif event.key == K_RIGHT and can_move["droite"]:
                    self.position = niveau.structure[self.x+1][self.y]
                    self.x += 1
                    self.now = self.droite
                elif event.key == K_LEFT and can_move["gauche"]:
                    self.position = niveau.structure[self.x-1][self.y]
                    self.x += -1
                    self.now = self.gauche

    def afficher(self, fenetre):
        """Méthode permettant d'afficher le personnage sur la fenetre"""

        coord_x = self.x * taille_sprite
        coord_y = self.y * taille_sprite

        fenetre.blit(self.now, (coord_x, coord_y))