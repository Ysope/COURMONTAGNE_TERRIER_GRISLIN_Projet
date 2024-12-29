import pygame
from Party import Partie, SUPER_MODE_END

# Initialisation de Pygame et de la partie
pygame.init()
partie = Partie()

# Variables de gestion
m_nouveau_mouvement = None
m_mouvement_actuel = None
m_prochain_mouvement = None

# Gestion du temps
m_clock = pygame.time.Clock()
m_dernier_deplacement_pacman = pygame.time.get_ticks()
m_dernier_deplacement_clyde = pygame.time.get_ticks()
m_dernier_deplacement_blinky = pygame.time.get_ticks()
m_dernier_deplacement_inky = pygame.time.get_ticks()
m_dernier_deplacement_pinky = pygame.time.get_ticks()

# Initialisation plateau
partie.RedessinerPlateau()

# Boucle principale
while partie.v_running:
    # Gestion des événements
    #region Gestion des événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, on quitte
        if event.type == pygame.QUIT:
            partie.v_running = False
        elif event.type == pygame.KEYDOWN:
            # Si la partie est en pause, on ne peut que quitter ou reprendre
            if partie.v_paused:
                # Si la touche Echap est pressée, on quitte
                if event.key == pygame.K_ESCAPE:
                    partie.v_running = False
                # Si la touche R est pressée, on reprend la partie
                elif event.key == pygame.K_r:
                    partie.v_paused = False
                    partie.RedessinerPlateau()
            # Si la partie est terminée, on ne peut que recommencer ou quitter
            elif partie.v_finished:
                #Si la touche Echap est pressée, on quitte
                if event.key == pygame.K_ESCAPE:
                    partie.v_running = False
                # Si la touche R est pressée, on recommence
                elif event.key == pygame.K_r:
                    m_nouveau_mouvement = None
                    m_mouvement_actuel = None
                    m_prochain_mouvement = None
                    partie = Partie()
                    partie.RedessinerPlateau()
            else:
                # Gestion des mouvements
                mouvements = {
                    pygame.K_RIGHT: 'DROITE',
                    pygame.K_LEFT: 'GAUCHE',
                    pygame.K_UP: 'HAUT',
                    pygame.K_DOWN: 'BAS'
                }
                if event.key in mouvements:
                    m_prochain_mouvement = mouvements[event.key]
                # Gestion de la pause
                elif event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    partie.v_paused = True
                    partie.AfficherPopup("Partie en pause", "Appuyez sur Echap pour quitter ou R pour rependre")
        # Gestion de la fin du super mode
        elif event.type == SUPER_MODE_END:
            partie.FinSuperMode()
    #endregion

    # Si la partie est en pause, on ne fait rien
    if partie.v_paused or partie.v_finished:
        continue

    #region Gestion des mouvements
    # Gestion du temps actuel
    m_temps_actuel = pygame.time.get_ticks()

    # Déplacer Pac-Man à intervalle régulier
    if m_temps_actuel - m_dernier_deplacement_pacman >= partie.v_pacman.v_intervalle:
        # Si le prochain mouvement est valide, on le rend actif
        if m_prochain_mouvement and partie.v_pacman.TesterDeplacement(m_prochain_mouvement):
            m_mouvement_actuel = m_prochain_mouvement
            m_prochain_mouvement = None  # Le prochain mouvement devient actif

        # Si le mouvement actuel est valide, on le déplace
        if m_mouvement_actuel and partie.v_pacman.TesterDeplacement(m_mouvement_actuel):
            partie.v_pacman.Mouvement(m_mouvement_actuel, partie.v_screen)
            partie.CollisionPacgum()
        m_dernier_deplacement_pacman = m_temps_actuel

    # Déplacer les fantômes à interval
    m_dernier_deplacement_clyde = partie.DeplacementTiming(m_temps_actuel, m_prochain_mouvement, m_dernier_deplacement_clyde, partie.v_clyde)
    m_dernier_deplacement_blinky = partie.DeplacementTiming(m_temps_actuel, m_prochain_mouvement, m_dernier_deplacement_blinky, partie.v_blinky)
    m_dernier_deplacement_inky = partie.DeplacementTiming(m_temps_actuel, m_prochain_mouvement, m_dernier_deplacement_inky, partie.v_inky)
    m_dernier_deplacement_pinky = partie.DeplacementTiming(m_temps_actuel, m_prochain_mouvement, m_dernier_deplacement_pinky, partie.v_pinky)
    #endregion

    # Redessiner l'écran
    partie.RedessinerPlateau()

    # Gestion des collisions avec les fantomes
    partie.Collision()

    # Limiter la boucle à 60 FPS
    m_clock.tick(60)

# Quitter Pygame
pygame.quit()