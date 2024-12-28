from collections import deque
from Graphe import m_graphe

# Méthodes du plus court chemin
def BfsShortestPath(p_start, p_goal):
    """
    Trouve le plus court chemin entre deux positions dans le graphe.
    Args :
        p_start (tuple) : Position de départ (x, y)
        p_goal (tuple) : Position d'arrivée (x, y)
    Returns :
        list : Liste des positions du chemin le plus court
    """
    # Parcours en largeur pour trouver le plus court chemin dans le graphe.
    v_queue = deque([(p_start, [])])  # Chaque élément est (position, chemin_actuel)
    v_visited = set()

    # Parcourir le graphe
    while v_queue:
        # Extraire le premier élément de la file d'attente
        v_current, v_path = v_queue.popleft()
        # Ignorer les positions déjà visitées
        if v_current in v_visited:
            continue
        v_visited.add(v_current)

        # Ajouter le chemin actuel à la position
        v_path = v_path + [v_current]

        # Si nous avons atteint le but, retourner le chemin
        if v_current == p_goal:
            return v_path

        # Parcourir les voisins
        for v_direction, v_neighbor in m_graphe[v_current][1].items():
            if v_neighbor and v_neighbor not in v_visited:
                v_queue.append((v_neighbor, v_path))

    return []  # Aucun chemin trouvé

def FollowTarget(p_fantome, p_positionTarget):
    """Fonction pour suivre une cible en utilisant le BFS.
    Args :
        p_fantome (tuple) : Position actuelle du fantôme (x, y)
        p_positionTarget (tuple) : Position cible (x, y)
    Returns :
        str : Direction à suivre
    """

    v_startPos = p_fantome.GetPosition()
    v_path = BfsShortestPath(v_startPos, p_positionTarget)
    if len(v_path) > 1:
        v_nextPos = v_path[1]  # Se placer derrière Pac-Man
        for v_direction, v_neighbor in m_graphe[v_startPos][1].items():
            if v_neighbor == v_nextPos:
                return v_direction
    return None

def FindTargetPosition(p_pacmanPos, p_pacmanDirection):
    """Trouve la position cible devant Pacman en fonction de sa direction.
    Args :
        p_pacmanPos (tuple) : Position de pacman (x, y)
        p_pacmanDirection (str) : Direction
    Returns :
        tuple : Position cible devant
    """

    # Trouver la position cible devant Pac-Man en fonction de sa direction.
    v_currentPos = p_pacmanPos

    # Avancer dans la direction de Pac-Man jusqu'à ce qu'il n'y ait plus de chemin
    for _ in range(3):  # Avancer de 3 étapes max ou jusqu'à un mur
        v_nextPos = m_graphe[v_currentPos][1].get(p_pacmanDirection)
        if v_nextPos is None:  # Mur ou fin de chemin
            break
        v_currentPos = v_nextPos

    return v_currentPos

def GetFantomeDirection(graph, p_fantomePos,
                        p_pacmanPos, p_pacmanDirection):
    """Calcule la direction que le fantôme doit prendre pour aller devant pacman
    Args :
        graph (dict) : Graphe du labyrinthe
        p_fantomePos (tuple) : Position du fantôme (x, y)
        p_pacmanPos (tuple) : Position de Pacman (x, y)
        p_pacmanDirection (str) : Direction de Pacman
    Returns :
        str : Direction à suivre
    """
    # Calculer la direction que le fantôme doit prendre pour aller devant Pac-Man.
    v_targetPos = FindTargetPosition(p_pacmanPos, p_pacmanDirection)
    # Calculer le chemin le plus court
    v_path = BfsShortestPath(p_fantomePos, v_targetPos)

    if len(v_path) > 1:
        # La première étape du chemin est la position actuelle, donc la deuxième indique la direction
        v_nextPos = v_path[1]
        for v_direction, v_neighbor in graph[p_fantomePos][1].items():
            if v_neighbor == v_nextPos:
                return v_direction
    return None