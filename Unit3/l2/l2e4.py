import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    def draw(l):
        drawn = random.randint(1, len(l) - 1)
        drwanElem = l[drawn]
        del l[drawn]
        return l, drwanElem

    def runTrial():
        success = True
        b = ['R'] * 3 + ['B'] * 3
        draws = 3
        b2, d = draw(b)
        for i in range(draws - 1):
            b3, d2 = draw(b)
            if (d2 != d):
                success = False
                break
        return success

    successes = 0
    for i in range(numTrials):
        if(runTrial()):
            successes += 1
    return successes / numTrials

print(noReplacementSimulation(20))