#!/usr/bin/python

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

count = 3 # ensures that the first calculation is done for 1 + 2
loop = True
largest = 2

def getTriangle(length):
    return reduce(lambda x,y: x+y, range(1, length))

def findDivisors(num):
    divisors = 2 # start at two because num is a divisor of itself, and because 1
    current = 1
    end = num
    while (current < end):
        if (num % current == 0):
            end = num / current
            divisors += 2
        current += 1
    return divisors

while (loop):
    triangle = getTriangle(count);
    divisors = findDivisors(triangle);
    if (divisors > largest):
        largest = divisors
    print "%s : %s : %s : %s\n" %(count, triangle, divisors, largest)
    if (divisors > 500):
        loop = False
    count += 1
