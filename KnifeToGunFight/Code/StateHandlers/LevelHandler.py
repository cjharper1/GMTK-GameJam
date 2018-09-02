from itertools import islice
import math
import os
import sys

import pygame

from .StateHandler import StateHandler
from Graphics.LevelMap import LevelMap
from Math.Vector2 import Vector2
from Objects.GameObject import GameObject
from Objects.Player import Player
from Objects.Teleporter import Teleporter
from Objects.Turret import Turret
from Utilities.CollisionDetection import MoveDirection
from Utilities.Pathing import Pathing

## The handler class for controlling a level of the game.
## \author  Michael Watkinson
## \date    09/01/2018
class LevelHandler(StateHandler):
    ## Initializes the level handler.
    ## \param[in]  game_window - The GameWindow object to display the level on.
    ## \param[in]   level_filepath - The filepath of the level to load.  Defaults to None.
    ##      If None is provided, the first level will be played.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, game_window, level_filepath = None):
        # INITIALIZE THE HANDLER.
        # Only initialize the background music for the first level.
        # It will be kept running throughout the game.
        audio = None
        level_filepath = level_filepath if (level_filepath is not None) else '../Maps/Level1.txt'
        start_background_music = ('Level1' in level_filepath)
        if start_background_music:
            audio = {
                'BackgroundMusic': '../Audio/background_music.mp3'}
        StateHandler.__init__(self, audio = audio)
        
        # INITIALIZE INSTANCE VARIABLES.
        self.GameWindow = game_window
        self.LevelFilepath = level_filepath
        self.Map = LevelMap(self.LevelFilepath)
        self.Pathing = Pathing(self.Map)

    ## Runs the level and and handles displaying all graphics, playing sounds, and player interaction.
    ## \return  The next StateHandler class to be run in the main game loop.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def Run(self):
        # HANDLE INTERACTION.
        # The clock is used to determine elapsed time between frames.
        clock = pygame.time.Clock()
        while True:
            # UPDATE THE GAME CLOCK.
            # Ticking will automatically delay the game if needed to achieve the desired frame rate.
            time_since_last_update_in_ms = clock.tick(self.MaxFramesPerSecond)
            MILLISECONDS_PER_SECOND = 1000
            time_since_last_update_in_seconds = (time_since_last_update_in_ms / MILLISECONDS_PER_SECOND)

            # UPDATE THE TELEPORTER ANIMATION.
            teleporter = self.Map.GetTeleporter()
            if teleporter is not None:
                teleporter.Update(time_since_last_update_in_seconds)

            # Set player position and rotation.
            #position = pygame.mouse.get_pos()
            #angle = math.atan2(int(position[1] - (self.PlayerPosition [1])), int(position[0] - self.PlayerPosition [0] + 26))
            #player_rotated = pygame.transform.rotate(self.Player, 360 - angle * 57.29)
            #player_position_1 = (self.PlayerPosition [0] - player_rotated.get_rect().width / 2, self.PlayerPosition [1] - player_rotated.get_rect().height / 2)
            #self.Screen.blit(player_rotated, player_position_1)
            
            # HANDLE PLAYER INTERACTION.
            move_to_next_level = self.HandlePlayerInteraction()
            
            # HANDLE MOVING TO NEXT LEVEL.
            if move_to_next_level:
                # Form the filepath for the next level.
                # Increment the level number in the filename by 1.
                next_level_index = (int(os.path.basename(self.LevelFilepath).replace('Level', '').replace('.txt', '')) + 1)
                next_level_filepath = os.path.join(os.path.dirname(self.LevelFilepath), 'Level{}.txt'.format(next_level_index))
                
                # Prepare the handler for the next level.
                return LevelHandler(self.GameWindow, next_level_filepath)

            # ALLOW ENEMIES TO REACT TO THE PLAYER.
            self.UpdateEnemies()

            # UPDATE GAME OBJECTS BASED ON ELAPSED TIME.
            ## \todo    Update all objects, not just sword.
            player = self.Map.GetPlayer()
            # The sword's handle position should follow the player when the player moves.
            player.Sword.HandleScreenPosition = player.HandScreenPosition
            player.Sword.Update(time_since_last_update_in_seconds)

            # HANDLE SWORD COLLISIONS IF THE SWORD IS OUT.
            if player.Sword.IsSwinging:
                # CHECK FOR COLLISIONS OF THE SWORD WITH OTHER GAME OBJECTS.
                for grid_coordinates, game_object in self.Map.Map.items():
                    # CHECK FOR COLLISIONS WITH PROJECTILES.
                    ## \todo    Switch this to projectiles in order to deflect them.
                    ## Turrets are just used now for testing.
                    if isinstance(game_object, Turret):
                        # DETERMINE IF THE SWORD HIT THE PROJECTILE.
                        sword_bounding_rectangle = player.Sword.BoundingScreenRectangle
                        projectile_rectangle = game_object.Coordinates
                        sword_collides_with_projectile = sword_bounding_rectangle.colliderect(projectile_rectangle)
                        if sword_collides_with_projectile:
                            ## \todo    Remove debug message.  A debug rectangle would be drawn instead,
                            ## but it's not easy to do that right now since all rendering is encapsulated
                            ## in GameWindow.Update().
                            projectile_debug_message = f'Collided @ time {pygame.time.get_ticks()} with {projectile_rectangle}.'
                            print(projectile_debug_message)

                            # REFLECT THE PROJECTILE.
                            ## \todo    Implement reflection!

            # UPDATE THE SCREEN.
            self.GameWindow.Update(self.Map)
           
    ## Handles player input from events, key presses and mouse interaction.
    ## \return  True if the player used the teleporter; False otherwise.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def HandlePlayerInteraction(self):
        # GET THE PLAYER OBJECT FROM THE MAP.
        player = self.Map.GetPlayer()

        # HANDLE QUIT EVENTS.
        for event in pygame.event.get():
            # Check if the X button of the window was clicked.
            if event.type is pygame.QUIT:
                # Quit the game.
                pygame.quit()
                sys.exit()
                
            # Check if a key was newly pressed down.
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    sys.exit()
                    pygame.quit()
                ## \todo    Do we want space to trigger swinging sword or something else?
                # Sword swinging is currently handled here (with keyboard events, rather
                # then just checking currently pressed keys) in order to have sword swinging
                # only triggered on new key presses, not be trigger when keys are held down.
                if event.key is pygame.K_SPACE:
                    # SWING THE PLAYER'S SWORD.
                    player.SwingSword()
        
        # HANDLE PLAYER MOVEMENT.
        collided_object = None
        allowed_collision_classes = (Teleporter)
        currently_pressed_keys = pygame.key.get_pressed()
        if currently_pressed_keys[pygame.K_w]:
            collided_object = player.MoveUp(self.Map, allowed_collision_classes)
        if currently_pressed_keys[pygame.K_a]:
            collided_object = player.MoveLeft(self.Map, allowed_collision_classes)
        if currently_pressed_keys[pygame.K_s]:
            collided_object = player.MoveDown(self.Map, allowed_collision_classes)
        if currently_pressed_keys[pygame.K_d]:
            collided_object = player.MoveRight(self.Map, allowed_collision_classes)
            
        # HANDLE USING TELEPORTER.
        collided_with_teleporter = isinstance(collided_object, Teleporter)
        return collided_with_teleporter

    ## Causes enemies to move, shoot, or perform other actions.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def UpdateEnemies(self):
        # UPDATE EACH ENEMY.
        player = self.Map.GetPlayer()
        player_position = self.Map.GetGridPosition(player.TopLeftCornerPosition)
        player_position_vector = Vector2(player_position[0], player_position[1])
        enemies = self.Map.GetEnemies()
        for enemy in enemies:
            # TODO: SHOOT AT PLAYER.
            

            # MOVE IF NON-STATIONARY.
            enemy_is_stationary = isinstance(enemy, Turret)
            if enemy_is_stationary:
                continue
            
            # CHECK IF THE ENEMY IS ALREADY CLOSE ENOUGH TO THE PLAYER.
            enemy_position = self.Map.GetGridPosition(enemy.TopLeftCornerPosition)
            enemy_position_vector = Vector2(enemy_position[0], enemy_position[1])
            distance_to_player = self.Pathing.GetDirectDistanceBetweenGridPositions(player_position_vector, enemy_position_vector)
            MINIMUM_DISTANCE = 3.0
            already_close_enough_to_player = (distance_to_player < MINIMUM_DISTANCE)
            if already_close_enough_to_player:
                # Back up, away from the player.
                direction_to_move = LevelHandler.GetDirectionTowardPosition(player_position_vector, enemy_position_vector)
            else:
                # Get the shortest path to the player from the enemy.
                path_to_player = self.Pathing.GetPath(enemy_position_vector, player_position_vector)
                if path_to_player is None:
                    # This enemy cannot currently reach the player.
                    continue

                # Get the next grid position that the enemy should move to in
                # order to reach the player.
                next_grid_position_in_path_to_player = next(islice(path_to_player, 1, None), None)
                direction_to_move = LevelHandler.GetDirectionTowardPosition(
                    enemy_position_vector,
                    next_grid_position_in_path_to_player)

            # Move.
            if direction_to_move is None:
                continue
            elif direction_to_move == MoveDirection.Up:
                enemy.MoveUp(self.Map)
            elif direction_to_move == MoveDirection.Down:
                enemy.MoveDown(self.Map)
            elif direction_to_move == MoveDirection.Left:
                enemy.MoveLeft(self.Map)
            elif direction_to_move == MoveDirection.Right:
                enemy.MoveRight(self.Map)

    ## Gets the direction (up, down, left, or right) from one position to another.
    ## \param[in]  origin_position - The first position as a Vector2 of column and row index.
    ## \param[in]  target_position - The target position as a Vector2 of column and row index.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    @staticmethod
    def GetDirectionTowardPosition(origin_position, target_position):
        if target_position is None:
            return None
        elif origin_position.Y > target_position.Y:
            return MoveDirection.Up
        elif origin_position.Y < target_position.Y:
            return MoveDirection.Down
        elif origin_position.X > target_position.X:
            return MoveDirection.Left
        elif origin_position.X < target_position.X:
            return MoveDirection.Right
        else:
            # Origin and target positions are the same.
            return None
