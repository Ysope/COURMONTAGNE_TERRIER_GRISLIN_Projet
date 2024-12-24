import pygame as pg
from Entities import Entity
from Graphe import m_graphe

class PACMAN(Entity):

    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.super = False

    # Mouvement de Pacman
    def tester_deplacement(self, direction):
        position = self.get_position()
        x, y = position

        if (x, y) in m_graphe and m_graphe[(x, y)][1][direction] is not None:
            return True

        return False



#Disparition des points si pacman mange un point

# Les cerises (mange cerise -> nbr de points + 100pts) (NIVEAU 1)

# Les pastèques (mange pastèque -> nbr de points + 500pts)

# Les fraises (mange fraise -> nbr de points + 300pts)

# Les PacGum (mange PacGum -> nbr de points + 10pts)
# Les Super PacGum (mange super PacGum -> nbr de points + 50pts et appel de la classe fantome transformé)

# Les fantômes (mange fantôme -> nbr de points 1er fantome + 200pts, 2ème + 400pts, 3ème + 800pts, 4ème + 1600pts
# et appel de la classe fantome Disparition)

# Next_input : on stocke la prochaine direction que le joueur veut prendre