import pygame
from Labyrinthe import Labyrinthe
from Matrice import MATRICE
from Graphe import m_graphe

pygame.init()
screen = pygame.display.set_mode((36*21, 36*22))
labyrinthe = Labyrinthe(screen, 36, 36, MATRICE)
labyrinthe.draw()
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



