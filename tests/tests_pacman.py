import unittest
import pygame
from Partie import Partie

class TestPacman(unittest.TestCase):

    def setUp(self):
        """Initialisation de la fenêtre de jeu et de la partie"""
        pygame.init()
        self.v_screen = pygame.display.set_mode((36 * 21, 36 * 22))
        self.v_partie = Partie()

    def tearDown(self):
        """Fermeture de la fenêtre de jeu"""
        pygame.quit()

    def testPacGum(self):
        """Test de la collision avec une pacgum"""
        # On place une pacgum à la position (10, 13)
        self.v_partie.v_score = 0
        self.v_partie.v_matrice[10][13] = 0
        self.v_partie.v_pacman.v_x= 13 * self.v_partie.v_tailleCellule
        self.v_partie.v_pacman.v_y= 10 * self.v_partie.v_tailleCellule
        # On vérifie que le score est incrémenté de 10
        self.v_partie.CollisionPacgum()
        self.assertEqual(self.v_partie.v_score, 10)

    def testSuperPacGum(self):
        """Test de la collision avec une super pacgum"""
        # On place une super pacgum à la position (10, 13)
        self.v_partie.v_score = 0
        self.v_partie.v_matrice[10][13] = 3
        self.v_partie.v_pacman.v_x= 13 * self.v_partie.v_tailleCellule
        self.v_partie.v_pacman.v_y= 10 * self.v_partie.v_tailleCellule
        # On vérifie que pacman est en mode super
        self.v_partie.CollisionPacgum()
        self.assertEqual(self.v_partie.v_pacman.v_super, True)
        # On vérifie que les fantômes sont en mode effrayé
        self.assertEqual(self.v_partie.v_blinky.v_effraye, True)
        self.assertEqual(self.v_partie.v_pinky.v_effraye, True)
        self.assertEqual(self.v_partie.v_inky.v_effraye, True)
        self.assertEqual(self.v_partie.v_clyde.v_effraye, True)

    def testCollisionFantome(self):
        """Test de la collision avec un fantôme"""
        # On place un fantôme et pacman à la position (10, 13)
        self.v_partie.v_score = 0
        self.v_partie.v_blinky.v_x = 13 * self.v_partie.v_tailleCellule
        self.v_partie.v_blinky.v_y = 10 * self.v_partie.v_tailleCellule
        self.v_partie.v_pacman.v_x = 13 * self.v_partie.v_tailleCellule
        self.v_partie.v_pacman.v_y = 10 * self.v_partie.v_tailleCellule
        # On met les deux entités en collision
        self.v_partie.v_pacman.v_rect.topleft = (self.v_partie.v_pacman.v_x, self.v_partie.v_pacman.v_y)
        self.v_partie.v_blinky.v_rect.topleft = (self.v_partie.v_blinky.v_x, self.v_partie.v_blinky.v_y)
        # On vérifie que la partie est terminée
        self.v_partie.Collision()
        self.assertEqual(self.v_partie.v_finished, True)


if __name__ == '__main__':
    unittest.main()