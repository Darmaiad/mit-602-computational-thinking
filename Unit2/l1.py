import pylab as plt
from enum import Enum

plotSize = 30

class PlotType(Enum):
    linear = "linear"
    quadratic = "quadratic"
    cubic = "cubic"
    exponential = "exponential"

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(plotSize):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

def plotList(x, y):
    plt.plot(x, y)

def getTitle(func):
    plt.title('Graph of ' + func + ' function')

def plot(y):
    plotList(mySamples, y)

def getXaxisLabel():
    plt.xlabel('Sample Points')

def plotExample():
    plot(myLinear)
    getXaxisLabel()
    plot(myQuadratic)
    plot(myCubic)
    plot(myExponential)

    plt.figure(PlotType.linear.value)
    getXaxisLabel()
    plt.ylabel(PlotType.linear.value.capitalize())
    plot(myLinear)

    plt.figure(PlotType.quadratic.value)
    getXaxisLabel()
    plot(myQuadratic)

    plt.figure(PlotType.cubic.value)
    getXaxisLabel()
    plt.ylabel(PlotType.cubic.value.capitalize())
    plot(myCubic)
    
    plt.figure(PlotType.exponential.value)
    getXaxisLabel()
    plt.ylabel(PlotType.exponential.value.capitalize())
    plot(myExponential)

    # Activate Quadratic figure, in order to add Y
    plt.figure(PlotType.quadratic.value)
    plt.ylabel(PlotType.quadratic.value.capitalize())

    # Re-open (Activate) each figure ino order to add title
    plt.figure(PlotType.linear.value)
    getTitle(PlotType.linear.value)

    plt.figure(PlotType.quadratic.value)
    getTitle(PlotType.quadratic.value)

    plt.figure(PlotType.cubic.value)
    getTitle(PlotType.cubic.value)
    
    plt.figure(PlotType.exponential.value)
    getTitle(PlotType.exponential.value)

    # Figures after activation, show both axes plus title
    # if we wanted to use the same window, and for instance
    # show only the title, we can clear the window, plot,
    # and then add the title only.
    plt.figure(PlotType.cubic.value)
    plt.clf() # Clear Frame
    plot(myCubic)

    # clf will remove the first window, meaning only
    # one cubic function will be visible.

def plotScaleExample():
    # in order to properly see the difference in growth
    # between linear and qudratic functions we need to
    # to select an appropriate Y-axis limit, we noticed
    # that if we plot we exponential function that goes
    # up to 140000, linear and qudratic functions appear
    # to be growing with the same rate, due to scaling
    yAxisFrom = 0
    yAxisTo = 1000
    plt.figure(PlotType.linear.value)
    # Get in the habbit of cleaning the windows first
    plt.clf()
    plt.ylim(yAxisFrom, yAxisTo)
    plot(myLinear)
    plt.figure(PlotType.quadratic.value)
    plt.clf()
    plt.ylim(yAxisFrom, yAxisTo)
    plot(myQuadratic)

def plotCompareExample():
    yAxisFrom = 0
    yAxisTo = 800

    plt.figure('lin quad')
    plt.clf()
    plt.title('Linear vs. Quadratic')
    plt.ylim(yAxisFrom, yAxisTo)
    plot(myLinear)
    plot(myQuadratic)

    plt.figure('cubic exp')
    plt.clf()
    plt.title('Cubic vs. Exponential')
    # Adding a legend, to know which func is being 
    # represented by each graph
    plt.plot(mySamples, myCubic, label = "Cubic")
    plt.plot(mySamples, myExponential, label = "Exponential")
    plt.legend(loc = 'upper left')

def plotStylingExample():
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear, 'b-', label = "Linear", linewidth = 5)
    plt.plot(mySamples, myQuadratic, 'ro', label = "Quadratic")
    plt.title('Linear vs. Quadratic')
    plt.legend(loc = 'upper left')

    plt.figure('cubic exp')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g^', label = "Cubic")
    plt.plot(mySamples, myExponential, 'r--', label = "Exponential" , linewidth = 4)
    plt.title('Cubic vs. Exponential')
    plt.legend(loc = 'upper left')

# Use two graphs in the same plot window 
def plotWithSubplotsExample():
    yAxisFrom = 0
    yAxisSmallTo = 800
    yAxisSmallLargeTo = 120000

    plt.figure('lin quad')
    plt.clf()
    # We have 3 arguments here meaning:
    # Number of rows, number of columns, and location
    plt.subplot(211)
    # Setting Y-axis lim in both graphs as a best practice
    plt.ylim(yAxisFrom, yAxisSmallTo)
    plt.plot(mySamples, myLinear, label = "Linear")
    plt.subplot(212)
    plt.ylim(yAxisFrom, yAxisSmallTo)
    plt.plot(mySamples, myQuadratic, label = "Quadratic")
    plt.title('Linear vs. Quadratic')
    plt.legend(loc = 'upper left')

    plt.figure('cubic exp')
    plt.clf()
    plt.subplot(121)
    plt.ylim(yAxisFrom, yAxisSmallLargeTo)
    plt.plot(mySamples, myCubic, label = "Cubic")
    plt.subplot(122)
    plt.ylim(yAxisFrom, yAxisSmallLargeTo)
    plt.plot(mySamples, myExponential, label = "Exponential")
    plt.title('Cubic vs. Exponential')
    plt.legend(loc = 'upper left')

# plotExample()
# plotScaleExample()
# plotCompareExample()
# plotStylingExample()
plotWithSubplotsExample()
