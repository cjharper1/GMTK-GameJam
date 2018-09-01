import pygame

# Base class of game objects that will be displayed on the map
class GameObject(object):
    # The width of a a game object in pixels.
    WidthPixels = 32
    # The height of a game object in pixels.
    HeightPixels = 32

    @property
    def TopLeftCornerPosition(self):
        return self.Coordinates.topleft

    @property
    def TopRightCornerPosition(self):
        return self.Coordinates.topright

    @property
    def BottomLeftCornerPosition(self):
        return self.Coordinates.bottomleft

    @property
    def BottomRightCornerPosition(self):
        return self.Coordinates.bottomright

    ## \todo    Figure out what to do about row/column positions so that default 0 values aren't used here.
    ## Can the row/column indices be removed?
    def __init__(self, initial_top_left_x_position, initial_top_left_y_position, row_index = 0, column_index = 0):
        # Create a rectangle object to store the coordinates.
        self.Coordinates = pygame.Rect(
            initial_top_left_x_position,
            initial_top_left_y_position,
            self.WidthPixels,
            self.HeightPixels)

        self.RowIndex = row_index
        self.ColumnIndex = column_index

    ## Moves the game object.
    ## \param[in]   x_movement_in_pixels - The number of pixels to move along the x axis.
    ## \param[in]   y_movement_in_pixels - The number of pixels to move along the y axis.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def Move(self, x_movement_in_pixels = 0, y_movement_in_pixels = 0):
        self.Coordinates = self.Coordinates.move(x_movement_in_pixels, y_movement_in_pixels)
