import math
import os
import sys

import pygame

from Game import HandleInput
from Graphics.GameMap import GameMap
from Graphics.GameWindow import GameWindow
from Graphics.Sprite import Sprite

pygame.init()
pygame.font.init()

# CREATE THE GAME WINDOW.
game_window = GameWindow(640, 480)

# CREATE THE GAME MAP.
game_map = GameMap('Maps/Map1.txt')

# CALCULATE THE FRAMES PER SECOND FOR THE GAME.
# Limit the game to 60 fps.
milliseconds_per_second = 1000
frames_per_second = 60
milliseconds_per_frame = math.floor(milliseconds_per_second/frames_per_second)

while True:
    # UPDATE THE SCREEN.
    game_window.Update(game_map)

    # HANDLE PLAYER INPUT.
    HandleInput(game_map)
    
    # WAIT BEFORE UPDATING THE GAME AGAIN.
    pygame.time.wait(milliseconds_per_frame)
