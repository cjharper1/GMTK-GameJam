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

    def __init__(self, initial_top_left_x_position, initial_top_left_y_position, row_index, column_index):
        # Create a rectangle object to store the coordinates.
        self.Coordinates = pygame.Rect(
            initial_top_left_x_position,
            initial_top_left_y_position,
            self.WidthPixels,
            self.HeightPixels)

        self.RowIndex = row_index
        self.ColumnIndex = column_index
