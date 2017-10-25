from snake import Snake
from random import randint


class World:
    def __init__ (self, size, snake_count, no_snake_radius):
        self.size = size
        self.snake_count = snake_count
        self.snakes = []
        self.tick = 0

        for x in range(0, snake_count):
            self.snakes.append(Snake((0, x*2), "right"))

    def update(self):
        for snake in self.snakes:
            if self.tick % 3 is 0:
                snake.grow()
            snake.move()

            # Kill snake if outside map
            if (snake.positions[0][0] < 0 or snake.positions[0][0] > self.size[0]) or \
                    (snake.positions[0][1] < 0 or snake.positions[0][1] > self.size[1]):
                self.snakes.remove(snake)

        self.tick += 1