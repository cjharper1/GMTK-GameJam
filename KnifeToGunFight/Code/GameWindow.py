from Graphics.Color import Color
from Graphics.Sprite import Sprite
import pygame

## The game window containing the main screen on which all game objects are drawn.
## \author  Michael Watkinson
## \date    09/01/2018
class GameWindow():
    ## Create the game window.
    ## \param[in]   height - The height in pixels of the game window screen.
    ## \param[in]   width - The width in pixels of the game window screen.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, height : int, width : int):
        # INITIALIZE THE SCREEN.
        self.Screen = pygame.display.set_mode((height, width))
        self.Screen.fill((0,0,0))

    ## Updates the screen by clearing it and drawing all of the sprites in their new positions
    ## based on the game map.
    ## \param[in]   game_map - The game map to use in redrawing all objects to the screen.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def Update(self, game_map):
        # CLEAR THE GAME WINDOW.
        self.Clear()
        
        # DRAW ALL OBJECTS IN THE GAME MAP.
        for game_object in game_map.Map.values():
            self.__DrawImage(game_object)

        # RENDER THE PLAYER'S SWORD.
        # It doesn't fall into the normal game object system.
        player = game_map.GetPlayer()
        if player:
            player.Sword.Render(self.Screen)

        # DRAW ALL LASERS.
        # Lasers can occupy the same space as enemies so they
        # are not stored in the map.
        # \todo Update map to store a list of objects
        # rather than be a dictionary.
        for laser in game_map.Lasers:
            self.__DrawImage(laser)
        
        # UPDATE THE DISPLAY TO MAKE THE UPDATED OBJECTS VISIBLE.
        pygame.display.update()

    ## Clears the screen.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def Clear(self):
        self.Screen.fill((0,0,0))

    ## Draws the game object to the screen.
    ## \param[in]   game_object - The game object to draw to the screen.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __DrawImage(self, game_object):
        # DRAW THE IMAGE TO THE SCREEN.
        # Objects are drawn in relation to their top-left corner.
        self.Screen.blit(game_object.Image, game_object.TopLeftCornerPosition)
