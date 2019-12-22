import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    masks = []
    solutions = []
    for i in range(2**len(choices)):
        mask = []
        binary = bin(i)[2:]
        strMask = (len(choices) - len(binary)) * '0' + binary
        for ch in strMask:
            mask.append(int(ch))
        masks.append(mask)
    # print(masks)

    for mask in masks:
        subTotal = 0
        for i in range(len(mask)):
            subTotal += mask[i] * choices[i]
        if(subTotal == total):
            solutions.append(mask)
    # print(solutions)

    if len(solutions) == 0:
        subparSolution = 0
        subparMask = []
        for mask in masks:
            subTotal = 0
            for i in range(len(mask)):
                subTotal += mask[i] * choices[i]
            if(subTotal >= subparSolution and subTotal < total ):
                subparSolution = subTotal
                subparMask = mask
        solutions.append(subparMask)
            
    bestSolution = solutions[0]
    for solution in solutions:
        if sum(solution) < sum(bestSolution):
            bestSolution = solution
    return np.array(bestSolution)

# print(find_combination([1,2,2,3], 4))
# print(find_combination([1,1,1,9], 4))
# print(find_combination([1,1,3,5,3], 5))
print(find_combination([4, 10, 3, 5, 8], 1))
