#!/usr/bin/python

"""
    Project Eular - Problem 22
  
    

    Using problem22_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

    What is the total of all the name scores in the file?
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

characters = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getNameScore(name):
    score = 0
    for char in name:
        score += getCharacterScore(char)
    return score

def getCharacterScore(character):
    return characters.index(character)

with open('files/problem22_names.txt') as f:
    nameBlock = f.read()
names = sorted(nameBlock[1:-1].split('","'))

line = 1
total = 0

for name in names:
    total += getNameScore(name) * line
    line += 1

print(total)
