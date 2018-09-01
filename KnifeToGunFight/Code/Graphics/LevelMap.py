# Class for displaying the map of a level.
from KnifeToGunFight.Code.Objects import GameObject


class LevelMap(object):
    def __init__(self, currentLevelFilePath):
        # Define the path to the current level.
        self.LevelMapFilepath = currentLevelFilePath

        # The height and width of the map.
        self.MapWidth = 0
        self.MapHeight = 0

        # A list of game objects that make up the map.
        self.Map = []

        # Build the map.

    # Opens up the file for the map of the given level and builds the game objects and map.
    def ParseMap(self):
        # READ THE MAP FILE.
        with open(self.LevelMapFilepath, 'r') as map_file:
            map_rows = map_file.readlines()

        # Remove newline characters from the rows.
        map_rows = [row.strip() for row in map_rows]

        # DETERMINE THE HEIGHT AND WIDTH OF THE MAP.
        self.MapHeight = len(map_rows)
        self.MapWidth = len(max(map_rows, key = len))

        # Loop through the file and create game objects for the map.
        current_pixel_row_position = 0
        current_pixel_column_position = 0
        for row_index, row in enumerate(map_rows):
            # Calculate the starting pixels position for objects in the current row.
            y_position = (row_index * GameObject.HeightPixels)

            # Parse the current row into game objects.
            for column_index, ascii_object in enumerate(list(row)):
                # Calculate starting X coordinate.
                x_position = (column_index * GameObject.WidthPixels)

                # Create the GameObject and add it to the map
                object = GameObject(y_position, x_position, row_index, column_index)
                self.Map.append(object)
