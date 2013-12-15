#!/usr/bin/python

"""
    Project Eular - Problem 33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

import math

def getDuplicateCharacter(num, den):
    sortedNum = sorted(str(num))
    sortedDen = sorted(str(den))
    if sortedNum == sortedDen:
        return -1 # false if both characters are present. This might be wrong.
    if sortedNum[0] in sortedDen:
        return sortedNum[0]
    if sortedNum[1] in sortedDen:
        return sortedNum[1]
    return -1

def isTrivial(num, den):
    return num % 10 == 0 or den % 10 == 0

def removeNumber(source, num):
    removed = str(source).replace(str(num), '', 1)
    return float(removed)
    

def reduces(n, d, dup):
    nReduced = removeNumber(n, dup)
    dReduced = removeNumber(d, dup)
    return float(d) / float(n) == dReduced / nReduced

fractions = []

for d in range(10, 100):
    for n in range(10, d):
        if n == d or isTrivial(n, d):
            continue
        dup = getDuplicateCharacter(n, d)
        if dup < 0:
            continue
        if reduces(n, d, dup):
            fractions.append([n,d])

print fractions

totalNum = 1
totalDen = 1

for f in fractions:
    totalNum *= f[0]
    totalDen *= f[1]

for i in range(int(math.ceil(math.sqrt(totalDen))), 1, -1):
    if totalNum % i == 0 and totalDen % i == 0:
        totalNum = totalNum / i
        totalDen = totalDen / i
        break

print totalNum, totalDen
