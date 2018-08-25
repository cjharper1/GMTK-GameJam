import pygame
from .GameObject import GameObject

## Represents a wall or a boundary in the game that the player cannot cross.
## \author  CJ Harper
## \date    08/25/2018
class Wall(GameObject):
    ## Constructor.
    ## \param[in]   x_position - The x position of the wall.
    ## \param[in]   y_position - The y position of the wall.
    ## \param[in]   image_filepath - The relative filepath to the image to use for the wall.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, x_position, y_position, image_filepath):
        GameObject.__init__(self, x_position, y_position)
        self.Image = pygame.image.load(image_filepath).convert()
    