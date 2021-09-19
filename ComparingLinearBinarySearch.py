# File: ComparingLinearBinarySearch.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 11/06/2020
# Date Last Modified: 11/06/2020
# Description of Program: A very poorly written program that compares the number of probes for binary and linear searches. For linear search, different numbers of tests
# carried out for the list with a given random integer. For binary search, 1000 tests are carried out and the difference from log2(1000) is printed. I probably
# should rewrite the linear search part to give it a number of tests input but I couldn't be bothered. I am tired.

import random 
import math 

def linearSearch(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i 
    return -1   
def binarySearch(lst, key):
    count = 0
    low = 0
    high = len(lst)-1
    while high >= low:
        count += 1
        mid = (high + low) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    return (-low - 1, count)
    
def makeListPartOne():       
    partOne = []
    for i in range(0,1000):
        partOne.append(i)
    random.shuffle(partOne)
    return partOne

def makeListPartTwo():
    partTwo = []
    for i in range(0,1000):
        partTwo.append(i)
    return partTwo
   
print("Linear search:")
number = 10
list1 = makeListPartOne()
# 10 tests
count10 = 0
total10 = 0
while count10 < 10:
    numProbes10 = linearSearch(list1, random.randint(0,999)) + 1
    total10 += numProbes10 
    count10 += 1
avg10 = total10 / 10 
print("  Tests:", format(10, "<6d"), "  Average probes:", avg10)

#100 tests
count100 = 0
total100 = 0
while count100 < 100:
    numProbes100 = linearSearch(list1, random.randint(0,999)) + 1
    total100 += numProbes100 
    count100 += 1
avg100 = total100 / 100 
print("  Tests:", format(100, "<6d"), "  Average probes:", avg100)

#1000 tests
count1000 = 0
total1000 = 0
while count1000 < 1000:
    numProbes1000 = linearSearch(list1, random.randint(0,999)) + 1
    total1000 += numProbes1000 
    count1000 += 1
avg1000 = total1000 / 1000
print("  Tests:", format(1000, "<6d"), "  Average probes:", avg1000)

#10000 tests
count10000 = 0
total10000 = 0
while count10000 < 10000:
    numProbes10000 = linearSearch(list1, random.randint(0,999)) + 1
    total10000 += numProbes10000 
    count10000 += 1
avg10000 = total10000 / 10000
print("  Tests:", format(10000, "<6d"), "  Average probes:", avg10000)

#100000 tests
count100000 = 0
total100000 = 0
while count100000 < 100000:
    numProbes100000 = linearSearch(list1, random.randint(0,999)) + 1
    total100000 += numProbes100000 
    count100000 += 1
avg100000 = total100000 / 100000
print("  Tests:", format(100000, "<6d"), "  Average probes:", avg100000)   

list2 = makeListPartTwo()
print("Binary search:")
count = 0
total = 0
while count <= 999:
    tempindex, tempcount = binarySearch(list2, random.randint(0,999))
    total += tempcount
    count += 1
avgProbes = total/1000
print("  Average number of probes:", avgProbes)
print("  Differs from log2(1000) by:", (math.log(1000, 2) - avgProbes))