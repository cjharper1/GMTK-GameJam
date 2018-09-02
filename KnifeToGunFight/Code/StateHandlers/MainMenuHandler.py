import pygame

from .StateHandler import StateHandler
from .LevelHandler import LevelHandler


class MainMenuHandler(StateHandler):
    def __init__(self, game_window):
        # INITIALIZE THE HANDLER.
        audio = {
            'BackgroundMusic': '../Audio/main_menu_music.mp3'}
        images = {
            'MainMenuWithPressAnyKeyText': '../Images/MainMenuWithPressAnyKeyText.gif',
            'MainMenuWithoutPressAnyKeyText': '../Images/MainMenuWithoutPressAnyKeyText.gif'}
        StateHandler.__init__(self, images = images, audio=audio)

        self.GameWindow = game_window

    def Run(self):
        clock = pygame.time.Clock()
        useWithoutPressAnyKeyText = False
        while True:
            clock.tick(2)

            if useWithoutPressAnyKeyText:
                self.GameWindow.Screen.blit(self.MainMenuWithPressAnyKeyText, [0, 0])
                useWithoutPressAnyKeyText = False
            else:
                self.GameWindow.Screen.blit(self.MainMenuWithoutPressAnyKeyText, [0, 0])
                useWithoutPressAnyKeyText = True

            # UPDATE THE DISPLAY TO MAKE THE UPDATED OBJECTS VISIBLE.
            pygame.display.update()

            for event in pygame.event.get():
                if event.type is pygame.KEYDOWN:
                    return LevelHandler(self.GameWindow)

