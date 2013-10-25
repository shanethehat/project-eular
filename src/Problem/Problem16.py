#!/usr/bin/python

"""
    Project Eular - Problem 16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
 
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

start = str(2**1000)
total = 0

for char in start:
    total += int(char)

print "Result: %s" %(total)
