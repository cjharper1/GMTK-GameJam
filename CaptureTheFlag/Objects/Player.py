import pygame
from .GameObject import GameObject

## Represents the player character.
## \author  CJ Harper
## \date    08/25/2018
class Player(GameObject):
    ## Constructor.
    ## \param[in]   sprite - The sprite representing this character.
    ## \param[in]   initial_x_position - The initial X position of the character with respect to the game world.
    ## \param[in]   initial_y_position - The initial Y position of the character with respect to the game world.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, initial_x_position : int, initial_y_position : int, image_filepath):
        GameObject.__init__(self, initial_x_position, initial_y_position)
        self.Image = pygame.image.load(image_filepath).convert()

        ## The flag this player is holding. This can be None if the player is not holding a flag.
        ## The player does not spawn holding a flag.
        self.HeldFlag = None

        ## The count of pixels this character moves each step.
        self.__Speed = 1

    ## Moves the player up one step.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def MoveUp(self):
        self.__Move(y_pixels_to_move = -self.__Speed)

    ## Moves the player down one step.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def MoveDown(self):
        self.__Move(y_pixels_to_move = self.__Speed)

    ## Moves the player left one step.
    ## \author  CJ Harper
    ## \date    08/25/2018 
    def MoveLeft(self):
        self.__Move(x_pixels_to_move = -self.__Speed)

    ## Moves the player right one step.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def MoveRight(self):
        self.__Move(x_pixels_to_move = self.__Speed)

    ## Moves the player by the specified number of pixels from their current location.
    ## \param[in]   x_pixels_to_move - The number of pixels to move in the x direction. A negative
    ##      number moves the character left. A positive number moves the character right.
    ## \param[in]   y_pixels_to_move - The number of pixels to move in the y direction. A negative
    ##      number moves the character down. A positive number moves the character up.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __Move(self, x_pixels_to_move = 0, y_pixels_to_move = 0):
        # MOVE THE CHARACTER.
        self.XPosition += x_pixels_to_move
        self.YPosition += y_pixels_to_move

        # MOVE THE FLAG ALONG WITH THE CHARACTER IF THEY ARE HOLDING ONE.
        character_is_holding_flag = self.HeldFlag is not None
        if character_is_holding_flag:
            self.HeldFlag.SetPosition(self.XPosition, self.YPosition)
