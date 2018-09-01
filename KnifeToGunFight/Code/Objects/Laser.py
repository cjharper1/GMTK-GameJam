from enum import Enum
import pygame

from .GameObject import GameObject

## Represents a laser shot by an enemy unit.
## \author  CJ Harper
## \date    09/01/2018
class Laser(GameObject):
    ## Represents the various colors a laser can be.
    class Color(Enum.enum):
        Red = 1
        Blue = 2
        Green = 3

    ## A lookup of image filepaths for each laser color.
    LASER_IMAGE_PER_COLOR = \
    {
        Color.Red: '../Images/RedLaser.gif', 
        Color.Blue: '../Images/BlueLaser.gif', 
        Color.Green: '../Images/Green.gif'
    }

    ## Constructor.
    ## \param[in]   initial_x_position - The initial x position of the laser.
    ## \param[in]   initial_y_position - The initial y position of the laser.
    ## \param[in]   color - The color of the laser.
    ## \param[in]   trajectory - The Vector2 indicating the direction and speed the laser is traveling in pixels per game update.
    ##      The x and y component of the trajectory will be added to the laser each game update.
    ##      Therefore, if the trajectory is [-1, -1] the laser would move one pixel to the left and one
    ##      pixel up each game update.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def __init__(self, initial_x_position, initial_y_position, color, trajectory):
        GameObject.__init__(self, initial_x_position, initial_y_position)
        ## The image representing this laser.
        self.Image = pygame.image.load(self.LASER_IMAGE_PER_COLOR[color]).convert()
        ## The trajectory of the laser.
        self.Trajectory = trajectory

    ## Updates the state of the laser.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def Update(self):
        self.Move(self.Trajectory.X, self.Trajectory.Y)
