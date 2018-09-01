import pygame
from .GameObject import GameObject


class Turret(GameObject):
    def __init__(self, initial_x_position, initial_y_position, row_index, column_index):
        GameObject.__init__(self, initial_x_position, initial_y_position, row_index, column_index)
        self.__DefaultImage = pygame.image.load('../Images/Turret.bmp').convert()

        ## The current image to show for the player. The default image is used until an action occurs
        ## which would change this from the default.
        self.Image = self.__DefaultImage