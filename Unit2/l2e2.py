import random

'''
    Generate a uniform distribution over the even 
    numbers between 0 and 100 (not including 100)
'''

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.choice([i for i in range(0, 100, 2)])
    
genEven()
