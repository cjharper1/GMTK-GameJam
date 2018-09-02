import pygame

from Utilities.CollisionDetection import CheckForCollision, MoveDirection

## Base class of game objects that will be displayed on the map.
## \author  Hannah McNeill
## \date    09/01/2018
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

    ## Initializes the game object.
    ## \author  Hannah McNeill
    ## \date    09/01/2018
    def __init__(self, initial_top_left_x_position, initial_top_left_y_position, speed = 0):
        # Create a rectangle object to store the coordinates.
        self.Coordinates = pygame.Rect(
            initial_top_left_x_position,
            initial_top_left_y_position,
            self.WidthPixels,
            self.HeightPixels)
            
        ## The count of pixels this GameObject moves each step.
        self.__Speed = speed
            
    ## Moves the player up one step.
    ## \param[in]   level_map - The LevelMap object to interact with.
    ## \param[in]   allowed_collision_classes - A tuple of classes for objects to allow collision with.  Defaults to [].
    ## \return   A collided object if a collision occurred; None otherwise.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveUp(self, level_map, allowed_collision_classes = ()):
        self.FacingDirection = MoveDirection.Up
        return self.Move(level_map, y_movement_in_pixels = -self.__Speed, allowed_collision_classes = allowed_collision_classes)

    ## Moves the player down one step.
    ## \param[in]   level_map - The LevelMap object to interact with.
    ## \param[in]   allowed_collision_classes - A tuple of classes for objects to allow collision with.  Defaults to [].
    ## \return   A collided object if a collision occurred; None otherwise.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveDown(self, level_map, allowed_collision_classes = ()):
        self.FacingDirection = MoveDirection.Down
        return self.Move(level_map, y_movement_in_pixels = self.__Speed, allowed_collision_classes = allowed_collision_classes)

    ## Moves the player left one step.
    ## \param[in]   level_map - The LevelMap object to interact with.
    ## \param[in]   allowed_collision_classes - A tuple of classes for objects to allow collision with.  Defaults to [].
    ## \return   A collided object if a collision occurred; None otherwise.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveLeft(self, level_map, allowed_collision_classes = ()):
        self.FacingDirection = MoveDirection.Left
        return self.Move(level_map, x_movement_in_pixels = -self.__Speed, allowed_collision_classes = allowed_collision_classes)

    ## Moves the player right one step.
    ## \param[in]   level_map - The LevelMap object to interact with.
    ## \param[in]   allowed_collision_classes - A tuple of classes for objects to allow collision with.  Defaults to [].
    ## \return   A collided object if a collision occurred; None otherwise.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def MoveRight(self, level_map, allowed_collision_classes = ()):
        self.FacingDirection = MoveDirection.Right
        return self.Move(level_map, x_movement_in_pixels = self.__Speed, allowed_collision_classes = allowed_collision_classes)

    ## Moves the game object.
    ## \param[in]   level_map - The LevelMap object to interact with.
    ## \param[in]   x_movement_in_pixels - The number of pixels to move along the x axis.
    ## \param[in]   y_movement_in_pixels - The number of pixels to move along the y axis.
    ## \param[in]   allowed_collision_classes - A tuple of classes for objects to allow collision with.  Defaults to [].
    ## \return   A collided object if a collision occurred; None otherwise.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def Move(self, level_map, x_movement_in_pixels = 0, y_movement_in_pixels = 0, allowed_collision_classes = ()):
        # MOVE THE GAME OBJECT.
        self.Coordinates = self.Coordinates.move(x_movement_in_pixels, y_movement_in_pixels)
        
        # CHECK FOR A COLLISION WITH ANOTHER OBJECT.
        collided_object = CheckForCollision(self, level_map)
        collision_occurred = collided_object is not None
        if collision_occurred:
            if not isinstance(collided_object, allowed_collision_classes):
                self.Coordinates = self.Coordinates.move(-x_movement_in_pixels, -y_movement_in_pixels)
                return None
        
        # UPDATE THE POSITION OF THE GAME OBJECT IN THE LEVEL MAP.
        level_map.MoveObjectInMap(self)
        return collided_object
