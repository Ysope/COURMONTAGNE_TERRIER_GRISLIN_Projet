# TO DO :
# Mouvements (Gérer le comportement des fantômes)

# Disparition (Les fantômes disparaissent (deviennent des yeux) + rentre à la maison)

# Les Super PacGum (Les fantômes deviennent bleus + fuis Pacman)
# Comportement des fantômes
#   Rouge(Blinky) : Plus court chemin vers Pacman + sort par défaut de la maison
#   Rose(Pinky) : Vise 4 cases devant Pacman + sort au bout de 1 seconde
#   Bleu(Inky) : Comme le Rose mais des fois se déplace à l'opposé de Pacman + sort au bout de 30 pts
#   Orange(Clyde) : Déplacement aléatoire + sort au bout de 60 pts

import pygame as pg
from pygame.locals import *
from Entities import Entity
import random
from collections import deque
from Graphe import m_graphe 

class Fantome(Entity):

    """
    Méthode qui rends les fantomes bleus et les fait fuir Pacman
    Self = Attributs de Entitiy + Fantome
    """
    def Fuite(self):
        duree = 6
        # Pour une durée de 6 secondes (remplacer la boucle for c'est pas beau + marche pas)
        for i in range(duree):
            self.sprite = pg.image.load('Sprite/Fantome_Bleu.png')
            self.vitesse = 9
            self.Mouvement(self.direction)
        
        # Changer l'état des fantomes si ils sont touchés par Pacman
        if(self.Collision() == True):
            self.sprite = pg.image.load('Sprite/Yeux.png')
    
    """
    Méthode pour déplacer l'entité
    Self = Attributs de Entitiy + Fantome
    direction = direction de déplacement
    position_pacman = position de Pacman
    """
    def Mouvement_Fantomes(self, direction, position_pacman):
        
        match self.name:
            case 'Blinky':
                # Se déplace sur le plus court chemin vers Pacman
                self.direction = self.follow_pacman(position_pacman)
                self.Mouvement (self.direction)

            case 'Pinky':
                # Se déplace 4 cases avant Pacman
                self.direction = self.get_fantome_direction(self, m_graphe, self.position, position_pacman, direction)
                self.Mouvement (self.direction)
                
            case 'Inky':
                # Se déplace 4 cases devant Pacman + des fois à l'opposé
                self.direction = random.choice(self.follow_pacman(position_pacman),random.choice(['HAUT', 'BAS', 'GAUCHE', 'DROITE']))
                self.Mouvement(self.direction)
            case 'Clyde':
                # Définir la direction
                self.direction = random.choice([dir for dir, pos in m_graphe[self.get_position()][1].items() if pos is not None])
                self.Mouvement(self.direction)

    """      
    Constructeur de la méthode Fantome
    x = position en x
    y = position en y
    sprite = sprite du fantome
    name = nom du fantome
    """
    def __init__(self, x, y, sprite, name):

        # Appeler le constructeur de la classe mère
        super().__init__()

        # Définir les noms des fantômes
        self.name = name

        # Définir l'image du fantôme
        self.sprite = pg.image.load('Sprite/fantome.png')

    """
    Méthode pour suivre Pacman
    self = Attributs de Entitiy + Fantome
    m_graphe = Graphe du jeu
    position_pacman = position de Pacman
    """
    def follow_pacman(self, position_pacman):
        path = self.bfs_shortest_path(m_graphe, self.get_position(), position_pacman)
        if len(path) > 1:
            next_pos = path[-2]  # Se placer derrière Pac-Man
            for direction, neighbor in m_graphe[self.get_position()][1].items():
                if neighbor == next_pos:
                    return direction

    """                  
    Méthode pour trouver le plus court chemin
    self = Attributs de Entitiy + Fantome
    graph = Graphe du jeu
    start = position de départ
    goal = position d'arrivée
    """
    def bfs_shortest_path(self, graph, start, goal):
        
        # Parcours en largeur pour trouver le plus court chemin dans le graphe.
        
        queue = deque([(start, [])])  # Chaque élément est (position, chemin_actuel)
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            # Ajouter le chemin actuel à la position
            path = path + [current]

            # Si nous avons atteint le but, retourner le chemin
            if current == goal:
                return path

            # Parcourir les voisins
            for direction, neighbor in graph[current][1].items():
                if neighbor and neighbor not in visited:
                    queue.append((neighbor, path))

        return []  # Aucun chemin trouvé

    """
    Méthode pour trouver la position cible devant
    self = Attributs de Entitiy + Fantome
    graph = Graphe du jeu
    pacman_pos = position de Pacman
    pacman_direction = direction de Pacman
    """
    def find_target_position(self, graph, pacman_pos, pacman_direction):
        
        # Trouver la position cible devant Pac-Man en fonction de sa direction.
        
        current_pos = pacman_pos

        # Avancer dans la direction de Pac-Man jusqu'à ce qu'il n'y ait plus de chemin
        for _ in range(3):  # Avancer de 3 étapes max ou jusqu'à un mur
            next_pos = graph[current_pos][1].get(pacman_direction)
            if next_pos is None:  # Mur ou fin de chemin
                break
            current_pos = next_pos

        return current_pos

    """
    Méthode pour obtenir la direction du fantôme
    self = Attributs de Entitiy + Fantome
    graph = Graphe du jeu
    fantome_pos = position du fantôme
    pacman_pos = position de Pacman
    pacman_direction = direction de Pacman
    """
    def get_fantome_direction(self, graph, fantome_pos, pacman_pos, pacman_direction):
        
        # Calculer la direction que le fantôme doit prendre pour aller devant Pac-Man.
        
        target_pos = self.find_target_position(self, graph, pacman_pos, pacman_direction)

        # Calculer le chemin le plus court
        path = self.bfs_shortest_path(self, graph, fantome_pos, target_pos)

        if len(path) > 1:
            # La première étape du chemin est la position actuelle, donc la deuxième indique la direction
            next_pos = path[1]
            for direction, neighbor in graph[fantome_pos][1].items():
                if neighbor == next_pos:
                    return direction
        return None

        