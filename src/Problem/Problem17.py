#!/usr/bin/python

"""
    Project Eular - Problem 17

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
 
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

w=lambda n:_(n, ["","thousand "] + p("m b tr quadr quint","illion"))[:-1] or "zero"

_=lambda n,S:n * "x" and _(n//M,S[1:]) + (Z[n%M//C]+"hundred ") * (n%M//C>0) + ((n>C and (not(n%C==0)))*"and ") + (n%C>19 and p("twen thir fo"+R,"ty")[n%C//10-2]+Z[n%10]or Z[n%C])+S[0]*(n%M>0)
p=lambda a,b="":[i+b+" "for i in a.split()]
R="r fif six seven eigh nine"
M=1000
C=100
Z=[""]+p("one two three four five%st nine ten eleven twelve"%R[5:20])+p(
        "thir fou"+R,"teen")

string = ''

for i in range(1, 1001):
    textNumber = w(i)
    print textNumber
    string += textNumber

string = string.replace(" ", "")

print string
print "Count: %s" %(len(string))
