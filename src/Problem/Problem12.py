"""
    Project Eular - Problem 12
    
    The sequence of triangle numbers is generated by adding the natural numbers. So 
    the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
    
    The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    
    28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

import math

number = 1
nextNumber = 2
loop = True

def getDivisors(num):
    divisors = 0
    for n in range(1, math.ceil(num/2)):
        if num % n == 0:
            divisors += 1
    return divisors

while loop:
    print("current: %d" % number)
    number += nextNumber
    nextNumber += 1
    divisors = getDivisors(number)
    print("divisors: %d" % divisors)
    if divisors > 500:
        loop = False
    
        
print("result: %d" % number)