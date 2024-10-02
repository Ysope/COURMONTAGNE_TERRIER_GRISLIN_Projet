import pygame as pg             # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

# Constantes
CHAR_SIZE = 32 # Taille d'une entité

class Entity(pg.sprite.Sprite):

    # Constructeur de la classe
    def __init__(self, ligne, colonne, sprite):
        super().__init__()
        self.abs_x = (ligne * CHAR_SIZE)
        self.abs_y = (colonne * CHAR_SIZE)
        self.image = pg.image.load(sprite)  # Chargement de l'image

# Afficher un rectangle
def Afficher(draw, screen,self):
    draw.rect(screen, (255, 0, 0), (self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE))
