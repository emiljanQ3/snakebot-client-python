import sys, pygame
from world import World
pygame.init()

size = width, height = 320, 320
black = 0, 0, 0
world = World((10, 10), 3, 4)
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    # print snake.positions
    for snake in world.snakes:
        for position in snake.positions:
            pygame.draw.rect(screen, (100,100,100), (position[0]*(width/world.size[0]), position[1]*(height/world.size[1]) ,width/world.size[0], height/world.size[1]))

    world.tick()

    pygame.display.flip()
    pygame.time.wait(500)