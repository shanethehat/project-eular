#!/usr/bin/python

"""
    Project Eular - Problem 25

    What is the first term in the Fibonacci sequence to contain 1000 digits?

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""
def checkLength(num):
    return len(str(num))

a = 1
b = 1
count = 1

while checkLength(a) < 1000:
    temp = a+b
    a = b
    b = temp
    count += 1

print count
