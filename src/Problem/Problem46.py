"""@package Problem
    
    Project Eular - Problem 46

    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2x1**2
    15 = 7 + 2x2**2
    21 = 3 + 2x3**2
    25 = 7 + 2x3**2
    27 = 19 + 2x2**2
    33 = 31 + 2x1**2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""

import math

primes = set([2, 3, 5, 7])

def isPrime(num):
    if num < 2:
        return False
    if num in primes:
        return True
    if num % 3 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num)))+1, 2):
        if num % i == 0:
            return False
    primes.add(num)
    return True

n = 9

while True:
    print n
    if isPrime(n):
        n += 2
        continue
    s = 1
    while s**2 < n:
        diff = n - ((s**2) * 2)
        if isPrime(diff):
            n += 2
            break
        s += 1
    else:
        break

print n
        
