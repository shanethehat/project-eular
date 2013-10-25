#!/usr/bin/python

"""
    Project Eular - Problem 14
   
    The following iterative sequence is defined for the set of positive integers:

    n = n/2 (n is even)
    n = 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?

        NOTE: Once the chain starts the terms are allowed to go above one million.
 
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

def numberIsEven(number):
    return number % 2 == 0

def getNumberFromEven(number):
    return number / 2

def getNumberFromOdd(number):
    return (number * 3) + 1

length = 0
start = 0

for i in range(1, 1000000):
    print "Starting: %s" %(i)
    num = i
    tempLength = 0
    while num != 1:
        num = getNumberFromEven(num) if numberIsEven(num) else getNumberFromOdd(num)
        tempLength += 1
    print "Sequence complete: %s %s" %(tempLength, length)
    if (tempLength > length):
        length = tempLength
        start = i

print "Start: %s, Length: %s" %(start, length)
