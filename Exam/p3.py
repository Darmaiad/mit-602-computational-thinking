import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    bucket = ['b', 'b', 'b', 'b', 'g', 'g', 'g', 'g']
    successes = 0

    for _ in range(numTrials):
        b = bucket.copy()
        draws = []
        for _ in range(3):
            idx = random.randint(0, len(b) -1)
            draws.append(b[idx])
            del b[idx]
        if len(set(draws)) == 1:
            successes += 1
    return successes / numTrials

print(drawing_without_replacement_sim(4000))
