from Labyrinth import Labyrinth
from Graph import m_graphe
from Matrix import m_matrice
from Pacman import Pacman
from Ghosts import Ghosts
import pygame
import copy
import os

m_basePath = os.path.dirname(os.path.abspath(__file__))
SUPER_MODE_END = pygame.USEREVENT + 1

class Partie:

    #region Constructeur
    def __init__(self, p_posPacman=(10, 12), p_posBlinky=(10, 8), p_posPinky=(10, 8), p_posInky=(10, 8), p_posClyde=(10, 8)):
        """Constructeur de la classe Partie
        Args :
            p_posPacman (tuple) : Position initiale du pacman
            p_posBlinky (tuple) : Position initiale de Blinky
            p_posPinky (tuple) : Position initiale de Pinky
            p_posInky (tuple) : Position initiale de Inky
            p_posClyde (tuple) : Position initiale de Clyde
        """
        self.v_ligne = len(m_matrice) - 1
        self.v_colonne = len(m_matrice[0])
        self.v_tailleCellule = 36
        # Variables de jeu
        self.v_running = True
        self.v_paused = False
        self.v_finished = False
        # Matrice et graphe de jeu
        self.v_matrice = copy.deepcopy(m_matrice)
        self.v_graphe = copy.deepcopy(m_graphe)
        # Variables de score
        self.v_score = 0
        self.v_totalPacgums = sum(row.count(0) + row.count(3) for row in m_matrice)  # Compter le nombre de pacgums et super pacgums
        self.v_screen = pygame.display.set_mode((self.v_tailleCellule * self.v_ligne
                                                 , self.v_tailleCellule * self.v_colonne), pygame.DOUBLEBUF)
        self.v_labyrinthe = Labyrinth(self.v_screen, self.v_tailleCellule, self.v_tailleCellule, self.v_matrice)
        # Entities
        self.v_pacman = Pacman(p_posPacman[0] * self.v_tailleCellule,
                               p_posPacman[1] * self.v_tailleCellule, os.path.join(m_basePath, 'Sprite/pacman.png'))
        self.v_blinky = Ghosts(p_posBlinky[0] * self.v_tailleCellule,
                               p_posBlinky[1] * self.v_tailleCellule, os.path.join(m_basePath, 'Sprite/Blinky.png'),
                                'Blinky')
        self.v_pinky = Ghosts(p_posPinky[0] * self.v_tailleCellule,
                              p_posPinky[1] * self.v_tailleCellule, os.path.join(m_basePath, 'Sprite/Pinky.png'),
                               'Pinky')
        self.v_inky = Ghosts(p_posInky[0] * self.v_tailleCellule,
                             p_posInky[1] * self.v_tailleCellule, os.path.join(m_basePath, 'Sprite/Inky.png'), 'Inky')
        self.v_clyde = Ghosts(p_posClyde[0] * self.v_tailleCellule,
                              p_posClyde[1] * self.v_tailleCellule, os.path.join(m_basePath, 'Sprite/Clyde.png'),
                               'Clyde')
    #endregion

    #region Méthodes
    def RedessinerPlateau(self):
        """Redessine le plateau de jeu"""
        self.v_screen.fill((0, 0, 0))
        self.v_labyrinthe.Draw()
        self.v_pacman.Affichage(self.v_screen)
        self.v_blinky.Affichage(self.v_screen)
        self.v_pinky.Affichage(self.v_screen)
        self.v_inky.Affichage(self.v_screen)
        self.v_clyde.Affichage(self.v_screen)
        self.AfficherScore()
        pygame.display.flip()

    def Collision(self):
        """Gestion des collisions entre les entités"""
        for v_fantome in [self.v_blinky, self.v_pinky, self.v_inky, self.v_clyde]:
            if self.v_pacman.Collision(v_fantome):
                if self.v_pacman.v_super:
                    v_fantome.Meurt()
                    self.v_score += 200
                else:
                    self.v_finished = True
                    self.AfficherPopup("Vous avez perdu(e)...",
                                        "Appuyez sur Echap pour quitter ou R pour recommencer")

    def CollisionPacgum(self):
        """Gestion des collisions avec les pacgums"""
        v_x, v_y = self.v_pacman.GetPosition()
        if self.v_graphe[(v_x, v_y)][0]:
            self.v_graphe[(v_x, v_y)][0] = False
            if self.v_matrice[v_x][v_y] == 3:
                self.DebutSuperMode()
            self.v_matrice[v_x][v_y] = -1
            self.v_totalPacgums -= 1
            if self.v_totalPacgums == 0:
                self.v_finished = True
                self.AfficherPopup("Bravo ! Vous avez gagné(e) !", "Vous avez gagné ! Appuyez sur Echap pour quitter ou R pour recommencer")
            self.v_score += 10

    def DebutSuperMode(self):
        """Début du super mode"""
        self.v_pacman.v_super = True
        self.v_pacman.v_intervalle = 200
        for v_fantome in [self.v_blinky, self.v_pinky, self.v_inky, self.v_clyde]:
            if not v_fantome.v_mort:
                v_fantome.v_intervalle = 800
                v_fantome.v_effraye = True
                v_fantome.v_sprite = pygame.image.load(os.path.join(m_basePath, 'Sprite/Fantome_Bleu.png'))
        pygame.time.set_timer(SUPER_MODE_END, 5000)

    def FinSuperMode(self):
        """Fin du super mode"""
        self.v_pacman.v_super = False
        self.v_pacman.v_intervalle = 300
        for v_fantome in [self.v_blinky, self.v_pinky, self.v_inky, self.v_clyde]:
            if not v_fantome.v_mort:
                v_fantome.v_effraye = False
                v_fantome.v_intervalle = 400
                v_fantome.v_sprite = pygame.image.load(os.path.join(m_basePath, f'Sprite/{v_fantome.v_name}.png'))
        pygame.time.set_timer(SUPER_MODE_END, 0)

    def DeplacementTiming(self, p_tempsActuel, p_prochainMouvement, p_dernierDeplacement, p_fantome):
        if p_tempsActuel - p_dernierDeplacement >= p_fantome.v_intervalle:
            p_fantome.MouvementFantomes(self.v_pacman.GetPosition(), self.v_screen, p_prochainMouvement)
            return p_tempsActuel
        return p_dernierDeplacement

    def AfficherPopup(self, p_message, p_instructions):
        v_font = pygame.font.Font(None, 36)
        # Rendre le texte du message principal
        v_main_text = v_font.render(p_message, True, (255, 255, 255))
        v_main_rect = v_main_text.get_rect(center=(self.v_screen.get_width() // 2,
                                               self.v_screen.get_height() // 2 - 20))

        # Rendre le texte des instructions
        v_instruction_text = v_font.render(p_instructions, True, (255, 255, 255))
        v_instruction_rect = v_instruction_text.get_rect(center=(self.v_screen.get_width() // 2,
                                                             self.v_screen.get_height() // 2 + 20))

        # Dessiner les rectangles de fond
        pygame.draw.rect(self.v_screen, (0, 0, 0), v_main_rect.inflate(20, 20))
        pygame.draw.rect(self.v_screen, (0, 0, 0), v_instruction_rect.inflate(20, 20))

        # Blitter les textes sur l'écran
        self.v_screen.blit(v_main_text, v_main_rect)
        self.v_screen.blit(v_instruction_text, v_instruction_rect)
        pygame.display.flip()

    def AfficherScore(self):
        """Affiche le score sur l'écran"""
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.v_score}", True, (255, 255, 255))
        self.v_screen.blit(score_text, (self.v_tailleCellule//2,8*self.v_tailleCellule))
    #endregion