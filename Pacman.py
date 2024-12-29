import pygame as pg
from Entities import Entities
from Graph import m_graphe

class Pacman(Entities):

    #region Constructeur
    def __init__(self, p_x, p_y, p_sprite):
        """Constructeur de la classe Pacman
        Args:
            p_x (int): Position x de Pacman
            p_y (int): Position y de Pacman
            p_sprite (str): Sprite de Pacman
        """
        super().__init__(p_x, p_y, p_sprite, p_intervalle=300)
        self.v_super = False
    #endregion

    #region Méthodes
    def TesterDeplacement(self, p_direction):
        """Tester si Pacman peut se déplacer dans une direction donnée
        Args :
            p_direction (str) : Direction dans laquelle Pacman doit se déplacer
        Returns :
            bool : True si Pacman peut se déplacer, False sinon
        """
        position = self.GetPosition()
        x, y = position

        if ((x, y) in m_graphe and m_graphe[(x, y)][1][p_direction]
                is not None):
            return True

        return False
    #endregion
