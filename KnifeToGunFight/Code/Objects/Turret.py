import pygame

from .Enemy import Enemy

## Represents a stationary turret that shoots at the player.
class Turret(Enemy):
    def __init__(self, initial_x_position, initial_y_position):
        Enemy.__init__(self, initial_x_position, initial_y_position)
        self.__DefaultImage = pygame.image.load('../Images/Turret.gif').convert()

        ## The default image will be shown upon load because the turret has not performed
        ## any action yet. 
        self.Image = self.__DefaultImage
        