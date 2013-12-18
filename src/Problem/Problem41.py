"""@package Problem
    
    Project Eular - Problem 41
  
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
   
import math
import itertools

primes = set([2, 3, 5, 7])

def isPrime(num):
    if num < 2:
        return False
    if num == 2 or num == 3 or num in primes:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num)))+1, 2):
        if num % i == 0:
            return False
    primes.add(num)
    return True

def isPandigital(num):
    return sorted(num) == range(1, len(num))

largest = 0

for s in [123, 1234, 12345, 123456, 1234567, 12345678, 123456789]:
    for v in [''.join(p) for p in itertools.permutations(str(s))]:
        intV = int(v)
        if isPrime(intV) and intV > largest:
            largest = intV

print largest

