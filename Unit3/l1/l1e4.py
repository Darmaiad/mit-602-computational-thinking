import numpy as np

# The coefficient of variation is the standard deviation divided by the mean. 
# Loosely, it's a measure of how variable the population is in relation to the mean.
# Compute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places.

def getCoefficient(L):
    sample = np.array(L)

    return round(np.std(sample) / np.mean(sample), 3)

print(getCoefficient([10, 4, 12, 15, 20, 5]))
