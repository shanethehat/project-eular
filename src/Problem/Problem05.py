"""@package Problem
    
    Project Eular - Problem 5
    
    What is the smallest positive number that is evenly divisible by all of the 
    numbers from 1 to 20?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
number = 2520
found = False

while found != True:
    number += 20
    for i in range(1,21):
        if number % i != 0:
            break
    else:
        found = True  
        
print('Result: %d' % number)        


