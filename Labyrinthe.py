import pygame

class Labyrinthe:
    def __init__(self, screen, width, height, labyrinthe):
        self.screen = screen
        self.width = width
        self.height = height
        self.labyrinthe = labyrinthe
        self.wall_thickness = 5  # Épaisseur du mur

    def draw(self):
        for i in range(len(self.labyrinthe)):
            for j in range(len(self.labyrinthe[i])):
                x = j * self.width
                y = i * self.height
                if self.labyrinthe[i][j] == 1:
                    self.draw_walls(x, y, i, j)
                elif self.labyrinthe[i][j] == 0:
                    pygame.draw.circle(self.screen, (255, 255, 0), (x + self.width // 2, y + self.height // 2), 3)
                elif self.labyrinthe[i][j] == 3:
                    pygame.draw.circle(self.screen, (255, 255, 0), (x + self.width // 2, y + self.height // 2), 5)
                elif self.labyrinthe[i][j] == -1:
                    pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.width, self.height))


    def draw_walls(self, x, y, i, j):
        """Dessine les murs autour d'un bloc '1' en fonction des voisins"""
        # Mur haut
        if i == 0 or self.labyrinthe[i - 1][j] == 0:
            pygame.draw.rect(self.screen, (0, 0, 255), (x, y, self.width, self.wall_thickness))
        # Mur bas
        if i == len(self.labyrinthe) - 1 or self.labyrinthe[i + 1][j] == 0:
            pygame.draw.rect(self.screen, (0, 0, 255), (x, y + self.height - self.wall_thickness, self.width, self.wall_thickness))
        # Mur gauche
        if j == 0 or self.labyrinthe[i][j - 1] == 0:
            pygame.draw.rect(self.screen, (0, 0, 255), (x, y, self.wall_thickness, self.height))
        # Mur droit
        if j == len(self.labyrinthe[i]) - 1 or self.labyrinthe[i][j + 1] == 0:
            pygame.draw.rect(self.screen, (0, 0, 255), (x + self.width - self.wall_thickness, y, self.wall_thickness, self.height))