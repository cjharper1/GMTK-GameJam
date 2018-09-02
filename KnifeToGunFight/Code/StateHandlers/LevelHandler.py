import math
import sys

import pygame

from Graphics.LevelMap import LevelMap
from .StateHandler import StateHandler
from Objects.Player import Player
from Objects.Turret import Turret

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
        audio = {
            'BackgroundMusic': '../Audio/background_music.wav'}
        StateHandler.__init__(self, audio = audio)
        
        # INITIALIZE INSTANCE VARIABLES.
        self.GameWindow = game_window
        self.LevelFilepath = level_filepath if level_filepath is not None else '../Maps/Level1.txt'
        self.Map = LevelMap(self.LevelFilepath)

    ## Runs the level and and handles displaying all graphics, playing sounds, and player interaction.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def Run(self):
        # PLAY BACKGROUND MUSIC.
        self.BackgroundMusic.set_volume(0.25)
        self.BackgroundMusic.play(-1, 0)
    
        # HANDLE INTERACTION.
        # The clock is used to determine elapsed time between frames.
        clock = pygame.time.Clock()
        while True:
            # UPDATE THE GAME CLOCK.
            # Ticking will automatically delay the game if needed to achieve the desired frame rate.
            time_since_last_update_in_ms = clock.tick(self.MaxFramesPerSecond)
            MILLISECONDS_PER_SECOND = 1000
            time_since_last_update_in_seconds = (time_since_last_update_in_ms / MILLISECONDS_PER_SECOND)

            # Set player position and rotation.
            #position = pygame.mouse.get_pos()
            #angle = math.atan2(int(position[1] - (self.PlayerPosition [1])), int(position[0] - self.PlayerPosition [0] + 26))
            #player_rotated = pygame.transform.rotate(self.Player, 360 - angle * 57.29)
            #player_position_1 = (self.PlayerPosition [0] - player_rotated.get_rect().width / 2, self.PlayerPosition [1] - player_rotated.get_rect().height / 2)
            #self.Screen.blit(player_rotated, player_position_1)
            
            # HANDLE PLAYER INTERACTION.
            self.HandlePlayerInteraction()

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
        currently_pressed_keys = pygame.key.get_pressed()
        if currently_pressed_keys[pygame.K_w]:
            player.MoveUp(self.Map)
        if currently_pressed_keys[pygame.K_a]:
            player.MoveLeft(self.Map)
        if currently_pressed_keys[pygame.K_s]:
            player.MoveDown(self.Map)
        if currently_pressed_keys[pygame.K_d]:
            player.MoveRight(self.Map)
            