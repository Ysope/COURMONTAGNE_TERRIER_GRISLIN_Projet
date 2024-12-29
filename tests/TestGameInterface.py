import unittest
import pygame
from Party import Partie

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
    def testPauseJeu(self):
        """Test de la pause du jeu"""
        # Simuler l'appui sur la touche pause
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p))
        self.v_partie.AfficherPopup("Partie en pause", "Appuyez sur Echap pour quitter ou R pour rependre")
        # Vérifier si le jeu est en pause
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_p for event in pygame.event.get()))

    def testReprendreJeu(self):
        """Test de la reprise du jeu"""
        self.v_partie.v_paused = True
        # Simuler l'appui sur la touche reprise
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r))
        self.v_partie.RedessinerPlateau()
        # Vérifier si le jeu est repris
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_r for event in pygame.event.get()))

    def testQuitterJeu(self):
        """Test de sortie du jeu"""
        # Simuler l'appui sur la touche quitter
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
        # Vérifier si le jeu est quitté
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE for event in pygame.event.get()))

    def testRecommencerJeu(self):
        """Test de redémarrage du jeu"""
        self.v_partie.v_finished = True
        # Simuler l'appui sur la touche redémarrer
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r))
        self.v_partie.RedessinerPlateau()
        # Vérifier si le jeu est redémarré
        self.assertTrue(any(event.type == pygame.KEYDOWN and event.key == pygame.K_r for event in pygame.event.get()))

if __name__ == '__main__':
    unittest.main()
