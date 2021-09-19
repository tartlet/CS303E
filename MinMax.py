# File: MinMax.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/02/2020
# Date Last Modified: 10/02/2020
# Description of Program: Program asks user to continuously input integers until 'stop' is typed. For each
# integer entered, the program compares it to the previously entered minimum and maximum integers to 
# see if the newly entered integer is a new minimum or maximum. If the user inputs 'stop,' the program
# does not ask for any more integers and displays the maximum and minimum of all entered integers.

userInputNumber = input("Enter an integer or 'stop' to end: ")
if userInputNumber == 'stop':
    print("You didn't enter any numbers")
    exit()
else:
    maxInitialNumber = int(userInputNumber)
    minInitialNumber = int(userInputNumber)
    
while userInputNumber != 'stop':
    userInputNumber = input("Enter an integer or 'stop' to end: ")
    if userInputNumber == 'stop':
        break
    if int(userInputNumber) < minInitialNumber:
        minimumNumber = int(userInputNumber)
    else:
        minimumNumber = minInitialNumber
    if int(userInputNumber) > maxInitialNumber:
        maximumNumber = int(userInputNumber)
    else: 
        maximumNumber = maxInitialNumber
    minInitialNumber = minimumNumber
    maxInitialNumber = maximumNumber
    
    
print("The maximum is", maximumNumber)
print("The minimum is", minimumNumber)
