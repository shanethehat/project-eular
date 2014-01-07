"""@package Problem
    
    Project Eular - Problem 49
    
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

import math
import itertools

primes = set([2, 3, 5, 7])

def isPrime(num):
    if num < 2:
        return False
    if num == 2 or num == 3 or num in primes:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num)))+1, 2):
        if num % i == 0:
            return False
    primes.add(num)
    return True

def isSequence(subject, num):
    if not isPrime(subject):
        return False
    perms = [''.join(p) for p in itertools.permutations(str(num))]
    return str(subject) in perms

step = 3330

for n in range(1000, 10000):
    if not isPrime(n) or n == 1487:
        continue
    first = n + step
    second = n + step*2
    if isSequence(first, n) and isSequence(second, n):
        print 'Found', n, first, second
        break
else:
    print 'Failed'    
