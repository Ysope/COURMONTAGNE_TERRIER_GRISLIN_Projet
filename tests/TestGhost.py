import unittest
import pygame
from Party import Partie

class TestGhost(unittest.TestCase):

    def setUp(self):
        """Initialisation de la fenêtre de jeu et de la partie"""
        pygame.init()
        self.v_screen = pygame.display.set_mode((36*21, 36*22))
        self.v_partie = Partie()

    def tearDown(self):
        """Fermeture de la fenêtre de jeu"""
        pygame.quit()

    def testMouvementFantome(self):
        """Test du mouvement des fantômes"""
        # On place un fantôme à la position (10, 13)
        self.v_partie.v_blinky.v_x = 13 * self.v_partie.v_tailleCellule
        self.v_partie.v_blinky.v_y = 10 * self.v_partie.v_tailleCellule
        # On vérifie que le fantôme se déplace
        self.v_partie.v_blinky.MouvementFantomes((10, 15), self.v_screen, 'DROITE')
        self.assertTrue(self.v_partie.v_blinky.v_x != 13 * self.v_partie.v_tailleCellule
                        or self.v_partie.v_blinky.v_y != 10 * self.v_partie.v_tailleCellule)