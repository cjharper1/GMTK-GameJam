import math
import os
import sys
import pygame
from Graphics.GameWindow import GameWindow
from Graphics.Sprite import Sprite

pygame.init()

# CREATE THE GAME WINDOW.
game_window = GameWindow(640, 480)

# CREATE THE PLAYER.
player = Sprite("Images/Player.bmp", 10, 10)

# ADD THE PLAYER TO THE SET OF OBJECTS DRAWN ON SCREEN.
game_window.AddSprite(player)

while (True):
        
    game_window.Update()

    # Limit the game to 60 fps.
    milliseconds_per_second = 1000
    frames_per_second = 60
    milliseconds_per_frame = math.floor(milliseconds_per_second/frames_per_second)
    pygame.time.wait(milliseconds_per_frame)
