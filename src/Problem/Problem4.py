"""@package Problem
    
    Project Eular - Problem 4
    
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math

def isPalindrome(n):
    # convert to a string
    n = str(n)
    length = len(n)
    split = math.floor(length / 2)
    n2 = n[length - split : length]
    # reverse it
    n2 = n2[::-1]
    return n[0:split] == n2

for number in range(999*999,100*100,-1): 
    if isPalindrome(number):
        break

    
print('Result: %d' % number)
    