"""
    Project Eular - Problem 10
    
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the 
    primes below two million.
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

import math, pprint

# assumption that all primes are either 6n-1 or 6n+1
n = 2

# start with obvious primes less than 11 (6*2-1)
primes = [1, 2, 3, 5, 7]

def isPrime(num):
    for i in range(3, math.ceil(math.sqrt(num))+1,2):
        if(num % i == 0):
            return False
    else:
        return True
    

while n*6-1 < 2000000:
    if isPrime(6*n-1):
        primes.append(6*n-1)
        if (n*6 == 2000000):
            break
    if isPrime(6*n+1):
        primes.append(6*n+1)
    n += 1
    print("next: %d" % n)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(primes)
print("result: %d" % sum(primes))