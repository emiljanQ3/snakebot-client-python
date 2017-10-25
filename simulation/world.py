from snake import Snake
from random import randint


class World:
    def __init__ (self, size, snake_count, no_snake_radius):
        self.size = size
        self.snake_count = snake_count
        self.snakes = []

        for x in range(0, snake_count):
            self.snakes.append(Snake((0, x*2), "right"))

    def tick(self):
        for snake in self.snakes:
            if randint(0, 2) is 0:
                snake.grow()
            snake.move()