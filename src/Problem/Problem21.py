#!/usr/bin/python

"""
    Project Eular - Problem 19
  
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

def getDivisorsSum(num):
    divisors = []
    current = 1
    end = num
    for current in range(1, num):
        if num % current == 0:
            divisors.append(current)
    return sum(divisors)

amicableTotal = 0    

for n in range (1, 10000):
    a = getDivisorsSum(n)
    b = getDivisorsSum(a)
    #print(n, a, b)
    if (n == b):
        print(n)
        amicableTotal += n

print(amicableTotal)
