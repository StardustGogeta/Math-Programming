from pygame.locals import *
import pygame, sys, time

# Setting and playing music when requested.
def playMusic(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

# Defining constant colors.
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pygame.init()
icon = pygame.image.load('marioEmblem.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((640,480))
screen.fill((255,0,255))
playMusic("groundTheme.mp3")
pygame.display.set_caption('Super Mario Bros.')
fpsTime, fps, fpsRefresh = time.clock(), 0, 1

# Drawing Mario and the background.
mario = pygame.transform.scale(pygame.image.load('mario.png').convert_alpha(), (40,50))
screen.blit(mario, (100,100))

while 1:
    screen.fill((255,0,255))

    # Exiting the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    # FPS Counter in standard Python.
    fps += 1
    if time.clock() > fpsTime + 1/fpsRefresh:
        pygame.display.set_caption('Super Mario Bros. - '+str(fps*fpsRefresh)+' FPS')
        fps = 0
        fpsTime = time.clock()
        
    # Drawing Mario and the background.

    screen.blit(mario, (200,100))
    
    
    # Refresh the screen.
    pygame.display.update()
