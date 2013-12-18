"""@package Problem
    
    Project Eular - Problem 40
   
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
   
s = ''
char = 1

while len(s) < 1000001:
    s += str(char)
    char += 1

result = 1

for m in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    result *= int(s[m-1:m])

print result

