from enum import Enum

import pygame

from Objects.Turret import Turret
from Objects.Wall import Wall

## A mapping of move directions to the relevant coordinates to check for collision.
## \author  Michael Watkinson
## \date    09/01/2018
class MoveDirection(Enum):
    Up = ('TopLeftCornerPosition', 'TopRightCornerPosition')
    Down = ('BottomLeftCornerPosition', 'BottomRightCornerPosition')
    Left = ('TopLeftCornerPosition', 'BottomLeftCornerPosition')
    Right = ('TopRightCornerPosition', 'BottomRightCornerPosition')
    
## Handles if a GameObject class is colliding with another GameObject.
## \param[in]   level_map - The GameMap object containing all of the game objects.
## \param[in]   game_object - The moving GameObject to determine collision for.
## \param[in]   move_direction - An enum value for the direction the GameObject is moving.
## \author  Michael Watkinson
## \date    09/01/2018
def HandleCollision(level_map, game_object, move_direction):
    # CHECK FOR COLLISION.
    colliding_object, coordinates = CheckForCollision(level_map, game_object, move_direction)
    collision_occurred = (colliding_object is not None)
    if not collision_occurred:
        return
    
    # HANDLE NORMAL COLLISION.
    # The GameObjects will just be moved to the closest pixel to the object they collided with.
    if (isinstance(colliding_object, (Wall, Turret))):
        HandleNormalCollision(game_object, colliding_object, coordinates, move_direction)
   
## \param[in]   level_map - The GameMap object containing all of the game objects.
## \param[in]   game_object - The moving GameObject to determine collision for.
## \param[in]   move_direction - An enum value for the direction the GameObject is moving.
## \return  A two-tuple of the GameObject that the moving GameObject collided with and the coordinates
##      where the collision occurred, if found; A two-tuple of None otherwise.
## \author  Michael Watkinson
## \date    09/01/2018
def CheckForCollision(level_map, game_object, move_direction):
    # CHECK BOTH COORDINATES AFFECTED BY MOVING IN THE SPECIFIED DIRECTION.
    collision_occurred = False
    for coordinate_name in move_direction.value:
        # Get the moving GameObject's coordinate.
        coordinates = getattr(game_object, coordinate_name)
        
        # Get the grid position corresponding the moving GameObject's new position.
        grid_position = level_map.GetGridPosition(coordinates)
        
        # Check for an object occupying the same space.
        colliding_object = level_map.Map.get(grid_position, None)
        collision_occurred = (colliding_object is not None)
        if collision_occurred:
            return (colliding_object, coordinates)
            
    # NO COLLISION OCCURRED.
    return (None, None)
    
## Handles normal collision by moving the GameObject as close to the border of the collided GameObject as possible.
## \param[in]   game_object - The moving GameObject to determine collision for.
## \param[in]   collided_object - The GameObject that the moving GameObject collided with.
## \param[in]   coordinates - The coordinates at which the collision occurred.
## \param[in]   move_direction - An enum value for the direction the GameObject is moving.
## \author  Michael Watkinson
## \date    09/01/2018
def HandleNormalCollision(game_object, collided_object, coordinates, move_direction):
    if (move_direction == MoveDirection.Up):
        collided_object_bottom_x, collided_object_bottom_y = collided_object.BottomLeftCornerPosition
        game_object_top_x, game_object_top_y = game_object.TopLeftCornerPosition
        pixels_to_move = (collided_object_bottom_y - game_object_top_y)
        game_object.Move(x_movement_in_pixels = 0, y_movement_in_pixels = pixels_to_move)
        
    elif (move_direction == MoveDirection.Down):
        collided_object_top_x, collided_object_top_y = collided_object.TopLeftCornerPosition
        game_object_bottom_x, game_object_bottom_y = game_object.BottomLeftCornerPosition
        pixels_to_move = (game_object_bottom_y - collided_object_top_y) + 1
        game_object.Move(x_movement_in_pixels = 0, y_movement_in_pixels = -pixels_to_move)
    
    elif (move_direction == MoveDirection.Left):
        collided_object_bottom_x, collided_object_bottom_y = collided_object.BottomRightCornerPosition
        game_object_top_x, game_object_top_y = game_object.TopLeftCornerPosition
        pixels_to_move = (collided_object_bottom_x - game_object_top_x)
        game_object.Move(x_movement_in_pixels = pixels_to_move, y_movement_in_pixels = 0)
    
    elif (move_direction == MoveDirection.Right):
        collided_object_bottom_x, collided_object_bottom_y = collided_object.BottomLeftCornerPosition
        game_object_top_x, game_object_top_y = game_object.TopRightCornerPosition
        pixels_to_move = (game_object_top_x - collided_object_bottom_x) + 1
        game_object.Move(x_movement_in_pixels = -pixels_to_move, y_movement_in_pixels = 0)
    