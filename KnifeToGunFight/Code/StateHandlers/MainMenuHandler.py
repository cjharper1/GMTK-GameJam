import pygame

from .StateHandler import StateHandler


class MainMenuHandler(StateHandler):
    def __init__(self, game_window):
        # INITIALIZE THE HANDLER.
        audio = {
            'BackgroundMusic': '../Audio/background_music.wav'}
        images = {
            'MainMenuWithPressAnyKeyText': '../Images/MainMenuWithPressAnyKeyText.gif',
            'MainMenuWithoutPressAnyKeyText': '../Images/MainMenuWithoutPressAnyKeyText.gif'}
        StateHandler.__init__(self, images = images, audio=audio)

        self.GameWindow = game_window

    def Run(self):
        # PLAY BACKGROUND MUSIC.
        self.BackgroundMusic.set_volume(0.25)
        self.BackgroundMusic.play(-1, 0)

        clock = pygame.time.Clock()
        useWithoutPressAnyKeyText = False
        while True:
            MILLISECONDS_PER_SECOND = 1000
            time_since_last_update_in_ms = clock.tick(self.MaxFramesPerSecond)
            time_since_last_update_in_seconds = (time_since_last_update_in_ms / MILLISECONDS_PER_SECOND)

            if useWithoutPressAnyKeyText:
                self.GameWindow.Screen.blit(self.MainMenuWithPressAnyKeyText, [0, 0])
                useWithoutPressAnyKeyText = False
            else:
                self.GameWindow.Screen.blit(self.MainMenuWithoutPressAnyKeyText, [0, 0])
                useWithoutPressAnyKeyText = True

            # UPDATE THE DISPLAY TO MAKE THE UPDATED OBJECTS VISIBLE.
            pygame.display.update()
            pygame.time.wait(500)

