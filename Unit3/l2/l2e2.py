import random

# If you wanted to run a simulation that estimates the value of  2–√  in a way 
# similar to the Pi estimation shown in lecture, what geometric shape would you throw needles at?
# ANS: A flat line ranging from 0 to root 2 and with a subsection that spans from 0 to 1.

# If the needles fall in the section from 1 to 2 then the ratio of the square of the successful random 
# throws in the unit section between 1 and 2 to the total number of throws will approximate the decimal 
# fraction of root 2. Since we started the lower bound at 1, we have to add 1 to the fraction to get the 
# actual approximation of root 2.

def throwNeedles(numNeedles):
    success = 0
    for n in range(numNeedles):
        x = random.random()
        print(x, (1 + x)**2)
        if (1+x)**2 < 2.0:
            success += 1
    sqrt2 = 1+(float(success)/numNeedles)
    return sqrt2   

print(throwNeedles(10))   