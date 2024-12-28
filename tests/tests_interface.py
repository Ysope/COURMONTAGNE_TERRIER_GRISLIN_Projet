import unittest
import pygame
from Partie import Partie

class TestGameInterface(unittest.TestCase):

    def setUp(self):
        """Initialisation de la fenêtre de jeu et de la partie"""
        pygame.init()
        self.v_screen = pygame.display.set_mode((36*21, 36*22))
        self.v_partie = Partie()

    def tearDown(self):
        """Fermeture de la fenêtre de jeu"""
        pygame.quit()

    #Camel case nécessaire pour les noms de méthodes par unittest
    def testPauseGame(self):
        """Test de la pause du jeu"""
        # Simulate pressing the pause key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p))
        self.v_partie.AfficherPopup("Partie en pause", "Appuyez sur Echap pour quitter ou R pour rependre")
        # Check if the popup is displayed
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_p for event in pygame.event.get()))

    def testResumeGame(self):
        # Simulate pressing the resume key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r))
        self.v_partie.RedessinerPlateau()
        # Check if the game is resumed
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_r for event in pygame.event.get()))

    def testQuitGame(self):
        # Simulate pressing the quit key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
        # Check if the game is quit
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE for event in pygame.event.get()))

    def testRestartGame(self):
        # Simulate pressing the restart key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r))
        self.v_partie.RedessinerPlateau()
        # Check if the game is restarted
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_r for event in pygame.event.get()))

if __name__ == '__main__':
    unittest.main()