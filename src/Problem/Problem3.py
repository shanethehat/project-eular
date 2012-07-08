"""@package Problem
    
    Project Eular - Problem 3
    
    What is the largest prime factor of the number 600851475143 ?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math

number = 600851475143
root = math.sqrt(number)
# ignore primes 1 and 2
prime = 3
largest = prime

while prime <= root:
    if prime % number == 0:
        largest = prime
    prime += 2

factor = number / largest    
print('Result: %d' % factor)