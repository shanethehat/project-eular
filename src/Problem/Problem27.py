#!/usr/bin/python

"""
    Project Eular - Problem 27

    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.


    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

import math

def isPrime(num):
    if num < 1:
        return False
    # test num
    for i in range(3, int(math.ceil(math.sqrt(num)))+1,2):
        if(num % i == 0):
            return False
    else:
        return True

def getResult(num, a, b):
    return num**2 + (a*num) + b

storedA = 0
storedB = 0
storedN = 0

for a in range (-1000, 1000):
    for b in range (-1000, 1000):
        n = 0
        while isPrime(getResult(n, a, b)):
            n += 1
        if n > storedN:
            storedA = a
            storedB = b
            storedN = n

print storedA, storedB, storedN
print storedA * storedB
