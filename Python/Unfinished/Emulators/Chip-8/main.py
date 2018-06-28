from random import randrange
import time, pygame, sys

def key_input(keys):
    key_dict = {pygame.K_1:'1',pygame.K_2:'2',pygame.K_3:'3',pygame.K_4:'c',
                pygame.K_q:'4',pygame.K_w:'5',pygame.K_e:'6',pygame.K_r:'d',
                pygame.K_a:'7',pygame.K_s:'8',pygame.K_d:'9',pygame.K_f:'e',
                pygame.K_z:'a',pygame.K_x:'0',pygame.K_c:'b',pygame.K_v:'f'}
    return ''.join(key_dict[x] if keys[x] else '' for x in key_dict)

def load_rom(path):
    with open(path,'rb') as rom:
        rom = rom.read()
        assert len(rom)<=4096, 'The ROM was too large.'
        for x in range(len(rom)):
            mem[512+x] = rom[x]

def reset_all():
    global mem, stack, delay, sound, screen, pc, reg, I
    mem = [0]*4096
    hexChars = [0xF0, 0x90, 0x90, 0x90, 0xF0,
                0x20, 0x60, 0x20, 0x20, 0x70,
                0xF0, 0x10, 0xF0, 0x80, 0xF0,
                0xF0, 0x10, 0xF0, 0x10, 0xF0,
                0x90, 0x90, 0xF0, 0x10, 0x10,
                0xF0, 0x80, 0xF0, 0x10, 0xF0,
                0xF0, 0x80, 0xF0, 0x90, 0xF0,
                0xF0, 0x10, 0x20, 0x40, 0x40,
                0xF0, 0x90, 0xF0, 0x90, 0xF0,
                0xF0, 0x90, 0xF0, 0x10, 0xF0,
                0xF0, 0x90, 0xF0, 0x90, 0x90,
                0xE0, 0x90, 0xE0, 0x90, 0xE0,
                0xF0, 0x80, 0x80, 0x80, 0xF0,
                0xE0, 0x90, 0x90, 0x90, 0xE0,
                0xF0, 0x80, 0xF0, 0x80, 0xF0,
                0xF0, 0x80, 0xF0, 0x80, 0x80]
    mem[:80] = hexChars
    pc = 512
    reg, I = [0]*16, 0
    stack = []
    delay, sound = 0,0
    screen = [[0 for x in range(64)] for y in range(32)]

def read_opcode(pc):
    return mem[pc]<<8|mem[pc+1]

def run_opcode(x,keys):
    global mem, stack, delay, sound, screen, pc, reg, I
    x = hex(x)[2:]
    x = '0'*(4-len(x))+x
    if x[0] == '0':
        if x == '00e0':
            screen = [[0 for x in range(64)] for y in range(32)]
        elif x == '00ee':
            pc = stack[-1]
            stack = stack[:-1]
        else:
            pass # Not planned
    elif x[0] == '1':
        pc = int(x[1:],16)-2
    elif x[0] == '2':
        stack += [pc]
        pc = int(x[1:],16)-2
    elif x[0] == '3':
        pc += 2 if reg[int(x[1],16)] == int(x[2:],16) else 0
    elif x[0] == '4':
        pc += 2 if reg[int(x[1],16)] != int(x[2:],16) else 0
    elif x[0] == '5':
        pc += 2 if reg[int(x[1],16)] == reg[int(x[2],16)] else 0
    elif x[0] == '6':
        reg[int(x[1],16)] = int(x[2:],16)
    elif x[0] == '7':
        reg[int(x[1],16)] += int(x[2:],16)
        if reg[int(x[1],16)] > 0xff:
            reg[int(x[1],16)] -= 0x100
    elif x[0] == '8':
        rX, rY = reg[int(x[1],16)], reg[int(x[2],16)]
        if x[3] == '0':
            reg[int(x[1],16)] = reg[int(x[2],16)]
        elif x[3] == '1':
            reg[int(x[1],16)] |= reg[int(x[2],16)]
        elif x[3] == '2':
            reg[int(x[1],16)] &= reg[int(x[2],16)]
        elif x[3] == '3':
            reg[int(x[1],16)] ^= reg[int(x[2],16)]
        elif x[3] == '4':
            reg[int(x[1],16)] += reg[int(x[2],16)]
            if reg[int(x[1],16)] > 0xff:
                reg[int(x[1],16)] -= 0x100
                reg[15] = 1
            else:
                reg[15] = 0
        elif x[3] == '5':
            reg[int(x[1],16)] -= reg[int(x[2],16)]
            if reg[int(x[1],16)] < 0:
                reg[int(x[1],16)] += 0x100
                reg[15] = 0
            else:
                reg[15] = 1
        elif x[3] == '6':
            reg[15] = reg[int(x[1],16)] & 1
            reg[int(x[1],16)] >>= 1
        elif x[3] == '7':
            reg[int(x[1],16)] = reg[int(x[2],16)] - reg[int(x[1],16)]
            if reg[int(x[1],16)] < 0:
                reg[int(x[1],16)] += 0x100
                reg[15] = 0
            else:
                reg[15] = 1
        else:
            reg[15] = reg[int(x[1],16)] & (1<<8)
            reg[int(x[1],16)] <<= 1
    elif x[0] == '9':
        pc += 2 if reg[int(x[1],16)] != reg[int(x[2],16)] else 0
    elif x[0] == 'a':
        I = int(x[1:],16)
    elif x[0] == 'b':
        pc = int(x[1:],16)-2 + reg[0]
    elif x[0] == 'c':
        reg[int(x[1],16)] = int(x[2:],16) & randrange(0xff)
    elif x[0] == 'd':
        reg[15] = 0
        rX, rY = reg[int(x[1],16)], reg[int(x[2],16)]
        for n in range(int(x[3],16)):
            for X in range(8):
                if mem[I+n] & (1 << 7-X):
                    coords = ((rX+X)%64,(rY+n)%32)
                    if screen[coords[1]][coords[0]]: reg[15] = 1
                    screen[coords[1]][coords[0]] ^= 1
                    #print(coords, screen[coords[1]][coords[0]])
    elif x[0] == 'e':
        if x[2] == '9':
            if x[1] in keys:
                pc += 2
        else:
            if x[1] not in keys:
                pc += 2
    else:
        if x[2] == '0':
            if x[3] == '7':
                reg[int(x[1],16)] = delay
            else:
                find_keys = pygame.key.get_pressed()
                while not key_input(find_keys):
                    find_keys = pygame.key.get_pressed()
                reg[int(x[1],16)] = int(key_input(find_keys)[0],16)
        elif x[2] == '1':
            if x[3] == '5':
                delay = reg[int(x[1],16)]
            elif x[3] == '8':
                sound = reg[int(x[1],16)]
            else:
                I += reg[int(x[1],16)]
        elif x[2] == '2':
            I = reg[int(x[1],16)]*5
        elif x[2] == '3':
            mem[I] = reg[int(x[1],16)] // 100
            mem[I+1] = (reg[int(x[1],16)] % 100) // 10
            mem[I+2] = (reg[int(x[1],16)] % 10)
        elif x[2] == '5':
            for index in range(reg[int(x[1],16)]+1):
                mem[I+index] = reg[index]
        elif x[3] == '6':
            for index in range(reg[int(x[1],16)]+1):
                reg[index] = mem[I+index]
    #print(x,reg,I,stack)

path = 'tetris.c8'
reset_all()
load_rom(path)

pygame.init()
pygame.mixer.music.load('beep.mp3')
pygame.mixer.music.set_volume(1)
PIXEL_WIDTH = 20
(width,height) = (64*PIXEL_WIDTH,32*PIXEL_WIDTH)
disp = pygame.display.set_mode((width,height))
pixel = pygame.transform.scale(pygame.image.load('pixel.png').convert(),(PIXEL_WIDTH-1,PIXEL_WIDTH-1))
pygame.display.set_caption('Stardust - Chip-8 Emulator')
counter = 0
while pc < 4096:
    start = time.clock()
    keys = pygame.key.get_pressed()
    new_keys = key_input(keys)
    opcode = read_opcode(pc)
    run_opcode(opcode,new_keys)
    
    disp.fill((0,0,0))
    for x in range(32):
        for y in range(64):
            if screen[x][y]:
                disp.blit(pixel,(y*PIXEL_WIDTH,x*PIXEL_WIDTH))
    pygame.display.update()
    
    pc += 2
    delay -= 1 if delay > 0 else 0
    if sound > 0: pygame.mixer.music.play()
    sound -= 1 if sound > 0 else 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
dump = open('rawDump.txt','wb+')
for x in range(len(mem)):
    if len(hex(mem[x]))<4:
        mem[x] = '0'+hex(mem[x])[2:]
    else:
        mem[x] = hex(mem[x])[2:]
dump.write(bytearray.fromhex(''.join(mem)))
dump.close()


    
