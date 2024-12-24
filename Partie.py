from Labyrinthe import Labyrinthe
from Graphe import m_graphe
from Matrice import MATRICE
from Pacman import PACMAN
from Fantomes import Fantome
import pygame
intervalle_pacman = 300  # En ms
intervalle_fantomes = 400  # En ms


SUPER_MODE_END = pygame.USEREVENT + 1

class Partie:

    def __init__(self):
        self.ligne =  len(MATRICE) - 1
        self.colonne = len(MATRICE[0])
        self.taille_cellule = 36
        self.running = True
        self.intervalle_pacman = intervalle_pacman
        self.intervalle_fantomes = intervalle_fantomes
        self.matrice = MATRICE
        self.m_graphe = m_graphe
        self.score = 0
        self.screen = pygame.display.set_mode((self.taille_cellule * self.ligne, self.taille_cellule * self.colonne), pygame.DOUBLEBUF)
        self.labyrinthe = Labyrinthe(self.screen, self.taille_cellule, self.taille_cellule, MATRICE)
        #Entities
        self.pacman = PACMAN(10 * self.taille_cellule, 12 * self.taille_cellule, './Sprite/pacman.png')
        self.blinky = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Blinky.png', 'Blinky')
        self.pinky = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Pinky.png', 'Pinky')
        self.inky = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Inky.png', 'Inky')
        self.clyde = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Clyde.png', 'Clyde')


    def redessiner_plateau(self):
        self.screen.fill((0, 0, 0))
        self.labyrinthe.draw()
        self.pacman.Affichage(self.screen)
        self.blinky.Affichage(self.screen)
        self.pinky.Affichage(self.screen)
        self.inky.Affichage(self.screen)
        self.clyde.Affichage(self.screen)
        pygame.display.flip()

    def collision(self):
        if self.pacman.rect.collidelist([self.blinky.rect, self.pinky.rect, self.inky.rect, self.clyde.rect]) != -1:
            if self.pacman.super:
                if self.pacman.rect.colliderect(self.blinky.rect):
                    self.blinky.sprite = pygame.image.load('Sprite/Yeux.png')
                    self.blinky.effraye = False  # Ils ne sont plus effrayés après la collision
                    self.inky = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Inky.png', 'Inky')
                if self.pacman.rect.colliderect(self.pinky.rect):
                    self.pinky.sprite = pygame.image.load('Sprite/Yeux.png')
                    self.pinky.effraye = False
                    self.pinky = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Pinky.png', 'Pinky')
                if self.pacman.rect.colliderect(self.inky.rect):
                    self.inky.sprite = pygame.image.load('Sprite/Yeux.png')
                    self.inky.effraye = False
                    self.inky = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Inky.png', 'Inky')
                if self.pacman.rect.colliderect(self.clyde.rect):
                    self.clyde.sprite = pygame.image.load('Sprite/Yeux.png')
                    self.clyde.effraye = False
                    #reset le fantome
                    self.clyde = Fantome(10 * self.taille_cellule, 8 * self.taille_cellule, './Sprite/Clyde.png', 'Clyde')
            else:
                self.running = False

    def check_collision_with_pacgum(self):
        position = self.pacman.get_position()
        x, y = position

        if self.m_graphe[(x, y)][0] == True:
            if self.matrice[x][y] == 0:
                self.m_graphe[(x, y)][0] = False
                self.matrice[x][y] = -1
                return 10
            elif self.matrice[x][y] == 3:
                self.m_graphe[(x, y)][0] = False
                self.matrice[x][y] = -1
                self.pacman.super = True
                self.pinky.effraye = True
                self.blinky.effraye = True
                self.inky.effraye = True
                self.clyde.effraye = True
                intervalle_fantomes = 800
                pygame.time.set_timer(SUPER_MODE_END, 5000)

        return 0
