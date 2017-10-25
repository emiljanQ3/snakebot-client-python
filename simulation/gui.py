import sys, pygame, snake
pygame.init()

size = width, height = 320, 320
grid = (10, 10)
black = 0, 0, 0

snake = snake.Snake(position=(0,5), direction="right")

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    # print snake.positions
    for position in snake.positions:
        pygame.draw.rect(screen, (100,100,100), (position[0]*(width/grid[0]), position[1]*(height/grid[1]) ,width/grid[0], height/grid[1]))
    snake.grow()
    snake.move()
    pygame.display.flip()
    pygame.time.wait(500)