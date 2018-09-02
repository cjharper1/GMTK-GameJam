import math
import random

from .GameObject import GameObject
from .Laser import Laser
from Math.Vector2 import Vector2

## Represents an enemy which is trying to harm the player.
class Enemy(GameObject):
    ## Constructor.
    def __init__(self, initial_x_position, initial_y_position, speed = 0):
        GameObject.__init__(self, initial_x_position, initial_y_position, speed = speed)

    ## Shoot at the player.
    ## \param[in]   player - The player to shoot at.
    ## \param[in]   game_map - The game map containing this enemy and the player.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def Shoot(self, player : GameObject, game_map):
        # CALCULATE THE TRAJECTORY TO THE PLAYER.
        # The trajectory is the amount of pixels an object will move each game update in
        # both the x and y position.
        # This is calculated by determining the slope between the enemy and the player.
        # slope = (y_player - y_enemy / x_player - x_enemy).
        # The trajectory would then be 1 x-pixel per slope y-pixels.
        x_distance_to_player = (player.Coordinates.centerx - self.Coordinates.centerx)
        y_distance_to_player = (player.Coordinates.centery - self.Coordinates.centery)
        slope = (y_distance_to_player / x_distance_to_player)
        
        # DETERMINE WHETHER THE ENEMY WILL OVERSHOOT OR UNDERSHOOT.
        # The slope may not divide into an integer number of pixels which would be impossible
        # to represent in game. Therefore, the slope needs to be rounded up or down. Always rounding the same
        # direction would end up being predictable since the enemy would always shoot to the left or
        # right of the player. The rounding will be determined randomly so the player cannot predict
        # whether the shot will be to the left or right.
        random_result = random.randint(0, 1)
        ROUND_UP_RANDOM_RESULT = 1
        round_up = (random_result == ROUND_UP_RANDOM_RESULT)
        if round_up:
            slope = math.ceil(slope)
        else:
            slope = math.floor(slope)
        trajectory_to_player = Vector2(1, slope)

        # GENERATE A LASER AND FIRE IT TOWARDS THE PLAYER.
        laser = Laser(self.Coordinates.centerx, self.Coordinates.centery, Laser.Color.Red, trajectory_to_player)

        ## \todo Add the laser to the map.

