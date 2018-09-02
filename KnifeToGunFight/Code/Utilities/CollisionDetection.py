from enum import Enum

import pygame
    
## A mapping of move directions to the relevant coordinates to check for collision.
## \author  Michael Watkinson
## \date    09/01/2018
class MoveDirection(Enum):
    Up = ('TopLeftCornerPosition', 'TopRightCornerPosition')
    Down = ('BottomLeftCornerPosition', 'BottomRightCornerPosition')
    Left = ('TopLeftCornerPosition', 'BottomLeftCornerPosition')
    Right = ('TopRightCornerPosition', 'BottomRightCornerPosition')
    
## Handles if a GameObject class is colliding with another GameObject.
## \param[in]   game_object - The moving GameObject to determine collision for.
## \param[in]   move_direction - An enum value for the direction the GameObject is moving.
## \author  Michael Watkinson
## \date    09/01/2018
def HandleCollision(game_object, move_direction):
    # CHECK FOR COLLISION.
    colliding_object = CheckForCollision(game_object)
    collision_occurred = (colliding_object is not None)
    if not collision_occurred:
        return
    
    # HANDLE NORMAL COLLISION.
    # The GameObjects will just be moved to the closest pixel to the object they collided with.
    if (colliding_object.__class__.__name__ in [Wall, Turret]):
        HandleNormalCollision(game_object, colliding_object, move_direction)
   
## \param[in]   game_object - The moving GameObject to determine collision for.
## \return  The GameObject that the moving GameObject collided with.
## \author  Michael Watkinson
## \date    09/01/2018
def CheckForCollision(game_object, map):
    # CHECK FOR COLLISION.
    objects_to_check = [object for object in map.Map.values() if not (object.__class__.__name__ == 'Player')]
    for object in objects_to_check:
        collision_occurred = game_object.Coordinates.colliderect(object.Coordinates)
        if collision_occurred:
            return object
            
    # NO COLLISION OCCURRED.
    return None
    