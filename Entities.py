import pygame as pg             # PYGAME package

class Entity(pg.sprite.Sprite):
    # Constructeur de la classe
    def __init__(self, p_x, p_y, p_sprite, p_vitesse=36, p_intervalle=400):
        """Constructeur de la classe Entity
        Args :
            p_x (int) : Position x de l'entité
            p_y (int) : Position y de l'entité
            p_sprite (str) : Chemin du sprite de l'entité
            p_vitesse (int, optional) : Vitesse de déplacement de l'entité. Defaults to 36
            p_intervalle (int, optional) : Intervalle de temps entre chaque déplacement de l'entité. Defaults to 400
        """
        self.v_x = p_x
        self.v_y = p_y
        self.v_intervalle = p_intervalle
        self.v_direction = None
        self.v_vitesse = p_vitesse
        self.v_sprite = pg.image.load(p_sprite)
        super().__init__()
        self.v_rect = self.v_sprite.get_rect()
        self.v_rect.topleft = (self.v_x, self.v_y)


    def Affichage(self, p_screen):
        """Affichage de l'entité
        Args :
            p_screen (Surface) : Surface sur laquelle l'entité sera affichée
        """
        # Position où l'image sera dessinée
        position = (self.v_x, self.v_y)
        # Dessiner l'image sur la surface
        p_screen.blit(self.v_sprite, position)
        # Mettre à jour l'affichage
        pg.display.flip()


    def SurCase(self):
        """Vérifie si l'entité est sur une case"""
        if self.v_x % 36 == 0 and self.v_y % 36 == 0:
            return True
        else:
            return False
    

    def GetPosition(self):
        """Récupère la position de l'entité sur la grille"""
        return self.v_y // 36 , self.v_x // 36
    

    def Mouvement(self, p_direction, p_screen):
        """Déplacement de l'entité
        Args :
            p_direction (str) : Direction de déplacement de l'entité
            p_screen (Surface) : Surface sur laquelle l'entité sera affichée
        """
        self.v_direction = p_direction
        if self.v_direction == 'HAUT':
            self.v_y -= self.v_vitesse
        elif self.v_direction == 'BAS':
            self.v_y += self.v_vitesse
        elif self.v_direction == 'GAUCHE':
            self.v_x -= self.v_vitesse
            if self.v_x < 0:
                self.v_x = p_screen.get_width() - 36
        elif self.v_direction == 'DROITE':
            self.v_x += self.v_vitesse
            if self.v_x >= p_screen.get_width():
                self.v_x = 0
        self.v_rect.topleft = (self.v_x, self.v_y)
        self.Affichage(p_screen)

    # Gestion des collisions
    def Collision(self, p_entity):
        """Gestion des collisions entre deux entités
        Args :
            p_entity (Entity) : Entité avec laquelle on teste la collision
        """
        if self.v_rect.colliderect(p_entity.v_rect):
            return True


