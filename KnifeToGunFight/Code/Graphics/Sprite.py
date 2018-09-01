import pygame

## Represents an image that can be drawn on the screen.
class Sprite():
    ## Constructor.
    ## param[in] image_path - The absolute path to the image which represents this sprite.
    ## param[in] initial_x_position - The initial X position of the sprite in relation to the main game window.
    ## param[in] initial_y_position - The initial Y position of the sprite in relation to the main game window.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, image_path, initial_x_position, initial_y_position):
        self.Image = pygame.image.load(image_path).convert()
        self.XPosition = initial_x_position 
        self.YPosition = initial_y_position

    ## Gets the position of this sprite as a touple of the x and y coordinates.
    ## \return A touble of the x,y coordinates of the sprite's position.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def GetPosition(self):
        return (self.XPosition, self.YPosition)

    ## Moves the position of the sprite.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## param[in] x_modifier - A modifier for the x-position. A positive value will increase the x-position.
    ##      A negative value will decrease the x-position.
    ## param[in] y_modifier - A modifier for the y-position. A positive value will increase the y-position.
    ##      A negative value will decrease the y-position.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def Move(self, x_modifier, y_modifier):
        self.XPosition += x_modifier
        self.YPosition += y_modifier
