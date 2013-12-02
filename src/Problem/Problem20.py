#!/usr/bin/python

"""
    Project Eular - Problem 19
   
    n! means n x (n - 1) x ... x 3 x 2 x 1

    For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

large = 100;

for n in range(99, 0, -1):
    large *= n

stringLarge = str(large)

total = 0

for c in stringLarge:
    total += int(c)

print(total)
