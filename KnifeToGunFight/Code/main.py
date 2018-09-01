import math
import sys

import pygame

pygame.init()

# INITIALIZE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 500
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode((SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

# LOOP UNTIL THE USER CHOOSES TO EXIT.
while True:
    # HANDLE EVENTS.
    for event in pygame.event.get():
        # EXIT THE GAME IF THE USER CLOSED THE WINDOW.
        if pygame.QUIT == event.type:
            pygame.quit()
            sys.exit()
        # HANDLE KEY PRESSES.
        ## \todo    Remove this debug keyboard handling.
        elif pygame.KEYDOWN == event.type:
            print('KEYDOWN unicode: ' + str(event.unicode))
            print('KEYDOWN key: ' + str(event.key))
            print('KEYDOWN mod: ' + str(event.mod))
            if pygame.K_UP == event.key:
                pass
            elif pygame.K_DOWN == event.key:
                pass
            elif pygame.K_LEFT == event.key:
                pass
            elif pygame.K_RIGHT == event.key:
                pass
        elif pygame.KEYUP == event.type:
            print('KEYUP key: ' + str(event.key))
            print('KEYUP mode: ' + str(event.mod))

    # CLEAR THE SCREEN TO BLACK.
    screen.fill((0, 0, 0))
    
    # DISPLAY THE RENDERED IMAGE.
    pygame.display.update()

    # SLEEP BEFORE THE NEXT FRAME TO MAINTAIN A MORE CONSISTENT FRAME RATE.
    DESIRED_FRAMES_PER_SECOND = 60
    MILLISECONDS_PER_SECOND = 1000
    MILLISECONDS_PER_FRAME = math.floor(MILLISECONDS_PER_SECOND / DESIRED_FRAMES_PER_SECOND)
    pygame.time.wait(MILLISECONDS_PER_FRAME)
