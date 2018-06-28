import time, pygame, sys

def key_input(keys):
    key_dict = {pygame.K_w:'2',pygame.K_a:'4',pygame.K_s:'8',pygame.K_d:'6',
                pygame.K_q:'5',pygame.K_e:'3',pygame.K_1:'1',pygame.K_2:'c',
                pygame.K_3:'d',pygame.K_4:'e',pygame.K_r:'f',pygame.K_f:'0',
                pygame.K_z:'7',pygame.K_x:'9',pygame.K_c:'a',pygame.K_v:'b'}
    return ''.join(key_dict[x] if keys[x] else '' for x in key_dict)

pygame.init()
PIXEL_WIDTH = 4
(width,height) = (64*PIXEL_WIDTH,32*PIXEL_WIDTH)
screen = pygame.display.set_mode((width,height))
while 1:
    keys = pygame.key.get_pressed()
    new_keys = key_input(keys)
    print('LOLOLOLOLOL'+new_keys if new_keys else '')
    # Draw gfx
    pygame.display.update()
    time.sleep(.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
