import pylab as plt

from Drunks import UsualDrunk, EDrunk
from Field import Field
from Location import Location

drunk = UsualDrunk('U')
edrunk = EDrunk('E')

field = Field(drunk)
loc = Location(0,0)
field.addDrunk(drunk, loc)

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
    
walks = []
ewalks = []
numOfWalks = 1350
numOfSteps = 350

for i in range(numOfWalks):
    walks.append(walkVector(field, drunk, numOfSteps))
    ewalks.append(walkVector(field, drunk, numOfSteps))
    
def getCoordinates(walkVectors):
    xs = []
    ys = []
    for walk in walkVectors:
        x , y = walk
        xs.append(x)
        ys.append(y)
    return xs, ys
        
xs, ys = getCoordinates(walks)
exs, eys = getCoordinates(ewalks)

plt.figure('Usual')
plt.title('Usual')
plt.plot(xs, ys, 'ro')
plt.axis([-100, 100, -100, 100])
plt.figure('Eucl')
plt.title('Eucl')
plt.plot(exs, eys, 'ro')
plt.axis([-100, 100, -100, 100])
# print(walks)
    
