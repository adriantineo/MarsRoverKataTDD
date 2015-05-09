

class MarsRover(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = "N"

    def getPosition(self):
        return (self.x, self.y)

    def getOrientation(self):
        return self.orientation

    def moveN(self):
        self.y += 1


