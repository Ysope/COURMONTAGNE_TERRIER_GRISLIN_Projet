import pygame as pg             # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 

# Initialiser Pygame
pg.init()

# Créer une surface (par exemple, la fenêtre principale)
screen = pg.display.set_mode((800, 600))



# Variables
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
image = pg.image.load('Sprite/pacman.png')
# Méthode pour afficher les éléments
# Probablement à modifier une fois que les classes Entity seront créées

def Affichage(screen, image):

    # Position où l'image sera dessinée
    position = (100, 100)

    # Dessiner l'image sur la surface
    screen.blit(image, position)

    # Mettre à jour l'affichage
    pg.display.flip()

class Entity(pg.sprite.Sprite):

    # Méthode pour afficher l'entité
    def Affichage(self, screen):

        # Position où l'image sera dessinée
        position = (self.x, self.y)

        # Dessiner l'image sur la surface
        screen.blit(self.sprite , position)

        # Mettre à jour l'affichage
        pg.display.flip()

    # Méthode pour déplacer l'entité
    # A modifier après tests (la valeur 1)
    def Mouvement(self, vitesse):
        self.vitesse = vitesse

        haut = self.y + 1
        bas = self.y - 1
        gauche = self.x - 1
        droite = self.x + 1
        
    # Gestion des collisions
    def Collision(self):
        pass

    # Constructeur de la classe
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite


        super().__init__()

        


# Boucle principale pour garder la fenêtre ouverte
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    

    # Afficher les éléments
    Affichage(screen, image)



# Quitter Pygame
pg.quit()