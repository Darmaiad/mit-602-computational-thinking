###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
from time import time
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./ps1_cow_data.txt")


#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    cowsOnEarth = cows.copy()
    haveCowsOnEarth = True
    trips = []
    
    while haveCowsOnEarth:
        cowsToProcess = cowsOnEarth.copy()
        remainingLimit = limit
        cowsAvailable = True
        currentTrip = []

        while cowsAvailable:
            fattest = ""
            weight = 0
            
            # Find fattest cow
            for cow in cowsToProcess.items():
                cowName = cow[0]
                cowWeight = cow[1]
                if cowWeight >= weight:
                    weight = cowWeight
                    fattest = cowName
                    
            # If it fits, add it and subtract the weight
            if remainingLimit >= weight:       
                currentTrip.append(fattest)
                remainingLimit = remainingLimit - weight
                
            # Either way it has been processed for this trip
            del cowsToProcess[fattest]
            
            # If we have processed all the cows append trip and exit
            if len(cowsToProcess) == 0:
                cowsAvailable = False
                trips.append(currentTrip)
                # Remove from earth the cows that left for this trip
                for cowInCurrentTrip in currentTrip:
                    del cowsOnEarth[cowInCurrentTrip]
                    
        if len(cowsOnEarth) == 0:
            haveCowsOnEarth = False
    return trips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    c = cows.copy()
    completedPartitions = []
    
    # We are going to process all combinations of trips
    for partition in get_partitions(c):
        # Check that all trips in this combination are valid   
        for trip in partition:
            abort = False
            tripWeight = 0
            for cow in trip:
                tripWeight = tripWeight + c[cow]
                # If we pass the limit abort trip
                if (tripWeight > limit):
                    abort = True
                    break
            # If we abort a single trip, we abort that combination
            if abort == True:
                break
        # If we did not abort any trip, the combination is valid
        if abort == False:
            completedPartitions.append(partition)
                        
    minTrips = len(cows)
    chosenPartition = []
    # Find out which combination has the fewer number of trips
    for completedPartition in completedPartitions:
        completedPartitionTrips = len(completedPartition)
        if completedPartitionTrips < minTrips:
            minTrips = completedPartitionTrips
            chosenPartition = completedPartition
    return chosenPartition
            
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
        
    start = time()
    greedyTrips = greedy_cow_transport(cows, limit)
    end = time()
    print('Greedy: ', end - start, len(greedyTrips))
    
    start = time()
    bruteTrips = brute_force_cow_transport(cows, limit)
    end = time()
    print('Brute: ', end - start, len(bruteTrips))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows(file_path)
# cows = load_cows("ps1_cow_data.txt")
limit=20
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()
