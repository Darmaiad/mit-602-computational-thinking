# You are given the following partially completed function and a file julytemps.txt containing 
# the daily maximum and minimum temperatures for each day in Boston for the 31 days of July 2012. 
# In the loop, we need to make sure we ignore all lines that don't contain the relevant data.

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if (len(fields) != 3) or (not fields[0].isnumeric()):
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

print(loadFile())