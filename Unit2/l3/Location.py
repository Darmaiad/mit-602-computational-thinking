class Location(object):
    def __init__(self, x, y):
        # X and Y are floats
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, deltaX, deltaY):
        # deltaX and deltaY are floats
        return Location(self.x + deltaX, self.y + deltaY)

    def distFrom(self, other):
        distX = self.x - other.x
        distY = self.y - other.y
        # Pythagorean theorem
        return (distX**2 + distY**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
