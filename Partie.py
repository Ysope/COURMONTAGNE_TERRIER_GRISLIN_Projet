import pygame
from Labyrinthe import Labyrinthe
from Matrice import MATRICE
from Pacman import PACMAN

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen = pygame.display.set_mode((36*21, 36*22))

# Créer une instance de la classe Labyrinthe
labyrinthe = Labyrinthe(screen, 36, 36, MATRICE)

# Dessiner le labyrinthe
labyrinthe.draw()

# Afficher Pacman sur le plateau
pacman = PACMAN.afficher_pacman(screen)

# Mettre à jour l'affichage
pygame.display.flip()

def afficher_popup(screen):
    font = pygame.font.Font(None, 36)
    # Rendre le texte "Jeu en pause"
    pause_text = font.render("Jeu en pause", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 20))
    
    # Rendre le texte "Appuyez sur Q pour quitter ou R pour reprendre"
    instruction_text = font.render("Appuyez sur Echap pour quitter ou R pour reprendre.", True, (255, 255, 255))
    instruction_rect = instruction_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 20))
    
    # Dessiner les rectangles de fond
    pygame.draw.rect(screen, (0, 0, 0), pause_rect.inflate(20, 20))
    pygame.draw.rect(screen, (0, 0, 0), instruction_rect.inflate(20, 20))
    
    # Blitter les textes sur l'écran
    screen.blit(pause_text, pause_rect)
    screen.blit(instruction_text, instruction_rect)
    pygame.display.flip()

def redessiner_plateau(screen, labyrinthe):
    screen.fill((0, 0, 0))  # Effacer l'écran
    labyrinthe.draw()
    pacman.Affichage(screen)  # Redessiner Pacman
    pygame.display.flip()

# Boucle principale pour garder la fenêtre ouverte
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if paused:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    paused = False
                    redessiner_plateau(screen, labyrinthe)
            else:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    paused = True
                    afficher_popup(screen)
                elif event.key == pygame.K_RIGHT:
                    if pacman.tester_deplacement('DROITE'):
                        PACMAN.pacmanDroite(pacman)
                        redessiner_plateau(screen, labyrinthe)
                elif event.key == pygame.K_LEFT:
                    if pacman.tester_deplacement('GAUCHE'):
                        PACMAN.pacmanGauche(pacman)
                        redessiner_plateau(screen, labyrinthe)
                elif event.key == pygame.K_UP:
                    if pacman.tester_deplacement('HAUT'):
                        PACMAN.pacmanHaut(pacman)
                        redessiner_plateau(screen, labyrinthe)
                elif event.key == pygame.K_DOWN:
                    if pacman.tester_deplacement('BAS'):
                        PACMAN.pacmanBas(pacman)
                        redessiner_plateau(screen, labyrinthe)

    if not paused:
        # Mettre à jour le jeu ici (par exemple, déplacer les entités, etc.)
        pass
# Quitter Pygame
pygame.quit()