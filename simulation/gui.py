import sys, pygame, snake
pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

snake = snake.Snake(position=(5,5), direction="right")

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    for position in snake.positions:
        print position + (4,4,)
        pygame.draw.rect(screen, (100,100,100), position + (4,4,))
    snake.move()
    pygame.display.flip()
    pygame.time.wait(100)