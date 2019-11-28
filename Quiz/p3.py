def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    totalSum = 0
    for l in L:
        # The maximum possible multiplier can be s
        # meaning we will have to go up to s + 1, so we can backtrack to s as valid value for m
        # range ending dooes not equal the value passed as an argument, so we need to pass s + 2
        for m in range(0, s + 2):
            if (l * m + totalSum) > s:
                multipliers.append(m - 1)
                totalSum += l * (m - 1)
                break

    if (totalSum == s):
        return sum(multipliers)
    return "no solution"

# print(greedySum([1], 20))
# print(greedySum([], 10))
# print(greedySum([10, 5, 1], 14))
# print(greedySum([16, 12, 5, 3, 1], 24))