from .Color import Color
from .Sprite import Sprite
import pygame

class GameWindow():
    def __init__(self, height : int, width : int):
        self.Screen = pygame.display.set_mode((height, width))
        self.Screen.fill((0,0,0))
        self._sprites = []

    ## Adds a sprite to be drawn on the screen. This sprite will not be drawn until the next screen update.
    ## param[in] sprite - The sprite to add to the group of sprites drawn on screen.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def AddSprite(self, sprite : Sprite):
        self._sprites.append(sprite)

    ## Removes an sprite from the group of sprites drawn on screen each update.
    ## The sprite will not be removed until the next screen update.
    ## param[in] sprite - The sprite to remove from the list of drawn sprites.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def RemoveSprite(self, sprite : Sprite):
        try:
            self._sprites.remove(sprite)
        except:
            # No action needs to be taken. The user wants this object to be removed from the collection
            # but the collection is already in the desired state. No reason to alert the user to this issue.
            pass

    ## Updates the screen by clearing it and drawing all of the sprites in their new positions.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def Update(self):
        self.Clear()
        self._drawSprites()
        pygame.display.update()

    ## Clears the screen.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def Clear(self):
        self.Screen.fill((0,0,0))

    ## Draws all sprites to the screen.
    ## \author  CJ Harper
    ## \date    08/04/2018
    def _drawSprites(self):
        for sprite in self._sprites:
            self.Screen.blit(sprite.Image, sprite.GetPosition())
