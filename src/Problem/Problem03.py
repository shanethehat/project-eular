"""@package Problem
    
    Project Eular - Problem 3
    
    What is the largest prime factor of the number 600851475143 ?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math 

number = 600851475143

def findPrime(n):
    root = int(math.sqrt(n))
    for i in range(2,root):
        if n % i == 0:
            return findPrime(n/i)
    return n

maxFactor = findPrime(number)   
    
print('Result: %d' % maxFactor)