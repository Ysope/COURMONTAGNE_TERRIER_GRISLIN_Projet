import unittest
import pygame
from Partie import afficher_popup, redessiner_plateau
from Labyrinthe import Labyrinthe
from Matrice import MATRICE

class TestGameInterface(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((36*21, 36*22))
        self.labyrinthe = Labyrinthe(self.screen, 36, 36, MATRICE)

    def tearDown(self):
        pygame.quit()

    def test_pause_game(self):
        # Simulate pressing the pause key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p))
        afficher_popup(self.screen)
        # Check if the popup is displayed
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_p for event in pygame.event.get()))

    def test_resume_game(self):
        # Simulate pressing the resume key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r))
        redessiner_plateau(self.screen, self.labyrinthe)
        # Check if the game is resumed
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_r for event in pygame.event.get()))

    def test_quit_game(self):
        # Simulate pressing the quit key
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
        # Check if the game is quit
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE for event in pygame.event.get()))

if __name__ == '__main__':
    unittest.main()