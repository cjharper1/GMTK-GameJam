import math
import sys

import pygame

from GameWindow import GameWindow
from Graphics.LevelMap import LevelMap

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
    ## \param[in]   audio - A dictionary with the audio name as the key and the filepath as the value.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, audio):
        # STORE THE IMAGE INSTANCE VARIABLES FOR THE HANDLER.
        #for image_name, image_filepath in images.items():
        #    # Load the image asset.
        #    image = pygame.image.load(image_filepath)
        #    setattr(self, image_name, image)
        
        # STORE THE AUDIO INSTANCE VARIABLES FOR THE HANDLER.
        for audio_name, audio_filepath in audio.items():
            # Load the audio asset.
            audio_asset = pygame.mixer.Sound(audio_filepath)
            setattr(self, audio_name, audio_asset)
            
        # CALCULATE THE FRAMES PER SECOND FOR THE GAME.
        # Limit the game to 60 fps.
        milliseconds_per_second = 1000
        frames_per_second = 60
        self.FrameRate = math.floor(milliseconds_per_second/frames_per_second)
    
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
        Handler.__init__(self, audio)
        
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
        while True:
            # UPDATE THE SCREEN.
            self.GameWindow.Update(self.Map)
            
            # Set player position and rotation.
            #position = pygame.mouse.get_pos()
            #angle = math.atan2(int(position[1] - (self.PlayerPosition [1])), int(position[0] - self.PlayerPosition [0] + 26))
            #player_rotated = pygame.transform.rotate(self.Player, 360 - angle * 57.29)
            #player_position_1 = (self.PlayerPosition [0] - player_rotated.get_rect().width / 2, self.PlayerPosition [1] - player_rotated.get_rect().height / 2)
            #self.Screen.blit(player_rotated, player_position_1)
            
            # HANDLE PLAYER INTERACTION.
            self.HandlePlayerInteraction()
            
            # WAIT BEFORE UPDATING THE GAME AGAIN.
            pygame.time.wait(self.FrameRate)
           
    ## Handles player input from events, key presses and mouse interaction.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def HandlePlayerInteraction(self):
            # HANDLE QUIT EVENTS.
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                    
            # Check for mouse events.
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    position = pygame.mouse.get_pos()
            #    arrows.append([math.atan2(position[1] - (player_position[1] + 32), position[0] - (player_position_1[0] + 26)), player_position_1[0] + 32, player_position_1[1] + 32])