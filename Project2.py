# File: Project2.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 11/06/2020
# Date Last Modified: 11/06/2020 
# Description of Program: Using the "isPrime" and "findNextPrime" functions from the
# slides, this program accepts input from a user. The user can either factor an integer
# or the user can find out if the integer is prime. The program also accepts invalid 
# commands and returns an error statement. Typing "end" into the prompt for a command
# allows the user to terminate the program. 


import math
print("Welcome to the Prime factory!")
print("")
userInput = input("Enter a command (factor, isprime, end): ")

def isPrime(num):
    if num % 2 == 0:
        return (num == 2)
    divisor = 3
    while divisor <= math.sqrt(num):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True
    
def findNextPrime(num):
    if num < 2:
        return 2
    guess = num + 1
    while (not isPrime(guess)):
        guess += 1
    return guess
    
def findFactorization(num):
    if isPrime(num):
        listFactors = [num]
        return listFactors
    else:
        listFactors = list()
        divisor = 2
        while num > 1:
            if num % divisor == 0:
                listFactors.append(divisor)
                num /= divisor 
            else:
                divisor = findNextPrime(divisor)
        return listFactors   

while userInput.lower() != "end":
    if userInput.lower() == "factor":
        inteNum = int(input("Enter an integer > 1: "))
        if inteNum <= 1:
            print("Illegal input: " + str(inteNum) + "; input must be an integer > 1.")
            print("")
            userInput = input("Enter a command (factor, isprime, end): ")
            continue
        else:
            print("The prime factorization of", inteNum, "is:", findFactorization(inteNum))
            print("")
            userInput = input("Enter a command (factor, isprime, end): ")
            continue
    elif userInput.lower() == "isprime":
        isPrimeNum = int(input("Enter an integer > 1: "))
        if isPrimeNum <= 1:
            print("Illegal input: " + str(isPrimeNum) + "; input must be an integer > 1.")
            print("")
            userInput = input("Enter a command (factor, isprime, end): ")
            continue
        if isPrime(isPrimeNum):
            print("The number", isPrimeNum, "is prime")
        else:
            print("The number", isPrimeNum, "is not prime")
        print("")
        userInput = input("Enter a command (factor, isprime, end): ")
        continue
    else: 
        print("Command", userInput.lower(), "not recognized. Try again!")
        print("")
        userInput = input("Enter a command (factor, isprime, end): ")
        continue
print("Thanks for using our service! Goodbye.")   
        