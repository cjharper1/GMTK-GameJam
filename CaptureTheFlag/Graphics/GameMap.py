from enum import Enum
import sys

import Constants
from Objects.Flag import Flag
from Objects.GameObject import GameObject
from Objects.Goal import Goal
from Objects.Player import Player
from Objects.Wall import Wall

## A mapping of ASCII character map objects to game object classes.
## \author  Michael Watkinson
## \date    08/25/2018
class ObjectMapping(Enum):
    F = ('Flag', Constants.FLAG_IMAGE_FILEPATH)
    O = ('Goal', Constants.GOAL_IMAGE_FILEPATH)
    P = ('Player', Constants.PLAYER_IMAGE_FILEPATH)
    X = ('Wall', Constants.WALL_IMAGE_FILEPATH)

## The map containing all game object coordinates.
## \author  Michael Watkinson
## \date    08/25/2018
class GameMap(object):
    ## Initializes the map based on the provided filepath.
    ## \param[in]   map_filepath - The filepath to the file containing the ASCII representation of the map.
    ## \author  Michael Watkinson
    ## \date    08/25/2018
    def __init__(self, map_filepath):
        # STORE INSTANCE VARIABLES.
        ## The filepath of the map file used to generate the game map.
        self.MapFilepath = map_filepath
        ## The height of the map in terms of game objects.
        self.MapHeight = 0
        ## The width of the map in terms of game objects.
        self.MapWidth = 0
        ## The map containing all of the game objects.
        self.Map = []
        
        # PARSE MAP FILE.
        self.ParseMap()
        
    ## Parses the map file to create the in game map.
    ## \author  Michael Watkinson
    ## \date    08/25/2018
    def ParseMap(self):
        # READ THE MAP FILE.
        with open(self.MapFilepath, 'r') as map_file:
            map_rows = map_file.readlines()
        
        # Remove newline characters from the rows.
        map_rows = [row.strip() for row in map_rows]
        
        # DETERMINE THE HEIGHT AND WIDTH OF THE MAP.
        self.MapHeight = len(map_rows)
        self.MapWidth = len(max(map_rows, key = len))
        
        # CREATE GAME OBJECTS FOR THE MAP.
        # Parse each row into game objects.
        current_y_position = 0
        current_x_position = 0
        for row_index, row in enumerate(map_rows):
            # Calculate the starting y position for objects in the current row.
            y_position = (row_index * GameObject.HeightPixels)
        
            # Parse the current row into game objects.
            for column_index, ascii_object in enumerate(list(row)):
                # Calculate starting X coordinate.
                x_position = (column_index * GameObject.WidthPixels)
            
                # Create the game object for the current ASCII object.
                try:
                    # Parse the game object using the ObjectMapping class.
                    object_class_name, image_filepath = ObjectMapping[ascii_object].value
                    object = getattr(sys.modules[__name__], object_class_name)(
                        x_position,
                        y_position)
                    self.Map.append(object)
                except KeyError:
                    # If the mapping didn't exist, then the current space is unoccupied.
                    pass
                  
    ## Returns the player object from the game map.
    ## \author  Michael Watkinson
    ## \date    08/25/2018
    def GetPlayer(self):
        # SEARCH THROUGH ALL THE OBJECTS IN THE MAP FOR THE PLAYER OBJECT.
        for object in self.Map:
            # Check if the current object is the player.
            player_found = (isinstance(object, Player))
            if player_found:
                return object
    