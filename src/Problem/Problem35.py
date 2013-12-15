#!/usr/bin/python

"""
    Project Eular - Problem 35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""
import itertools, math

primes = set([])

def rotate(string):
    return string[1:] + string[0]

def getRotations(num):
    stringNum = str(num)
    rotations = [stringNum]
    rotated = rotate(stringNum)
    while rotated != stringNum:
        rotations.append(rotated)
        rotated = rotate(rotated)
    return rotations

def isPrime(num):
    if num == 2 or num == 3 or num in primes:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num))), 2):
        if num % i == 0:
            return False
    return True

circularPrimes = []

for n in range(2, 1000000):
    print n
    permutations = getRotations(n)
    fail = False
    for p in permutations:
        if not isPrime(int(p)):
            fail = True
            break
        primes.add(int(p))
    if not fail:
        circularPrimes.append(n)

print circularPrimes
print(len(circularPrimes))

