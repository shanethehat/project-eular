#!/usr/bin/python

"""
    Project Eular - Problem 19
    
    You are given the following information, but you may prefer to do some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    
    @package Problem
    @author Shane Auckland <shane.auckland@gmail.com>
"""

monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [1]
totalDays = 0
validSundays = 0

def isLeapYear(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0

def getMonthLength(month, year):
    length = monthLengths[month]
    if month > 0 and isLeapYear(year):
        length += 1
    return length

daysIn1900 = 366 if isLeapYear(1900) else 365
startDay = daysIn1900 % 7
print(startDay)

for y in range(1901, 2001):
    for i in range(12):
        days.append(days[-1] + getMonthLength(i, y))

for y in range(1901, 2001):
    totalDays += 366 if isLeapYear(y) else 365
    
for d in range(startDay, totalDays, 7):
    if d in days:
        validSundays += 1

print totalDays
print validSundays

