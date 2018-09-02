import pygame

from .GameObject import GameObject

## Represents a teleporter that will take you to the next level. 
class Teleporter(GameObject):
    ## The images a teleporter cycles through.
    IMAGES = \
    [
        pygame.image.load('../Images/Teleporter1.gif').convert(),
        pygame.image.load('../Images/Teleporter2.gif').convert(),
        pygame.image.load('../Images/Teleporter3.gif').convert(),
        pygame.image.load('../Images/Teleporter4.gif').convert(),
        pygame.image.load('../Images/Teleporter5.gif').convert(),
        pygame.image.load('../Images/Teleporter6.gif').convert()
    ]

    ## Constructor.
    ## \param[in]   x_position - The x position of the teleporter.
    ## \param[in]   y_position - The y position of the teleporter.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def __init__(self, x_position, y_position):
        GameObject.__init__(self, x_position, y_position)

        ## Set the initial image of the teleporter.
        self.Image = IMAGES[0]
        self.CurrentlyDisplayedImageIndex = 0

        