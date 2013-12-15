#!/usr/bin/python

"""
    Project Eular - Problem 34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

def getFactorial(d):
    if d < 2:
        return 1
    return reduce(lambda x, y: x*y, range(d, 0, -1))

def isCurious(num):
    nums = str(num)
    total = 0
    for c in nums:
        total += getFactorial(int(c))
    return total == num
        

results = []

for n in range(3, 100000):
    if isCurious(n):
        results.append(n)

print sum(results)
