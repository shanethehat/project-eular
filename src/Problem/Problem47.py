"""@package Problem
    
    Project Eular - Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 x 7
    15 = 3 x 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2**2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19.

    Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

def getDistinctFactors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num /= divisor
        divisor += 1
    return set(factors)

n = 600
found = 0
target = 4

while found < target:
    print n, found
    f = getDistinctFactors(n)
    n += 1
    found = found + 1 if len(f) == target else 0

print n - target   
