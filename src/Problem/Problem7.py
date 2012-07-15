"""@package Problem
    
    Project Eular - Problem 7
    
    What is the 10001st prime number?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math;

totalPrimes = 10001
# start with the primes 1, 2, 3, 5, 7
foundPrimes = 5
# keep track of the last found prime
lastPrime = 7
# assumption that all primes are either 6n-1 or 6n+1
n = 2

def isPrime(num):
    # test num
    for i in range(3, math.ceil(math.sqrt(num))+1,2):
        if(num % i == 0):
            return False
    else:
        return True
    

while foundPrimes < totalPrimes:
    if isPrime(6*n-1):
        foundPrimes += 1
        lastPrime = 6*n-1
        if foundPrimes == totalPrimes:
            break
    if isPrime(6*n+1):
        foundPrimes += 1
        lastPrime = 6*n+1
    n += 1
    
print("Result 10001st prime is: %d" % lastPrime)