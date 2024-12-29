import unittest
import pygame
from Party import Partie

class TestParty(unittest.TestCase):

    def setUp(self):
        """Initialisation de la fenêtre de jeu et de la partie"""
        pygame.init()
        self.v_screen = pygame.display.set_mode((36*21, 36*22))
        self.v_partie = Partie()

    def tearDown(self):
        """Fermeture de la fenêtre de jeu"""
        pygame.quit()

    def testGameOver(self):
        """Test de la fin de la partie"""
        # On vérifie que la partie est terminée
        self.v_partie.v_finished = True
        self.assertTrue(self.v_partie.v_finished)