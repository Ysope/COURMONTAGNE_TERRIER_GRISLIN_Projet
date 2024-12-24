import pygame
from Partie import Partie, SUPER_MODE_END, intervalle_pacman, intervalle_fantomes

pygame.init()

partie = Partie()

# Variables de gestion
nouveau_mouvement = None
mouvement_actuel = None
prochain_mouvement = None

# Gestion du temps
clock = pygame.time.Clock()
dernier_deplacement_pacman = pygame.time.get_ticks()

dernier_deplacement_clyde = pygame.time.get_ticks()
dernier_deplacement_blinky = pygame.time.get_ticks()
dernier_deplacement_inky = pygame.time.get_ticks()
dernier_deplacement_pinky = pygame.time.get_ticks()


# Initialisation plateau
partie.redessiner_plateau()

# Boucle principale
while partie.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            partie.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                prochain_mouvement = 'DROITE'
            elif event.key == pygame.K_LEFT:
                prochain_mouvement = 'GAUCHE'
            elif event.key == pygame.K_UP:
                prochain_mouvement = 'HAUT'
            elif event.key == pygame.K_DOWN:
                prochain_mouvement = 'BAS'
        elif event.type == SUPER_MODE_END:
            partie.pacman.super = False
            partie.blinky.effraye = False
            partie.pinky.effraye = False
            partie.inky.effraye = False
            partie.clyde.effraye = False

            partie.clyde.sprite = pygame.image.load('Sprite/Clyde.png')
            partie.blinky.sprite = pygame.image.load('Sprite/Blinky.png')
            partie.pinky.sprite = pygame.image.load('Sprite/Pinky.png')
            partie.inky.sprite = pygame.image.load('Sprite/Inky.png')

            # Arrêter le timer (si vous voulez éviter de répéter l'événement)
            pygame.time.set_timer(SUPER_MODE_END, 0)

    # Gestion du temps actuel
    temps_actuel = pygame.time.get_ticks()

    # Déplacer Pac-Man à intervalle régulier
    if temps_actuel - dernier_deplacement_pacman >= partie.intervalle_pacman:
        if prochain_mouvement and partie.pacman.tester_deplacement(prochain_mouvement):
            mouvement_actuel = prochain_mouvement
            prochain_mouvement = None  # Le prochain mouvement devient actif

        if mouvement_actuel and partie.pacman.tester_deplacement(mouvement_actuel):
            partie.pacman.Mouvement(36, mouvement_actuel, partie.screen)
            partie.score += partie.check_collision_with_pacgum()
        dernier_deplacement_pacman = temps_actuel

    # Déplacer les fantômes à intervalle régulier
    if temps_actuel - dernier_deplacement_clyde >= partie.intervalle_fantomes:
        partie.clyde.Mouvement_Fantomes(36, partie.pacman.get_position(), partie.screen, prochain_mouvement)
        dernier_deplacement_clyde = temps_actuel

    if temps_actuel - dernier_deplacement_blinky >= partie.intervalle_fantomes:
        partie.blinky.Mouvement_Fantomes(36, partie.pacman.get_position(), partie.screen, prochain_mouvement)
        dernier_deplacement_blinky = temps_actuel

    if temps_actuel - dernier_deplacement_inky >= partie.intervalle_fantomes:
        partie.inky.Mouvement_Fantomes(36, partie.pacman.get_position(), partie.screen, prochain_mouvement)
        dernier_deplacement_inky = temps_actuel

    if temps_actuel - dernier_deplacement_pinky >= partie.intervalle_fantomes:
        partie.pinky.Mouvement_Fantomes(36, partie.pacman.get_position(), partie.screen, prochain_mouvement)
        dernier_deplacement_pinky = temps_actuel

    # Redessiner l'écran
    partie.redessiner_plateau()

    # Gestion des collisions avec les fantomes
    partie.collision()

    # Limiter la boucle à 60 FPS
    clock.tick(60)

# Quitter Pygame
pygame.quit()
