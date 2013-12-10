#!/usr/bin/python

"""
    Project Eular - Problem 23

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.  
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

import math
import time
import itertools

def getDivisorsOf(num):
    if num < 2:
        return []
    divisors = [1]
    end = math.sqrt(num)
    if end % 1 == 0:
        divisors.append(end)
    for i in range(2, int(math.ceil(end))):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num/i)
    return divisors

def removeDuplicates(l):
    return list(set(l))

def getAbundantNumbers():
    numbers = []
    for i in range (12, 28123):
        if sum(getDivisorsOf(i)) > i:
            numbers.append(i)
    return removeDuplicates(numbers)

def getSum(a, b):
    return a + b


start_time = time.time()

abundantNumbers = getAbundantNumbers()
print len(abundantNumbers), 'abundant numbers'

allNumbers = range (1, 28123)
abundantSums = []

for pair in itertools.product(abundantNumbers, repeat=2):
    abundantSums.append(getSum(*pair))

abundantSums = removeDuplicates(abundantSums)

allNumbers = [x for x in allNumbers if not x in abundantSums]

print len(allNumbers), 'remaining numbers'
print sum(allNumbers)

print time.time() - start_time, "seconds"
            
