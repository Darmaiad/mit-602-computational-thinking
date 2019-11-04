# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1: # Basically (i // 2**j)
                combo.append(items[j])
        yield combo

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            exp = (i // 3**j ) % 3
            if exp != 0:
                item = items[j]
                if exp == 1: 
                    bag1.append(item)
                else:
                    bag2.append(item)
        yield bag1, bag2
        