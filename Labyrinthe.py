import pygame

class Labyrinthe:
    def __init__(self, screen, width, height, labyrinthe):
        self.screen = screen
        self.width = width
        self.height = height
        self.labyrinthe = labyrinthe

    def draw(self):
        for i in range(len(self.labyrinthe)):
            for j in range(len(self.labyrinthe[i])):
                if self.labyrinthe[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), (j * self.width, i * self.height, self.width, self.height))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255),(j * self.width, i * self.height, self.width, self.height))


