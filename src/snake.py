def snakeUpdater(action):
    def wrapper(*args):
        self = args[0]
        action(self)
        self.actions = self.actions[:self.length]
        self.updatePositions()

    return wrapper


class Snake():
    """Main player"""
    def __init__(self, start_x, start_y):
        super().__init__()
        
        self.length = 1
        self.x = start_x
        self.y = start_y
        self.positions = [(self.x, self.y)]
        self.actions = []
        self.direction = self.moveDown

    @snakeUpdater
    def moveUp(self):
        self.y -= 20
        self.direction = self.moveUp
        self.actions.insert(0, 'up')

    @snakeUpdater
    def moveDown(self):
        self.y += 20
        self.direction = self.moveDown
        self.actions.insert(0, 'down')

    @snakeUpdater
    def moveLeft(self):
        self.x -= 20
        self.direction = self.moveLeft
        self.actions.insert(0, 'left')

    @snakeUpdater
    def moveRight(self):
        self.x += 20
        self.direction = self.moveRight
        self.actions.insert(0, 'right')

    def moveByDirection(self):
        self.direction()

    def eat(self):
        self.length += 1
        self.positions.insert(0, (self.x, self.y))

    def pos(self):
        return self.x, self.y

    def updatePositions(self):
        try:
            for index in range(len(self.positions)):
                if index == 0:
                    self.positions[0] = (self.x, self.y)
                else:
                    prev_x, prev_y = self.positions[index - 1]

                    if self.actions[index - 1] == 'up':
                        self.positions[index] = (prev_x, prev_y + 20)
                    elif self.actions[index - 1] == 'down':
                        self.positions[index] = (prev_x, prev_y - 20)
                    elif self.actions[index - 1] == 'left':
                        self.positions[index] = (prev_x + 20, prev_y)
                    elif self.actions[index - 1] == 'right':
                        self.positions[index] = (prev_x - 20, prev_y)
        except Exception as err:
            print(str(err))
