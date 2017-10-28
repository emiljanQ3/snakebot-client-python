from snake import Snake
from obstacle import Obstacle
import util


class World:
    def __init__ (self, size=(20,20), snake_count=4, no_snake_radius=5, score_per_kill=5, obstacle_count=10):
        self.size = size
        self.snake_count = snake_count
        self.snakes = []
        self.tick = 0
        self.score_per_kill = score_per_kill
        self.obstacle_count = obstacle_count
        self.obstacles = []
        self.init()

    def init(self):
        # Spawn snakes
        for x in range(0, self.snake_count):
            self.snakes.append(Snake((0, x*2), "right"))
        self.snakes.append(Snake((5, 6), "down"))

        # Spawn obstacles
        for x in range(0, self.obstacle_count):
            self.obstacles.append(Obstacle((8, x)))

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
            # Check for collisions with obstacles
            for obstacle in self.obstacles:
                if obstacle.position == snake.positions[0]:
                    snake.kill()
        # Remove dead snakes
        for snake in self.snakes[:]:
            if not snake.isAlive:
                self.snakes.remove(snake)
        self.tick += 1

    def convert_position(self, position):
        return position[1]*self.size[0] + position[0]

    def get_map(self):
        game_map = {}
        game_map["width"] = self.size[0]
        game_map["height"] = self.size[1]
        game_map["worldTick"] = self.tick
        # Generate map information about snakes
        snake_infos = []
        for snake in self.snakes:
            snake_info = {}
            snake_info["points"] = snake.score
            snake_positions = []
            for position in snake.positions:
                # Todo this depends on how num is calculated in the real game
                snake_positions.append(self.convert_position(position))
            snake_info["positions"] = snake_positions
            snake_infos.append(snake_info)
        game_map["snakeInfos"] = snake_infos
        # Generate map information about obstacles
        obstacles = []
        for obstacle in self.obstacles:
            obstacles.append(self.convert_position(obstacle.position))
        game_map["obstacles"] = obstacles
        print(game_map)
        return util.Map(game_map)