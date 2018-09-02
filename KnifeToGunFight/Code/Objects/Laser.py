from enum import Enum
import math
import pygame

from .GameObject import GameObject
from Math.Vector2 import Vector2

## Represents a laser shot by an enemy unit.
## \author  CJ Harper
## \date    09/01/2018
class Laser(GameObject):
    ## Represents the various colors a laser can be.
    class Color(Enum):
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
        ## The trajectory of the laser.
        self.Trajectory = trajectory

        ## The image needs to be rotated based on the trajectory.
        radians_to_rotate = -math.atan2(trajectory.Y, trajectory.X)
        degrees_of_rotation = math.degrees(radians_to_rotate)

        # 90 degrees is subtracted from the rotation since the image spawns facing upward (i.e. rotated 90 degrees from the x-axis)
        # and the arctan function calculates rotation as if the image spawned facing the x-axis.
        degrees_of_rotation -= 90

        # The default image is rotated every time because continuing to rotate the same image
        # over and over will result in degradation of image quality.
        self.Image = pygame.transform.rotate(pygame.image.load(self.LASER_IMAGE_PER_COLOR[color]).convert(), degrees_of_rotation)

    ## Updates the state of the laser.
    ## \param[in]   time_since_last_update_in_seconds - The time since the laser was last
    ##      updated, in seconds.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def Update(self, time_since_last_update_in_seconds):
        MOVE_SPEED_IN_PIXELS_PER_SECOND = 200
        movement_distance_in_pixels = MOVE_SPEED_IN_PIXELS_PER_SECOND * time_since_last_update_in_seconds
        movement_amount_in_pixels = Vector2.Scale(movement_distance_in_pixels, self.Trajectory)
        self.Coordinates = self.Coordinates.move(movement_amount_in_pixels.X, movement_amount_in_pixels.Y)

    ## Reflects the projectile.
    ## \author  CJ Harper
    ## \date    09/02/2018
    def Reflect(self):
        # REVERSE THE TRAJECTORY OF THE LASER.
        # Multiplying a vector by -1 will make it point in the opposite direction.
        REVERSE_DIRECTION = -1
        self.Trajectory.X = (self.Trajectory.X * REVERSE_DIRECTION)
        self.Trajectory.Y = (self.Trajectory.Y * REVERSE_DIRECTION)
