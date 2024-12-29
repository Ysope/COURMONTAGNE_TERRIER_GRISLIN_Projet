from Graph import m_graphe

def FindFurthestFirection(p_fantome_pos, p_target_pos):
    """
    Trouve la direction qui mène à la position la plus éloignée de Pac-Man.
    Args :
        p_fantome_pos (tuple) : Position du fantôme (x, y)
        p_target_pos (tuple) : Position de la cible (x, y)
    Returns :
        str : Meilleure direction
    """
    v_max_distance = -1
    v_best_direction = None

    for v_direction, v_neighbor in (
            m_graphe[p_fantome_pos][1].items()):
        if v_neighbor:  # Vérifie que la position voisine est valide
            v_distance = (CalculateDistance
                          (v_neighbor, p_target_pos))
            if v_distance > v_max_distance:
                v_max_distance = v_distance
                v_best_direction = v_direction

    return v_best_direction

def CalculateDistance(p_pos1, p_pos2):
    """
    Calcule la distance entre deux positions (x1, y1) et (x2, y2).
    Args :
        p_pos1 (tuple) : Position 1 (x1, y1)
        p_pos2 (tuple) : Position 2 (x2, y2)
    Returns :
        float : Distance entre les deux positions
    """
    v_x1, v_y1 = p_pos1
    v_x2, v_y2 = p_pos2
    return ((v_x2 - v_x1) ** 2 +
            (v_y2 - v_y1) ** 2) ** 0.5  # Distance euclidienne
