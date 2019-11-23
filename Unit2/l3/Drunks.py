import random

# Base class to be inherited
class Drunk(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'This drunk is named: ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        return random.choice([
            (0.0, 1.0), # North
            (0.0, -1.0), # South
            (-1.0, 0.0), # West
            (1.0, 0.0) # East
        ])

class ColdDrunk(Drunk):
    def takeStep(self):
        return random.choice([
            (0.0, 0.9), # Wants to avoid cold (north)
            (0.0, -1.1), # He would rather go south
            (-1.0, 0.0), 
            (1.0, 0.0) 
        ])
    
