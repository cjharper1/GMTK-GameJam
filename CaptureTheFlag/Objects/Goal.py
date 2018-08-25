import pygame
import Constants
from .GameObject import GameObject

## Represents the goal the player is trying to get the flag into.
## \author  CJ Harper
## \date    08/25/2018
class Goal(GameObject):
    ## Constructor.
    ## \param[in]   x_position - The x position of the goal.
    ## \param[in]   y_position - The y position of the goal.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, x_position, y_position):
        GameObject.__init__(self, x_position, y_position)
        self.Image = pygame.image.load(Constants.GOAL_IMAGE_FILEPATH).convert()
    