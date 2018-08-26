from enum import Enum
import math
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
    F = 'Flag'
    O = 'Goal'
    P = 'Player'
    X = 'Wall'

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
        ## The map containing all of the game objects as a dictionary.  The key of the dictionary is
        ## a two-tuple of the coordinates of the block the object is currently occupying and the 
        ## value is the object.
        self.Map = {}
        
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
                    object_class_name = ObjectMapping[ascii_object].value
                    object = getattr(sys.modules[__name__], object_class_name)(
                        x_position,
                        y_position)
<<<<<<< HEAD
                    self.Map[(row_index, column_index)] = object
=======
                    self.Map.append(object)
>>>>>>> d3485473ea3b8055e5f40346b67a450c0014a204
                except KeyError:
                    # If the mapping didn't exist, then the current space is unoccupied.
                    pass
                  
    ## Gets the player object from the game map.
    ## \return  The Player object.
    ## \author  Michael Watkinson
    ## \date    08/25/2018
    def GetPlayer(self):
        # SEARCH THROUGH ALL THE OBJECTS IN THE MAP FOR THE PLAYER OBJECT.
        for object in self.Map.values():
            # Check if the current object is the player.
            player_found = (isinstance(object, Player))
            if player_found:
                return object
                
    ## Gets the grid position for the specified coordinates.
    ## \param[in]   coordinates - A two-tuple of the X and Y coordinates.
    ## \return  A two-tuple for the row and column indices of the grid position.
    ## \author  Michael Watkinson
    ## \date    08/25/2018
    def GetGridPosition(self, coordinates):
        # DETERMINE THE GRID POSITION OF THE COORDINATES.
        x_coordinate, y_coordinate = coordinates
        grid_row_index = math.ceil(y_coordinate / GameObject.HeightPixels)
        grid_column_index = math.ceil(x_coordinate / GameObject.WidthPixels)
        return (grid_row_index, grid_column_index)
        