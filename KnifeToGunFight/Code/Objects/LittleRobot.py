import pygame

from .Enemy import Enemy

## Represents a robot that can chase and shoot at the player.
class LittleRobot(Enemy):
    def __init__(self, initial_x_position, initial_y_position):
        Enemy.__init__(self, initial_x_position, initial_y_position, speed = 1)
        self.__DefaultImage = pygame.image.load('../Images/LittleRobot.gif').convert()

        ## The default image will be shown upon load because the robot has not performed
        ## any action yet. 
        self.Image = self.__DefaultImage
        