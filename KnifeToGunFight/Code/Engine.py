import math
import sys

import pygame

from GameWindow import GameWindow
from Graphics.LevelMap import LevelMap
from Objects.Player import Player
from Utilities.CollisionDetection import HandleCollision, MoveDirection

## Handles the main execution of the game.
## \author  Michael Watkinson
## \date    09/01/2018
def RunGame():
    # INITIALIZE PYGAME.
    pygame.init()
    WIDTH = 1024
    HEIGHT = 720
    game_window = GameWindow(WIDTH, HEIGHT)
    pygame.mixer.init()

    # ENTER THE GAME MAIN LOOP.
    current_state = LevelHandler(game_window)
    while True:
        # HANDLE THE CURRENT STATE OF THE GAME.
        current_state = current_state.Run()
        
## The base state handler class.
## \author  Michael Watkinson
## \date    09/01/2018
class Handler(object):
    ## Initializes the handler object.
    ## \param[in]   images - A dictionary with the image name as the key and the filepath as the value.
    ## \param[in]   audio - A dictionary with the audio name as the key and the filepath as the value.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, images = None, audio = None):
        # STORE THE IMAGE INSTANCE VARIABLES FOR THE HANDLER.
        images_provided = images is not None
        if images_provided:
            for image_name, image_filepath in images.items():
                # Load the image asset.
                image = pygame.image.load(image_filepath)
                setattr(self, image_name, image)
        
        # STORE THE AUDIO INSTANCE VARIABLES FOR THE HANDLER.
        audio_provided = audio is not None
        if audio_provided:
            for audio_name, audio_filepath in audio.items():
                # Load the audio asset.
                audio_asset = pygame.mixer.Sound(audio_filepath)
                setattr(self, audio_name, audio_asset)
            
        # CALCULATE THE FRAMES PER SECOND FOR THE GAME.
        # Limit the game to 60 fps.
        milliseconds_per_second = 1000
        self.MaxFramesPerSecond = 60
        self.FrameRate = math.floor(milliseconds_per_second / self.MaxFramesPerSecond)
    
## The handler class for controlling a level of the game.
## \author  Michael Watkinson
## \date    09/01/2018
class LevelHandler(Handler):
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
        Handler.__init__(self, audio = audio)
        
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

            # UPDATE THE SCREEN.
            self.GameWindow.Update(self.Map)
           
    ## Handles player input from events, key presses and mouse interaction.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def HandlePlayerInteraction(self):
        # HANDLE QUIT EVENTS.
        for event in pygame.event.get():
            # Check if the X button of the window was clicked.
            if event.type is pygame.QUIT:
                # Quit the game.
                pygame.quit()
                sys.exit()
                
            # Check if the 
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_ESCAPE:
                    sys.exit()
                    pygame.quit()

        # GET THE PLAYER OBJECT FROM THE MAP.
        player = self.Map.GetPlayer()
        
        # HANDLE PLAYER MOVEMENT.
        currently_pressed_keys = pygame.key.get_pressed()
        if currently_pressed_keys[pygame.K_w]:
            player.MoveUp()
            ## \todo    HandleCollision(self.Map, player, MoveDirection.Up)
        if currently_pressed_keys[pygame.K_a]:
            player.MoveLeft()
            ## \todo    HandleCollision(self.Map, player, MoveDirection.Left)
        if currently_pressed_keys[pygame.K_s]:
            player.MoveDown()
            ## \todo    HandleCollision(self.Map, player, MoveDirection.Down)
        if currently_pressed_keys[pygame.K_d]:
            player.MoveRight()
            ## \todo    HandleCollision(self.Map, player, MoveDirection.Right)
                
        # Check for mouse events.
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    position = pygame.mouse.get_pos()
        #    arrows.append([math.atan2(position[1] - (player_position[1] + 32), position[0] - (player_position_1[0] + 26)), player_position_1[0] + 32, player_position_1[1] + 32])
