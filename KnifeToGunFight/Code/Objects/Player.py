import pygame

from Math.Vector2 import Vector2
from Objects.GameObject import GameObject
from Objects.Sword import Sword
from Utilities.CollisionDetection import MoveDirection

## Represents the player character.
## \author  Michael Watkinson
## \date    09/01/2018
class Player(GameObject):
    ## The screen position of the player's hand, which may change
    ## depending on which direction the player is facing.
    @property
    def HandScreenPosition(self):
        player_hand_position = None

        # GET THE HAND POSITION BASED ON THE FACING DIRECTION.
        # Note that the positions below aren't strictly the hand position of the player
        # image right now, but they're what appears to look best.  The general approach
        # for the positions below is that they're centered along one of the borders of
        # the player.
        if MoveDirection.Up == self.FacingDirection:
            player_hand_position = Vector2(self.Coordinates.centerx, self.Coordinates.top)
        elif MoveDirection.Down == self.FacingDirection:
            player_hand_position = Vector2(self.Coordinates.centerx, self.Coordinates.bottom)
        elif MoveDirection.Left == self.FacingDirection:
            player_hand_position = Vector2(self.Coordinates.left, self.Coordinates.centery)
        elif MoveDirection.Right == self.FacingDirection:
            player_hand_position = Vector2(self.Coordinates.right, self.Coordinates.centery)
        else:
            # Default to using center position so that a valid position
            # that is close to the player is used.
            player_hand_position = Vector2(self.Coordinates.centerx, self.Coordinates.centery)

        return player_hand_position

    ## Constructor.
    ## \param[in]   initial_x_position - The initial X position of the character with respect to the game world.
    ## \param[in]   initial_y_position - The initial Y position of the character with respect to the game world.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, initial_x_position : int, initial_y_position : int):
        GameObject.__init__(self, initial_x_position, initial_y_position)
        self.__DefaultImage = pygame.image.load('../Images/Player.gif').convert()

        ## The current image to show for the player. The default image is used until an action occurs
        ## which would change this from the default.
        self.Image = self.__DefaultImage

        ## The count of pixels this character moves each step.
        self.__Speed = 1

        ## The direction the player is currently facing.
        ## (starts facing up by default).
        ## \todo    Should this go into the base GameObject class?
        self.FacingDirection = MoveDirection.Up

        ## The player's sword.
        self.Sword = Sword()

    ## Moves the player up one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveUp(self):
        self.FacingDirection = MoveDirection.Up
        self.Move(y_movement_in_pixels = -self.__Speed)

    ## Moves the player down one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveDown(self):
        self.FacingDirection = MoveDirection.Down
        self.Move(y_movement_in_pixels = self.__Speed)

    ## Moves the player left one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveLeft(self):
        self.FacingDirection = MoveDirection.Left
        self.Move(x_movement_in_pixels = -self.__Speed)

    ## Moves the player right one step.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveRight(self):
        self.FacingDirection = MoveDirection.Right
        self.Move(x_movement_in_pixels = self.__Speed)

    ## Starts swinging the player's sword if it's not already swinging.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def SwingSword(self):
        # SWING THE SWORD BASED ON THE PLAYER'S FACING DIRECTION.
        if MoveDirection.Up == self.FacingDirection:
            self.Sword.StartSwingingFromRightToUp(self.HandScreenPosition)
        elif MoveDirection.Down == self.FacingDirection:
            self.Sword.StartSwingingFromLeftToDown(self.HandScreenPosition)
        elif MoveDirection.Left == self.FacingDirection:
            self.Sword.StartSwingingFromUpToLeft(self.HandScreenPosition)
        elif MoveDirection.Right == self.FacingDirection:
            self.Sword.StartSwingingFromDownToRight(self.HandScreenPosition)
