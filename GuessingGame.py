# File: GuessingGame.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/09/2020
# Date Last Modified: 10/10/2020
# Description of Program: This program is a interactive guessing game. However, for the purpose of testing the program
# the random number is set to 1458 rather than a random integer function. The user/player is allowed 10 guesses, after which 
# the game ends. If the user correctly guesses the number, the program returns a message that says so. If the guess is too 
# high or too low, the user/player receives such feedback. Also, if invalid guesses are entered, the number of guesses used 
# does not change and the user/player is prompted to enter a valid guess.

def main():
    number = 1458
    count = 0
    guess = eval(input("Welcome to the guessing game. You have ten tries to guess my number. \nPlease enter your guess: "))
    while count < 11:
        if guess < 1 or guess > 9999:
            guess = eval(input("Your guess must be between 0001 and 9999. \nPlease enter a valid guess: "))
            continue
        elif guess < number:
            count = count + 1
            print("Your guess is too low. \nGuesses so far:", count)
            if count == 10:
                print("Game over: you ran out of guesses.")
                return
            guess = eval(input("Please enter your guess: "))
        elif guess > number: 
            count = count + 1 
            print("Your guess is too high. \nGuesses so far:", count)
            if count == 10:
                print("Game over: you ran out of guesses.")
                return
            guess = eval(input("Please enter your guess: "))
        else:
            count = count + 1
            if count == 1:
                print("That's correct! \nCongratulations! You guessed it on the first try!")
                return
            print("That's correct! \nCongratulations! You guessed it in", count, "guesses.")
            return
main()
            