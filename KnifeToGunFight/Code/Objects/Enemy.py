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

        ## The amount of time elapsed since the last shot in seconds.
        self.TimeElapsedSinceLastShotInSeconds = 0

    ## Tries shooting the player.
    ## Shooting is capped to avoid overloading the player with too many lasers.
    ## \param[in]   time_since_last_update_in_seconds - The time since the last enemy update, in seconds.
    ## \param[in]   player - The player to shoot at.
    ## \return  A Laser, if shot; None otherwise.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    def TryShooting(self, time_since_last_update_in_seconds, player : GameObject, game_map):
        # CHECK IF SUFFICIENT TIME HAS ELAPSED SINCE THE LAST SHOT AT THE PLAYER.
        MIN_TIME_BETWEEN_SHOTS_IN_SECONDS = 3
        self.TimeElapsedSinceLastShotInSeconds += time_since_last_update_in_seconds
        long_enough_since_last_shot = (self.TimeElapsedSinceLastShotInSeconds >= MIN_TIME_BETWEEN_SHOTS_IN_SECONDS)
        if not long_enough_since_last_shot:
            return

        # RANDOMLY CHOOSE TO SHOOT THE PLAYER OR NOT.
        shoot_player = random.choice([True, False])
        if shoot_player:
            laser = self.Shoot(player)
            return laser
        else:
            return None

    ## Shoot at the player.
    ## \param[in]   player - The player to shoot at.
    ## \return  The shot laser.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def Shoot(self, player):
        # CALCULATE THE TRAJECTORY TO THE PLAYER.
        enemy_position = Vector2(self.Coordinates.centerx, self.Coordinates.centery)
        player_position = Vector2(player.Coordinates.centerx, player.Coordinates.centery)
        trajectory_to_player = Vector2.Subtract(player_position, enemy_position)

        # The trajectory should be normalized to have it just represent the direction.
        # The laser can independently control the speed at which it moves.
        trajectory_to_player = Vector2.Normalize(trajectory_to_player)

        # GENERATE A LASER AND FIRE IT TOWARDS THE PLAYER.
        laser = Laser(self.Coordinates.centerx, self.Coordinates.centery, Laser.Color.Red, trajectory_to_player)

        # Move the laser closer to the player so that it doesn't hit the wall when it spawns.
        laser.Update(0.2)
        
        # INDICATE THAT A SHOT WAS JUST FIRED.
        self.TimeElapsedSinceLastShotInSeconds = 0
        return laser

