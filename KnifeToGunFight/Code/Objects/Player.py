import math

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
        GameObject.__init__(self, initial_x_position, initial_y_position, speed = 1)
        self.__DefaultImage = pygame.image.load('../Images/Player.gif').convert()

        ## The current image to show for the player. The default image is used until an action occurs
        ## which would change this from the default.
        self.Image = self.__DefaultImage

        ## The direction the player is currently facing.
        ## (starts facing up by default).
        ## \todo    Should this go into the base GameObject class?
        self.FacingDirection = MoveDirection.Up

        ## The player's sword.
        self.Sword = Sword()

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

    ## Updates the player's current state.
    ## Right now this just handles rotating the player based on
    ## their mouse cursor position.
    ## \author  CJ Harper
    ## \date    09/02/2018
    def Update(self):
        # GET THE POSITION OF THE PLAYER'S CURSOR.
        (mouse_x_position, mouse_y_position) = pygame.mouse.get_pos()

        # ROTATE THE PLAYER.
        # The top of the player is used as the reference rather than the center
        # so the character looks at the cursor.
        mouse_x_position, mouse_y_position = pygame.mouse.get_pos()
        distance_from_player_to_mouse_x = (mouse_x_position - self.Coordinates.x)
        distance_from_player_to_mouse_y = (mouse_y_position - self.Coordinates.y)
        radians_to_rotate = -math.atan2(distance_from_player_to_mouse_y, distance_from_player_to_mouse_x)
        degrees_of_rotation = math.degrees(radians_to_rotate)

        # 90 degrees is subtracted from the rotation since the image spawns facing upward (i.e. rotated 90 degrees from the x-axis)
        # and the arctan function calculates rotation as if the image spawned facing the x-axis.
        degrees_of_rotation_relative_to_image_facing_up = degrees_of_rotation - 90

        # The default image is rotated every time because continuing to rotate the same image
        # over and over will result in degradation of image quality.
        self.Image = pygame.transform.rotate(self.__DefaultImage, degrees_of_rotation_relative_to_image_facing_up)

        # UPDATE THE PLAYER'S FACING DIRECTION.
        # This needs to be updated to try and keep the sword in front of the player.
        # This can be done by looking at the rotated orientation of the player
        # and approximating which of the 4 cardinal directions fit best
        # (reference a unit circle diagram).  The degrees are normalized to
        # fit within a range of [0, 360] to simplify these checks.
        MAX_DEGREES_IN_CIRCLE = 360
        normalized_degrees_of_rotation = degrees_of_rotation % MAX_DEGREES_IN_CIRCLE
        degrees_of_rotation_negative = (normalized_degrees_of_rotation < 0)
        if degrees_of_rotation_negative:
            normalized_degrees_of_rotation += MAX_DEGREES_IN_CIRCLE
        facing_up = (45 <= normalized_degrees_of_rotation) and (normalized_degrees_of_rotation <= 135)
        facing_down = (225 <= normalized_degrees_of_rotation) and (normalized_degrees_of_rotation <= 315)
        facing_left = (135 <= normalized_degrees_of_rotation) and (normalized_degrees_of_rotation <= 225)
        # Note that it's important for this "facing right" check to come last
        # because this is where the degrees of the circle wrap around, meaning
        # an "or" check is necessary.  Alternatively, we could complicate this
        # condition by adding in additional checks for around 360 or 0 degrees.
        facing_right = (315 <= normalized_degrees_of_rotation) or (normalized_degrees_of_rotation <= 45)
        if facing_up:
            self.FacingDirection = MoveDirection.Up
        elif facing_down:
            self.FacingDirection = MoveDirection.Down
        elif facing_left:
            self.FacingDirection = MoveDirection.Left
        elif facing_right:
            self.FacingDirection = MoveDirection.Right

        # UPDATE THE PLAYER POSITION.
        # The rotation repositions the character's image slightly so the
        # player's position needs to be updated to account for this.
        ## \todo Figure out why this causes player to get stuck in walls.
        ## Part of the reason for this is likely that rotating an image results
        ## in the image itself have a larger rectangle to fully encompass the bounds
        ## of the rotated image.  If you add debug rectangle drawing similar to what
        ## exists in the Sword class, you could probably see this.
        #self.Coordinates = self.Image.get_rect(center = self.Coordinates.center)
