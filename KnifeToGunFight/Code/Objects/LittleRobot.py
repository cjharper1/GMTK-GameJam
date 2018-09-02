import math

import pygame

from .Enemy import Enemy

## Represents a robot that can chase and shoot at the player.
class LittleRobot(Enemy):
    def __init__(self, initial_x_position, initial_y_position):
        Enemy.__init__(self, initial_x_position, initial_y_position, speed = 1)
        self.__DefaultImage = pygame.image.load('../Images/LittleRobot.gif').convert()

        ## The default image will be shown upon load because the robot has not performed
        ## any action yet. 
        self.Image = self.__DefaultImage
        
    ## Targets the player by rotating the turret to face the player.
    ## \param[in]   player - The player GameObject to target.
    ## \author  Michael Watkinson
    ## \date    09/02/2018
    def TargetPlayer(self, player):
        # GET THE POSITION OF THE PLAYER.
        player_x_position, player_y_position = player.Coordinates.center

        # CALCULATE ROTATION.
        # The top of the turret is used as the reference rather than the center
        # so it faces the player.
        distance_from_enemy_to_player_x = (player_x_position - self.Coordinates.x)
        distance_from_enemy_to_player_y = (player_y_position - self.Coordinates.y)
        radians_to_rotate = -math.atan2(distance_from_enemy_to_player_y, distance_from_enemy_to_player_x)
        degrees_of_rotation = math.degrees(radians_to_rotate)

        # 90 degrees is added to the rotation since the image spawns facing downwards (i.e. rotated 90 degrees from the x-axis)
        # and the arctan function calculates rotation as if the image spawned facing the x-axis.
        degrees_of_rotation_relative_to_image_facing_up = degrees_of_rotation + 90

        # ROTATE AND POSITION THE PLAYER.
        # The original size and shape are preserved to preserve collision detection.
        original_rect = self.Coordinates
        rotated_image = pygame.transform.rotate(self.__DefaultImage, degrees_of_rotation_relative_to_image_facing_up)
        rotated_rect = original_rect.copy()
        rotated_rect.center = rotated_image.get_rect().center
        self.Image = rotated_image.subsurface(rotated_rect).copy()
        