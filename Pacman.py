import pygame as pg
from Entities import Entity
from Matrice import MATRICE

class PACMAN(Entity):

    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)


    #Affichage de Pacman sur le plateau
    @staticmethod
    def afficher_pacman(screen):
        # Charger l'image de Pacman
        pacman_image = pg.image.load('pacman.png')

        # Calculer les coordonnées de Pacman en fonction de la matrice
        ligne = 12
        colonne = 10
        taille_cellule = 36
        x = colonne * taille_cellule
        y = ligne * taille_cellule

        # Créer une instance de la classe Entity pour Pacman
        pacman = PACMAN(x, y, pacman_image)

        # Afficher Pacman sur le plateau
        pacman.Affichage(screen)

        # Mettre à jour l'affichage
        pg.display.flip()

        return pacman

    def tester_deplacement(self, direction):
        position = self.get_position()
        x, y = position

        if direction == 'DROITE':
            new_x, new_y = x, y + 1
        elif direction == 'GAUCHE':
            new_x, new_y = x, y - 1
        elif direction == 'HAUT':
            new_x, new_y = x - 1, y
        elif direction == 'BAS':
            new_x, new_y = x + 1, y
        else:
            return False

        # Vérifier si la nouvelle position est un mur
        if MATRICE[new_x][new_y] == 1:
            return False

        return True

    # Mouvements (Gérer les touches)
    #Deplacement de Pacman vers la droite 
    def pacmanDroite(pacman):
        pacman.Mouvement(36, 'DROITE')
        
    #Deplacement de Pacman vers la gauche 
    def pacmanGauche(pacman):
        pacman.Mouvement(36, 'GAUCHE')

    #Deplacement de Pacman vers le haut 
    def pacmanHaut(pacman):
        pacman.Mouvement(36, 'HAUT')

    #Deplacement de Pacman vers le bas 
    def pacmanBas(pacman):
        pacman.Mouvement(36, 'BAS')


#Disparition des points si pacman mange un point

# Les cerises (mange cerise -> nbr de points + 100pts) (NIVEAU 1)

# Les pastèques (mange pastèque -> nbr de points + 500pts)

# Les fraises (mange fraise -> nbr de points + 300pts)

# Les PacGum (mange PacGum -> nbr de points + 10pts)
# Les Super PacGum (mange super PacGum -> nbr de points + 50pts et appel de la classe fantome transformé)

# Les fantômes (mange fantôme -> nbr de points 1er fantome + 200pts, 2ème + 400pts, 3ème + 800pts, 4ème + 1600pts
# et appel de la classe fantome Disparition)

# Next_input : on stocke la prochaine direction que le joueur veut prendre