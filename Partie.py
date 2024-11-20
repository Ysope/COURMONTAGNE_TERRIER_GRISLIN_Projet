import pygame
from Labyrinthe import Labyrinthe
from Matrice import MATRICE
import pygame_popup
from pygame_popup.components import Button, InfoBox, TextElement
from pygame_popup.menu_manager import MenuManager

# Initialiser Pygame
pygame.init()

class Partie:
    def __init__(self, screen):
        self.screen = screen
        self.labyrinthe = Labyrinthe(screen, 36, 36, MATRICE)

    def afficher_popup(self):
        popup = Popup(
            self.screen,
            "Jeu en pause",
            "Appuyez sur Echap pour quitter ou R pour reprendre.",
            font_size=36,
            font_color=(255, 255, 255),
            bg_color=(0, 0, 0),
            padding=20
        )
        popup.show()

    def jouer(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        running = False
                    elif event.key == pygame.K_r:
                        running = False


pygame.quit()