#!/usr/bin/python

"""
    Project Eular - Problem 36

    The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

import math

def isPalindrome(n):
    length = len(n)
    if length == 1:
        return True
    split = int(math.floor(length / 2))
    n2 = n[length - split : length]
    # reverse it
    n2 = n2[::-1]
    return n[0:split] == n2

def decimal2Binary(n):
    string = ''
    if n == 0: 
        return '0'
    while n > 0:
        string = str(n % 2) + string
        n = n >> 1
    return string

results = []

for n in range(1, 1000000):
    if isPalindrome(str(n)):
        if isPalindrome(decimal2Binary(n)):
            results.append(n)

print results
print sum(results)

