import pygame

from Objects.GameObject import GameObject
from Objects.Enemy import Enemy
from Objects.LittleRobot import LittleRobot
from Objects.Player import Player
from Objects.Wall import Wall
from Objects.Teleporter import Teleporter
from Objects.Turret import Turret

# A mapping of ASCII character map objects to game object classes.
class GameObjectMapping(object):
    @staticmethod
    def buildObject(ascii_object, x_position, y_position):
        if ascii_object == 'P':
            return Player(x_position, y_position)
        if ascii_object == 'X':
            return Wall(x_position, y_position)
        if ascii_object == 'T':
            return Turret(x_position, y_position)
        if ascii_object == 'D':
            return Teleporter(x_position, y_position)
        if ascii_object == 'S':
            return LittleRobot(x_position, y_position)
        else:
            return None

# Class for displaying the map of a level.
class LevelMap(object):
    def __init__(self, currentLevelFilePath):
        # Define the path to the current level.
        self.LevelMapFilepath = currentLevelFilePath

        # The width of the map.
        self.MapWidth = 0
        ## The height of the map.
        self.MapHeight = 0
        ## The map containing all of the game objects as a dictionary.  They key of the dictionary is
        ## a two-tuple of the coordinates of the block the object is currently occupying and the value is the object.
        self.Map = {}
        ## The lasers on the map. These are stored separately since they can occupy the same space as other objects.
        self.Lasers = []
        
        # Build the map.
        self.ParseMap()

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
        for row_index, row in enumerate(map_rows):
            # Calculate the starting pixels position for objects in the current row.
            y_position = (row_index * GameObject.HeightPixels)

            # Parse the current row into game objects.
            for column_index, ascii_object in enumerate(list(row)):
                # Calculate starting X coordinate.
                x_position = (column_index * GameObject.WidthPixels)

                # Create the GameObject and add it to the map
                mappedObject = GameObjectMapping.buildObject(ascii_object, x_position, y_position)

                if mappedObject is not None:
                    self.Map[(column_index, row_index)] = mappedObject

    ## Gets the player object from the game map.
    ## \return  The Player object.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def GetPlayer(self):
        # SEARCH THROUGH ALL THE OBJECTS IN THE MAP FOR THE PLAYER OBJECT.
        for object in self.Map.values():
            # Check if the current object is the player.
            player_found = (isinstance(object, Player))
            if player_found:
                return object
                
    ## Gets all enemies from the game map.
    ## \return  A list of all Enemy objects on the map.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def GetEnemies(self):
        # SEARCH THROUGH ALL THE OBJECTS IN THE MAP FOR THE ENEMY OBJECTS.
        return [object for object in self.Map.values() if isinstance(object, Enemy)]
        
    ## Gets all walls from the game map.
    ## \return  A list of all Wall objects on the map.
    ## \author  Michael Watkinson
    ## \date    09/02/2018
    def GetWalls(self):
        # SEARCH THROUGH ALL THE OBJECTS IN THE MAP FOR THE ENEMY OBJECTS.
        return [object for object in self.Map.values() if isinstance(object, Wall)]

    ## Gets the teleporter object from the game map.
    ## \return  The Teleporter object.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def GetTeleporter(self):
        # SEARCH THROUGH ALL THE OBJECTS IN THE MAP FOR THE TELEPORTER OBJECT.
        for object in self.Map.values():
            # Check if the current object is the teleporter.
            teleporter_found = (isinstance(object, Teleporter))
            if teleporter_found:
                return object
                
    ## Gets the grid position for the specified coordinates.
    ## \param[in]   coordinates - A two-tuple of the X and Y coordinates.
    ## \return  A two-tuple for the row and column indices of the grid position.
    ## Handles the main execution of the game.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def GetGridPosition(self, coordinates):
        # DETERMINE THE GRID POSITION OF THE COORDINATES.
        x_coordinate, y_coordinate = coordinates
        grid_row_index = int(y_coordinate / GameObject.HeightPixels)
        grid_column_index = int(x_coordinate / GameObject.WidthPixels)
        return (grid_column_index, grid_row_index)
                
    ## Checks if a given game object is within bounds of the map.
    ## \param[in]   game_object - The GameObject to check.
    ## \return  True if the object is in bounds; false otherwise.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    def ObjectInBounds(self, game_object):
        # DEFINE A BOUNDING RECTANGLE FOR THE MAP.
        map_max_x_screen_position = self.MapWidth * GameObject.WidthPixels
        map_max_y_screen_position = self.MapHeight * GameObject.HeightPixels
        map_bounding_rectangle = pygame.Rect(0, 0, map_max_x_screen_position, map_max_y_screen_position)
        
        # CHECK OF THE GAME OBJECT IS WITHIN BOUNDS.
        object_in_bounds = map_bounding_rectangle.colliderect(game_object.Coordinates)
        return object_in_bounds

    ## Moves the specified GameObject to a new grid position.
    ## \param[in]   game_object - The GameObject to move.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveObjectInMap(self, game_object):
        # REMOVE THE OBJECT FROM THE MAP.
        self.RemoveObject(game_object)

        # GET THE NEW GRID POSITION.
        new_grid_position = self.GetGridPosition(game_object.TopLeftCornerPosition)
        
        # UPDATE THE POSITION.
        self.Map[new_grid_position] = game_object

    ## Removes an object from the map.
    ## \param[in]   game_object - The object to remove.
    ## \author  CJ Harper
    ## \date    09/02/2018
    def RemoveObject(self, game_object):
        # REMOVE THE GAME OBJECT FROM THE MAP.
        self.Map = {key:value for key, value in self.Map.items() if (not value == game_object)}
