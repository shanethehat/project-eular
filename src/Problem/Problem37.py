#!/usr/bin/python

"""
    Project Eular - Problem 37

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

import math

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

results = []
count = 10

while len(results) < 11:
    isTrunc = False
    if isPrime(count):
        string = str(count)
        isTrunc = True
        while len(string) > 1:
            string = string[1:]
            if not isPrime(int(string)):
                isTrunc = False
                break
        if isTrunc:
            string = str(count)
            while len(string) > 1:
                string = string[0:-1]
                if not isPrime(int(string)):
                    isTrunc = False
                    break
    if isTrunc:
        results.append(count)
    count += 1

print(results)
print sum(results)            
    
