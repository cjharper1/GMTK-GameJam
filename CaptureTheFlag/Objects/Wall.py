import pygame
import Constants
from .GameObject import GameObject

## Represents a wall or a boundary in the game that the player cannot cross.
## \author  CJ Harper
## \date    08/25/2018
class Wall(GameObject):
    ## Constructor.
    ## \param[in]   x_position - The x position of the wall.
    ## \param[in]   y_position - The y position of the wall.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, x_position, y_position):
        GameObject.__init__(self, x_position, y_position)
        self.Image = pygame.image.load(Constants.WALL_IMAGE_FILEPATH).convert()
    