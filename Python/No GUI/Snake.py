import pygame as pg, random, os

# Change these to alter map size
gridDims = (30,30)
boxWidth = 20
clock_speed = 15


os.environ['SDL_VIDEO_CENTERED'] = '1'
points = 0
grid = [[0 for x in range(gridDims[1])] for y in range(gridDims[0])]
black, white = (0,0,0), (255,255,255)
boxDims = (boxWidth,boxWidth)
pg.init()
screen = pg.display.set_mode((gridDims[1]*boxWidth,gridDims[0]*boxWidth))
pg.display.set_caption("Snake")

def placeBox(y,x,color): # Place a single box at coordinates given
    box = pg.Rect((boxWidth*x, boxWidth*y), boxDims)
    pg.draw.rect(screen, color, box)

def spawnFood(snake): # Place new food in empty spot on grid
    foodY, foodX = random.randrange(0,gridDims[0]), random.randrange(0,gridDims[1])
    while [foodY, foodX] in snake:
        foodY, foodX = random.randrange(0,gridDims[0]), random.randrange(0,gridDims[1])
    grid[foodY][foodX] = 1
    placeBox(foodY,foodX,white)

def move(direction, snake): # Move the snake in a given direction
    h = snake[-1] # Head of snake
    newPiece = 0
    y,x = 0,0
    if direction < 2: # Up and down
        y = h[0]-1+direction*2
        x = h[1]
    else: # Left and right
        y = h[0]
        x = h[1]+5-direction*2
    y %= gridDims[0] # Protecting against overflow
    x %= gridDims[1]
    if not [y,x] in snake: # Checking for collision
        if grid[y][x]:
            newPiece = 1
        else:
            grid[y][x] = 1
        placeBox(y,x,white)
        snake.append([y,x])
    else:
        return False
    if newPiece: # Absorbing food
        spawnFood(snake)
        return 1
    else: # Removing snake tail
        t = snake[0] # Tail of snake
        grid[t[0]][t[1]] = 0
        placeBox(t[0],t[1],black)
        snake.pop(0)
    return 0

snakeInitY = random.randrange(1,gridDims[0])
snakeInitX = random.randrange(0,gridDims[1])
snake = [[snakeInitY,snakeInitX],[snakeInitY-1,snakeInitX]]
direction = 0 # Start facing upwards
spawnFood(snake)

running = True
game = True
lost = False
clock = pg.time.Clock()
while running:
    clock.tick(clock_speed)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE: # Restart the game
                game = True
                grid = [[0 for x in range(gridDims[1])] for y in range(gridDims[0])]
                screen.fill(black)
                snakeInitY = random.randrange(1,gridDims[0])
                snakeInitX = random.randrange(0,gridDims[1])
                snake = [[snakeInitY,snakeInitX],[snakeInitY-1,snakeInitX]]
                direction = 0
                spawnFood(snake)
            keys = pg.key.get_pressed()[273:277] # Grab pressed arrow keys (U/D/R/L)
            if keys.count(1):
                key = pg.key.get_pressed()[273:277].index(1)
            else:
                continue
            if (direction+key)%4 == 1: # This prevents backpedaling into yourself
                #   Direction and key cannot equal 1 and 0 or 2 and 3 in any order, or it is colliding
                #   with the piece immediately behind the head of the snake. These combinations sum
                #   to 1 and 5, respectively, each equal to 1 modulo 4.
                continue
            direction = key
    if game:
        movement = move(direction, snake)
        pg.display.update()
        if movement is False: # Movement is False if collision is detected
            game = False
            print("You lost with {} points.".format(points))
        elif movement: # Movement returns 1 if food is eaten
            points += 1
pg.quit()
