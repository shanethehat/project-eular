"""@package Problem
    
    Project Eular - Problem 42
 
    The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

    Using files/problem42_words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
    
    @author Shane Auckland <shane.auckland@gmail.com>
    
"""
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('files/problem42_words.txt') as f:
    wordBlock = f.read()
    words = wordBlock[1:-1].split('","')

scores = []

for w in words:
    score = 0
    for c in w:
        score += characters.find(c) + 1
    scores.append(score)

scores.sort()

target = scores[-1]
triangles = [1]
n = 3

while triangles[-1] < target:
    triangles.append(int(0.5 * n * (n-1)))
    n += 1

print len([x for x in scores if x in triangles])

