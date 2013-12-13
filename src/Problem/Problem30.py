#!/usr/bin/python

"""
    Project Eular - Problem 30

    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

def getDigits(num):
    string = str(num)
    return [int(c) for c in string]

matches = []

for n in range(2, 500000):
    digits = getDigits(n)
    powers = []
    for d in digits:
        powers.append(d**5)
    sumPowers = sum(powers)
    if sumPowers == n:
        matches.append(n)

print matches
print sum(matches)
