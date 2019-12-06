import numpy as np

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
      return np.nan

    return np.std(np.array([len(L[i]) for i in range(len(L))]))

# Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
# print(stdDevOfLengths(['a', 'z', 'p']))

# Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.
print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
