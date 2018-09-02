# Class for displaying the map of a level.
from Objects.GameObject import GameObject
from Objects.Player import Player
from Objects.Wall import Wall
from Objects.Turret import Turret

from Objects.Teleporter import Teleporter

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
        else:
            return None

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
                
    ## Moves the specified GameObject to a new grid position.
    ## \param[in]   game_object - The GameObject to move.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveObjectInMap(self, game_object):
        # REMOVE THE GAME OBJECT FROM THE MAP.
        self.Map = {key:value for key, value in self.Map.items() if (not value == game_object)}
        
        # GET THE NEW GRID POSITION.
        new_grid_position = self.GetGridPosition(game_object.TopLeftCornerPosition)
        
        # UPDATE THE POSITION.
        self.Map[new_grid_position] = game_object
