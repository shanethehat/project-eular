"""@package Problem
    
    Project Eular - Problem 9
    
    There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find 
    the product abc.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

target = 1000

for c in range(1, 600):
    for b in range(1, c):
        for a in range(1, b):
            if (a**2 + b**2 == c**2):
                # we have a triple
                total = a + b + c
                print("total: %d" % total)
                if (total == target):
                    product = a * b * c
                    print("result: %d" % product)
                    break
                    