from .Color import Color
from .Sprite import Sprite
import pygame

## The game window containing the main screen on which all game objects are drawn.
## \author  CJ Harper
## \date    08/04/2018
class GameWindow():
    ## Create the game window.
    ## \param[in]   height - The height in pixels of the game window screen.
    ## \param[in]   width - The width in pixels of the game window screen.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def __init__(self, height : int, width : int):
        # INITIALIZE THE SCREEN.
        self.Screen = pygame.display.set_mode((height, width))
        self.Screen.fill((0,0,0))

    ## Updates the screen by clearing it and drawing all of the sprites in their new positions
    ## based on the game map.
    ## \param[in]   game_map - The game map to use in redrawing all objects to the screen.
    ## \author  Michael Watkinson
    ## \date    08/25/2018
    def Update(self, game_map):
        # CLEAR THE GAME WINDOW.
        self.Clear()
        
        # DRAW ALL OBJECTS IN THE GAME MAP.
        for game_object in game_map.Map:
            self.__DrawImage(game_object)
        
        # UPDATE THE DISPLAY TO MAKE THE UPDATED OBJECTS VISIBLE.
        pygame.display.update()

    ## Clears the screen.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def Clear(self):
        self.Screen.fill((0,0,0))

    ## Draws the game object to the screen.
    ## \param[in]   game_object - The game object to draw to the screen.
    ## \author  Michael Watkinson
    ## \date    08/04/2018
    def __DrawImage(self, game_object):
        # DRAW THE IMAGE TO THE SCREEN.
        # Objects are drawn in relation to their top-left corner.
        self.Screen.blit(game_object.Image, game_object.TopLeftCornerPosition)
