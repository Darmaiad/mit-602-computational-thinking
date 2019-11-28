def max_contig_sum(L): 
    """ L, a list of integers, at least one positive 
    Returns the maximum sum of a contiguous subsequence in L 
    """
    maxSum = -999999999
    currentSum = 0
       
    for l in L: 
        currentSum += l 
        if (maxSum < currentSum): 
            maxSum = currentSum 
  
        if currentSum < 0: 
            currentSum = 0   

    return maxSum

# in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
print(max_contig_sum([3, 4, -1, 5, -4]))

# in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
print(max_contig_sum([3, 4, -8, 15, -1, 2]))