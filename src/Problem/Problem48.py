"""@package Problem
    
    Project Eular - Problem 48

    The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

    Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

num = 0

for n in  range(1, 1001):
    num += n**n

print str(num)[-10:]
