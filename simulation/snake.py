class Snake:
    def __init__ (self, position, direction):
        self.positions = [position]
        self.direction = direction
        self.isAlive = True

    def set_direction(self, direction):
        # TODO this might not be nessesary as it might be allowed on the server
        if not self.is_valid_direction(direction):
            print("Invalid direction!")
            return
        self.direction = direction

    def is_valid_direction(self, direction):
        if self.direction == "up" and direction == "down":
            return False
        if self.direction == "right" and direction == "left":
            return False
        if self.direction == "down" and direction == "up":
            return False
        if self.direction == "left" and direction == "right":
            return False
        return True

    def move(self):
        # Move all body parts
        for x in range(len(self.positions), 1):
            self.positions[x] = self.positions[x-1]
        # Move head
        if self.direction == "up":
            self.positions[0] = self.positions[0] + (0, 1)
        if self.direction == "right":
            self.positions[0] = self.positions[0] + (1, 0)
        if self.direction == "down":
            self.positions[0] = self.positions[0] + (0, -1)
        if self.direction == "left":
            self.positions[0] = self.positions[0] + (-1, 0)