

class MarsRover():
    def __init__(self, grid):
        self.x = 0
        self.y = 0
        self.orientation = "N"
        self.grid = grid

    def getPosition(self):
        return (self.x, self.y)

    def getOrientation(self):
        return self.orientation

    def moveN(self):
        self.y += 1

    def getGrid(self):
        return self.grid

