import sys

import pygame

## Handles player input events and key presses.
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
    if currently_pressed_keys[pygame.K_a]:
        player.MoveLeft()
    if currently_pressed_keys[pygame.K_s]:
        player.MoveDown()
    if currently_pressed_keys[pygame.K_d]:
        player.MoveRight()
        