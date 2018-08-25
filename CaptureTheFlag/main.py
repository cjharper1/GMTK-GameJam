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

print (player.Image)

# ADD THE PLAYER TO THE SET OF OBJECTS DRAWN ON SCREEN.
game_window.AddSprite(player)

while (True):
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_ESCAPE:
                sys.exit()
    
    currently_pressed_keys = pygame.key.get_pressed()
    if currently_pressed_keys[pygame.K_w]:
        player.Move(0,-2)
    if currently_pressed_keys[pygame.K_a]:
        player.Move(-2,0)
    if currently_pressed_keys[pygame.K_s]:
        player.Move(0,2)
    if currently_pressed_keys[pygame.K_d]:
        player.Move(2,0)
        
    game_window.Update()

    # Limit the game to 60 fps.
    milliseconds_per_second = 1000
    frames_per_second = 60
    milliseconds_per_frame = math.floor(milliseconds_per_second/frames_per_second)
    
    pygame.time.wait(milliseconds_per_frame)
