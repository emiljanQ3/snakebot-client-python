from snake import Snake
from random import randint


class World:
    def __init__ (self, size, snake_count, no_snake_radius, score_per_kill):
        self.size = size
        self.snake_count = snake_count
        self.snakes = []
        self.tick = 0
        self.score_per_kill = score_per_kill

        for x in range(0, snake_count):
            self.snakes.append(Snake((0, x*2), "right"))
        self.snakes.append(Snake((5, 6), "down"))

    def update(self):
        for snake in self.snakes:
            if self.tick % 3 is 0:
                snake.grow()
            snake.move()

            # Kill snake if outside map
            if (snake.positions[0][0] < 0 or snake.positions[0][0] > self.size[0]) or \
                    (snake.positions[0][1] < 0 or snake.positions[0][1] > self.size[1]):
                snake.kill()

            # Check for collisions with other snakes
            # TODO this might be wrong if both goes into eachothers heads.
            for other_snake in self.snakes:
                # Create iterator for iterating all snake parts. If other_snake is same as snake, skip head
                iter_snake = iter(other_snake.positions)
                if other_snake is snake:
                    iter_snake = next(iter_snake)
                for other_snake_parts in iter_snake:
                    if other_snake_parts == snake.positions[0]:
                        if not other_snake is snake:
                            other_snake.add_score(self.score_per_kill)
                        snake.kill()
        # Remove dead snakes
        for snake in self.snakes[:]:
            if not snake.isAlive:
                self.snakes.remove(snake)
        self.tick += 1