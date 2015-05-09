

class MarsRover():
    def __init__(self, grid):
        self.x = 0
        self.y = 0
        self.orientationVector = ["N", "E", "S", "W"]
        self.orientationIdx = 0
        self.grid = grid

    def getPosition(self):
        return (self.x, self.y)

    def getOrientation(self):
        return self.orientationVector[self.orientationIdx]

    def turnRight(self):
        self.orientationIdx = (self.orientationIdx + 1) % len(self.orientationVector)

    def turnLeft(self):
        self.orientationIdx = (self.orientationIdx - 1) % len(self.orientationVector)

    def moveF(self):
        if self.y < self.grid.getSize()[1] -1:
            self.y += 1
        else:
            self.y = 0

    def getGrid(self):
        return self.grid

