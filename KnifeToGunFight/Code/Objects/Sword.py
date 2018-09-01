import pygame

from Graphics.Color import Color
from Math.Vector2 import Vector2

## A sword that can be used by the player.
## The player can swing the sword to deflect objects.
## \author  Jacob Pike
## \date    09/01/2018
class Sword(object):
    ## The length of the sword in pixels (from handle to tip).
    SWORD_LENGTH_IN_PIXELS = 32
    ## The dimensions of the sword image surface in pixels.
    ## The dimensions are designed to be twice as big as the sword's length.
    ## This allows the sword to be completely horizontal or vertical.
    ## It also supports easy and intuitive rotation, with the sword's handle
    ## being located at the center of the image, which can then be rotated
    ## in any direction.
    IMAGE_DIMENSION_IN_PIXELS = 2 * SWORD_LENGTH_IN_PIXELS
    ## The left x position within the local coordinate frame of the sword's image.
    IMAGE_LEFT_X_LOCAL_POSITION_IN_PIXELS = 0
    ## The right x position within the local coordinate frame of the sword's image.
    ## Since coordinates start at 0, the max position within the image is 1 less than the width.
    IMAGE_RIGHT_X_LOCAL_POSITION_IN_PIXELS = IMAGE_DIMENSION_IN_PIXELS - 1
    ## The top y position within the local coordinate frame of the sword's image.
    IMAGE_TOP_Y_LOCAL_POSITION_IN_PIXELS = 0
    ## The bottom y position within the local coordinate frame of the sword's image.
    ## Since coordinates start at 0, the max position within the image is 1 less than the height.
    IMAGE_BOTTOM_Y_LOCAL_POSITION_IN_PIXELS = IMAGE_DIMENSION_IN_PIXELS - 1
    ## The color used for transparency for the sword.
    TRANSPARENT_COLOR = Color.Magenta

    ## Gets the sword's handle position in screen coordinates.
    @property
    def HandleScreenPosition(self):
        return self.__HandleScreenPosition

    ## Sets the sword's handle position in screen coordinates.
    @HandleScreenPosition.setter
    def HandleScreenPosition(self, value):
        self.__HandleScreenPosition = value
        # When calling code sets the handle position, it's not aware of the
        # larger image rectangle used internally by this class.  To keep
        # the sword appearing on-screen at the position expected by the
        # calling code, the length of the sword needs to be subtracted.
        self.__HandleScreenPosition.X -= Sword.SWORD_LENGTH_IN_PIXELS
        self.__HandleScreenPosition.Y -= Sword.SWORD_LENGTH_IN_PIXELS

    ## Initializes a default sword positioned at (0, 0).
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def __init__(self):
        # CREATE AN EMPTY SPRITE.
        ## The sprite (image) for the sword.
        self.Sprite = pygame.sprite.Sprite()

        ## \todo    Load image from file.
        self.Sprite.image = pygame.Surface((Sword.IMAGE_DIMENSION_IN_PIXELS, Sword.IMAGE_DIMENSION_IN_PIXELS))
        # Color-keying is currently used for transparency due to its simplicity.
        self.Sprite.image.fill(Sword.TRANSPARENT_COLOR.value)
        self.Sprite.image.set_colorkey(Sword.TRANSPARENT_COLOR.value)

        # INITIALIZE REMAINING MEMBER VARIABLES.
        ## The screen position of the sword's handle.
        ## Expected to be set to near the player's position anytime
        ## the sword starts being swung.
        self.__HandleScreenPosition = Vector2(0, 0)
        ## The local position of the handle within the image.
        ## Should be properly initialized whenever the sword starts being swung.
        self.HandleLocalImagePosition = Vector2(0, 0)
        ## The tip position of the handle within the image.
        ## Should be properly initialized whenever the sword starts being swung.
        self.TipLocalImagePosition = Vector2(0, 0)
        ## The current amount of rotation of the sword from its initial
        ## position when being swung.
        self.CurrentRotationAngleInDegrees = 0.0
        ## The destination rotation angle for the sword when it has finished
        ## being completely swung.
        self.DestinationRotationAngleInDegrees = 0.0
        ## True if the sword is currently being swung; false if not.
        self.IsSwinging = False
        ## The width of the sword in pixels.
        self.WidthInPixels = 1
        ## The color of the sword.
        self.Color = Color.Gray

    ## Updates the sword if it's being swung.
    ## \param[in]   time_since_last_update_in_seconds - The time since the sword was last
    ##      updated, in seconds.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def Update(self, time_since_last_update_in_seconds):
        # ONLY UPDATE THE SWORD IF BEING SWUNG.
        # There's nothing to do otherwise.
        if not self.IsSwinging:
            return

        # ROTATE THE SWORD AN APPROPRIATE AMOUNT.
        ROTATION_SPEED_IN_DEGREES_PER_SECOND = 90.0
        rotation_amount_in_degrees = ROTATION_SPEED_IN_DEGREES_PER_SECOND * time_since_last_update_in_seconds
        self.CurrentRotationAngleInDegrees += rotation_amount_in_degrees

        # CHECK IF THE SWORD HAS FINISHED SWINGING.
        finished_swinging = (self.CurrentRotationAngleInDegrees >= self.DestinationRotationAngleInDegrees)
        if finished_swinging:
            self.IsSwinging = False

    ## Renders the sword to screen.
    ## \param[in]   screen - The pygame.Surface to render to.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def Render(self, screen):
        # ONLY RENDER THE SWORD IF IT'S BEING SWUNG.
        if not self.IsSwinging:
            return

        # CLEAR ANY PREVIOUS RENDERINGS OF THE SWORD.
        self.Sprite.image.fill(Sword.TRANSPARENT_COLOR.value)

        # DRAW THE SWORD.
        pygame.draw.line(
            self.Sprite.image, 
            self.Color.value, 
            self.HandleLocalImagePosition.AsXYTuple(), 
            self.TipLocalImagePosition.AsXYTuple(), 
            self.WidthInPixels)

        # ROTATE THE SWORD BASED ON HOW IT'S BEING SWUNG.
        rotated_sword_image = pygame.transform.rotate(self.Sprite.image, self.CurrentRotationAngleInDegrees)

        # ADJUST THE SWORD'S POSITION BASED ON ROTATION.
        # When an image is rotated, the actual size of the bounding rectangle increases to encompass
        # an axis-aligned box that encompasses all of the image.  To avoid having the sword appear
        # to change positions, the handle's position must be adjusted to account for the changing
        # size of the bounding rectangle.
        rotated_image_rect = rotated_sword_image.get_rect()
        original_image_rect = self.Sprite.image.get_rect()
        image_width_increase_in_pixels = rotated_image_rect.width - original_image_rect.width
        image_height_increase_in_pixels = rotated_image_rect.height - original_image_rect.height
        # A copy of the screen position is made to avoid altering the original position.
        handle_screen_position = Vector2(self.HandleScreenPosition.X, self.HandleScreenPosition.Y)
        # Due to this position being the center of rotation, it only needs to be adjusted by
        # half of the change in dimensions of the image's bounding box.
        handle_screen_position.X -= image_width_increase_in_pixels / 2
        handle_screen_position.Y -= image_height_increase_in_pixels / 2

        # DRAW THE SWORD ON THE SCREEN.
        screen.blit(rotated_sword_image, handle_screen_position.AsXYTuple())

        # DRAW DEBUG RECTANGLES IF DEBUGGING IS ENABLED.
        DEBUG_DRAWING_ENABLED = True
        if DEBUG_DRAWING_ENABLED:
            # DRAW A DEBUG RECTANGLE FOR THE UNADJUSTED POSITION.
            DEBUG_RECTANGLE_OUTLINE_WIDTH_IN_PIXELS = 1
            unadjusted_debug_image_rect = rotated_image_rect.move(self.HandleScreenPosition.X, self.HandleScreenPosition.Y)
            pygame.draw.rect(screen, Color.FullGreen.value, unadjusted_debug_image_rect, DEBUG_RECTANGLE_OUTLINE_WIDTH_IN_PIXELS)

            # DRAW A DEBUG RECTANGLE FOR THE ADJUSTED POSITION.
            adjusted_debug_image_rect = rotated_image_rect.move(handle_screen_position.AsXYTuple())
            pygame.draw.rect(screen, Color.Magenta.value, adjusted_debug_image_rect, DEBUG_RECTANGLE_OUTLINE_WIDTH_IN_PIXELS)

    ## Starts swinging the sword left (if not already swinging).
    ## \param[in]   sword_handle_screen_position - The screen position of the sword's handle.
    ##      Intended to be placed such that the sword appears attached to the player.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def StartSwingingFromRightToUp(self, sword_handle_screen_position):
        # DON'T START SWINGING THE SWORD IF IT'S ALREADY BEING SWUNG.
        # The player has to wait for a sword swing to finish before swinging again.
        if self.IsSwinging:
            return

        # GLOBALLY POSITION THE HANDLE AT THE APPROPRIATE POSITION.
        self.HandleScreenPosition = sword_handle_screen_position

        # CONFIGURE THE SWORD FOR SWINGING LEFT.
        self.IsSwinging = True

        # The sword will start being horizontal (from left to right).
        self.__FaceRight()

        # The sword will swing counterclockwise from 0 degrees (horizontal) to 90 degrees (vertical).
        self.CurrentRotationAngleInDegrees = 0.0
        self.DestinationRotationAngleInDegrees = 90.0

    ## Starts swinging the sword right (if not already swinging).
    ## \param[in]   sword_handle_screen_position - The screen position of the sword's handle.
    ##      Intended to be placed such that the sword appears attached to the player.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def StartSwingingFromUpToLeft(self, sword_handle_screen_position):
        # DON'T START SWINGING THE SWORD IF IT'S ALREADY BEING SWUNG.
        # The player has to wait for a sword swing to finish before swinging again.
        if self.IsSwinging:
            return

        # GLOBALLY POSITION THE HANDLE AT THE APPROPRIATE POSITION.
        self.HandleScreenPosition = sword_handle_screen_position

        # CONFIGURE THE SWORD FOR SWINGING RIGHT.
        self.IsSwinging = True

        # The sword will start being horizontal (from right to left).
        self.__FaceRight()

        # The sword will swing clockwise from 0 degrees (horizontal) to 270 degrees (vertical).
        self.CurrentRotationAngleInDegrees = 90.0
        self.DestinationRotationAngleInDegrees = 180.0

    ## Starts swinging the sword down (if not already swinging).
    ## \param[in]   sword_handle_screen_position - The screen position of the sword's handle.
    ##      Intended to be placed such that the sword appears attached to the player.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def StartSwingingFromLeftToDown(self, sword_handle_screen_position):
        # DON'T START SWINGING THE SWORD IF IT'S ALREADY BEING SWUNG.
        # The player has to wait for a sword swing to finish before swinging again.
        if self.IsSwinging:
            return

        # GLOBALLY POSITION THE HANDLE AT THE APPROPRIATE POSITION.
        self.HandleScreenPosition = sword_handle_screen_position

        # CONFIGURE THE SWORD FOR SWINGING DOWN.
        self.IsSwinging = True

        # The sword will start being vertical (from top to bottom).
        self.__FaceRight()

        # The sword will swing counterclockwise from 0 degrees to 90 degrees.
        self.CurrentRotationAngleInDegrees = 180.0
        self.DestinationRotationAngleInDegrees = 270.0

    ## Starts swinging the sword up (if not already swinging).
    ## \param[in]   sword_handle_screen_position - The screen position of the sword's handle.
    ##      Intended to be placed such that the sword appears attached to the player.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def StartSwingingFromDownToRight(self, sword_handle_screen_position):
        # DON'T START SWINGING THE SWORD IF IT'S ALREADY BEING SWUNG.
        # The player has to wait for a sword swing to finish before swinging again.
        if self.IsSwinging:
            return

        # GLOBALLY POSITION THE HANDLE AT THE APPROPRIATE POSITION.
        self.HandleScreenPosition = sword_handle_screen_position

        # CONFIGURE THE SWORD FOR SWINGING UP.
        self.IsSwinging = True

        # The sword will start being vertical (from bottom to top).
        self.__FaceRight()

        # The sword will swing counterclockwise from 0 degrees to 90 degrees.
        self.CurrentRotationAngleInDegrees = 270.0
        self.DestinationRotationAngleInDegrees = 360.0

    ## Has the sword face right horizontally when rendered within its local image.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def __FaceRight(self):
        image_bounding_rectangle = self.Sprite.image.get_rect()
        # The handle should be in the center in order to support easy rotation.
        self.HandleLocalImagePosition = Vector2(image_bounding_rectangle.centerx, image_bounding_rectangle.centery)
        # The tip should be at the right of the image.
        self.TipLocalImagePosition = Vector2(image_bounding_rectangle.right, image_bounding_rectangle.centery)
