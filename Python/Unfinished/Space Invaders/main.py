# All visual content originates from the Taito corporation.
# The sound effects and music come from Star Wars: Dark Forces game files.

from pygame.locals import *
import pygame, sys, time, re

# Setting and playing music when requested.
def playMusic(track,loop=-1,startPt=0):
    pygame.mixer.music.load(track)
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loop,startPt)

# Checking all pygame events.
def checkEvents():
    for event in pygame.event.get():
        # Exiting the window.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'],pygame.RESIZABLE)
            global WIDTH, HEIGHT
            WIDTH, HEIGHT = event.dict['size']
            print(WIDTH, HEIGHT)

# Defining constant colors.
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

# Start the game.
if __name__ == '__main__':
    pygame.mixer.init(frequency=44800,buffer=2**13)
    pygame.init()
    playMusic('CRIXMUS1.mp3')
    icon = pygame.image.load('space_invader.jpg')
    pygame.display.set_icon(icon)
    global WIDTH, HEIGHT
    WIDTH = 640
    HEIGHT = int(3/4*WIDTH)
    screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
    pygame.display.set_caption('Space Invaders')
    fpsTime, fps, fpsRefresh = time.clock(), 0, 1

    # Create all of the space invaders in the back-end.
    invaders = []
    for x in range(55):
        invaders += [x]

    # Initialize the player.
    playerX = WIDTH/2
    player = pygame.transform.scale(pygame.image.load('space_invader.jpg').convert(), (int(WIDTH/16),int(WIDTH/16)))
        
    while 1:
        # Reset background.
        screen.fill(BLACK)
        checkEvents()

        # Draw the player.
        playerX = WIDTH/2
        player = pygame.transform.scale(pygame.image.load('space_invader.jpg').convert(), (int(WIDTH/16),int(WIDTH/16)))
        screen.blit(player,(playerX,HEIGHT*3/4))
        
        # Creating an FPS counter.
        fps += 1
        if time.clock() > fpsTime + 1/fpsRefresh:
            pygame.display.set_caption('Space Invaders - {0} FPS'.format(str(fps*fpsRefresh)))
            fps, fpsTime = 0, time.clock()

        # Refresh the screen.
        pygame.display.update()
