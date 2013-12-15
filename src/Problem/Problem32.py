#!/usr/bin/python

"""
    Project Eular - Problem 32

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""
import math

def isPandigital(aNum, bNum, nNum):
    joined = str(aNum) + str(bNum) + str(nNum)
    return sorted(joined) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

pandigitals = set([])

for n in range(1, 10000):
    for a in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % a == 0 and isPandigital(a, n / a, n):
            pandigitals.add(n)
print pandigitals
print sum(pandigitals)
             
