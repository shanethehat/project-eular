"""@package Problem
    
    Project Eular - Problem 1
    
    Add all the natural numbers below one thousand that are multiples of 3 or 5.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

total = 0
current = 1

while current < 1000:
    if current % 3 == 0 or current % 5 == 0:
        total += current
    current += 1
    
print('Total: %d' % total)