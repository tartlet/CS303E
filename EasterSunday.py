# File: EasterSunday.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/10/2020
# Date Last Modified: 09/10/2020
# Description of Program: Given a year that is input by the user, this program 
# calculates the day on which Easter Sunday falls for that year.

y = eval(input("Enter year: "))

a = y % 19

b = y // 100
c = y % 100

d = b // 4
e = int(b % 4)

g = (8 * b + 13) // 25


h = (19 * a + b - d - g + 15) % 30 

j = c // 4
k = c % 4
 
m = (a + 11 * h) // 319

r = (2 * e + 2 * j - k - h + m + 32) % 7

n = int((h - m + r + 90) / 25)
p = int((h - m + r + n + 19) % 32 )

print("In " + str(y) + " Easter Sunday is on month " + str(n)+ " and day " + str(p))