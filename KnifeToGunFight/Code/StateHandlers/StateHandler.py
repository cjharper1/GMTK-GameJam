import math

import pygame

## The base state handler class.
## \author  Michael Watkinson
## \date    09/01/2018
class StateHandler(object):
    ## Initializes the handler object.
    ## \param[in]   images - A dictionary with the image name as the key and the filepath as the value.
    ## \param[in]   audio - A dictionary with the audio name as the key and the filepath as the value.
    ## \author  Michael Watkinson
    ## \date    09/01/2018
    def __init__(self, images = None, audio = None):
        # STORE THE IMAGE INSTANCE VARIABLES FOR THE HANDLER.
        images_provided = images is not None
        if images_provided:
            for image_name, image_filepath in images.items():
                # Load the image asset.
                image = pygame.image.load(image_filepath)
                setattr(self, image_name, image)
        
        # STORE THE AUDIO INSTANCE VARIABLES FOR THE HANDLER.
        audio_provided = audio is not None
        if audio_provided:
            for audio_name, audio_filepath in audio.items():
                # Determine how to handle the audio.
                if ('.mp3' in audio_filepath):
                    audio_asset = pygame.mixer.music.load(audio_filepath)
                    pygame.mixer.music.play(loops = -1)
                    
                else:
                    # Load the audio asset.
                    audio_asset = pygame.mixer.Sound(audio_filepath)
                    setattr(self, audio_name, audio_asset)
            
        # CALCULATE THE FRAMES PER SECOND FOR THE GAME.
        # Limit the game to 60 fps.
        milliseconds_per_second = 1000
        self.MaxFramesPerSecond = 60
        self.FrameRate = math.floor(milliseconds_per_second / self.MaxFramesPerSecond)
        