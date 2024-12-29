import pygame as pg
from Entities import Entities
import random
import os
from Graph import m_graphe
from FollowInFrontOf import FollowTarget, GetFantomeDirection
from Flee import FindFurthestFirection

m_basePath = os.path.dirname(os.path.abspath(__file__))

class Ghosts(Entities):

    #region Constructeur
    def __init__(self, p_x, p_y, p_sprite, p_name):
        """Constructeur de la classe Fantome
        Args :
            p_x (int) : Position x
            p_y (int) : Position y
            p_sprite (str) : Sprite
            p_name (str) : Nom du fantôme
        """
        # Appeler le constructeur de la classe mère
        super().__init__(p_x, p_y, p_sprite)
        self.v_spawn = (p_x, p_y)
        self.v_name = p_name
        self.v_mort = False
        self.v_effraye = False
    #endregion

    #region Méthodes
    def Fuite(self, p_pacmanPos, p_screen):
        """
        Méthode qui rend les fantômes effrayés et les fait fuir dans la direction
        la plus éloignée de Pac-Man.
        Args :
            p_pacmanPos (tuple) : Position
            p_screen (Surface) : Surface de jeu
        """
        # Trouver la direction la plus éloignée
        v_furthestDirection = FindFurthestFirection(self.GetPosition(), p_pacmanPos)

        # Déplacer le fantôme si une direction est trouvée
        if v_furthestDirection:
            self.Mouvement(v_furthestDirection, p_screen)

    def MouvementFantomes(self, p_positionPacman, p_screen, p_pacmanDirection):
        """
        Méthode qui gère le mouvement des fantômes
        Args :
            p_positionPacman (tuple) : Position de Pacman
            p_screen (Surface) : Surface de jeu
            p_pacmanDirection (str) : Direction de Pacman
        """
        if self.v_mort:
            self.v_direction = FollowTarget(self, (8, 10))  # Retour à la base
            self.Mouvement(self.v_direction, p_screen)
            if self.GetPosition() == (8, 10):  # Vérifier si le fantôme est de retour à la base
                self.v_intervalle = 400
                self.v_mort = False
                self.v_sprite = pg.image.load(os.path.join(m_basePath,f'Sprite/'
                                            f'{self.v_name}.png'))
        elif self.v_effraye:
            self.Fuite(p_positionPacman, p_screen)
        else:
            match self.v_name:
                case 'Blinky':
                    # Se déplace sur le plus court chemin vers Pacman
                    self.v_direction = FollowTarget(self, p_positionPacman)
                    self.Mouvement(self.v_direction, p_screen)
                case 'Pinky':
                    # Se déplace 4 cases avant Pacman
                    self.v_direction = GetFantomeDirection(m_graphe,
                                                           self.GetPosition(), p_positionPacman, p_pacmanDirection)
                    self.Mouvement(self.v_direction, p_screen)
                case 'Inky':
                    # Se déplace 4 cases devant Pacman + des fois à l'opposé
                    self.v_direction = random.choice([FollowTarget(self, p_positionPacman),
                                                      random.choice([direction for direction, pos in
                                                                   m_graphe[self.GetPosition()][1].items() if pos is not None])])
                    self.Mouvement(self.v_direction, p_screen)
                case 'Clyde':
                    # Se déplace aléatoirement
                    self.v_direction = random.choice([direction for direction, pos
                                                    in m_graphe[self.GetPosition()][1].items() if pos is not None])
                    self.Mouvement(self.v_direction, p_screen)


    def Meurt(self):
        """Méthode qui tue le fantôme"""
        self.v_mort = True
        self.v_sprite = pg.image.load(os.path.join(m_basePath,'Sprite/Yeux.png'))
        self.v_intervalle = 100
    #endregion







        