from enum import Enum
import sys

import pygame

from Objects.GameObject import GameObject
from Objects.Wall import Wall

## A mapping of player move direction to the relevant coordinates to check for collision.
## \author  Michael Watkinson
## \date    08/25/2018
class MoveDirection(Enum):
    Up = ('TopLeftCornerPosition', 'TopRightCornerPosition')
    Down = ('BottomLeftCornerPosition', 'BottomRightCornerPosition')
    Left = ('TopLeftCornerPosition', 'BottomLeftCornerPosition')
    Right = ('TopRightCornerPosition', 'BottomRightCornerPosition')

## Handles player input events and key presses.
## \param[in]   game_map - The GameMap object containing all of the game objects.
## \author  Michael Watkinson
## \date    08/25/2018
def HandleInput(game_map):
    # HANDLE QUIT EVENTS.
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_ESCAPE:
                sys.exit()

    # GET THE PLAYER OBJECT FROM THE MAP.
    player = game_map.GetPlayer()
    
    # HANDLE PLAYER MOVEMENT.
    currently_pressed_keys = pygame.key.get_pressed()
    if currently_pressed_keys[pygame.K_w]:
        player.MoveUp()
        HandleCollision(game_map, player, MoveDirection.Up)
    if currently_pressed_keys[pygame.K_a]:
        player.MoveLeft()
        HandleCollision(game_map, player, MoveDirection.Left)
    if currently_pressed_keys[pygame.K_s]:
        player.MoveDown()
        HandleCollision(game_map, player, MoveDirection.Down)
    if currently_pressed_keys[pygame.K_d]:
        player.MoveRight()
        HandleCollision(game_map, player, MoveDirection.Right)
    
## Handles if the player is colliding with another game object.
## \param[in]   game_map - The GameMap object containing all of the game objects.
## \param[in]   player - The Player object to determine collision for.
## \param[in]   move_direction - An enum value for the direction the player is moving.
## \author  Michael Watkinson
## \date    08/25/2018
def HandleCollision(game_map, player, move_direction):
    # CHECK FOR COLLISION.
    colliding_object, coordinates = CheckForCollision(game_map, player, move_direction)
    collision_occurred = (colliding_object is not None)
    if not collision_occurred:
        return
    
    # HANDLE WALL COLLISION.
    if (isinstance(colliding_object, Wall)):
        HandleWallCollision(player, colliding_object, coordinates, move_direction)

## \param[in]   game_map - The GameMap object containing all of the game objects.
## \param[in]   player_object - The Player object to determine collision for.
## \param[in]   move_direction - An enum value for the direction the player is moving.
## \return  A two-tuple of the game object that the player collided with and the coordinates
##      where the collision occurred, if found; A two-tuple of None otherwise.
## \author  Michael Watkinson
## \date    08/25/2018
def CheckForCollision(game_map, player_object, move_direction):
    # CHECK BOTH COORDINATES AFFECTED BY MOVING IN THE SPECIFIED DIRECTION.
    collision_occurred = False
    for coordinate_name in move_direction.value:
        # Get the player's coordinate.
        coordinates = getattr(player_object, coordinate_name)
        
        # Get the grid position corresponding the player's new position.
        grid_position = game_map.GetGridPosition(coordinates)
        
        # Check for an object occupying the same space.
        colliding_object = game_map.Map.get(grid_position, None)
        collision_occurred = (colliding_object is not None)
        if collision_occurred:
            return (colliding_object, coordinates)
            
    # NO COLLISION OCCURRED.
    return (None, None)
    
## Handles a wall collision by moving the player as close to the border of the wall as possible.
## \param[in]   player_object - The Player object to determine collision for.
## \param[in]   wall_object - The Wall object that the player collided with.
## \param[in]   coordinates - The coordinates at which the collision occurred.
## \param[in]   move_direction - An enum value for the direction the player is moving.
## \author  Michael Watkinson
## \date    08/25/2018
def HandleWallCollision(player_object, wall_object, coordinates, move_direction):
    if (move_direction == MoveDirection.Up):
        wall_bottom_x, wall_bottom_y = wall_object.BottomLeftCornerPosition
        player_top_x, player_top_y = player_object.TopLeftCornerPosition
        pixels_to_move = (wall_bottom_y - player_top_y)
        player_object.Move(x_movement_in_pixels = 0, y_movement_in_pixels = pixels_to_move)
        
    elif (move_direction == MoveDirection.Down):
        wall_top_x, wall_top_y = wall_object.TopLeftCornerPosition
        player_bottom_x, player_bottom_y = player_object.BottomLeftCornerPosition
        pixels_to_move = (player_bottom_y - wall_top_y) + 1
        player_object.Move(x_movement_in_pixels = 0, y_movement_in_pixels = -pixels_to_move)
    
    elif (move_direction == MoveDirection.Left):
        wall_bottom_x, wall_bottom_y = wall_object.BottomRightCornerPosition
        player_top_x, player_top_y = player_object.TopLeftCornerPosition
        pixels_to_move = (wall_bottom_x - player_top_x)
        player_object.Move(x_movement_in_pixels = pixels_to_move, y_movement_in_pixels = 0)
    
    elif (move_direction == MoveDirection.Right):
        wall_bottom_x, wall_bottom_y = wall_object.BottomLeftCornerPosition
        player_top_x, player_top_y = player_object.TopRightCornerPosition
        pixels_to_move = (player_top_x - wall_bottom_x) + 1
        player_object.Move(x_movement_in_pixels = -pixels_to_move, y_movement_in_pixels = 0)
    