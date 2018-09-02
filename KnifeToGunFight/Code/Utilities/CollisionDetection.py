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
    
## \param[in]   game_object - The moving GameObject to determine collision for.
## \return  The GameObject that the moving GameObject collided with.
## \author  Michael Watkinson
## \date    09/01/2018
def CheckForCollision(game_object, map):
    # CHECK FOR COLLISION.
    # The object is allowed to collide with itself.
    objects_to_check = [object for object in map.Map.values() if
        not object == game_object]
    for object in objects_to_check:
        collision_occurred = game_object.Coordinates.colliderect(object.Coordinates)
        if collision_occurred:
            return object
            
    # NO COLLISION OCCURRED.
    return None
    