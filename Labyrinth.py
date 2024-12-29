import pygame

class Labyrinth:
    #region Constructeur
    def __init__(self, p_screen, p_width, p_height, p_labyrinthe):
        """Constructeur de la classe Labyrinthe
        Args :
            p_screen (Surface) : Surface de jeu
            p_width (int) : Largeur d'une cellule
            p_height (int) : Hauteur d'une cellule
            p_labyrinthe (list) : Matrice représentant le labyrinthe
        """
        self.v_screen = p_screen
        self.v_width = p_width
        self.v_height = p_height
        self.v_labyrinthe = p_labyrinthe
        self.v_wallThickness = 5  # Épaisseur du mur
    #endregion

    #region Méthodes
    def Draw(self):
        """Dessine le labyrinthe"""
        for i in range(len(self.v_labyrinthe)):
            for j in range(len(self.v_labyrinthe[i])):
                v_x = j * self.v_width
                v_y = i * self.v_height
                if self.v_labyrinthe[i][j]== 1:
                    self.DrawWalls(v_x, v_y, i, j)
                elif self.v_labyrinthe[i][j] == 0:
                    pygame.draw.circle(self.v_screen, (255, 255, 0),
                                       (v_x + self.v_width // 2, v_y + self.v_height // 2), 3)
                elif self.v_labyrinthe[i][j] == 3:
                    pygame.draw.circle(self.v_screen, (255, 255, 0),
                                       (v_x + self.v_width // 2, v_y + self.v_height // 2), 5)


    def DrawWalls(self, p_x, p_y, p_i, p_j):
        """Dessine les murs autour d'un bloc en fonction des voisins
        Args :
            p_x (int) : Position x du bloc
            p_y (int) : Position y du bloc
            p_i (int) : Position i du bloc dans la matrice
            p_j (int) : Position j du bloc dans la matrice
        """

        # Mur haut
        if p_i == 0 or self.v_labyrinthe[p_i - 1][p_j] in [0, -1, 3]:
            pygame.draw.rect(self.v_screen, (0, 0, 255),
                             (p_x, p_y, self.v_width, self.v_wallThickness))
        # Mur bas
        if p_i == len(self.v_labyrinthe) - 1 or self.v_labyrinthe[p_i + 1][p_j] in [0, -1, 3]:
            pygame.draw.rect(self.v_screen, (0, 0, 255),
                             (p_x, p_y + self.v_height - self.v_wallThickness, self.v_width, self.v_wallThickness))
        # Mur gauche
        if p_j == 0 or self.v_labyrinthe[p_i][p_j - 1] in [0, -1, 3]:
            pygame.draw.rect(self.v_screen, (0, 0, 255),
                             (p_x, p_y, self.v_wallThickness, self.v_height))
        # Mur droit
        if p_j == len(self.v_labyrinthe[p_i]) - 1 or self.v_labyrinthe[p_i][p_j + 1] in [0, -1, 3]:
            pygame.draw.rect(self.v_screen, (0, 0, 255),
                             (p_x + self.v_width - self.v_wallThickness, p_y, self.v_wallThickness, self.v_height))
    #endregion