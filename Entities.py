import pygame as pg             # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

"""
# Charger la spritesheet
spritesheet = pg.image.load('Sprite/spritesheet.png')

# Classe pour les sprites
# Il y a un problème avec le découpage de la spritesheet
class Sprite:
    # Définir la largeur et la hauteur de chaque sprite
    largeur_sprite = 32
    hauteur_sprite = 32

    # Fonction pour découper la spritesheet
    def decouper_spritesheet(spritesheet, largeur_sprite, hauteur_sprite):
        sprites = []
        sheet_rect = spritesheet.get_rect()
        for y in range(0, sheet_rect.height, hauteur_sprite):
            for x in range(0, sheet_rect.width, largeur_sprite):
                rect = pg.Rect(x, y, largeur_sprite, hauteur_sprite)
                sprite = spritesheet.subsurface(rect)
                sprites.append(sprite)
        return sprites

    # Découper la spritesheet en sous-images
    sprites = decouper_spritesheet(spritesheet, largeur_sprite, hauteur_sprite)

image = Sprite.sprites[1]
"""
# Charger l'image
# image = pg.image.load('Sprite/pacman.png')

class Entity(pg.sprite.Sprite):

    # Méthode pour afficher l'entité
    def Affichage(self, screen):

        # Position où l'image sera dessinée
        position = (self.x, self.y)

        # Dessiner l'image sur la surface
        screen.blit(self.sprite , position)

        # Mettre à jour l'affichage
        pg.display.flip()

    # Méthode pour savoir si l'entité est sur une case
    def Position(self):
        if self.x % 36 == 0 and self.y % 36 == 0:
            return True
        else:
            return False
    
    # Méthode pour déplacer l'entité
    # A modifier après tests (la valeur 1)
    def Mouvement(self, vitesse, direction, screen):
        self.direction = direction
        if self.direction == 'HAUT':
            self.y -= vitesse
        elif self.direction == 'BAS':
            self.y += vitesse
        elif self.direction == 'GAUCHE':
            self.x -= vitesse
            if self.x < 0:
                self.x = screen.get_width() - 36
        elif self.direction == 'DROITE':
            self.x += vitesse
            if self.x >= screen.get_width():
                self.x = 0
    
    def get_position(self):
        return self.y // 36 , self.x // 36
    
    # Gestion des collisions
    def Collision(self, entity):
        if self.rect.colliderect(entity.rect):
            return True

    def stop(self):
        self.x = self.x // 36 * 36
        self.y = self.y // 36 * 36
        
    # Constructeur de la classe
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = pg.image.load(sprite)
        #self.rect = self.sprite.get_rect()

        super().__init__()
