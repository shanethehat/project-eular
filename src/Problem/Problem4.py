"""@package Problem
    
    Project Eular - Problem 4
    
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
import math

def isNotPalindrome(n):
    # convert to a string
    n = str(n)
    length = len(n)
    split = math.floor(length / 2)
    n2 = n[length - split : length]
    # reverse it
    n2 = n2[::-1]
    return n[0:split] != n2

a = 999    
number = a * 999

while isNotPalindrome(number):
    a -= 1
    number = a * 999
    
print('Result: %d' % number)
    