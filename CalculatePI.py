# File: CalculatePI.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 10/23/2020
# Date Last Modified: 10/23/2020
# Description of Program: Monte Carlo simulation for variable number of "throws" to calculate pi.

import math
import random

def computePI(numThrows):
    count = 0
    for i in range(0, numThrows):
        xPos = random.uniform (-1.0, 1.0)
        yPos = random.uniform (-1.0, 1.0)
        distanceCenter = math.hypot(xPos, yPos)
        if distanceCenter < 1:
            count += 1
    prob = count/numThrows
    calculatedpi = prob * 4
    return calculatedpi
        

def main ():
    num = 100
    while num <= 10000000:
        calcpi =  computePI(num)
        diff = calcpi - math.pi
        print("num =", format(num, "<8d"), "   Calculated PI =", format(calcpi, "<8.6f"), "   Difference =", format(diff, "<+9.6f"))
        num = num * 10

main()