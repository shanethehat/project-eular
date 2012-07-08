"""@package Problem
    
    Project Eular - Problem 2
    
    By considering the terms in the Fibonacci sequence whose values do not exceed 
    four million, find the sum of the even-valued terms.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

a = 1
b = 2

total = 0

while b <= 4000000:
    if b % 2 == 0:
        total += b
    tmp = a + b
    a = b
    b = tmp
    
print('Total: %d' % total)