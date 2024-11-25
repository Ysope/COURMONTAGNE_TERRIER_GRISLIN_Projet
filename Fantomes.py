# TO DO :
# Mouvements (Gérer le comportement des fantômes)

# Nouvelle méthode ou dans méthode Fuite ????
# Disparition (Les fantômes disparaissent (deviennent des yeux) + rentre à la maison)

# Les Super PacGum (Les fantômes deviennent bleus + fuis Pacman)
# Comportement des fantômes
#   Rouge(Blinky) : Plus court chemin vers Pacman + sort par défaut de la maison
#   Rose(Pinky) : Vise 4 cases devant Pacman + sort au bout de .... pts
#   Bleu(Inky) : Comme le Rose mais des fois se déplace à l'opposé de Pacman + sort au bout de .... pts
#   Orange(Clyde) : Déplacement aléatoire + sort au bout de .... pts

import pygame as pg
from pygame.locals import * 
from Entities import Entity
import random

class Fantome(Entity):

    # Méthode qui rends les fantomes bleus et les fait fuir Pacman
    def Fuite(self):
        duree = 6
        # Pour une durée de 6 secondes (remplacer la boucle for c'est pas beau + marche pas)
        for i in range(duree):
            self.sprite = pg.image.load('Sprite/fantome_bleu.png')
            self.vitesse = 9
            self.Mouvement(self.vitesse, self.direction)
        
        if(Collision ==True)
            self.sprite = pg.image.load('Sprite/yeux.png')
 
    
    # Méthode pour déplacer l'entité
    def Mouvement_Fantomes(self, vitesse, direction, position_pacman):
        
        match self.name:
            case 'Blinky':
                return
            case 'Pinky':
                return 
            case 'Inky':
                return
            case 'Clyde':
                # Définir la direction
                self.direction = random.choice(['HAUT', 'BAS', 'GAUCHE', 'DROITE'])
                return super().Mouvement(vitesse, direction)
                
    # Constructeur de la méthode Fantome
    def __init__(self, x, y, sprite, name):

        # Appeler le constructeur de la classe mère
        super().__init__()

        # Définir la vitesse du fantôme (pixels par seconde)
        self.vitesse = 18

        # Définir les noms des fantômes
        self.name = name

        # Définir l'image du fantôme
        self.sprite = pg.image.load('Sprite/fantome.png')