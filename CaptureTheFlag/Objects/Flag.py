import pygame
from .GameObject import GameObject

## The flag the player is trying to obtain and bring back to the goal.
## \author  CJ Harper
## \date    08/25/2018
class Flag(GameObject):
    ## Constructor.
    ## \param[in]   initial_x_position - The initial X position of the flag.
    ## \param[in]   initial_y_position - The initial Y position of the flag.
    ## \param[in]   image_filepath - The filepath to the image to use for the flag.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, initial_x_position, initial_y_position, image_filepath):
        GameObject.__init__(self, initial_x_position, initial_y_position)
        self.Image = pygame.image.load(image_filepath).convert()

    ## Moves the flag to the specified location.
    ## \param[in]   x_position - The X position to move the flag to.
    ## \param[in]   y_position - The Y position to move the flag to.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def SetPosition(self, x_position, y_position):
        self.XPosition = x_position,
        self.YPosition = y_position
