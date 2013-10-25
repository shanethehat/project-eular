#!/usr/bin/python

"""
    Project Eular - Problem 14

    Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    
    How many such routes are there through a 20x20 grid?
 
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

"""
    Uses binomial coefficients to calculate to possibilities
    http://www.mathwords.com/b/binomial_coefficients.htm
"""
gridX = 20
gridY = 20

topNum = gridX + gridY
bottomNum = gridX

def getFactorial(num):
    return reduce(lambda x, y: x*y, range(1, num+1))

topFactored = getFactorial(topNum)
bottomLeftFactored = getFactorial(bottomNum)
bottomRightFactored = getFactorial(topNum - bottomNum)

result = topFactored / (bottomLeftFactored * bottomRightFactored)

print "Result: %s" %(result)
