import os
import pygame

from GameWindow import GameWindow
from StateHandlers.MainMenuHandler import MainMenuHandler

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
    current_state = MainMenuHandler(game_window)
    while True:
        # HANDLE THE CURRENT STATE OF THE GAME.
        current_state = current_state.Run()

if __name__ == '__main__':
    # SET CWD.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    
    # ENTER THE MAIN GAME LOOP.
    RunGame()