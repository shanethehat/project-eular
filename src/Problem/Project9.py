"""@package Problem
    
    Project Eular - Problem 9
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find 
    the product abc.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math

count = 1;

for a in range(3, 500, 2):
    b = (count * a) + a
    c = math.sqrt(a**2 + b**2) 
    n = a + b + c
    print("Sum: {}".format(n))
    if 1000 == int(n):
        product = a * b * c
        print("Result: {0} x {1} x {2} = {3}".format(a,b,c,product))
        break;
           
        
    