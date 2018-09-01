import pygame
from .GameObject import GameObject

## Represents the player character.
## \author  Michael Watkinson
## \date    09/01/2018
class Player(GameObject):
    ## Constructor.
    ## \param[in]   initial_x_position - The initial X position of the character with respect to the game world.
    ## \param[in]   initial_y_position - The initial Y position of the character with respect to the game world.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, initial_x_position : int, initial_y_position : int, row_index, column_index):
        GameObject.__init__(self, initial_x_position, initial_y_position, row_index, column_index)
        self.__DefaultImage = pygame.image.load('../Images/Player.bmp').convert()

        ## The current image to show for the player. The default image is used until an action occurs
        ## which would change this from the default.
        self.Image = self.__DefaultImage


        ## The count of pixels this character moves each step.
        self.__Speed = 1

    ## Moves the player up one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveUp(self):
        self.Move(y_movement_in_pixels = -self.__Speed)

    ## Moves the player down one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveDown(self):
        self.Move(y_movement_in_pixels = self.__Speed)

    ## Moves the player left one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveLeft(self):
        self.Move(x_movement_in_pixels = -self.__Speed)

    ## Moves the player right one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveRight(self):
        self.Move(x_movement_in_pixels = self.__Speed)
