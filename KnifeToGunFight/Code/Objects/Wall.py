import pygame
from Objects.GameObject import GameObject

## Represents a wall or a boundary in the game that the player cannot cross.
## \author  Michael Watkinson
## \date    09/01/2018
class Wall(GameObject):
    ## Constructor.
    ## \param[in]   x_position - The x position of the wall.
    ## \param[in]   y_position - The y position of the wall.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, x_position, y_position, row_index, column_index):
        GameObject.__init__(self, x_position, y_position, row_index, column_index)
        self.Image = pygame.image.load('../Images/Wall.bmp').convert()
    