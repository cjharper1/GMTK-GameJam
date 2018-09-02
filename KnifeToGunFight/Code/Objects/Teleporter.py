import pygame

from Objects.GameObject import GameObject

## Represents a teleporter that will take you to the next level. 
class Teleporter(GameObject):
    ## The number of frames to display each image in the teleporter animation.
    FRAMES_TO_DISPLAY_EACH_IMAGE = 10

    ## Constructor.
    ## \param[in]   x_position - The x position of the teleporter.
    ## \param[in]   y_position - The y position of the teleporter.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def __init__(self, x_position, y_position):
        GameObject.__init__(self, x_position, y_position)

        self.IMAGES = \
        [
            pygame.image.load('../Images/Teleporter1.gif').convert(),
            pygame.image.load('../Images/Teleporter2.gif').convert(),
            pygame.image.load('../Images/Teleporter3.gif').convert(),
            pygame.image.load('../Images/Teleporter4.gif').convert(),
            pygame.image.load('../Images/Teleporter5.gif').convert(),
            pygame.image.load('../Images/Teleporter6.gif').convert()
        ]

        ## Set the initial image of the teleporter.
        self.Image = self.IMAGES[0]
        self.CurrentlyDisplayedImageIndex = 0
        self.FramesSinceLastImageSwap = 0

    ## Updates the teleporter.
    ## \param[in]   seconds_since_last_update - The amount of seconds that have elapsed since last update.
    ## \author  CJ Harper
    ## \date    09/01/2018
    def Update(self, seconds_since_last_update):
        # DETERMINE IF THE NEXT FRAME IN THE TELEPORTER ANIMATION SHOULD BE SHOWN.
        FRAMES_PER_SECOND = 60
        frames_since_last_update = (seconds_since_last_update * FRAMES_PER_SECOND)
        self.FramesSinceLastImageSwap += frames_since_last_update
        image_swap_needed = (self.FramesSinceLastImageSwap >= self.FRAMES_TO_DISPLAY_EACH_IMAGE)
        if image_swap_needed:
            # SWAP THE IMAGE.
            # It's possible the final image of the animation is currently being shown.
            # Therefore, we should wrap back around to the first image of the animation to
            # cause it to loop.
            self.CurrentlyDisplayedImageIndex += 1
            restart_animation = (self.CurrentlyDisplayedImageIndex >= len(self.IMAGES))
            if restart_animation:
                self.CurrentlyDisplayedImageIndex = 0
            self.Image = self.IMAGES[self.CurrentlyDisplayedImageIndex]

            # The timer has to be reset so another image swap does not occur until
            # the timer has elapsed again.
            self.FramesSinceLastImageSwap = 0
