#!/usr/bin/python

"""
    Project Eular - Problem 39

    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""
import math

def findSolutionsFor(p):
    limit = p/2
    solutions = []
    for a in range(1, limit):
        for b in range(1,limit):
            c = math.sqrt(a**2 + b**2)
            if c % 1 != 0:
                continue
            if a+b+int(c) == p:
                sortSolution = sorted([a,b,c])
                if not sortSolution in solutions:
                    solutions.append(sortSolution)
    return len(solutions)

largest = 0;
maxP = 0

for perimeter in range(2, 1001):
    print perimeter
    num = findSolutionsFor(perimeter)
    if num > largest:
        largest = num
        maxP = perimeter

print maxP
