"""@package Problem
    
    Project Eular - Problem 6
    
    Find the difference between the sum of the squares of the first one hundred 
    natural numbers and the square of the sum.
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
sumOfSquares = 0
for i in range(1,101):
    sumOfSquares += i**2
    
squareOfSums = 0
for i in range(1,101):
    squareOfSums += i
squareOfSums = squareOfSums**2

result = squareOfSums - sumOfSquares

print('Sum of squares: %d' % sumOfSquares)
print('Square of sums: %d' % squareOfSums)
print('Result: %d' % result)