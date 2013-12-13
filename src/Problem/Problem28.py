#!/usr/bin/python

"""
    Project Eular - Problem 28

    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

"""
   n = number of cells from center point, 0 = center, 1 = first ring etc
   a = direction of travel:
       2 = bottom right
       4 = bottom left
       6 = top left
       8 = top right
"""
def getAdderValue(n, a):
    return (8 * (n - 1)) + a

total = 1
lastValues = {
    2: 1,
    4: 1,
    6: 1,
    8: 1
}

for n in range(1, 501):
    for a in lastValues:
        adder = getAdderValue(n, a)
        lastValues[a] += adder
        total += lastValues[a]

print total
