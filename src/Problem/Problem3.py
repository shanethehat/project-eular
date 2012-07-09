"""@package Problem
    
    Project Eular - Problem 3
    
    What is the largest prime factor of the number 600851475143 ?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math 

number =int( math.sqrt(600851475143))
print('Root: %d' % number)

maxFactor = 1

while number % 2 == 0:
    maxFactor = 2
    number = number / 2
    
i = 3
while i < number:
    while number % i == 0:
        maxFactor = i
        number = number / i
    i += 2
    
print('Result: %d' % maxFactor)