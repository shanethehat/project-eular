#!/usr/bin/python

"""
    Project Eular - Problem 31

    In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
    It is possible to make $2 in the following way:

    1x$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
    How many different ways can $2 be made using any number of coins?

    @package Problem
    @author Shane Auckland <shane.auckland@gmail.con>
"""

coins = [200, 100, 50, 20, 10, 5, 2]

def findTotal(i, l):
    if i == len(coins):
        return 1
    subTotal = 0
    for n in range(l, -1, -coins[i]):
        subTotal += findTotal(i+1, n)
    return subTotal
#
print findTotal(0, coins[0])

