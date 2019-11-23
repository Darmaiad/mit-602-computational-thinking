# A collection of places and Drunks
class Field(object):
    def __init__(self, drunks):
        # Dictionary <Drunk, Location>
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            # drunk will be used as a key in the drunks dict
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in Field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in Field')

        distX, distY = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(distX, distY)

    # def __str__(self):
    #     return '<' + str(self.drunks) + ', ' + str(self.y) + '>'
