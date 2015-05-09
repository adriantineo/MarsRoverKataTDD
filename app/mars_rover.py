

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

    def _incrementY(self):
        if self.getPosition()[1] < self.grid.getSize()[1] - 1:
            self.y += 1
        else:
            self.y = 0

    def _decrementY(self):
        if self.getPosition()[1] > 0:
            self.y -= 1
        else:
            self.y = self.grid.getSize()[1] - 1

    def _incrementX(self):
        if self.getPosition()[0] < self.grid.getSize()[0] - 1:
            self.x += 1
        else:
            self.x = 0

    def _decrementX(self):
        if self.getPosition()[0] > 0:
            self.x -= 1
        else:
            self.x = self.grid.getSize()[0] - 1

    def moveF(self):
        if self.getOrientation() == "N":
            self._incrementY()
        elif self.getOrientation() == "E":
            self._incrementX()
        elif self.getOrientation() == "S":
            self._decrementY()
        elif self.getOrientation() == "W":
            self._decrementX()
        else:
            raise Exception("Unknown orientation: {0}".format(self.getOrientation()))

    def getGrid(self):
        return self.grid

