import pygame
from Labyrinthe import Labyrinthe
from Matrice import MATRICE
from Pacman import PACMAN

TAILLE_CELLULE = 36
LIGNE = len(MATRICE) - 1
COLLONE = len(MATRICE[0])

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen = pygame.display.set_mode((TAILLE_CELLULE * LIGNE, TAILLE_CELLULE * COLLONE))

# Créer une instance de la classe Labyrinthe et l'afficher
labyrinthe = Labyrinthe(screen, TAILLE_CELLULE, TAILLE_CELLULE, MATRICE)
labyrinthe.draw()

# Afficher Pacman sur le plateau
pacman = PACMAN(10 * TAILLE_CELLULE, 12 * TAILLE_CELLULE, 'pacman.png')
pacman.Affichage(screen)

# Mettre à jour l'affichage
pygame.display.flip()


def redessiner_plateau(screen, labyrinthe, pacman):
    screen.fill((0, 0, 0))  # Effacer l'écran
    labyrinthe.draw()
    pacman.Affichage(screen)  # Redessiner Pacman
    pygame.display.flip()


# Variables de gestion
nouveau_mouvement = None
mouvement_actuel = None
prochain_mouvement = None
running = True

# Gestion du temps
clock = pygame.time.Clock()

# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                prochain_mouvement = 'DROITE'
            elif event.key == pygame.K_LEFT:
                prochain_mouvement = 'GAUCHE'
            elif event.key == pygame.K_UP:
                prochain_mouvement = 'HAUT'
            elif event.key == pygame.K_DOWN:
                prochain_mouvement = 'BAS'

    # Appliquer un nouveau mouvement si demandé
    if prochain_mouvement:
        if pacman.tester_deplacement(prochain_mouvement):
            mouvement_actuel = prochain_mouvement
            prochain_mouvement = None  # Le prochain mouvement devient actif

    # Continuer le mouvement actuel si possible
    if mouvement_actuel:
        if pacman.tester_deplacement(mouvement_actuel):
            pacman.Mouvement(36, mouvement_actuel, screen)
            redessiner_plateau(screen, labyrinthe, pacman)
        else:
            mouvement_actuel = None  # Arrêter si le mouvement n'est plus possible

    # Limiter la boucle à 5 frames par seconde (contrôle de la vitesse)
    clock.tick(5)

# Quitter Pygame
pygame.quit()